#!/usr/bin/env python3
"""
Postgres-backed storage for ELx808 runs and readings.
"""

from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass
from typing import Any, Iterable

try:
    import psycopg
except ImportError:  # pragma: no cover - optional dependency
    psycopg = None


class DatabaseError(RuntimeError):
    pass


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS samples (
    id BIGSERIAL PRIMARY KEY,
    label TEXT,
    ph DOUBLE PRECISION,
    metadata JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS runs (
    id BIGSERIAL PRIMARY KEY,
    run_code TEXT UNIQUE NOT NULL,
    mode TEXT,
    profile TEXT,
    port TEXT,
    started_at TIMESTAMPTZ,
    ended_at TIMESTAMPTZ,
    returncode INTEGER,
    status TEXT,
    csv_path TEXT,
    log_path TEXT,
    manifest_path TEXT,
    meta JSONB,
    sample_id BIGINT REFERENCES samples(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS readings (
    id BIGSERIAL PRIMARY KEY,
    run_id BIGINT REFERENCES runs(id) ON DELETE CASCADE,
    interval INTEGER,
    wavelength_index INTEGER,
    wavelength_nm INTEGER,
    row INTEGER,
    col INTEGER,
    well TEXT,
    value DOUBLE PRECISION,
    status TEXT,
    temperature_c DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS readings_run_id_idx ON readings(run_id);
CREATE INDEX IF NOT EXISTS readings_run_well_idx ON readings(run_id, well);
CREATE INDEX IF NOT EXISTS readings_run_interval_idx ON readings(run_id, interval);
CREATE INDEX IF NOT EXISTS readings_run_well_interval_idx ON readings(run_id, well, interval);
CREATE INDEX IF NOT EXISTS readings_run_wavelength_idx ON readings(run_id, wavelength_nm);
"""


def _require_driver() -> None:
    if psycopg is None:
        raise DatabaseError(
            "psycopg is not installed. Install with `pip install psycopg[binary]`."
        )


def _load_dsn() -> str | None:
    return os.environ.get("ELX808_DB_URL") or os.environ.get("DATABASE_URL")


def _to_json(value: dict[str, Any] | None) -> str | None:
    if not value:
        return None
    return json.dumps(value)


@dataclass(frozen=True)
class RunRecord:
    run_code: str
    mode: str | None
    profile: str | None
    port: str | None
    started_at: str | None
    ended_at: str | None
    returncode: int | None
    status: str | None
    sample_label: str | None
    sample_ph: float | None
    reading_count: int


class Database:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn

    @classmethod
    def from_env(cls) -> "Database | None":
        dsn = _load_dsn()
        if not dsn:
            return None
        return cls(dsn)

    def connect(self):
        _require_driver()
        return psycopg.connect(self._dsn)

    def ensure_schema(self) -> None:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(SCHEMA_SQL)

    def seed_demo_if_empty(self) -> None:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM runs")
                count = cur.fetchone()[0]
                if count:
                    return
                cur.execute(
                    "INSERT INTO samples (label, ph, metadata) VALUES (%s, %s, %s) RETURNING id",
                    ("Demo Soil", 8.2, _to_json({"source": "demo"})),
                )
                sample_id = cur.fetchone()[0]
                cur.execute(
                    """
                    INSERT INTO runs
                        (run_code, mode, profile, port, started_at, ended_at, returncode,
                         status, meta, sample_id)
                    VALUES (%s, %s, %s, %s, NOW(), NOW(), %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (
                        "demo-ecoplate",
                        "run-ecoplate",
                        "ECO590",
                        "/dev/demo",
                        0,
                        "demo",
                        _to_json({"note": "Seeded demo data"}),
                        sample_id,
                    ),
                )
                run_id = cur.fetchone()[0]
                rows = []
                for interval in (1, 2):
                    for wavelength_index, wavelength_nm in ((1, 590), (2, 750)):
                        for row_label, row in (("A", 1), ("B", 2)):
                            for col in (1, 2):
                                well = f"{row_label}{col}"
                                value = float(interval) + wavelength_index * 0.1 + col * 0.01
                                rows.append(
                                    (
                                        run_id,
                                        interval,
                                        wavelength_index,
                                        wavelength_nm,
                                        row,
                                        col,
                                        well,
                                        value,
                                        "ok",
                                        None,
                                    )
                                )
                cur.executemany(
                    """
                    INSERT INTO readings
                        (run_id, interval, wavelength_index, wavelength_nm, row, col, well,
                         value, status, temperature_c)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    rows,
                )

    def record_run_start(
        self,
        *,
        run_code: str,
        mode: str | None,
        profile: str | None,
        port: str | None,
        started_at,
        paths: dict[str, str],
        meta: dict[str, Any] | None,
    ) -> int:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO runs
                        (run_code, mode, profile, port, started_at, status,
                         csv_path, log_path, manifest_path, meta)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb)
                    ON CONFLICT (run_code) DO UPDATE SET
                        mode = EXCLUDED.mode,
                        profile = EXCLUDED.profile,
                        port = EXCLUDED.port,
                        started_at = EXCLUDED.started_at,
                        status = EXCLUDED.status,
                        csv_path = EXCLUDED.csv_path,
                        log_path = EXCLUDED.log_path,
                        manifest_path = EXCLUDED.manifest_path,
                        meta = EXCLUDED.meta
                    RETURNING id
                    """,
                    (
                        run_code,
                        mode,
                        profile,
                        port,
                        started_at,
                        "running",
                        paths.get("csv"),
                        paths.get("log"),
                        paths.get("manifest"),
                        _to_json(meta),
                    ),
                )
                return cur.fetchone()[0]

    def record_run_end(
        self,
        *,
        run_code: str,
        ended_at,
        returncode: int | None,
        status: str,
        meta: dict[str, Any] | None,
    ) -> int | None:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE runs
                    SET ended_at = %s,
                        returncode = %s,
                        status = %s,
                        meta = COALESCE(meta, '{}'::jsonb) || %s::jsonb
                    WHERE run_code = %s
                    RETURNING id
                    """,
                    (ended_at, returncode, status, _to_json(meta), run_code),
                )
                row = cur.fetchone()
                return row[0] if row else None

    def mark_run_stored(self, run_code: str) -> None:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE runs SET status = %s WHERE run_code = %s",
                    ("stored", run_code),
                )

    def _get_run_id(self, run_code: str) -> int | None:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM runs WHERE run_code = %s", (run_code,))
                row = cur.fetchone()
                return row[0] if row else None

    def replace_readings_from_csv(self, run_code: str, csv_path: str) -> int:
        run_id = self._get_run_id(run_code)
        if run_id is None:
            raise DatabaseError(f"Run not found: {run_code}")
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM readings WHERE run_id = %s", (run_id,))
                inserted = 0
                with open(csv_path, "r", encoding="utf-8") as handle:
                    reader = csv.DictReader(handle)
                    batch = []
                    for row in reader:
                        interval = int(row["interval"]) if row.get("interval") else None
                        wavelength_index = (
                            int(row["wavelength_index"]) if row.get("wavelength_index") else None
                        )
                        wavelength_nm = (
                            int(row["wavelength_nm"]) if row.get("wavelength_nm") else None
                        )
                        row_num = int(row["row"]) if row.get("row") else None
                        col_num = int(row["col"]) if row.get("col") else None
                        value = float(row["value"]) if row.get("value") else None
                        temperature = (
                            float(row["temperature_c"]) if row.get("temperature_c") else None
                        )
                        batch.append(
                            (
                                run_id,
                                interval,
                                wavelength_index,
                                wavelength_nm,
                                row_num,
                                col_num,
                                row.get("well"),
                                value,
                                row.get("status"),
                                temperature,
                            )
                        )
                        if len(batch) >= 1000:
                            cur.executemany(
                                """
                                INSERT INTO readings
                                    (run_id, interval, wavelength_index, wavelength_nm, row, col, well,
                                     value, status, temperature_c)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """,
                                batch,
                            )
                            inserted += len(batch)
                            batch = []
                    if batch:
                        cur.executemany(
                            """
                            INSERT INTO readings
                                (run_id, interval, wavelength_index, wavelength_nm, row, col, well,
                                 value, status, temperature_c)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            batch,
                        )
                        inserted += len(batch)
        return inserted

    def list_runs(self, limit: int = 50) -> list[RunRecord]:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT r.run_code,
                           r.mode,
                           r.profile,
                           r.port,
                           r.started_at,
                           r.ended_at,
                           r.returncode,
                           r.status,
                           s.label,
                           s.ph,
                           COUNT(rd.id) AS reading_count
                    FROM runs r
                    LEFT JOIN samples s ON r.sample_id = s.id
                    LEFT JOIN readings rd ON rd.run_id = r.id
                    GROUP BY r.id, s.id
                    ORDER BY r.started_at DESC NULLS LAST
                    LIMIT %s
                    """,
                    (limit,),
                )
                rows = []
                for row in cur.fetchall():
                    rows.append(
                        RunRecord(
                            run_code=row[0],
                            mode=row[1],
                            profile=row[2],
                            port=row[3],
                            started_at=row[4].isoformat() if row[4] else None,
                            ended_at=row[5].isoformat() if row[5] else None,
                            returncode=row[6],
                            status=row[7],
                            sample_label=row[8],
                            sample_ph=row[9],
                            reading_count=int(row[10] or 0),
                        )
                    )
                return rows

    def get_run_summary(self, run_code: str) -> dict[str, Any] | None:
        run_id = self._get_run_id(run_code)
        if run_id is None:
            return None
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT DISTINCT interval FROM readings WHERE run_id = %s ORDER BY interval",
                    (run_id,),
                )
                intervals = [row[0] for row in cur.fetchall() if row[0] is not None]
                cur.execute(
                    """
                    SELECT DISTINCT wavelength_nm
                    FROM readings
                    WHERE run_id = %s AND wavelength_nm IS NOT NULL
                    ORDER BY wavelength_nm
                    """,
                    (run_id,),
                )
                wavelengths_nm = [row[0] for row in cur.fetchall() if row[0] is not None]
                cur.execute(
                    """
                    SELECT DISTINCT wavelength_index
                    FROM readings
                    WHERE run_id = %s AND wavelength_index IS NOT NULL
                    ORDER BY wavelength_index
                    """,
                    (run_id,),
                )
                wavelengths_index = [row[0] for row in cur.fetchall() if row[0] is not None]
                cur.execute(
                    "SELECT COALESCE(MAX(row), 0), COALESCE(MAX(col), 0) FROM readings WHERE run_id = %s",
                    (run_id,),
                )
                row = cur.fetchone()
                max_row = int(row[0] or 0)
                max_col = int(row[1] or 0)
                return {
                    "run_code": run_code,
                    "intervals": intervals,
                    "wavelengths_nm": wavelengths_nm,
                    "wavelengths_index": wavelengths_index,
                    "rows": max_row,
                    "cols": max_col,
                }

    def get_matrix(
        self,
        run_code: str,
        *,
        interval: int,
        wavelength_nm: int | None = None,
        wavelength_index: int | None = None,
    ) -> dict[str, Any] | None:
        run_id = self._get_run_id(run_code)
        if run_id is None:
            return None
        clause = ""
        params: list[Any] = [run_id, interval]
        if wavelength_nm is not None:
            clause = "AND wavelength_nm = %s"
            params.append(wavelength_nm)
        elif wavelength_index is not None:
            clause = "AND wavelength_index = %s"
            params.append(wavelength_index)
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COALESCE(MAX(row), 0), COALESCE(MAX(col), 0) FROM readings WHERE run_id = %s",
                    (run_id,),
                )
                row = cur.fetchone()
                max_row = int(row[0] or 0)
                max_col = int(row[1] or 0)
                cur.execute(
                    f"""
                    SELECT row, col, well, value, status, temperature_c, wavelength_nm, wavelength_index
                    FROM readings
                    WHERE run_id = %s AND interval = %s {clause}
                    ORDER BY row, col
                    """,
                    params,
                )
                cells = []
                for item in cur.fetchall():
                    cells.append(
                        {
                            "row": item[0],
                            "col": item[1],
                            "well": item[2],
                            "value": item[3],
                            "status": item[4],
                            "temperature_c": item[5],
                            "wavelength_nm": item[6],
                            "wavelength_index": item[7],
                        }
                    )
                return {
                    "run_code": run_code,
                    "interval": interval,
                    "wavelength_nm": wavelength_nm,
                    "wavelength_index": wavelength_index,
                    "rows": max_row,
                    "cols": max_col,
                    "cells": cells,
                }

    def get_kinetic_series(
        self,
        run_code: str,
        *,
        wavelength_nm: int | None = None,
        wavelength_index: int | None = None,
    ) -> dict[str, Any] | None:
        run_id = self._get_run_id(run_code)
        if run_id is None:
            return None
        clause = ""
        params: list[Any] = [run_id]
        if wavelength_nm is not None:
            clause = "AND wavelength_nm = %s"
            params.append(wavelength_nm)
        elif wavelength_index is not None:
            clause = "AND wavelength_index = %s"
            params.append(wavelength_index)
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COALESCE(MAX(row), 0), COALESCE(MAX(col), 0) FROM readings WHERE run_id = %s",
                    (run_id,),
                )
                row = cur.fetchone()
                max_row = int(row[0] or 0)
                max_col = int(row[1] or 0)
                cur.execute(
                    f"""
                    SELECT interval, row, col, well, value
                    FROM readings
                    WHERE run_id = %s AND interval IS NOT NULL {clause}
                    ORDER BY row, col, interval
                    """,
                    params,
                )
                intervals: set[int] = set()
                cells: dict[tuple[int, int], dict[str, Any]] = {}
                for item in cur.fetchall():
                    interval, row_num, col_num, well, value = item
                    if row_num is None or col_num is None:
                        continue
                    interval = int(interval)
                    intervals.add(interval)
                    key = (int(row_num), int(col_num))
                    cell = cells.get(key)
                    if cell is None:
                        label = well or f"{chr(64 + key[0])}{key[1]}"
                        cell = {
                            "row": key[0],
                            "col": key[1],
                            "well": label,
                            "values": {},
                        }
                        cells[key] = cell
                    cell["values"][interval] = value
                sorted_intervals = sorted(intervals)
                wells = []
                for key in sorted(cells.keys()):
                    cell = cells[key]
                    values = [cell["values"].get(interval) for interval in sorted_intervals]
                    wells.append(
                        {
                            "row": cell["row"],
                            "col": cell["col"],
                            "well": cell["well"],
                            "values": values,
                        }
                    )
                return {
                    "run_code": run_code,
                    "intervals": sorted_intervals,
                    "rows": max_row,
                    "cols": max_col,
                    "wavelength_nm": wavelength_nm,
                    "wavelength_index": wavelength_index,
                    "wells": wells,
                }

    def export_run_csv(self, run_code: str) -> str:
        run_id = self._get_run_id(run_code)
        if run_id is None:
            raise DatabaseError(f"Run not found: {run_code}")
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT interval,
                           wavelength_index,
                           wavelength_nm,
                           row,
                           col,
                           well,
                           value,
                           status,
                           temperature_c
                    FROM readings
                    WHERE run_id = %s
                    ORDER BY interval, wavelength_index, row, col
                    """,
                    (run_id,),
                )
                output_lines = []
                output_lines.append(
                    "interval,wavelength_index,wavelength_nm,row,col,well,value,status,temperature_c"
                )
                for row in cur.fetchall():
                    fields = [
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        "" if row[6] is None else f"{row[6]:.3f}",
                        row[7] or "",
                        "" if row[8] is None else f"{row[8]:.1f}",
                    ]
                    output_lines.append(",".join(str(field) for field in fields))
                return "\n".join(output_lines) + "\n"

    def delete_run(self, run_code: str) -> bool:
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM runs WHERE run_code = %s", (run_code,))
                return cur.rowcount > 0
