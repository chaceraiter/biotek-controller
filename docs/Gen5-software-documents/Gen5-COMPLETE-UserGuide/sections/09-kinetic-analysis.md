# Chapter 9: Kinetic Analysis

     This chapter focuses on the tools and techniques available for
     creating a kinetic analysis assay.


 How to set up a Kinetic Analysis ................................................ 186
 Kinetic timelines ...................................................................... 186
 Kinetic Minimum Interval .......................................................... 188
 Discontinuous (Long) Kinetic Procedure ...................................... 189
 Well Zoom .............................................................................. 191
 Well Analysis Calculation Types.................................................. 196



186 | Chapter 9: Kinetic Analysis




How to set up a Kinetic Analysis
     Begin with Protocol> Procedure
         In the Procedure, for kinetic analysis, you set up the timelines and intervals to define
         the number of reads per wavelength and any other required activities. If you're
         performing time-sensitive studies review the Synchronized Mode options in the
         Fluorescence and Luminescence chapter.

To set up a kinetic analysis protocol or time course work:
          1.   Open Procedures (Protocol> Procedure)
          2.   Click Kinetic. Gen5 opens the Kinetic Step controls. Define the timelines (see
               the next page for more information):
                Use the spin buttons or click in the Run Time and Interval fields and enter
                  the desired time settings. Alternatively, let your reader determine the
                  Minimum Interval for the desired Run Time. Follow these instructions for
                  applying the Minimum Interval on page 188.
                Gen5 adds a kinetic loop to the Procedure.
          3.   With the End Kinetic step of the kinetic loop highlighted, click Read to add at
               least one read step to the loop. If desired, include a Shake step before the read.
               (Scanning and Spectrum reads are not supported.)
          4.   Add other steps, including other kinetic loops, to the Procedure, as needed.
               Click Validate to make sure the current reader is capable of processing the
               sequence.
          5.   Next, go to Data Reduction. At least one Well Analysis calculation is
               automatically created for you. Double-click the Well Analysis step to view or
               modify it. Add more Well Analysis or other calculations, as needed. 0.


Dispensing Reagent in a Kinetic Analysis
      Select Help>Help Topics in Gen5 to review suggestions for including a dispense step
      in your Kinetic Procedure.


Kinetic timelines
         Numerous factors affect the runtime parameters for a kinetic loop. The minimum
         interval for readings can be increased or decreased by the defined reading parameters.
         Here are some facts to consider and some limitations of the BioTek readers:






Reading parameters that can affect kinetic timelines:
      Plate size: a 96-well plate can have a shorter minimum interval and obtain more
        reads than a 384-well plate in the same runtime duration. Similarly, reading a
        partial plate generates more reads during the same time period.
      Read Speed in Absorbance reads: more reads can be obtained in Rapid mode than
        at Normal speed
      Measurement Options in Fluorescent reads: you can control the read speed (and
        affect the kinetic timelines) by adjusting the number of measurements per data
        point, and the delay after plate movement
      Integration Time in Luminescent reads: you can control the read speed (and affect
        the kinetic timelines) by adjusting the read duration for each well
      Number of steps in the kinetic loop: adding steps, a Shake and one or more Read
        steps, to the kinetic loop effects the timelines
      Duration of a Shake step in the kinetic loop is added to the Run Time

Reader limitations:
      All readers are limited to obtaining 9999 reads in Absorbance mode within the 168
      hour timeline. The longest interval between reads is 2.5 hours. Fluorescence and
      Luminescence kinetic reads and intervals are reader dependent:

        Reader                              Total #         Max
                                            Reads           Interval

        Synergy HT: Standard mode           300             9999 sec

        Synergy 2/4: Standard mode          9999            9999 sec

        Synergy HT/Synergy 2/4:             999             9999 sec
        Synchronized Plate

        Synergy HT/Synergy 2/4:             999             99.99 sec
        Synchronized Well

        Flx800: Standard mode               300             9999 sec

        FLx800: Synchronized Plate          300             9999 sec

        FLx800: Synchronized Well           300             12.00 sec



188 | Chapter 9: Kinetic Analysis




Kinetic Minimum Interval
         Here are instructions for letting Gen5 determine the shortest valid kinetic interval:

           Prerequisite: Your reader must be connected and turned on, i.e.
             communicating with Gen5, to determine the minimum interval

         Gen5 communicates with the reader to determine how quickly the Kinetic loop can be
         processed. You must click the Validate button to trigger this communication. Follow
         these steps:
          1.   In the StepWise Procedure, click Kinetic to add a loop
          2.   Define the Run Time for the Kinetic loop and select       Minimum Interval,
               click OK
          3.   Add a Shake step if desired and define one or more Read steps with the
               required wavelengths/filter sets and other conditions. For an Absorbance read
               you can increase the Read Speed, for faster processing. For a Fluorescence
               analysis, you can modify the Filter Set Options to speed up processing.

          4.             Click the Validate button. Gen5 will display a confirmation
               message and the Interval will be defined.

What you'll see
         You'll notice that the description of the Start Kinetic step will change from "generate
         minimum interval" before you hit the Validate button to a specific time setting for
         Interval:




           Important: Gen5 replaces the "minimum interval" setting with an
             actual interval time. If you subsequently make changes to the
             Procedure that have an effect on the kinetic interval, e.g. increase the
             plate size or add another read step, the minimum interval must be
             recalculated.






Discontinuous Kinetic Procedure
   Procedure> Kinetic> Read

About Discontinuous Kinetics
      For cell growth assays and similar types of studies, Gen5 provides a way to take
      readings over a long time period without tying up the reader, so it can be used in other
      experiments during the rest or incubation periods. Gen5 calls this type of analysis:
      Discontinuous Kinetic, because the measurements obtained from the multiple readings
      are combined, resulting in a multi-read data set. There is virtually no time limit to this
      type of procedure.
      Limitations of Discontinuous Kinetics:
         Endpoint and Kinetic reads are supported, but Area Scan, Linear Scan, and
           Spectral Scans are prohibited
         Synchronous Mode is not supported, i.e. you cannot perform readings in
           Synchronized Plate or Well Mode
         Stop/Resume steps are prohibited, i.e. you cannot include a Stop/Resume step
           in the Procedure

        Gen5's Data Reduction Well Analysis Options are available for this type
          of experiment

How to set up a Discontinuous Kinetic Experiment:
       1.   Create a new Protocol in the usual way

       2.                      When defining the Procedure, select Advanced Options,
            and select the Discontinuous Kinetic Procedure option
       3.   Enter "estimated" time points in Days:Hours:Minutes: for the Estimated total
            time and Estimated interval
            This is just an estimate, and will not interfere with actual experiment activity.
            Gen5 uses your estimated time lines to set up the data views and formulas with
            placeholders until the actual data is captured. When in doubt about the
            required time period and intervals, it is best to over-estimate them. See the
            example on the next page.
       4.   Define the Read step(s) as usual, and save the Protocol
       5.   Create an Experiment based on the Protocol, and conduct the first Read on the
            plate
       6.   Close and save the Experiment
       7.   Remove the plate and process (e.g. add reagent) or store it (e.g. incubate), until
            it is time for the next reading
       8.   Open the Experiment, put the plate on the carrier, click the Read button, and
            select Next Read



190 | Chapter 9: Kinetic Analysis



          9.   Repeat steps 5-7 until all the required reads are completed0.
         Gen5 compiles all the reads into a kinetic data set, and performs Data Reduction, e.g.
         Well Analysis, as defined in the Protocol.

   Example of Discontinuous Kinetic Estimated Time Points
           If you expect to read the plate twice a day for 3 days, but an extended time period
           may be needed, enter 5 days for the Estimated total time, and 12 hours for the
           Estimated interval:







Well Zoom
      Performing a multiple-read Read Step generates the Well Zoom feature, which lets you
      zero-in on each well of the microplate to view the reading results for individual wells.
      Multiple wells can be selected for simultaneous viewing. Setting up Well Analysis as a
      Data Reduction step enhances the view, displaying the calculation results for each
      well.

          Gen5 automatically creates one Well Analysis step when you define a
            kinetic loop




How to:

          Tip: To use this feature to monitor kinetic readings in real time, perform these
      steps before you start the reading. However...see the note below.

          1.   After reading the plate, open the Plate View that represents the plate
          2.   In the Matrix view, use the drop-down list of available Data sets to display the
               set labeled Curves. (The raw data set upon which a Well Analysis data
               reduction has been performed offers the most useful display, for example: When
               you assign blanks to the plate, Gen5 first creates a blank-subtraction data set, and
               then performs well analysis on that data set. Gen5 creates a Curves data set based on



192 | Chapter 9: Kinetic Analysis



               this well analysis, e.g. Curves [Blank 450] where 450 is the wavelength of the reading.
               Select this data set for the best well zoom.)
          3.   Click any well in the matrix to see its Well Zoom view.0.

           Do not display Gen5's "Curves" data in the Plate View while
             performing a kinetic analysis. Wait until the read step is finished
             before viewing the "Curves" data set. Displaying the Curves data set
             during a Kinetic read can consume excessive resources resulting in
             performance degradation. You can drill down to a Well Zoom to
             monitor the progress of one well, then, leaving the Well Zoom open,
             change the Matrix Data to a numeric view.

Open the Well Zoom View




     Set the Data set in the Matrix view to Curves, and click in a well for the Well Zoom


           Hold the Ctrl key, while selecting up to 8 wells in the Curves data set of the Plate
         View, to see all the well results simultaneously (except for Area Scans)


                                   Use the View data/View chart toggle button to show the
         data in either a table or graph. See examples beginning on page 198.

View Multiple Wells Simultaneously

            Click the 3-dot button next to the Wells field to select multiple wells to view in one
         graph. This is dynamic, so you can select and de-select the wells you want to see. Up to
         8 wells can be selected at one time.






Zoom Zoom




      Within a well zoom you can further zoom in on selected data points:
       1.   Click and drag your mouse over an area of the well zoom. The pointer changes
            to a cross as Gen5 maps the selected area. Gen5 presents a pop-up menu when
            you release the click
       2.   Select an option from the menu:0.
             Zoom In or Zoom Out
             Mask or UnMask Points

Well Zoom Plotting
      When Gen5 plots the well zoom curves, the X axis represents the individual reads for
      the well, and the Y axis represents the measurements:

             Y Axis X Axis
             ODs      Kinetic read times
             RFUs     Spectrum wavelengths

             RLUs     Linear horizontal positions



Well Analysis Results Table
      When a Well Analysis Data Reduction step is defined, Gen5 shows the calculation
      results in a table beneath the curve. The "Curves" or "Scan" data set that leads to a well
      zoom, must be the subject of a Well Analysis step; raw data well zoom views do not
      include a Well Analysis Results table.



194 | Chapter 9: Kinetic Analysis



Calculation Zone
         The range of reads considered for analysis is determined by the Calculation Zone
         setting of the Well Analysis. When the original range is reduced, Gen5 plots the
         revised Calculation Zone with brackets: [ ]

Viewing Appended Kinetic Results
         When one or more kinetic reads are appended, Gen5 combines them into one data set.
         When a Dispense step occurs between the kinetic loops, Gen5 represents the event as a
         blue diamond on the X-Axis timeline.

           FLx800 with Injectors may show the "Dispensing" event occurring
             in the same interval as a Read. This is a limitation of the reader's
             basecode or on-board software.


Customizing the Well Zoom View
         After launching the Well Zoom dialog, you can:
            Select a different Curve to display (if available)
                       At the Curve field, click the   drop-down list to select another data set
                       for the selected well
            Mask or exclude a data point and Recalculate
                  1.   Click on a data point to temporarily exclude or mask it from the
                       calculation, then click Recalculate
                  2.   Click on the data point again to restore it 0

           Important: modifying data may adversely effect or possibly invalidate
             results!

            Overlay up to 8 other kinetic curves on top of the current one

                       Click the     3-dot button next to the Wells field to select curves from
                       other wells to overlay onto the current one.
            Modify or Create a new table (to select the data displayed beneath
               the graph)

                        Click the      3-dot button next to the Results field to modify the
                           table.
                        Click the      drop-down list and select Create a New Table
                        Learn more at  Customizing Data Views, Reports, and Exports in the
                           Reporting Results chapter






 Display or hide a legend for the graph

        Click    next to the Curve field. On the Layout tab, click in the checkbox
        to Show the Legend or remove the checkmark to hide it.
 Modify the text and line formatting of the graph

        Click    next to the Curve field.
 Create a new graph (curve)

        Click    at the Curve field and select Create New Graph. You can combine
        multiple curves, if available, with this option, to simultaneously view the well
        results of each curve.



196 | Chapter 9: Kinetic Analysis




Well Analysis Calculation Types

           Also see the Data Reduction chapter for useful information

     Protocol> Data Reduction> Well Analysis
         Gen5TM offers the following calculation types when a multiple-index read step is
         defined. Each option has its own specific parameters, which you define by selecting the
         Calculation Options button.




            Mean V is the calculated value of the mean slope. It is calculated by a linear
              regression on points in the Calculation Zone. Define the Calculation Zone with
              the Calculation Options button. For Mean V, the zone is typically adjusted to
              ignore misleading data points generated at the beginning of a kinetic assay due
              to "noise."
            Max V is the calculated value of the maximum slope:
              1. Starting at the first point in the calculation zone, Gen5 evaluates n points
              and calculates the slope among these n points.
              2. Gen5 repeats the operation, starting at the second point in the calculation
              zone, and repeats it again, starting at the third point, and so on.
              3. Finally, Gen5 compares all calculated slopes to determine the maximum
              slope.
              Gen5 registers the Delta t time in the middle of the point where the Vmax is
              calculated. By default, the calculation zone starts at 2 points and at time zero.






   Select the Calculation Options button to modify the calculation zone.
   Gen5 also calculates the kinetic Lag Time, which is the time interval between
   the line of maximum slope of the propagation phase and the absorbance
   baseline at time = 0. Also calculated: Y Intercept, R and R2, delta time at Max
   V, and Max V minus minimum and maximum time.
 Mean Min/Max Mean Min is the mean minimum OD* based on n points. Mean
   Max OD is the mean maximum OD based on n points. Gen5 calculates the
   Mean Min and Mean Max ODs as follows:
   1. Starting at the first point in the calculation zone, Gen5 evaluates n points
   and calculates the mean among these n points.
   2. Gen5 repeats the operation, starting at the second point in the calculation
   zone, and repeats it again, starting at the third point, and so on.
   3. Finally, Gen5 compares all of the calculated means to determine the
   minimum and maximum of these values.
   Gen5 registers the Delta t time at Min/Max OD. Select the Calculation Options
   button to modify the calculation zone.
   *: For fluorescence and luminescence reads, Gen5 performs calculations based
   on fluorescence units (RFU) and luminescence units (RLU), respectively.
 Mean, Std, CV This option calculates and reports the Mean, Standard Deviation,
   and Coefficient of Variation for all points in the calculation zone. By default,
   the calculation zone includes all of the Reading Points defined in the protocol.
   To change the calculation zone, click the Calculation Options button.
 Onset OD Gen5TM reports:
   Onset Time: the time it takes to reach Onset OD*
   Onset OD: the user-specified value. It can be defined as an absolute value or a
   relative value based on the Basis OD
   Basis OD: is an optional value used to adjust all wells to a baseline. It is defined
   under Calculation Options as a fixed value or the "Mean of first n points"
   Basis Time: the time it takes to reach Basis OD,when defined
   *: For fluorescence and luminescence reads, Gen5 performs calculations based
   on fluorescence units (RFU) and luminescence units (RLU/sec), respectively.
 Integral calculates the area under the curve according to the trapezoidal
   method, shown here:




   Where y = measurement value and x = read point value.
   The area under the curve is displayed in the Well Zoom when this option is
   selected.
   By default, the calculation zone spans the full Run Time and includes all of the
   reading points defined in the protocol. Click Calculation Options to change
   the calculation zone.



198 | Chapter 9: Kinetic Analysis



            Formula allows you to calculate a value using data from individual reading
              points. Reading points are designated Rn, where n is the reading number. Use
              Wn for spectrum reads.
              The Formula is calculated for each well and results in one new data set named
              "Formula Result [nm]", where nm is the wavelength or filter set defined in the
              read step. When a Label is defined it precedes the naming convention: "Label:
              Formula Result [nm]".
              For example: (R1+R2)/2 + R10 is read point 1 + read point 2 divided by 2 plus
              read point 10.

   Well Zoom: View Chart/View Data




         Gen5 lets you toggle the Well Zoom view between a chart and a table. Click the View
         Data button to see the table, click the View Chart button to view the kinetic curve.
