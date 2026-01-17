# Chapter 10: Scanning Analysis Options

     Gen5, depending on the capabilities of the current reader, makes it
     easy to conduct an area or linear scan of wells in a plate, or a
     multi-wavelength spectrum scan. Selecting one of these methods
     also enables Well Analysis data reduction features. This chapter
     provides details about these capabilities.


 Area Scan ............................................................................... 200
 Linear Scan ............................................................................. 202
 Spectrum Scan ........................................................................ 203



200 | Chapter 10: Scanning Analysis Options




Area Scan
        When the reader is capable of performing an area scan, Gen5 provides three ways to
        control the output of the captured measurements:
            Scan Options, defined in the Read Step of the Procedures, determine the Read
              Matrix Size. The potential Read Matrix Size is a function of the well size of the
              current plate.
            Calculation Zone, defined in the Well Analysis Data Reduction step, lets you
              limit the values reported, ignoring the lowest OD/RFU measurements for
              example, for meaningful results
            Display Options provide more control over the appearance of the results,
              letting you limit the results displayed based on their measurement values and
              changing the color scale applied to the values for a better presentation of the
              results.

           The Synergy 2's and Synergy 4's probe size limits its ability to perform
             Fluorescence area scan in plates with a small well diameter. Generally,
             this means you must use a plate with fewer than 96 wells.

           While you can control the temperature (and incubate the plate) for
             these types of reads, due to a reader limitation, area and spectral
             scans do not report the temperature on-screen or in reports or export
             files.

Calculation Types
                Gen5 calculates and reports the Mean OD/RFU, Standard Deviation and
                  Coefficient of Variation of samples

Viewing and Reporting Results
      When a Well Analysis data reduction step has been defined, Gen5 displays a graphical
      representation of the measurements taken across the well:
          1.   In the Matrix tab of the Plate workspace, use the drop-down list of available
               Data sets to display the set labeled Scans
          2.   Click in a cell to show its Well Zoom

           As described in Display Options above, Gen5 offers extra controls for
             adjusting the view of Area Scans. Perform the next step, Step 3, to
             access the controls, which are especially useful for customizing reports
             of the scan results.


          3.      Click the 3-dot button next to the Curve field to open the controls for
               adjusting the view.0.






In Gen5's Help you can find detailed instructions to:
      Assign a different Title for the graph displayed
      Hide or show the Color Scale legend
      Change the online view to Gray Scale to match the output from non-color
        printers
      Change the Data Range and Color Range applied to the results



202 | Chapter 10: Scanning Analysis Options




Linear Scan
        When the reader is capable of performing a linear scan, Gen5 plots a curve for each
        well using the reading points in the scan.
            Scan Options: You define the number of reading points in the Read Step of the
              Procedure

           PowerWave-series readers require updating the Filter Table with the
             wavelength you want to scan before reading the plate. Enter the
             desired wavelength in the table and click Send Wavelengths, then
             define the Read step.

Calculation Types
        Gen5TM offers the following types of well analysis for linear scan:
                Mean, Std Dev, CV: Gen5 calculates and reports the Mean OD, Standard Deviation
                  and Coefficient of Variation of samples when this calculation type is selected.

                  You can define the Calculation Zone, which is based on the number of Horizontal
                  Reading Points, which you define as Scan Options in the Read Step of the
                  Procedures




                Mean Min/Max
               Integral
        For each of these calculation types, you can adjust the Calculation Zone as desired.
        Click on the type to review your options and Gen5's default settings.

Viewing Results
          1.   After reading the plate, in the Plate workspace use the drop-down list for Data
               to select the data set labeled Curves
          2.   Click in a well to see the Well Zoom. When a Well Analysis data reduction step
               has been defined, a table beneath the curve shows the results. 0.







Spectrum Scan

Absorbance Spectral Scan
   During a Spectrum Read, multiple readings are taken across a wavelength range. The
   objective is to plot a graph with absorbance/RFU/RLU versus wavelength. Gen5
   automatically generates the spectrum data views:
           one multi-index raw data set: measurements taken at each wavelength
             one "Curves" data set (Well Zoom): plot of OD/RFU/RLU per wavelength for
              each well
    Readers that support Absorbance spectrum reads are uQuant, all models of the
    PowerWave and Synergy HT, Synergy 2, and Synergy 4. Only the Synergy 4 supports
    spectral scans for Fluorescence and Luminescence detection.

Fluorescence Spectral Scan
    Fluorescence spectrum analysis can be performed on either the Excitation or Emission
    wavelength, with the opposite wavelength set to a fixed value. And the range of
    wavelengths scanned can either be lower or higher than the fixed wavelength (with no
    overlap).
    Since it is recommended that each individual spectrum read limits the range of
    wavelengths to above or below the fixed wavelength, you can define multiple read steps in
    one procedure that straddle the fixed wavelength and/or alternate between EX and EM
    scans.
    For example, to determine the peak response at both an EX and EM wavelengths you
    could define a procedure like this:




    After reading the plate and reviewing the results, you may want to modify the fixed
    wavelengths to match the peak responses.

          Gaps in a spectral curve: over-range or immeasurable values, in
            combination with Gen5's automatic spectral raw data correction, can
            cause unexpected gaps in a curve. Lower the Sensitivity setting and
            reread the plate to obtain reliable data.



204 | Chapter 10: Scanning Analysis Options



Calculation Types
                Min/Max is the Well Analysis option Gen5 offers for spectrum scans. It
                  generates the data sets: Mean Minimum OD and Wavelength at Mean
                  Minimum OD, Mean Maximum OD and Wavelength at Mean Maximum
                  OD


Define the Calculation Zone:
                 You can refine the results output of the well analysis:
                Reduce the range of wavelengths upon which to perform the calculations.
                  The default zone corresponds to the Start (beginning) wavelength and the
                  Stop (ending) wavelength defined in the Procedures.
                Reduce the number of spectrum reads upon which to perform the
                  calculations. The default zone is the total number of wavelengths to be read
                  based on the Procedure settings: from read 1 to the total number of reads
                  calculated from the Start, Stop and Step values. Limiting the number of
                  reads is another way to effectively reduce the wavelength range (nm)
                  considered in the calculation.
                Set the number of points on which to average/calculate the minimum and
                  maximum values. The default number of points is 1 (each read stands alone
                  to determine the min and max). The valid entry range is from 1 to the total
                  number of reads calculated from the Start, Stop and Step values.

                  When you increase the number of points, Gen5 first identifies the mean
                  value for the specified number of consecutive reads, and then determines
                  which of them is the min and max. For example, if you define 2 as the
                  number of points, Gen5 determines the mean of the first two reads, the
                  second two reads, the third two reads, etc., to perform the calculation. This
                  option is most useful when there are numerous reads to work with.

Viewing the Spectrum Scan
          1.   After reading the plate, in the Plate workspace use the drop-down list for Data
               to select the data set labeled Spectrum Curves
          2.   Click in a well to see the Well Zoom. When a Well Analysis data reduction step
               has been defined, a table beneath the curve shows the Well Analysis Results
               and you can use the View Data and View Chart toggle button to see the basis
               for the curve.

          3.       Click the 3-dot button next to the Curve field to change the appearance of
               the well zoom. 0.


          You can display multiple well zooms simultaneously by holding down the Ctrl key
        while selecting (up to 8) wells.
