# Chapter 8: Fluorescence and

Luminescence

     This chapter provides useful information for conducting
     Fluorescence and Luminescence analysis, including Time-Resolved
     Fluorescence. For Synergy HT, Synergy 2 and Synergy 4 readers,
     there is also a section on Multi-Mode assays. You'll find details
     about how to set the PMT Sensitivity and use Gen5's Synchronized
     Modes in this chapter.


 Fluorescence Analysis ............................................................... 150
 Luminescence Analysis ............................................................. 153
 Time-Resolved Fluorescence...................................................... 154
 Fluorescence Polarization .......................................................... 155
 Filter Set Options ..................................................................... 156
 PMT Sensitivity ........................................................................ 158
 Measurement Options............................................................... 162
 Synchronized Modes................................................................. 164
 Troubleshooting ....................................................................... 169
 Multi-Mode Detection................................................................ 182



150 | Chapter 8: Fluorescence and Luminescence




Fluorescence Analysis
        Your choice of fluorescent detection method depends on the reader's capability. All
        BioTek readers are capable of performing filter-based reads, only the Synergy 4 also
        offers monochromator-based reads, as well. When Fluorescence is the chosen detection
        method, Gen5 presents the filters installed in the reader or defined in the Filter Wheels
        Library. When you're running a Synergy 4, Synergy 2, or a Synergy HT or FLx800 with
        Injectors, you can perform fluorescence analysis in Synchronized Mode.
        Read Type options for fluorescence analysis (depending on the reader) are:

           Endpoint (FI)
           Area Scan
           Time Resolved (TRF or TR-FRET)
           Polarization (FP)
           Spectrum

Read Parameters
           Read Speed is a Synergy 2 and Synergy 4 option: Click the 3-dot button to change
        the default settings for Measurement Options
          The Filter Set buttons (up to 6) determine the number of reads to perform. Only
        two filter sets are permitted in a Kinetic loop.
               Filter-based Fluorescence: Excitation and Emission filters can be selected
                 using the drop-down list of filters available for the current reader. The list is
                 defined from one or two sources: the Filter Wheels Library or the Reader
                 Setup
               Monochromator-based Fluorescence: Excitation and Emission wavelengths
                 can be set to any value supported by the reader. Synergy 4's range is
                 dependent on the light source for Excitation wavelengths: the Xenon Flash
                 supports 250-700 nm, the Tungsten Lamp supports 340-700 nm; for
                 Emission wavelengths the range is 300-800 nm.
        Filter Switching is offered when only two filter sets are defined (described below). It
        is similar to Synchronized Well Mode.
        Optics Position can be set to Top or Bottom for each selected filter set, depending on
        the reader's capability. Readers are equipped with one or two optical probes,
        positioned above (Top) and/or below (Bottom) the assay plate. Synergy 2/4 offers
        mirror selection for the Top probe.
        Sensitivity of the PMT can be set by entering the desired value (valid settings range
        between 25-255) or by letting Gen5 determine the optimal sensitivity setting using the
        Filter Set Options (described below).






                Filter Set Options: Each filter set has a corresponding set of measurement
      options which can be defined by clicking the Options button. See page 156.
      Filter Switching: When two filter sets are selected Gen5 offers this option to read
      every well with each filter set before moving onto read the next well. When this option
      is not selected the reader reads the whole plate with one filter set, then reads it again
      with the second filter set.
      The advantage of this option is closely timed well measurements. The disadvantage is
      a longer runtime. It is useful when working with two, possibly unstable, fluorescent
      labels. Learn more in Gen5's Help.
      Top Probe Vertical Offset: parameter is available when at least one of the filter sets
      uses the "top" optics position. It allows you to define how far the top probe is
      positioned from the top surface of the plate during the read. The valid range is
      determined on a plate-by-plate basis. The calculation is based on the plate height and
      the maximum travel of the top probe. Learn more in Gen5's Help.
      Column Offset (for Monochromator-based reads only): Valid Range: 0.0 - 3.0
      Due to the angled approach of the probe, lowering it may also require a small
      adjustment to the plate position beneath it.

Troubleshooting
        If you're not getting expected results review these suggestions:
        Troubleshooting Fluorescence/Luminescence Measurements on page 169.


About Fluorescence Monochromator Reads
   Synergy 4's monochromator has a quadruple-grating design for maximum spectral
   control. Background noise is significantly reduced by the angled approach of the probe to
   the well and the use of an order-sorting filter. And, the mono uses a red-shifted PMT that
   can read up to 900 nm. Here are some essential facts to keep in mind when using the
   monochromator for fluorescent measurements:
         It requires a special configuration of the Excitation filter wheel. Two positions
           are needed for the monochromator, one for the order-sorting filter called Mono
           LP that is shipped with the reader, the other position is empty, defined as a
           Hole. The reader tests for this configuration and will not perform a mono read
           without it.
         The Xenon Flash lamp is more sensitive and thus the best choice for most
           assays. The Xenon also offers a choice of Lamp Energy, to give you more
           control. However, the Tungsten lamp offers stronger output in the red range,
           and a choice of Dynamic range: Extended or Standard, which may be better for
           some assays.
         Time Resolved Fluorescence (TRF) can be performed with the monochromator,
           but it is much less sensitive than filter-based processing.



152 | Chapter 8: Fluorescence and Luminescence



           Sufficient well volume is an important factor for this system. 384-well plates
             show optimal performance. A minimum volume of 200 ul is required for
             regular 96-well plates; half-area 96-well or 384-well plates should be used for
             lower volumes. When well volumes cannot be increased, Gen5's Top Probe
             Vertical Offset and Column Offset controls can be used to improve
             performance.
     Perform multiple read steps with slightly varied settings to determine the optimal
     combination of settings for a mono read. Multiple experiments may be needed because all
     read steps must use the same light source in one experiment.







Luminescence Analysis
   When Luminescence is the chosen detection method, the Read Step presents the emission
   filters for the current reader or you can select Hole for no filtering. The excitation filters are
   not available for selection, because the reader will automatically use a Plug in the
   excitation filter wheel. Also see Luminescence Best Practices in Gen5's Help.
   Read Type is limited to Endpoint , except with Synergy 4 which offers spectrum scans.
   Integration Time is set as minutes:seconds.milliseconds (MM:SS.ss).
          Synergy HT and FLx800: Gen5 reports the measurement results as RLU
            (Relative Luminescence Units) per Second, except in Well Mode Kinetic
            experiments, which are reported as RLU, and integration time is replaced with
            the kinetic timelines. Gen5 collects data in each well for the duration of the
            integration time, then sums the data points and displays the result as
            RLU/second.
          Synergy 2 and Synery 4: Gen5 reports the measurement results as RLU
            (Relative Luminescence Units). The reader collects data in each well for the
            duration of the integration time, then averages the data points and displays the
            result as RLU.


         You should know: in Luminescence Reading Mode there is a tight link between
      CV's and integration time. This correlation is independent of the instrument (type,
      brand) and of the reagents. If you increase your measurement time by a factor of 2, you
      will decrease your CV's by the square root of 2. If you increase your measurement time
      by a factor of X, you will decrease your CV's by the square root of X.


Reading Parameters
               The Filter Set buttons (up to 6) determine the number of reads to perform.
              Only two filter sets are permitted in a Kinetic loop. Emission Filters can be
              selected using the drop down list of filters available for the current reader.
          The recommended Optics Position for Luminescence readings is Top.
          Sensitivity of the PMT can be set by entering the desired value (valid settings
            range between 25-255), or by letting Gen5 determine the optimal sensitivity
            setting using the Measurement Options (learn more on page 158). BioTek
            recommends a setting between 100-160 for Luminescence

                      Filter Set Options - For each filter set you can use Gen5's tool to
              automatically determine the optimal Sensitivity of the PMT. See page 156.
          Top Probe Vertical Offset parameter is available when at least one of the
            filter sets uses the "top" optics position. Generally, you do not have to change
            the default value. For all Luminescence assays Gen5 sets the probe as close to
            the well as possible.



154 | Chapter 8: Fluorescence and Luminescence




Time-Resolved Fluorescence Analysis
     Measuring fluorescence using a delay after the cessation of excitatory light is called time-
     resolved fluorescence (TRF). Auto-fluorescence in a sample or microplate is a common
     source of background fluorescence. Lanthanide ions, for example, have extremely long
     fluorescent decay times, several hundred microseconds instead of several nanoseconds.
     The rapid on/off nature of a xenon flash lamp allows for fluorescence analysis of the these
     compounds with a delay after the excitation flash. The delay lets virtually all of the
     background fluorescence diminish before measuring lanthanide's long-lived fluorescence,
     resulting in superior detection limits. The TRF option is available if the selected detection
     method is Fluorescence and the current reader supports it.




          1.   For each Excitation filter set:
                Synergy HTTR: enter a wavelength value between 200 and 999 nm. The
                  bandpass is not variable; it is pre-defined to be 10 nm.
                Synergy 2: select the filter, as usual. The light source is fixed to Xenon.
                Synergy 4: opt to "Use Filter Wheels" or the monochromator (but filter-
                  based is more sensitive). The light source is fixed to Xenon Flash (at High
                  intensity). Spectrum and Area Scan read types, in addition to Endpoint, are
                  available when other constraints are met, e.g. well size of the plate.
          2.   For each Emission filter, use the drop-down lists to select the wavelengths.
          3.   Sensitivity: BioTek recommends a setting between 150-200 for TRF.

          4.               click the Options button when using the Synergy HTTR
               or click the 3-dot button next to the Time Resolved checkbox when using the
               Synergy 2/4: Specify the length of time to delay before data collection and the
               data collection duration and define the other related measurement options.0.







Fluorescence Polarization
        For each Fluorescence Polarization (FP) read step, Gen5 actually performs two reads. It
        takes a measurement through a parallel polarizer, and then, through a perpendicular
        polarizer. Two raw data sets are generated. Gen5 automatically transforms the data in
        an FP-dedicated data reduction step.
        When applicable, Gen5 also performs the other automated data reductions, blank
        subtraction and kinetic well analysis on the FP data sets. Anisotropy is also offered as a
        data reduction option for FP analysis. You can choose to transform the data to produce
        Polarization results, Anisotropy results or both. Results are reported as mP (millipees),
        with an expected range between 0 - 500 mP with precision of +/- 2 mP.
        When the reader is equipped with the polarizers and mirrors required to excite the
        sample and capture the polarized emission, the polarizing lenses reside in position 3 of
        the mirror holder. Thus, when FP is the selected read type, the Optics Position choice
        of mirrors is fixed to position 3.

Top 5 Things to Know about Fluorescence Polarization
            Mirror selection is fixed by Gen5 to use position 3. If you have a dichroic mirror
              in position 3 (which is the default configuration), you must select filters that
              correspond to its Min-Max range
            When Gen5's Auto-Sensitivity adjustment is used to determine the optimal
              PMT sensitivity, it is performed on the parallel read/measurement
            Either light source can be used for FP: Tungsten or Xenon Flash
            Read Speed can be set to sweep when the Xenon Flash is used
            Synchronized Well and Plate Modes are available for time-sensitive FP assays

BioTek's FP Process
     For each sample in an FP experiment, the Excitation light travels from the light source
     through the EX polarizer and then is reflected by the mirror to excite the sample. The
     sample's emitted light travels through the mirror and parallel Emission (EM) polarizer
     and then through the emission filter into the PMT. The mirror holder then shifts so that
     the emitted light travels through the perpendicular EM polarizer, through the emission
     filter, and into the PMT. Gen5 corrects for the optical variations between the parallel and
     perpendicular emission paths during the FP data reduction step. Learn more in the Data
     Reduction chapter, page 307.



156 | Chapter 8: Fluorescence and Luminescence




Filter Set Options

                   In Fluorescence and Luminescence assays, you can set the sensitivity level of
        the PMT or let Gen5 determine the optimal setting. You may need to experiment with
        the settings to find the combination of options that works best for your assay. In
        Fluorescence analysis, you can also set the Measurement Options.

Automatic Sensitivity Adjustment
           Click in the checkbox to use this option to determine the optimum Sensitivity
        setting for the plate:
         1.   First, select one:
               Scale to High Wells - to evaluate optimal sensitivity based on the strongest
                 signal
               Scale to Low Wells - to evaluate optimal sensitivity based on the weakest
                 signal
               Use First Filter Set Sensitivity:
                   of This read step when there is more than one filter set;
                   of First read step when there is more than one read step of the same
                     detection method, i.e., Fluorescence or Luminescence.
         2.   Then, define:0.
               Scale Wells - a range of microplate wells with the highest or lowest
                 expected signals, click in the field to select one or a range of adjacent wells,
                 e.g., A1-B12
               Scale Value - the highest or lowest expected value for the entire plate.
        For input recommendations review the valid value ranges in the PMT Sensitivity
        section on page 158.

Luminescence
      Synergy HT and FLx800: Gen5 performs the Automatic Sensitivity Adjustment based
      on an integration time of 1 second (0:01:0) regardless of the Integration Time defined
      for the Read step .
        Synergy 2 and Synergy 4: Gen5 uses the read step's integration time to peform the
        Automatic Sensitivity Adjustment. It may be unable to determine the optimal
        sensitivity, especially when scaling to low wells, if the determination takes longer than
        3 minutes, which generally translates into integration times > 1 second.






Fluorescence Measurement Options
     The values for each measurement option depend on whether the assay is defined as
     Standard (Non-Synchronized Mode), Synchronized Plate Mode or Well Mode. This table
     displays the recommended values and Allowable Range for these modes for each option.
     Note: For Kinetic analysis in Well mode these options are unavailable, they are determined
     by the kinetic interval.

       Option                    Standard &         Plate           Well         Allowable
                                 Time               Mode            Mode         Range
                                 Resolved

       Delay after plate         100 msec           250 msec        10 msec      10-2550
       movement                                                                  msec

       Measurements per          10                 10              1            1-255
       well

       Delay between             1 msec             24 msec         0            0-255 msec
       measurements


Time-Resolved Fluorescence Parameters
      Delay before data collection: is time delay between the flash and the beginning of data
      collection or the delay before integration. Valid values are 0 usec and 20 - 16000 usec.
      The default value is 20 usec.
             A delay of 0 usec is not the same as a fluorescence read with the time-resolved
             option turned off. They differ in two ways: (1) the excitation wavelength is
             generated by the monochromator; and (2) the user can specify the data collection
             time, which is not an available parameter for normal fluorescence reads.
        Data collection duration: is the amount of time for which readings are collected after
        the delay before integration time has expired. The valid range is from 20 - 16000 usec.
        The default value is 100 usec.



158 | Chapter 8: Fluorescence and Luminescence




PMT Sensitivity
     In fluorescence and luminescence assays, the signal can be very weak, very strong, or
     anywhere in between. For each assay, the Sensitivity of the photomultiplier tube (PMT)
     should be adjusted to ensure that the signals from all wells fall within the appropriate
     dynamic range of 0 to 99998 relative fluorescence or luminescence units (RFU or RLU).

          Automatic Sensitivity Adjustment
          You can let Gen5 determine the optimal sensitivity setting: click Options and
          provide some criteria on which a determination can be made.

 Guidelines:
           Typical fluorescent assays using 96- (or fewer) well plates require sensitivities
             between 35 and 130. Assays using 384-well or other higher-density plates will
             likely require higher sensitivities due to narrower optical probes. Luminescent
             reactions may require sensitivities up to 200. BioTek recommends selecting a
             PMT Sensitivity setting between these ranges:

              Detection                           Type               Low      High

              Fluorescence                        Filter wheel       35       120

              Fluorescence                        Monochromator      50       150

              Luminescence                        Filter wheel       100      255

              Luminescence                        Monochromator      100      255

              Time-Resolved FL                    Filter wheel       100      255

              Time-Resolved FL: Synergy HT        Filter wheel       150      255

              Time-Resolved FL                    Monochromator      100      255

              Fluorescence Polarization           Filter wheel       35       120

           As the sensitivity setting increases, so will the fluorescence values. If many
             wells result in "OVRFLW," the sensitivity setting is probably too high:
               OVRFLW indicates RFU or RLU values greater than 99998 in Standard
                 Range (e.g. with Xenon Flash)
               OVRFLW indicates RFU or RLU values greater than 5.8 million in Extended
                 Range.
           Recommendation: one way to determine the optimal Sensitivity setting is to set
             up one Read Step to perform 6 filter-set reads each applying a different
             Sensitivity. Review the results to determine the best setting.






            When the wells contain more than one fluorophore, one of which might give
              brighter or weaker results, assign each filter set its own sensitivity.
            When the field shows 'Auto', the Automatic Sensitivity Adjustment feature is
              enabled to determine optimum sensitivity. See Filter Set Options above.


Automatic Sensitivity Adjustment for PMT
       Gen5TM can determine the optimum PMT Sensitivity setting for the plate based on one
       of three methods: Scale to High Wells, Scale to Low Wells, or when multiple filter sets
       are used: Use First Filter Set Sensitivity. The best method depends on your
       application (some experimentation may be necessary).

  Scale to High Wells
       High Wells are wells with the highest expected signal (measurement value) on the
       plate, such as the highest standard wells.
       Scale to High Wells searches for two consecutive gain values where the measured
       values are lower and higher than the defined high well values.

  Scale to Low Wells
       Low Wells are wells with the lowest expected signal (measurement value) on the plate,
       such as blank wells, negative controls, or the zero standard wells.
       Scale to Low Wells searches for two consecutive gain values where the measured
       values are lower and higher than the defined low value wells. Scale to Low Wells is
       recommended for weakly luminescent reactions.
       When you let Gen5 determine the optimal sensitivity setting for your assay, the valid
       values for Scale to High or Low Wells is dependent on the reader, detection method,
       and light source:

Dynamic         Synergy HT/FLx800                Synergy 2/Synergy 4
Range           FI              Lum              Xe               Tg              Lum

Standard        0-99,999                         0-99,999         0-99,999        0-99,999
                RFU                              RFU              RFU             RLU

Extended                        0-                                0-              0-
                                5,000,000                         5,800,000       5,800,000
                                RLU/sec                           RFU             RLU

       BioTek recommends retaining Gen5's default values when the expected measurements
       are unknown.

  Use First Filter Set Sensitivity of This or the First read step
             This option is available when multiple filter sets and/or multiple read steps of the
             same detection method have been defined. It applies the same sensitivity setting
             to the current filter set read.



160 | Chapter 8: Fluorescence and Luminescence



              Use first filter set from First read step: Notice that both the first filter set and first
              read step are referenced: it applies either the manually input or automatically
              determined Sensitivity setting of the first read step's first filter set. This only
              applies to the same detection method. In a multi-mode Procedure, Gen5 selects
              the first read step of the same detection method (e.g. FI or Lum).
              Use first filter set from This read step is offered when there are multiple filter
              sets in the current read step. It applies either the manually input or automatically
              determined Sensitivity setting of the first filter set to the current read.

          In Dispense protocols, if two filter sets are defined, the Sensitivity
            field for the second filter set always shows Auto and it will use the first
            filter set's sensitivity.

          In multiple-plate experiments, when the Automatic Sensitivity
            option is used, Gen5 applies the sensitivity setting determined for the
            first plate, to all other plates processed in the experiment.

   How to let Gen5 determine the Sensitivity setting:

         1.              In the Fluorescence or Luminescence read step, click the Options
              button for the Filter Set
         2.     Turn on Automatic Sensitivity Adjustment: click the box to insert a
              checkmark
         3.   Select a button for one of the options described above:0.
               Scale Wells: click in the field to select one or a range of adjacent wells that
                 you expect to produce the highest or lowest measurements
               Scale Value: Enter a value that represents the upper limit when scaling to
                 High Wells and the lowest limit when scaling to Low Wells of the expected
                 range of values for the entire microplate. The recommended high value is
                 50,000 to 70,000 RFU/RLU. The recommended low value is 100 to 200
                 RFU/RLU.


Reviewing results
     After using the AutoSensitivity feature in an experiment, you can view on-screen and
     include in reports the applied Sensitivity value. When the read step is completed:
           to Report the Sensitivity Value in reports (see below)
           to Display the AutoSensitivity Value on-screen described on page 161

          The sensitivity value applied during the experiment is retained in the
            Experiment file, but not in the protocol (.prt) the experiment was
            based on. Unless it is updated, the protocol will continue to be defined
            as using the AutoSensitivity option.






Report the Sensitivity Value
   Fixed Value: use the pre-built Procedure Summary in the Report and Export Builders and
   set it to Detailed report to include the defined Sensitivity value in a report.
    AutoSensitivity: when you let Gen5 determine the optimal sensitivity, follow these
    instructions to include the Sensitivity value in a report. You must use a field group. After
    you have defined a fluorescence or luminescence Read Step using Gen5's AutoSensitivty
    determination:
         1.    Select Protocol> Data Views
         2.    Locate the Field Group element at the bottom of the tree, highlight Field Group
               and click New
         3.    Name the new Field Group

         4.       Click in the first cell in the first column to enable the 3-dot button, and click
               the 3-dot button to open the Fields dialog

         5.         Set the Category to Procedure
         6.    Set the Field to Sensitivity # (there is one value for each read/filter set)
         7.    Now, you can add this field group to Reports or Export files
         8.    Save or Save As the Protocol to make sure this field group is available
               whenever you run the experiment.0.


Display the AutoSensitivity Value
        When the Procedure is completed in an experiment:

                  Highlight Procedure in the menu tree and right click, select
               AutoSensitivity Results
               or
           Open the Procedure dialog (double click the menu tree item), the sensitivity
             value applied during the first read step is displayed.



162 | Chapter 8: Fluorescence and Luminescence




Measurement Options

               Procedure> Read> Fluorescence> click Options

         Synergy 2/4: Procedure> Read> click 3-dot button next to Read Speed

          This section describes all the possible measurement options available
            in Gen5. You will be offered more or fewer of them depending on your
            reader and the context of the Read step.

        You may need to experiment with various combinations of settings to determine the
        optimal value for each. Generally it is a trade off between speed and precision. Increase
        the number of measurements per well for better precision; decrease them to increase
        speed.
        Define the measurement parameters for read speed:
           Delay after plate movement is the time between the end of the movement
             of the plate carrier (plate is in the read position) and the beginning of the
             acquisition of the data. The valid range is from 10 to 2550 milliseconds. The
             recommended setting to ensure that the fluid has settled in a 96-well plate is
             100 milliseconds. This parameter is especially important in absorbance mode,
             where the vibration of the liquid's surface meniscus just after a plate movement
             can lead to variations in OD measurements.
           Measurements per data point are the number of measurements the reader
             takes per well per read. The data point reported for each well represents the
             average of its measurements. The valid range is from 1 to 255 measurements.
             Usually, the more measurements per well the better the CVs, although selecting
             a large number of measurements typically results in only marginal
             improvement. Consider a setting that represents the optimal combination of
             precision and speed. The recommended setting to achieve a balance between
             speed and precision is 10 measurements per well. This is not adjustable in
             Absorbance reads.

          Note: The reader takes approximately 10 milliseconds to perform each
            measurement.

           Delay between measurements is the time delay between measurements
             taken in each well. The valid range is from 0 to 255 milliseconds. The
             recommended setting is 1 millisecond. Longer delays between samples may
             result in better CVs between replicates.
           Dynamic Range: offers two ways to express the measurements taken by the
             reader:
               Standard Range: reports measurements between 0 - 99,999, higher values
                 are reported as "OVRFLW." This is the only setting available for Synergy






   HT, FLx800. Synergy 4 and Synergy 2 are limited to this option when the
   Xenon Flash is used, e.g. for TRF.
 Extended Range: reports measurements between 0 - 5,800,000, higher
   values are reported as "OVRFLW."
   Some of the benefits of Extended Range, you can:
    take measurements with a high Sensitivity setting without fear of over-
      ranging the wells,
    measure samples with very low and very high outputs in the same Read
      step,
    reduce the risk of over-ranging in kinetic mode (when the signal grows
      over time).



164 | Chapter 8: Fluorescence and Luminescence




Synchronized Modes
     Synergy 2/4, Synergy HT/FLx800 with Injectors: Protocol> Procedure>
     Synchronized Modes
        Gen5 supports three modes of processing plates. All readers can process plates in the
        standard mode, we'll call Non-Synchronized Plate Mode to distinguish it from the
        other options. If you're running a Synergy 4, Synergy 2, or a Synergy HT or FLx800
        with Injectors, you have two more processing mode options: Synchronized Plate
        Mode and Well Mode. These options give you more control in time-sensitive
        procedures.


           Tip: When defining a Synchronized Plate Mode and Well Mode procedure, in the
        Procedure dialog the first step is adding the Well or Plate mode block. Then, put the
        Read and other steps inside the block.


Non-Synchronized Plate Mode
        Non-Synchronized Plate Mode is the standard mode for processing and is supported
        by all BioTek readers. Each step in a Procedure is processed for the entire plate (or
        partial plate) before the next step is processed. No attempt is made to maintain
        consistent well-to-well timing from one step to the next.

Multi-Detection Kinetics
          For readers that support multiple detection methods (absorbance, fluorescence,
          luminescence), the Non-Synchronized Plate Mode supports the ability to include
          multiple read steps in a single kinetic block. This capability is called Multi-
          Detection Kinetics.
          With a Synergy HT, for example, in Non-Synchronized Plate Mode, you can
          perform a four-wavelength absorbance read, followed by a kinetic loop that
          includes a dual-wavelength fluorescence read.

Synchronized Plate Mode
        In Synchronized Plate Mode each step is processed for the entire plate (or partial plate)
        before the next step is processed, but the time spent at each well is identical. Steps
        within a Synchronized Plate Mode block maintain consistent well-to-well timing, such
        that the time required to process two successive steps is the same for each well on the
        plate. The Synergy HT and FLx800 readers can only perform Fluorescence in Plate
        Mode; the Synergy 2 and Synergy 4 can perform all detection methods.
        When timing is critical to your research, Synchronized Plate Mode gives you the ability
        to perform a precisely timed sequence of steps on each well. For example, you can
        define the timeline for a Dispense>Wait>Read block of steps that encompasses the time
        to complete all three steps from beginning to end, so you know precisely when reagent
        was dispensed to each well and when it was read.






Synchronized Well Mode
      In Synchronized Well Mode, all steps within a block are performed on a single well,
      before proceeding to the next well. Like Synchronized Plate Mode, the time spent at
      each well is exactly the same. The Synergy HT and FLx800 readers can only perform
      Luminescence and Fluorescence in Well Mode; the Synergy 2 and Synergy 4 can
      perform all detection methods.

How to choose which option to use?
      You may want to test the different options to see which works best for your
      experiments, but here are some general guidelines to help narrow the choice:
         When you expect the well signal to vary over time, select Synchronized Plate
           Mode or Well Mode (Synergy HT and FLx800 do not support a Shake step
           following reagent dispensing in Well Mode)
         Non-Synchronized Plate Mode is efficient when using a Stop solution and the
           well signal is stable over time
         In kinetic analysis, use Synchronized Plate Mode or Well Mode when it is
           important to have the same exact timing for each well
         In kinetic analysis, use Non-Synchronized Plate Mode when it is important to
           obtain as many data points as possible
         When conducting long-time-span kinetic reads (hours), Non-Synchronized
           Plate Mode is sufficient
         In Synchronized Mode you can define the duration of a Delay step to include
           the time it takes to perform the previous step
         Multi-Detection (multi-mode) Kinetic Reads can only be performed in Non-
           Synchronized Plate Mode



166 | Chapter 8: Fluorescence and Luminescence



Processing Modes Comparison
         Here's a tabular breakdown of the differences between Non-Synchronized Plate
         Mode, Synchronized Plate Mode, and Well Mode.

Process             Detection       Supported       Kinetic     Read           Partial
                                    Steps           Loop        Settings       Plate
                                                    Steps                      Processing

Non-                Absorbance      All             Shake       Can define     Can define
Synchronized        Fluorescence    Procedure       Read        unique         unique
Plate Mode          Luminescence    steps                       settings for   setting for
                                    supported                   each read      each step
                                    by Reader                   step

Synchronized        Synergy 2/4:    Read            Shake       Defined in     Defined in
Plate Mode          all methods     Dispense        Read        first step     first step for
                    Synergy HT &    Shake                       for all        all
                    FLx800:         Delay                       subsequent     subsequent
                    Fluorescence    Kinetic                     steps          steps

Well Mode           Synergy HT &    Read            Read        Defined in     Defined in
                    FLx800:         Dispense        Synergy     first step     first step for
                    Fluorescence    Delay           2/4:        for all        all
                    Luminescence    Kinetic         Shake       subsequent     subsequent
                    Synergy 2/4:    Synergy                     steps          steps
                    all methods     2/4: Shake



Synchronized Mode Performance Chart

Reader          Max #       Max #           Max Kinetic                Time Increment
                of          Kinetic         Interval (sec)
                Steps       Reads

Synergy HT      9           999             Plate = 9999              Plate = 1 sec
                                            Well = 99.99              Well = 20 ms

FLx800          3           300             Plate = 9999              Plate = 1 sec
                                            Well = 12                 Well = 20 ms

Synergy 2       20          999             Plate = 9999              Plate = 1 sec
Synergy 4                                   Well = 99.99              Well = 20 ms






Synchronized Plate Mode Limitations
      Here is a listing of the Plate Mode limitations:
             Synergy 2/4 support all detection methods, but Synergy HT and FLx800
               only support Fluorescence
             All parameters set in the first read step of the block are automatically
               applied to subsequent read steps, with the exception of Step Label and
               Light Shuttering
             Partial plate settings are automatically applied to all read and dispense
               steps using the settings in the first step
             The only available steps in a plate mode block are: Read, Dispense, Shake,
               Delay, and Kinetic
             When two filter sets are used in the read step, the second filter set
               automatically uses the sensitivity of the first, except Synergy 2/4 allow
               different sensitivity values for each step
             A Shake step must immediately precede a Read step or a Kinetic Start step
             The maximum duration of a plate-mode block is approximately 27 hours 47
               minutes for Synergy HT an FLx800 and approximately 277 hours 47
               minutes for the Synergy 2/4
             The only available steps within a plate mode kinetic loop are Shake and
               Read and the maximum runtime duration for a loop is 24 hours
             A maximum of one read step and one shake step is supported in a plate
               mode kinetic block
             384- and 1536-well plates are not supported
             In the FLx800, a plate mode block must contain at least one kinetic loop to
               be valid. If two kinetic loops are present in the plate mode block, they must
               have the same kinetic interval
             In the FLx800, a plate mode block can contain only one dispense step, and a
               dispense step cannot be the last step in the plate mode block
             Light Shuttering is available



168 | Chapter 8: Fluorescence and Luminescence




Synchronized Well Mode Limitations
        Here is a listing of the limitations that apply to Well Mode blocks:
               Synergy 2/4 support all detection methods, but Synergy HT and FLx800
                 only support Fluorescence and Luminescence
               All parameters set in the first read step of the block are automatically
                 applied to subsequent read steps, with the exception of Step Label and
                 Light Shuttering
               Partial plate settings are automatically applied to all read and dispense
                 steps using the settings in the first step
               The only available steps in a well mode block are: Read, Dispense, Delay,
                 and Kinetic, except Synergy 2/4 also support a Shake step before a Read or
                 Kinetic loop
               The maximum duration of a well-mode block is approximately 16 minutes
                 40 seconds
               The only available step within a well mode kinetic loop is a Read step,
                 except Synergy 2/4 also support a Shake step
               When two filter sets are used in the read step, the second filter set
                 automatically uses the sensitivity of the first, except Synergy 2/4 allow
                 different sensitivity values for each step
               A maximum of one read step is supported within a well mode kinetic block
               Luminescence read steps within a well mode kinetic loop do not support
                 the entry of an Integration Time. It is replaced by the kinetic run time
               384- and 1536-well plates are not supported
               Light Shuttering is available
               Important: FLx800 readers require adding a Delay step (beginning at the
                 start of the previous step) to the Procedure to avoid potential loss of data.
                 You must determine the correct duration of the delays







Troubleshooting Fluorescence/Luminescence
   Here's a list of potential problems, the possible cause and a remedy:

Fluorescence / Luminescence Readings Too Low
      Possible cause: The Sensitivity in the Read Step dialog is currently set too low
         Raise the Sensitivity to an appropriate level. For fluorescence, the Sensitivity is
         usually set between 45 and 130. For luminescence it is usually set between 100 and
         200.
         If using Automatic Sensitivity Adjustment, use the Scale to High Well option and
         set the target value to be between 20,000 and 80,000 for standard range; or
         1,000,000-3,500,000 for extended range.
      Possible cause: The wrong filters are selected in the Read Step dialog
         Examine the current filter settings and make any corrections. If the filter settings
         appear to be correct, check the locations of the actual filters in the instrument.
      Possible cause: Top probe is too high
            Synergy HT: If a plate cover is not being used, lower the top probe to 1 mm
               above the selected plate using the Top Probe Vertical Offset option in the
               Read Step dialog
            Synergy 2/4: Gen5 generally positions the top probe at the optimal height
               for fluorescence reads: it focuses the beam above the well. Refer to Gen5's
               Help and use the Top Probe Vertical Offset option in the Read Step dialog
               to make adjustments
            FLx800: Refer to the Operator's Manual for instructions to manually lower
               the Top Optical Probe

Fluorescence Background Too High
      Possible cause: Using incorrect microplates
         Solid black plates and top probe reading lower the background. Black plates with
         clear bottoms lower the background if bottom reading is necessary. Corning 3615
         or 3614 (for cell culture) are appropriate.
      Possible cause: The wrong filters are selected in the Read Step dialog
         Examine the current filter settings and make any corrections. If the filter settings
         appear to be correct, check the locations of the actual filters in the instrument.
      Possible cause: Phenol red is used in the media when exciting at 485 nm and
         reading at 528-530 nm
         Eliminate or replace the phenol red
      Possible cause: Cells, media and other contents fluoresce



170 | Chapter 8: Fluorescence and Luminescence



          Use deionized-water blank wells as a diagnostic tool. The blank-well reading will
          help you determine the background value contributed by the instrument, labware
          and media.
        Possible cause: The top and/or bottom probe needs cleaning
          Refer to the Operator's Manual for instructions to open and clean the reader's
          internal components.
        Possible cause: The instrument has fluorescing material spilled inside
          Refer to the Operator's Manual for instructions to open and clean the reader's
          internal components.
        Possible cause: The Sensitivity in the Reading parameters dialog is currently set
          too high
          Lower the Sensitivity setting. The background should still read higher than zero.
           200 is a recommended minimum and a value of 1000 takes advantage of the
          system's 5-digit resolution.

Reader Not Achieving Desired Fluorescence Detection Limit
        Possible cause: The wrong filters are selected in the Read Step dialog
          Examine the current filter settings and make any corrections. If the filter settings
          appear to be correct, check the locations of the actual filters in the instrument.
        Possible cause: Using incorrect microplates
          Solid black plates and top probe reading lower the background. Black plates with
          clear bottoms lower the background if bottom reading is necessary. Corning 3615
          or 3614 (for cell culture) are appropriate.
        Possible cause: The Sensitivity is currently set too low
          Raise the Sensitivity setting until the background wells read at least 200 RFU, (1000
          RFU is preferred) in the Read Step dialog
        Possible cause: Readings are taken using the bottom probe
          Switch to the top probe (Optics Position in the Read Step dialog)
        Possible cause: The solution volume is 50 ul or less
          Increase the solution volume to 150 - 200 ul, if possible.
        Possible cause: Wrong pH
          Fluorescence is very pH dependent. Use the appropriate pH.
        Possible cause: Phenol red is used in the media when exciting at 485 nm and
          reading at 528-530 nm
          Eliminate or replace the phenol red.
        Possible cause: Top probe is too high






               Synergy HT: If a plate cover is not being used, lower the top probe to 1 mm
                 above the selected plate using the Top Probe Vertical Offset option in the
                 Read Step dialog
             Synergy 2/4 filter-based reads: Gen5 generally positions the top probe
               at the optimal height for fluorescence reads: it focuses the beam above the
               well. Refer to Gen5's Help and use the Top Probe Vertical Offset option in
               the Read Step dialog to make adjustments
             Synergy 4 mono-based reads: Gen5 positions the top probe at 4 mm for
               96-well plates and at 6 mm for 384-well plates because these settings were
               determined to be the optimal height. You may be able to lower the probe,
               but lowering it may require a small adjustment to the Column Offset, as
               well.
             FLx800: Refer to the Operator's Manual for instructions to manually lower
               the Top Optical Probe
      Possible cause: Transfection efficiency in gene expression is too low
        Use more cells, or improve the transfection efficiency.
      Possible cause: DNA is old or of poor quality
        Use high quality, new DNA.
      Possible cause: Not using nuclease-free buffer in DNA quantitation
        Use nuclease-free buffer.
      Possible cause: Poor dilution methods
        Use appropriate dilution method in tubes.

Reader Over-ranging in Fluorescence
      Possible cause: The Sensitivity in the Read Step dialog is currently set too high
        Lower the Sensitivity setting. Refer to the Sensitivity table on page 157 for valid
        values.
        If using Automatic Sensitivity Adjustment, try the Scale to High Well option and
        set the High Value in the range of 50,000 to 70,000 for standard range.

Bandwidth Verification Failed
      Error or warning messages are issued when Gen5 detects overlapping
        wavelengths or bandwidth
        Select/enter Filter Set wavelengths that do not overlap. Learn more about Gen5's
        bandwidth verification in Gen5's Help.

Error during Auto-Sensitivity Determination
      Reader cannot fulfill request to determine optimal Sensitivity
        Gen5 displays an error message when the reader cannot determine the optimal
        sensitivity based on the defined reading parameters.



172 | Chapter 8: Fluorescence and Luminescence



        Luminescence integration time should be <= 1 sec and > 1 ms, especially when
          scaling to low wells.
        Manually enter a Sensitivity value or use an alternative method to determine the
          optimal sensitivity, if the error persists. Learn more in Gen5's Help.







Filters and Mirrors

Changing Filter Wheels
    Important! It is essential to conform to the specific BioTek instrument procedures for
    altering the filter wheel configuration. The reader does not automatically detect which
    filters are installed. Before the instrument is shipped from the factory, BioTek updates the
    reader's internal software with the current filter wheel settings. When you make changes
    to a filter wheel, it is your responsibility to ensure that Gen5's wavelength table exactly
    matches the new contents of each filter wheel. For specific instructions on changing filters,
    see the reader's operator's manual. In order to obtain accurate results and prevent damage
    to the PMT, they must match exactly.

          To exchange wavelength information between Gen5 and the
            instrument, the two must be communicating: the reader must be
            turned on and properly configured in Gen5.

    In Gen5, there are two ways to update the reader with filter wheel configuration:
           use the Fluorescence/Luminescence tab of the Reader Setup (System>Reader
             Configuration>View/Modify>Setup) to ensure the wavelengths table matches
             the filters installed in the attached reader
           use the Filter Wheels Library (System>Optics Library>Filter Wheels) to select a
             pre-defined wheel and send its values to the reader.


Filter Wheels Library
    System> Filter Wheels

          Only for Fluorescence- and Luminescence-equipped readers

          Refer to the reader's Operator's Manual for instructions for physically
            changing the filter wheel

About the Filter Wheels Library
       Gen5 provides these controls to create a catalog of your Fluorescence and
       Luminescence excitation and emission filter wheels. If you regularly change filter
       wheels, this feature provides significant time savings: define the filters in each wheel
       once, and with one click, update the reader's internal software to match the
       configuration of the selected wheel.
       When you add new filters to the catalog, Gen5 offers them for selection when you're
       defining a Read step. This feature lets you create protocols, i.e. define reading
       parameters, using filters that are not currently installed in the reader. The Read Plate
       Prompt Option will ensure that users are alerted when they try to run a Procedure that
       calls for filters not currently installed.



174 | Chapter 8: Fluorescence and Luminescence



        Gen5 considers filter wheels to have distinct uses, they are either Excitation or
        Emission wheels. BioTek ships wheels labeled either EX for excitation or EM for
        emission. The Time-Resolved Fluorescence, TR cartridge for the Synergy HTTR is NOT
        eligible for this catalog.
        Some Read-step parameters, e.g. Light Shuttering, require a special filter-wheel
        configuration. This feature provides a short-cut for setting up this type of experiment.
        After creating a record for the special wheel in the library, you can simply exchange
        the wheels and with one click, update the reader's settings.

How to use the Filter Wheels Library
     Select System>Filter Wheels to perform these functions:
         1.   First, the library records (descriptions of your filter wheels), must be created
              (page 175)

         2.      When records have been added to the library, select the Type of wheel you
              want to view or modify using the drop-down list. The list box shows all
              previously defined wheels of that type.
         3.   Highlight a record and click View/Modify to see or change the details of a
              record or Delete, as needed.




         4.   Select a Read Plate Prompt Option:
               Select the Always prompt option to tell Gen5 to always open the Filter
                 Wheel Selection dialog whenever the Procedure is Validated and when a
                 plate is read
               Select the Only prompt option to tell Gen5 to only open the dialog when
                 the Read step calls for a filter that is not in a currently installed wheel

         5.               After you have physically exchanged a filter wheel, when you
              want to update the reader's internal software to match a selected wheel, click
              Set Reader. This performs the same function as the Reader Setting's Setup
              option.0.


        Updating the reader with a filter-wheel configuration from the Filter Wheel Library
     also updates the Reader Configuration> Reader Settings> Fluorescence/
     Luminescence Filters table






Creating and Modifying Filter Wheels
    System> Optics Library> Filter Wheels> Add or View/Modify

  Creating new filter wheel records
   To add a new filter wheel to your library:
        1.   Select System> Optics Library> Filter Wheels
        2.   Click Add...
        3.   Name the new filter wheel
        4.     Select the Wheel Type: Excitation or Emission
        5.   Select the filter Type using the drop-down list for each Filter position in the
             Excitation and Emission filter wheels.
        6.   When applicable for the filter Type, enter Wavelength and Bandwidth values
             in the fields.

         The Wavelength value and its accompanying Bandwidth, in
           nanometers, are etched into the filters. For example, the
           Wavelength/Bandwidth combination of 485/20 will transmit light from
           475 to 495 nm (10 nm on either side of the center). See the reader's
           operator's manual for details.

        7.   When the filter wheel is fully defined, click OK. 0.

  Special filter position requirements for the Synchronized Modes:
   For Dispensing Protocols and certain other procedures, Gen5 offers an option: Close Light
   Shutter, to block the light between measurements to inhibit photo bleaching:
          Single filter-set protocols: When light blocking is enabled, a blocking filter
            (Plug) must be placed in the excitation filter wheel in one of the two positions
            next to the excitation filter that is specified in the protocol.
          Dual filter-set protocols: When light blocking is enabled, two blocking filters
            (Plugs) must be placed next to each other in the excitation filter wheel, except
            for Synergy 2 and Synergy 4, which need only one plug anywhere in the filter
            wheel.

         Gen5 issues an error message when the configuration of the filter
           wheel does not match the requirements of the Procedure/Read step.


Filter Wheel Configurations
   The valid combination of filters, plugs, and holes in a filter wheel depends on the reader
   model.
   Band Pass - standard interference filter with a defined central wavelength and bandwidth.



176 | Chapter 8: Fluorescence and Luminescence



     Plug - light blocker or solid plug in the filter wheel. A plug in the Excitation filter wheel is
     typical for luminescence assays, to prevent ambient light from entering the measurement
     chamber.
     Hole - empty space in the filter wheel to allow unfiltered light to pass through. An empty
     location in the Emission filter wheel is typical for luminescence assays.

Synergy 4 Readers Only support:
     Long Pass - an "edge pass filter" with a cut-on Wavelength where the filter stops reflecting
     and starts transmitting light. It can be used in the Emission filter wheel.
     Short Pass - an "edge pass filter" with a cut-off Wavelength where the filter stops
     transmitting and starts reflecting light. It can be used in the Emission filter wheel.
     Mono LP - positioned in the Excitation wheel for use as an order-sorting filter by the dual
     monochromator.

           Important filter wheel requirement: to perform monochromator
             reads, the reader's excitation filter wheel must contain a Hole and a
             Mono LP filter. And, when light shuttering is required, there must be a
             Plug between the Hole and the Mono LP filter.


Mirrors and Mirror Holders
     Before shipping the reader, BioTek configures the reader's internal basecode to match the
     mirrors installed in the reader. Unless you are changing the current configuration do not
     alter the settings.
     Your reader's Operator's Manual provides detailed instructions for maintaining and
     changing mirrors and mirror holders.


About Mirrors
        For all top-reading filter-based fluorescent reads, Fluorescence Intensity (FI),
        Fluorescence Polarization (FP), and Time-Resolved Fluorescence (TRF), the Synergy 2
        and Synergy 4 use mirrors to direct light to the sample and obtain measurements from
        it. Up to three mirrors, either 50%, Dichroic, or custom, can be installed in the reader.




        Mirrors reside in a mirror holder with three possible reading positions. Any mirror can
        be used for any type of experiment, except FP (Fluorescence Polarization), which






      requires using the mirror in position 3, because it holds the polarizing lenses. Keep in
      mind when using dichroic mirrors that the filter sets must match the wavelength
      range.
      The mirror holder (pictured above) is a rectangular box located inside the reader.
      (Additional mirror holders can be purchased as an accessory and kept track of in the
      Mirror Holder Library.) The mirror holder and the mirrors are user-changeable. You
      can replace the entire holder with a different one; this is the recommended option. Or,
      alternatively, you can install different mirrors in the mirror holder. Contact BioTek for
      more information on purchasing additional mirrors and holders. Refer to the reader's
      Operator's Manual for replacement instructions.
      The reader cannot detect which mirrors are installed in it. Whenever you change a
      mirror holder or the mirrors in the holder, use Gen5 to update the reader's internal
      basecode to match the new hardware.
      Gen5 provides two ways to download information about your mirrors to the reader:
             Update the Mirror Configuration table when you have only one mirror
               holder
             or use the Mirror Holder Library when you have multiple holders



Dichroic Mirrors




      Dichroic mirrors have to match the Excitation and Emission filters. If the excitation
      filter and dichroic do not match, the excitation light goes through the mirror, instead of
      reflected to the sample and the sample does not get excited. If the emission filter and
      dichroic don't match, even when the excitation light is reflected to excite the sample,
      the emission light is also reflected by the mirror and goes back to the light source
      instead of the detector (PMT).
      Mirrors and filters are defined under Reader Configuration and then, offered for
      selection when the Procedure is being defined. Filters can also be defined in the Filter
      Wheel Library.



178 | Chapter 8: Fluorescence and Luminescence



        When defining and performing a Read step, the filter set must be compatible with the
        mirror. 50% mirrors do not have wavelength requirements; they can be used with any
        filter sets. But Dichroic mirrors require the filter's central wavelength to fall within the
        mirror's EX and EM Min-Max range.

                                            In the Read Step dialog, hover your mouse
                                            over the Optics Position to see a tool-tip
                                            that lists the Excitation and Emission range
                                            for the selected dichroic mirror. Either select
                                            filters that fall within the Ex and Em ranges
                                            (respectively) or change the selected mirror.




Mirrors Configuration
     System> Reader Configuration> View/Modify button> Setup button
     Normally, these controls are only needed when you are changing a mirror or mirror
     holder

To change the current settings and download them to the instrument:
        When you exchange a mirror or mirror holder, follow these steps to update the reader:
         1.   Select System> Reader Configuration
         2.   Double-click the reader to be updated. This opens the Reader Settings dialog.

         3.   Click
         4.   Select the Mirrors tab
         5.   For each Mirror position, 1, 2, 3, use the drop-down list to select the Type of
              mirror. Gen5 assigns a Label based on your selection. For details about the
              valid values see Define a Mirror Holder on page .
         6.   For a Dichroic mirror, you must enter its wavelength range. Refer to the fact
              sheet provided with the mirror to enter the values for the Excitation Minimum
              and Maximum and the Emission Minimum and Maximum. Gen5 creates the
              Label for the mirror based on your input.
         7.     with Polarizers: if the mirror holder is equipped with polarizing lenses,
              enable this option in Gen5.
         8.   When the actual mirrors in the mirror holder are described correctly in the
              table, click Send Values to download the data to the reader.0.






Define a Mirror Holder
   Gen5 provides two ways to manage information about your mirror holders:
              Use the Mirror Holder Library when you have multiple holders
              Otherwise, you can simply update the Mirrors table

  To define the mirrors in a Mirror Holder:
        1.   Either update the library or the mirror table:
              Select System> Optics Library> Mirror Holders> Add or Modify
              Select System> Reader Configuration> Reader Settings> Setup >
                Select the Mirrors tab
        2.   For each Mirror position, 1, 2, 3, use the drop-down list to select the Type of
             mirror. Gen5 assigns a Label based on your selection:
              50% = works with any wavelength. It is a glass slide with small, reflective
                silver dots; 50% of the surface reflects light, 50% of the surface transmits
                light. It's Label is Top 50%.
              Dichroic = works with a specific wavelength range; they are transparent to
                one part of the spectrum and block the other part. You must know the
                mirror's specific excitation and emission wavelength range to properly
                configure the reader.
              Custom = select this option when your mirror is neither a 50% nor a
                dichroic. Gen5 lets you select any combination of filters when defining a
                Read step using a custom mirror. Assign it a Custom Name to distinguish it
                from other mirrors. You can use up to 8 characters.
              None = select this option when there is an empty position in the mirror
                holder. It is not given a label and this position cannot be selected when
                defining a Read step.
        3.   For a Dichroic mirror, you must enter its wavelength range. Refer to the fact
             sheet provided with the mirror to enter the values for the Excitation Minimum
             and Maximum and the Emission Minimum and Maximum. Gen5 creates the
             Label for the mirror based on your input. Learn more...
        4.     with Polarizers: if the mirror holder is equipped with polarizing lenses,
             enable this option in Gen5.0.

  Mirror Labels
   Gen5 assigns each mirror a Label as you define or modify them. Mirrors are only used
   when top reading (rather than bottom reading) is performed on the plate, thus all labels
   (except Custom) begin with Top:
              50% mirrors are always labeled Top 50%.



180 | Chapter 8: Fluorescence and Luminescence



                For dichroic mirrors Gen5 calculates the average of the Excitation Max and
                  Emission Min and assigns this value as the label. For example, Top 400
                  becomes the label when the EX Max = 390 and the EM Min = 410.
                Labels for custom mirrors are the user-defined Custom Name.


Mirror Holder Library
System> Optics Library> Mirror Holders...

           Refer to the reader's Operator's Manual for instructions for physically
             changing the mirror holder

About the Mirror Holder Library
     Gen5 provides these controls to create a catalog of your Mirror Holders. If you regularly
     change mirror holders, this feature provides significant time savings: define the mirrors in
     each holder once, and with one click, update the reader's internal software to match the
     configuration of the installed holder.
     First you must create a library record for each mirror holder. Then, after you physically
     change a mirror holder, you can select its record and instantly update the reader's internal
     mirror table.
     When you add new mirrors to the catalog, Gen5 offers them for selection when you're
     defining a Read step. This feature lets you create protocols, i.e. define reading parameters,
     using mirrors that are not currently installed in the reader. The Read Plate Prompt Option
     will ensure that users are alerted when they try to run a Procedure that calls for mirrors
     not currently installed.

           Changing mirrors in a mirror holder: the library is intended to
             keep track of multiple mirror holders. When you are limited to
             changing individual mirrors in a single mirror holder, it is quicker and
             easier to simply update the reader's internal mirror table using the
             Reader Setup controls.

  How to use the Mirror Holder Library
     Select System>Optics Library>Mirror Holders to perform these functions:
          1.   First, the library records (descriptions of your mirror holders) must be created.
               See Define a Mirror Holder on page 179.
               When records have been added to the library the list box displays them.
          2.   Highlight a record and click View/Modify to review or change its details or to
               Delete it, as needed.






       3.   Select a Read Plate Prompt Option:
             Select the Always prompt option to tell Gen5 to always open the Filter
               Wheel Selection dialog whenever the Procedure is validated and when a
               plate is read
             Select the Only prompt option to tell Gen5 to only open the dialog when
               the Read step calls for a filter that is not in a currently installed wheel

       4.                 When you want to update the reader's internal software to match
            a selected mirror holder, click Set Reader. This performs the same function
            as the Reader Setting's Setup option.


Select a Mirror Holder
System> Optics Library> Mirror Holders...

   These controls are presented during Procedure Validation and plate processing when Gen5
   is instructed to "Always prompt before a procedure" or when the Read step calls for
   mirrors that are not currently installed in the reader.

  When validating a Procedure
   Gen5 opens the Mirror Holder Selection dialog when validating a Procedure to offer any
   mirror holder that meets the requirements of the read step:
       1.   Highlight a holder in the Available Mirror Holders box
       2.   Click Continue to validate the Procedure using the selected filter wheel.0.

  When executing a Procedure
   Gen5 displays an error message and, if a valid mirror holder is available, opens the Mirror
   Holder Selection dialog when the Procedure calls for a mirror that is not currently
   installed in the reader. Only holders that meet the requirements of the read step are
   offered for selection in this scenario.
       1.   Highlight a holder in the Available Mirror Holders box
       2.   Click Update Reader to select the mirror holder you will install.
       3.   Physically change the mirror holder in the reader. Follow instructions provided
            in the Operator's Manual. After it is changed and the reader is turned on and
            has completed its self test, return to Gen5 and click Send Values. The reader's
            mirror table is not updated until this final step is completed.0.

  When using the Mirror Holder Library

                 From the Mirror Holder Library, click Set Reader... when you want to
   update the reader's internal software to match the configuration of a selected holder



182 | Chapter 8: Fluorescence and Luminescence




Multi-Detection/Multi-Mode Protocols




                          SynergyTM HT and SynergyTM 2/4 Only

Prerequisite

  Currently only BioTek's multi-detection readers Synergy HT, Synergy 4 and
    Synergy 2 are capable of running multi-mode protocols.

        Gen5TM lets you perform multiple detection methods on a plate within one protocol.
        Examples
           Stand-Alone Multi-Detection Protocol - You can define independent read
             steps, performing each read with a different detection method. Other
             Procedure steps (e.g. Shake) can be included in the sequence, following the
             rules for all types of protocols.
           Kinetic Multi-Detection Protocol - You can perform a multi-detection kinetic
             analysis, conducting the reads within a kinetic loop, reading each plate with a
             different method in sequence. Reads must be done in Standard Plate Mode (not
             in Synchronized Mode).


           Read the permissions and restrictions for conducting multi-detection within a
        kinetic loop on the next page and view examples on page 184.







Features and Restrictions of Kinetic Multi-Detection
Protocols

Supported features:
            Up to 6 wavelengths for Absorbance reads
            Up to 2 filter sets for Fluorescence and Luminescence reads
            Time-Resolved Fluorescence (TRF)
            Automatic Sensitivity Adjustment
            All other valid combinations of Procedures can precede or follow the
              kinetic loop

Limitations:
            Only Standard (non-synchronous) plate mode reads are supported
            Up to 3 read steps can be performed in a multi-detection kinetic loop
            A Shake step is the only reading-related activity that can be inside a multi-
              detection kinetic loop
            Synergy HT cannot perform a time-resolved fluorescence and standard
              fluorescence read in the same kinetic loop (nor in the same protocol).
              Synergy 2/4 can perform TRF and other types of fluorescence analysis (FI
              and FP) within a kinetic loop when every read within the loop uses the
              same light source. TRF requires use of the Xenon Flash, so you must select
              this light source for any other fluorescence read within the kinetic loop
            A continuous shake event must be the first step in the sequence
            When more than one kinetic loop is defined you cannot "Append to
              previous Kinetic data" as is possible in a mono-detection kinetic Procedure

Features that are not supported:
            Spectrum and Scanning read types
            Pathlength correction
            Dispense steps (Readers with Injectors)
            (but you can work around this limitation, see Dispensing Reagent in a
              Kinetic Analysis Protocol in Gen5's Help)



184 | Chapter 8: Fluorescence and Luminescence




Examples of Kinetic and Stand-Alone Multi-Detection Procedures
     In a Kinetic Multi-Detection Protocol readings are performed sequentially in a kinetic
     loop




        In a Stand-Alone Multi-Detection Protocol readings are performed independently
