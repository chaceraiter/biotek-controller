# Chapter 7: Defining the Procedure

     This chapter provides instructions for setting up Gen5's Procedure,
     the reading parameters.


 Defining the Reading Parameters ............................................... 122
 About Gen5's StepWiseTM Procedure ........................................... 123
 Validate the Procedure.............................................................. 125
 Read Step ............................................................................... 127
 Procedure Steps (Reading Related) ............................................ 137



122 | Chapter 7: Defining the Procedure




Defining the Reading Parameters
     Protocol> Procedure

        Set up the Procedure to control the reader: define the                 reading
        parameters and related activities of the Protocol/Experiment.

           Grayed out? When more than one plate has been read in an
             experiment, the Procedure cannot be changed for the current
             experiment. If this isn't the case, your System Administrator may have
             restricted your ability to modify the protocol elements.

           Grayed out buttons mean the action cannot be performed by the
             current reader or because previously defined steps, e.g. kinetic loop,
             limit the function.

How to:
          1.   Use the drop-down list to define the Plate Type
          2.   Click a button to add that step to the procedure. Most buttons open a screen for
               defining the parameters of that step, e.g. Read lets you define wavelengths, etc.
               When defining a kinetic or synchronized well/plate mode analysis, add the
               Kinetic or Synchronized Mode steps first. Kinetic and Synchronized Mode
               steps form a loop or block. Put the Read and other valid steps to be performed
               inside the loop, between the Start and End. Monitor Well is similar, first add
               the Monitor Well step and then, add a Read step inside the monitor-well loop.
          3.   Define the details of the step and click OK
          4.   Click Validate to check the selection and sequence of the steps0.

           Gen5 must be communicating with the reader to fully validate the
             Procedure. Make sure the reader is correctly attached, turned on, and
             not busy reading a plate or performing a test.

Features:
            You can Drag and Drop steps in the Procedure to change their sequence order
            Highlight a step in the Procedure, and then click an action button to add a step
              before it
            Double click a step to open it for editing
            Select a step in the sequence and right click for additional options
            Click Validate at any time to verify the reader's ability to perform the current
              sequence of steps
            Highlight a step and press Delete to remove it from the procedure






         Drag and Drop is limited in Synchronized Modes, for example, you
           cannot drag and drop a step into or out of a Well Mode block

Review the Validation Checklist on page 125

       Learn about: Synchronized Modes (for Synergy 2, Synergy 4; Synergy HT and FLx800
       with Injectors) in the Fluorescence and Luminescence chapter.


About Gen5's StepWise Procedure
       Gen5TM offers lots of flexibility in defining a Procedure: the read steps and related
       activities, like incubation, shaking (or mixing), dispensing reagent, and so on. Each
       activity or requirement is defined chronologically or StepWise.
       The StepWise Procedure can be simple, performing only one reading at one
       wavelength. It can also be complex, a series of events that includes multiple readings,
       incubation, shaking, and ejecting plates between reads to add reagent. The sequence of
       steps in the StepWise Procedure workspace defines the order of events performed by
       the reader.
       After a plate has been read based on the Procedure, it cannot be changed unless the
       data obtained is discarded. Gen5 offers several ways to modify the Procedure, as
       described on page 114.


The current reader determines the availability of options:
          Readers are set up under System>Reader Configuration.
          When more than one reader is connected to the PC, Gen5 opens the Instrument
            Selection dialog to let you select the desired reader before offering the
            Procedures dialog.
       Depending on your reader, the possible combination of steps in a Procedure is
       numerous. For example, you can:
              Set the Temperature followed by a Delay to reach the correct setting,
                before adding a multiple-wavelength Read step
              Give the plates a long time to react in an experiment by adding a
                Stop/Resume step between readings. This frees up the reader for use in
                other experiments during the down time
              Perform multiple Read steps, each interspersed with a Plate In/Out to add
                reagent, followed by a Shake step to mix the contents before performing the
                next read
              Define a kinetic analysis: Click Kinetic, followed by a Read step. Gen5 adds
                an End Kinetic event to close the kinetic loop
              Apply different read methods within a Procedure, performing a Scanning
                step, followed by a multi-read Endpoint step, and finish with a kinetic loop



124 | Chapter 7: Defining the Procedure



               Define one Read step for half the plate, and another Read step (with
                 different parameters) for the other half of the plate
               Perform a multi-mode or multi-detection experiment by defining
                 Absorbance and Fluorescence Read steps in the same Procedure
               and so on ...

                    Along with the reader's capabilities, the sequence of a step in the
        Procedure, especially the steps immediately before and after it, determines its validity.
        Click Validate to test the sequence of steps.







Validate the Procedure
  About Procedure Validation
          Gen5TM supports your effort to design a protocol by validating the Procedure
          based on the capabilities of the current microplate reader and the sequence of
          steps to be performed. Validation is also helpful at runtime, when a protocol may
          have been designed without a specific reader attached to Gen5, and the actual
          reader's capabilities are more limited than expected by the protocol. Gen5's
          validation feature will display an error message alerting you of the need to fix the
          Procedure.

       Important: Gen5 must be communicating with the reader to fully
         validate the Procedure.


                 Click the Validate button in the Procedure dialog to validate the reading
     events. Certain activities in the Procedure sequence, like Shake, cannot be standalone
     events, but must be related to a read or other activity. Here are the rules:

     Device Step                 Valid Combination/Limitations

     Read                        May be a standalone event. At least one read step is
                                 required.

     Set Temperature             May be a standalone event
                                 Cannot be inside a Kinetic loop
                                 Cannot be in a synchronous block

     Shake                       Shake >> Read
                                 Shake >> Start Kinetic >> Read >> End Kinetic
     These restrictions          Star? End Kinetic
     apply to all readers
                                 Shake cannot:
     except the Synergy
                                   precede a Spectral or Area Scan
     4, which supports a
     shake step anywhere            be included in a Well Mode block
     in the Procedure.
                                     be the first step in a multi-detection
                                      kinetic loop if the first read is
                                      Luminescence

     Dispense                    May be a standalone event

     Delay                       May be a standalone event
                                 Cannot be in a kinetic loop
                                 Cannot be between Shake and Read

     Kinetic                     Requires at least one read step
                                 Start Kinetic >> Read >> End Kinetic
                                 Sh? End Kinetic
                                 Start Kinetic >> Shake >> Read >> End Kinetic



126 | Chapter 7: Defining the Procedure




         Device Step                Valid Combination/Limitations

                                    Cannot include Scanning and Spectral reads
                                    Only one read step allowed in Synchronized Well
                                    Mode
                                    Only one read and one shake step allowed in
                                    Synchronized Plate Mode

         Monitor Well               Monitor Well >> Read >> End Monitoring
                                    Monitor Well >> Shake >> Read >> End Monitoring
                                    ? End Monitoring

         Plate In/Out               May be a standalone event
                                    Cannot be inside a Kinetic loop
                                    Cannot be in a synchronous block

         Stop/Resume                May be a standalone event
                                    Cannot be inside a Kinetic loop
                                    Cannot be in a synchronous block
                                    Cannot be the final event in a sequence

         Well Mode                  Requires at least one read step
                                    Excluding a Delay step:
                                    Synergy HT: can have up to 9 steps
                                    Synergy 2/4: can have up to 20 steps
                                    FLx800: can have up to 3 steps;
                                    Kinetic loop is limited to one read, except Synergy
                                    2/4 allows a Shake
                                    Multi-Detection kinetic loop is not allowed

         Plate Mode                 Requires at least one read step
                                    Synergy HT: can have up to 9 steps (excluding
                                    Delay)
                                    Synergy 2/4: can have up to 20 steps (excluding
                                    Delay)
                                    FLx800: can have up to 3 steps (excluding Delay)
                                    Kinetic loop is limited to one read and one shake
                                    Multi-Detection kinetic loop is not allowed







Read Step
   Protocol> Procedure> Read
  Define the reading parameters based on the capability of the current reader:
        1.   (Optional) Enter a Step Label or unique name for this step. Data sets based on
             the reading results will use the label in online views, reports, and export files.
        2.   Keep the Full Plate or set a portion of the plate to process.
             (The Plate Type is set for all steps in the Procedure.)
        3.   Select the Detection Method. Options are controlled by the current reader.
        4.   Select the Read Type. Options are controlled by the current reader and the
             detection method selected above.
        5.   Select the Read Speed from the list offered for the current reader
        6.   Set the Wavelengths or Filter Sets:
                1   Use the numbered buttons to set the number of wavelengths/filter sets
                    to obtain measurements with. Kinetic, Spectrum, Area and Linear Scans
                    limit this option.
                2   Click the down arrow or type in the text field to set the wavelengths.
        7.   If applicable, define:0.
              Pathlength Correction
              Optics Position
              Sensitivity and Filter Set Options
              Top Probe Vertical Offset


Read Types
   Depending on the reader, detection method, Gen5 product level, and the type of analysis
   you're conducting, one of several read types can be selected:
          Endpoint
                 The most commonly used Read Type, Endpoint, performs one read in the
                 center of the well for each wavelength. It is the only read type that
                 supports Pathlength Correction.
                    Check your assay kit instructions to determine if this type of reading is
                    required. Endpoint reads are generally conducted after a Stopping
                    Solution is applied to the samples or when the effects of the chemistry
                    occur at an expected time point.



128 | Chapter 7: Defining the Procedure



            Area Scan
                   When performing an Area Scan, the reader takes multiple measurements
                   down and across each well, in a "matrix" format. This method is more
                   effective for cellular assays than reading once in the center of the well.
                         Learn more in the Scanning Analysis Options and Features chapter
                         Readers that support Area Scanning include the ELx800, uQuant, FLx800,
                         SynergyHT, Synergy 2, and Synergy 4.

           Note: If the Scanning options are inaccessible, well scanning cannot
             be performed with the currently defined plate type. This may be due to
             a hardware limitation or an unacceptable combination of optic probe
             size and well diameter.

                         Read Matrix Size represents the number of measurements taken across
                         and down each well. If, for example, the Read Matrix Size is 5 x 5 a total
                         of 25 measurements are taken. The potential Read Matrix Size is a
                         function of the well size of the current plate.
            Linear Scan
                   When performing a Linear Scan, the reader takes multiple measurements
                   in a line across the center of each well. Linear scanning allows you to
                   observe a pattern that may be present in the well bottom, such as an
                   agglutination pattern.
                         Learn more in the Scanning Analysis Options and Features chapter
                         Readers that support linear scanning include the ELx808 and all
                         PowerWave models. Note for PowerWave X Select: Linear scanning is
                         supported for the 96-well plate type only.
                         Horizontal Reading Points setting represents the total number of points
                         to be read across the center of each well. Valid entries are odd integers
                         from 1 to 39.

                  Note: If the Scanning options are inaccessible, well scanning
                    cannot be performed with the currently defined plate type. This
                    may be due to a hardware limitation or an unacceptable
                    combination of optic probe size and well diameter.

            Spectrum
                   During a Spectrum Read, multiple readings are taken across a wavelength
                   range. The objective is to plot a graph with absorbance versus wavelength.
                         Learn more in the Scanning Analysis Options and Features chapter
                         The Stop wavelength must be greater than or equal to the Start
                           wavelength + the Step
                         Readers that support spectrum reads are uQuant, and all models of the
                         PowerWave, Synergy HT, Synergy 2, and Synergy 4.







Fluorescence Read Step for FLx800 and Synergy HT

       Synergy 2/4 users find instructions beginning on page 131

   Protocol> Procedure> Read



                                           When defining reading parameters for
     Fluorescence analysis, setting the PMT Sensitivity (for the Filter Sets) is important for
     obtaining useful measurements. The valid range is 25 to 255, but too low a setting, like
     25, can result in insufficient readings, and too high a setting, >120, can damage the
     PMT. BioTek recommends a setting between 40 -120 for Fluorescence assays and
     between 150 - 255 for Time Resolved Fluorescence.


      1.   (Optional) Enter a Step Label or unique name for this step. Data sets based on
           the reading results will use the label in online views, reports, and export files.
      2.   Keep the Full Plate or set a portion of the plate to process.
           (The Plate Type is set for all steps in the Procedure.)

      3.      Click the down arrow at Detection Method to select Fluorescence
      4.   Select Time Resolved to perform this type of fluorescence analysis (learn more
           in the Florescence and Luminescence chapter)

      5.   In Synchronized mode, you can select Close Light Shutter to turn off the light
           between reads. Optionally, to protect the fluorescent nature of your samples,
           use this feature to block the light between measurements to prevent photo-
           bleaching effects. Gen5 blocks the light with a Plug in the filter wheel.
           Important:
           A plug or blocking filter in the excitation filter wheel must be adjacent to the filter used
           in the reading. Two plugs must be placed next to each other (which ensures they are
           adjacent to the two filters used) in a dual-filter-set read step. Define the Reader
           Settings
      5.   For the Read Type select:
            Endpoint
                          The most common read type, Endpoint, performs one reading per
                          well for each filter set defined.
            Area Scan (not available in Synchronized mode)
                       When performing an Area Scan, the reader takes multiple
                       measurements down and across each well, in a "matrix" format.
                        This method is more effective for cellular assays than reading once
                       in the center of the well.
      6.   Set the Filter Sets:0.
              1       Use the numbered buttons to set the number of wavelengths.



130 | Chapter 7: Defining the Procedure



                 2    Click the down arrow to select the filter
                 3    If applicable, define:0
                       Optics Position
                       Sensitivity or click Options to let Gen5 determine the optimal
                         setting
                       Filter Switching: reading each well with both filters before moving
                         to the next well, is offered when only two filters are selected.

           In Synchronized Mode, the read step settings for the first read in a
             Plate or Well mode block are applied to any subsequent read steps in
             the block.

     Learn more in the Florescence and Luminescence chapter






Filter-based Fluorescence Read for Synergy 2 and Synergy 4 readers
    Protocol> Procedure> Read



      When defining reading parameters for Fluorescence analysis, setting the PMT
   Sensitivity (for the Filter Sets) is important for obtaining useful measurements.


       1.   (Optional) Enter a Step Label or unique name for this step. Data sets based on
            the reading results will use the label in online views, reports, and export files.
       2.   Keep the Full Plate or set a portion of the plate to process.
            (The Plate Type is set for all steps in the Procedure.)

       3.      Click the down arrow at Detection Method to select Fluorescence
       4.   Optionally, select Time Resolved or Polarization to perform this type of
            fluorescence analysis. Your choice enables or disables related options as
            appropriate for the process.
       5.   Read Speed: Use the drop-down list to make a selection and/or click the 3-dot
            button to change the default settings for Measurement Options
       6.   For the Read Type select:
             Endpoint: The most common read type, Endpoint, performs one reading
               per well for each filter set defined.
             Area Scan: (not available in Kinetic or Synchronized mode): When
               performing an Area Scan, the reader takes multiple measurements down
               and across each well, in a "matrix" format. This method is more effective
               for cellular assays than reading once in the center of the well. But, The
               Synergy 2's and Synergy 4's probe size limits its ability to perform
               Fluorescence area scan in plates with a small well diameter. Generally, this
               means you must use a plate with fewer than 96 wells.
       7.   Light Source: except for TRF, you can select the lamp to use for this read step:
            Xenon Flash (Xe) or Tungsten (Tg)

              Using the Xenon Flash (Xe)

              Advantages                                Disadvantages

              Enables Sweep mode as a Read Speed        Prohibits use of the Extended Range

              Very high energy, slightly more           It is expensive compared to the Tg
              sensitive than Tg bulb

              High light output below 300 nm (UV        Noise
              Fluorescence)



132 | Chapter 7: Defining the Procedure



                Performs direct protein and amino
                acid quantification assays


                Using the Tungsten Lamp (Tg)

                Advantages                                   Disadvantages

                Inexpensive, with high sensitivity for       Sweep read speed is prohibited
                Fluorescence Intensity (FI) and
                Fluorescence Polarization (FP)

                Enables Extended Dynamic Range               Cannot perform TRF

                Strong and stable light output in            Slightly less sensitivity than Xe Flash
                visible range

                                                             No light output below 300 nm


          8.   In Synchronized (non-kinetic) mode, you can select Close Light Shutter to turn
               off the light between reads. To protect the fluorescent nature of your samples,
               use this feature to block the light between measurements to prevent photo-
               bleaching effects. Gen5 blocks the light with a Plug in the filter wheel.
          9.   Set the Filter Sets:
         10.     Use the numbered buttons to set the number of wavelengths
         11. Click the down arrow to select the filter
         12. If applicable, define:

                Optics Position: for top reading select the mirror

                Sensitivity or click              to let Gen5 determine the optimal setting
                Filter Switching: reading each well with both filters before moving to the
                  next well, is offered when only two filters are selected.
                Top Probe Vertical Offset

           In Synchronized mode, the read step settings for the first read in a
             Plate or Well mode block are applied to any subsequent read steps in
             the block.

           The Filters offered for selection are defined by the Filter Wheel Library
             or Reader Configuration







Monochromator-based Fluorescence Read for Synergy 4
    Protocol> Procedure> Read

Prerequisites
         Filter wheel: to perform monochromator reads, the reader's excitation filter
           wheel must contain a Hole and a Mono LP filter.
         PMT Sensitivity: a setting between 50-150 for monochromator-based reads is
           required for obtaining useful measurements.
         Well volume: a minimum volume of 200 ul is needed for regular 96-well plates,
           100 ul for 384-well plates. Consider using 96-well half-area plates for smaller
           volumes.

Procedure
       1.   (Optional) Enter a Step Label or unique name for this step. Data sets based on
            the reading results will use the label in online views, reports, and export files.
       2.   Keep the Full Plate or set a portion of the plate to process.
            (The Plate Type is set for all steps in the Procedure.)

       3.        Click the down arrow at Detection Method to select Fluorescence

       4.        Optionally, click the Read Type down arrow to select a different option
       5.   For endpoint reads you can select Time Resolved to perform this type of
            fluorescence analysis. Your choice enables or disables related options
       6.   Read Speed: Use the drop-down list to make a selection and/or click the 3-dot
            button to change the default settings for Measurement Options
       7.   Light Source: except for TRF, you can select the lamp to use for this read step:
            Xenon Flash (Xe) or Tungsten (Tg)
       8.   In Synchronized (non-kinetic) mode, you can select Close Light Shutter to turn
            off the light between reads.
       9.        De-select Use Filter Wheel to use the monochromator
       10. Set the Filter Sets:
            1.     Use the numbered buttons to set the number of wavelengths
            2.   Enter wavelengths for the monochromator. Valid values for Excitation
                 wavelengths depend on the Light Source selected above: Xe supports 250-
                 700 nm, while Tg supports 340-700 nm; for Emission wavelengths the range
                 is 300-800 nm.
       11. If applicable, define:0.

             Sensitivity or click             to let Gen5 determine the optimal setting
               Top Probe Vertical Offset



134 | Chapter 7: Defining the Procedure



               Column Offset
                      Valid Range: 0.0 - 3.0
                      Due to the angled approach of the probe, lowering it may also require a
                      small adjustment to the plate position beneath it.

           In Synchronized Mode, the read step settings for the first read in a
             Plate or Well mode block are applied to any subsequent read steps in
             the block.







Read Step for Luminescence
   Protocol> Procedure> Read



                                         When defining reading parameters for
     Luminescence analysis, setting the PMT Sensitivity is important for obtaining useful
     measurements. The valid range is 25 to 255, but BioTek recommends a setting between
     100 - 160 for Luminescence assays.


      1.   (Optional) Enter a Step Label or unique name for this step. Data sets based on
           the reading results will use the label in online views, reports, and export files.
      2.   Keep the Full Plate or set a portion of the plate to process.
           (The Plate Type is set for all steps in the Procedure.)

      3.      Click the down arrow at Detection Method to select Luminescence
           The Read Type must be set to Endpoint
      4.   Enter the Integration Time: to set the read duration for each well in seconds or
           milliseconds. Click in the field and enter the Sec.Msec or use the spin buttons to
           set the duration.
           Valid values:
                Synergy HT: 0.1 - 19.9 seconds;
               Synergy 2/4: 0.1 - 99.9 seconds, in 20 ms intervals
               FLx800: 0.1 - 6.0 seconds
      5.   Synergy 2/4: Click the 3-dot button to change the default settings for
           Measurement Options
      6.   Set the Filter Sets:0.
              1      Use the numbered buttons to set the number of wavelengths.
              2   Click the down arrow to select the filter or Hole (to not filter the light)
              3   If applicable, define: (Learn more in the Florescence and Luminescence
                  chapter)0
                   Optics Position

                   Sensitivity or click             to let Gen5 determine the optimal
                     setting

       In Synchronized Mode, the read step settings for the first read in a
         Plate or Well mode block are applied to any subsequent read steps in
         the block.



136 | Chapter 7: Defining the Procedure




Read Step for Spectrum Analysis
     Protocol> Procedure> Read
        Define the reading parameters based on the capability of the current reader:
          1.   (Optional) Enter a Step Label or unique name for this step.
          2.   Keep the Full Plate or set a portion of the plate to process.
          3.   Set the Detection Method to Absorbance (except for Synergy 4, Absorbance is
               the only option.)

          4.      Click the down arrow to set the Read Type to Spectrum.
           Certain parameters specific to the detection method and reader's capability must
           be defined:
                Read Speed: Use the drop-down list to make a selection and/or click the 3-
                  dot button to change the default settings for Measurement Options
                Calibrate Before Read: When selected, the reader will always perform
                  calibration at the wavelengths specified in the protocol, just prior to plate
                  reading. If Calibrate is not selected, the reader will calibrate at only those
                  wavelengths specified in the protocol that have not yet been calibrated since
                  the reader was turned on.
                Spectrum Type (for Fluorescence Only): Fluorescence spectrum analysis
                  can be performed on either the Excitation or Emission wavelength, with the
                  opposite wavelength set to a fixed value. And the range of wavelengths
                  scanned can either be lower or higher than the fixed wavelength (including
                  bandwidth). See the description of Acceptable Values below.
                Light Source (for Fluorescence Only)
                Integration Time (for Luminescence Only): Enter the Integration Time: to
                  set the read duration for each well in seconds or milliseconds. Click in the
                  field to enter the Min:Sec:Msec (MM.SS.ss) or use the spin buttons to set the
                  duration. Valid values.
          5.   Set the range of Wavelengths:
               Acceptable Values:
                The acceptable range for the Start wavelength is from the lowest
                  wavelength the reader supports to one less than the Stop wavelength
                  selected.
                The acceptable range for the Stop wavelength is any wavelength greater
                  than the Start wavelength to the highest wavelength allowed by the reader.
                The acceptable range for the Step value is any number equal to or less than
                  the difference between the Start and Stop values.
                The only read speeds available for Spectrum reads are Normal and Sweep.
          6.   Enter the Start and Stop wavelengths to define the spectral range.






              For Fluorescence reads: select a Spectrum Type, enter a fixed wavelength
                for the opposite type, and enter a wavelength range that does not overlap
                the fixed wavelength.
        7.   Enter the number of Steps to define the number of measurements to take.
              Fluorescence and Luminescence readers let you adjust the Top Probe
                Vertical Offset and the Column Offset.



Read Step for Clarity
    Protocol> Procedure
   Gen5 communicates with the ClarityTM software to define the Procedure.

         Learn about the relationship between Gen5 and the Clarity PC
           software, if you haven't already done so.

   When creating a new protocol or experiment for the Clarity, Gen5 replaces its StepWiseTM
   Procedure dialog with a gateway to the Clarity PC software, which you must use to define
   the read command. Select:
          Create New... to create a new procedure (.bpf file)
          Browse... to select/run an existing Clarity protocol (.bpf file)
          Edit... after using Browse to select a file, to modify an existing Clarity protocol
             (.bpf file)
   After the read step (Procedure) is defined/selected, you can set up the rest of the Protocol
   elements, like Plate Layout and Data Reduction, and so on.
   Double-click Procedure in the menu tree to modify it (select Edit). This is possible before
   the plate is read. After the plate is read, like all Gen5 protocols, the Procedure can not be
   modified.


      Specific instructions for defining the Clarity read parameters are provided in the
   Clarity Operator's Manual.



138 | Chapter 7: Defining the Procedure




Procedure Steps: Reading-Related Activities
     Protocol > Procedure
     The following features may or may not be available for creating a protocol depending on
     the attached reader, and your level of software.
            Set Temperature (Incubation): page 138
            Shake the plate: page 139
            Dispensing Reagent: page 140
            Kinetic Analysis: page 142
            Delay Step: page 143
            Monitor Wells: page 144
            Plate In/Out: page 145
            Stop/Resume the experiment: page 146
            Synchronized Modes: refer to the Fluorescence and Luminescence chapter




   Set Temperature
     Use these controls to set the desired temperature for the reading chamber or incubator.
     Most BioTek readers allow a temperature range of 20-50^0C. Add a Delay step to the
     Procedure to incubate the plate. Learn more below. turn off the incubator
          1.   Enter the desired temperature in the Temperature field.
          2.   Select (or de-select) the option to Preheat before continuing with next step
               to wait for the temperature to reach the set point before proceeding with the
               next step in the Procedure. Selecting this option activates the Pre-Heating
               function available from the Control Panel: System>Control Panel.0.

           Stop/Resume: Gen5 considers a Stop/Resume step the end point of
             the series of steps that precede it. It frees up the reader for running
             other experiments. If you want the steps following a Stop/Resume to
             be performed at a certain temperature you must add a Set
             Temperature step after the Stop/Resume step.

           You cannot put a Temperature Step inside a kinetic loop

           When the experiment is started (the Read button is pressed) before
             the reader has reached the defined temperature, Gen5 offers the
             option to override the Set Temperature step.







            Reporting the temperature: you can include the temperature of a read step in a
         report or export file. Add the Fields to your report: from the Plate Information
         category, select the desired Temperature field.


   How to incubate the plate:
         The Set Temperature step in Gen5's StepWise Procedure does not by itself incubate the
         plate. It heats up or cools down the reader to the defined setting. To use your reader to
         incubate the plate define the Procedure this way:
              1.   Set Temperature with preheating
              2.   Plate Out/In step, enter Incubate Plate in the Comments field
              3.   Delay for the incubation duration
              4.   Read



    Shake the Plate
Use these controls to set the Intensity and Duration of a Shake step to mix the plate contents:
            Intensity - use the drop-down list to select a level. The reader's operator's
              manual may define the specifications of each level.
            Duration - enter a time period (minutes:seconds) to shake the plate. The
              potential range is 1 second to 60 minutes.
            Continuous Shake - within a kinetic loop, if the reader is capable of
              performing it, you can select this option to shake the plate whenever it is not
              being read during the kinetic time interval

As part of a Kinetic Analysis:
                To shake the plate only before the first reading in a kinetic analysis define
                  the sequence of activities: Sha? End Kinetic
                To shake the plate before every reading in a kinetic loop define the
                  sequence of activities: Start Kinetic >> Shake >> Read >> End Kinetic
                To continually shake the plate whenever it is not being read, select
                  Continuous Shake instead of a time interval

           In multi-mode kinetic analysis a Shake step cannot precede the kinetic
             loop, but can be the first step in the loop: Start Kinetic >> Shake >> Read
             >> Read >> End Kinetic



140 | Chapter 7: Defining the Procedure




    Dispensing
        This option is only available for Readers with Injectors.
        The Dispense dialog fields are described here and information to help you choose the
        optimal Dispense Rate begins on page 141.
Dispenser
        Select the number of the Dispenser to be used for this step. The numbers correspond to
        the numbers on the dispense module.
Partial or Full Plate?



     The button to define a full or partial plate is dynamic, it changes from Full Plate to a plate-
     map description of the area to be dispensed to/read, e.g. A1..H5. Click the button to define
     the specific wells for dispensing, and if this step is in a loop, for reading in the subsequent
     Read Step(s).

            In Synchronized Mode the first step in a block controls the full or
              partial plate for the entire block. For example, if the steps in a Well
              Mode block are Dispense>Delay>Read, when the Dispense step is
              defined to dispense to the first two columns of the plate, the Read step
              is also limited to the first two columns. Likewise, if the steps in a Plate
              Mode block are Read>Dispense>Read, and the first Read step is a
              partial plate read E5...H12, the Dispense and Read steps to follow will
              automatically be set to the same portion of the plate

Tip Prime
        Priming: select an option:
                none: Do not prime the tip
                before the dispense step: Prime the tip with fluid before injection of fluid
                  to the plate
                once before the Well/Plate Mode block: In Synchronized mode, you can
                  prime the tip one-time-only before the process begins
                before this dispense step: In Synchronized Plate Mode, you can prime the
                  tip before each dispense step in the block
                More About Tip Priming: Priming is performed in a small, removable priming trough
                   located in the rear of the carrier. The purpose of tip priming is to compensate for
                   any fluid loss at the dispense tip due to evaporation since the last dispense. Each
                   trough holds up to 1500 ul of liquid and must be periodically emptied and cleaned.
                   Gen5 warns you to empty the trough before the first Dispense event and keeps
                   track of the amount of fluid primed into the trough during the Procedure. Selecting
                   Yes at one of Gen5's messages to empty the trough resets the trough volume
                   record to zero.






           Do not perform Tip Priming when using tall plates. Generally, plates with fewer
             than 96 wells are too tall for error-free tip priming, and it is rarely required for
             these larger-volume plates.

      Volume: enter the amount of fluid in microliters. The valid range is 5 to 20.

           Important: For optimal dispense accuracy and precision when
             dispensing volumes less than or equal to 20 ul/well, BioTek
             recommends priming the tip: use a tip prime volume equal to the
             dispense volume. For dispense volumes greater than 20 ul/well, we
             recommend a tip prime volume of 20 ul.

Dispense
      Volume: Enter the dispense volume in microliters. The valid range is 5 to 1000

            Rate: Select the dispense rate (microliters per second) based on the volume.


          Keep the fluid path clean: You'll get the best results from your BioTek reader with
      Injectors if you keep the fluid path clean. Minimally, you should Purge the reagent and
      flush the lines with DI water when the experiment is finished. Follow instructions for
      daily maintenance in your Operator's Manual.


           When the Dispense step is the last step in the Procedure, add a Plate
             Out step to eject the plate carrier when the Procedure is finished.

Dispense Rate
      Gen5's options are:

               Rate (ul/sec) Volume Range (ul)

                 225                  5-1000

                 250                  15-1000

                 275                  25-1000

                 300                  30-1000
      The maximum volume for a dispense operation is 1000ul. The minimum volume
      depends on the dispense rate. For example, when dispensing <= 10ul you must use a
      rate of 225.
      Here are some factors to consider when selecting the dispense rate or injection speed:
            Use the fastest rate for the best mixing affect in the wells
            Use the slowest rate (225) when a cell layer is involved; especially if the level of
              liquid in the well is low (<100ul) before injection



142 | Chapter 7: Defining the Procedure



            Lower the rate if you notice some spills on the plate after injection. (This may
              be caused by a high (>200ul) or low (<50ul) pre-injection volume, or to a
              specific plate type, like round-bottom wells.)
            Assay kits generally provide guidelines, review the kit insert to determine its
              recommendation for a slow or high dispense speed
            High-viscosity fluids perform better with a slow rate

    Kinetic

           Learn more in the Kinetic Analysis chapter beginning on page 185.

        To set up a kinetic (or time-course) analysis, put one or more Read steps within the
        Start Kinetic and End Kinetic loop. The steps are conducted within the specified
        timelines:
        Run Time: Enter the full duration of the kinetic analysis, i.e. the length of time
        required to perform all the steps within the kinetic loop:
               Time Format: Hours (HH): Minutes (MM): Seconds (SS) in standard mode
                 and Minutes (MM): Seconds (SS): Milliseconds (ss) in synchronized mode.
               Maximum time period is 168 hours except in Synchronized Modes. Well
                 Mode kinetic run time is limited to 60 minutes and the block must be
                 completed in 2.78 hours. Plate Mode kinetic run time is limited to 24 hours
                 and the block must be completed in 27.8 hours.
        Interval: Enter the desired time interval between readings or select Minimum Interval.
        Gen5 will read the plate at every interval, e.g. every 00:10:30 = 10 minutes and 30
        seconds, for the duration of the Run Time
        Minimum Interval: Select this option to let Gen5 determine the fastest possible
        processing time. Follow the instructions in the Kinetic Analysis chapter.
        Reads: Gen5 calculates the number of reads from your input of Run Time and Interval.
        The maximum number of reads depends on your reader and detection method.

           Important: Numerous factors affect the acceptable kinetic run time.
             To make sure your reader can process the steps in the kinetic loop
             within the defined timelines, click Validate (with the reader attached
             and communicating with Gen5) when all the Procedure steps have
             been defined. If the interval is too short for the parameters chosen, an
             error will be displayed.

           Discontinuous Kinetic Interval: Gen5 let's you perform a
             discontinuous-interval analysis that requires long periods of downtime
             (for rest, manipulation, or incubation) between reads. Engage this
             feature with the Procedure's Advanced Options.

           Note: The actual runtime of a kinetic loop may exceed the defined
             Run Time by +1 Interval. Gen5 does this to ensure that the number
             of Reads displayed are actually captured.






Delay the Procedure
  Use this command to add a Delay event to the series of steps defined, telling the reader
  to halt processing for the defined duration. You cannot put a Delay step in a kinetic
  loop, nor can you have a Delay between Shake and Read steps.
  Delay Time: Enter a time period for the duration: HH:MM:SS


     You may want to use a Stop/Resume step or Plate In/Out instead




Delay in Synchronized Mode
  Use these controls to add a Delay event to the steps in a Synchronized Mode block,
  telling the reader to halt processing for the defined duration.
  Delay Time: Enter a time period for the duration
        In Plate mode: HH:MM:SS (hours:minutes:seconds)
        In Well mode: Min:Sec.Msec (minutes:seconds:milliseconds)
  Start Delay From: Select an option
        Beginning of Previous Step: to define the delay time to include the time it
          takes to perform the previous step, as well as the delay time
        End of Previous Step: to set the delay time to begin when the previous step
          is finished. This is the default and most typical setting


        Example: You may want to use the Start Delay from Beginning of Previous Step
    option in a Dispense>Wait>Read protocol when the precise timing of every step is
    critical to your experiment.




       FLx800: In Well Mode it is necessary to include a Delay step set to "Start delay
    from Beginning of previous step" to precisely control the reader to process each
    well within the same timeline. Set the Delay Time sufficient to perform the
    previous step with a little padding: this is usually 0:00.10 milliseconds or more.
    When you click the Validate button, Gen5 communicates with the FLx800 to
    determine if the Procedure is doable. If not, it provides instructions for adding a
    Delay step or increasing the Delay Time.



144 | Chapter 7: Defining the Procedure



    Monitor Wells
        Use these controls to define well-monitoring criteria that must be met before the reader
        begins to capture the actual measurement values used in the experiment.

   About Monitoring Wells
        Gen5's Monitor Wells feature can be used to detect a certain level of activity in the
        plate before capturing regular, saved measurements. You define measurement criteria
        that must be met in one or more specific wells before the complete plate read can
        begin. Gen5 directs the reader to continuously read the wells at the defined time
        interval until the criteria are met. This feature sets up a loop, like a Kinetic loop, with a
        start step and an end step in the Procedure. A Monitor Read step must be defined
        within the loop. A Shake step is also permitted either before the read or before the
        entire Monitor Well loop.
        Example: you can specify that the average of the measurements in wells A1, A2, B1
        and B2 must be greater than or equal to 0.500 OD before initiating the plate read. When
        the Monitor Wells step is executed, the following information will be displayed: wells
        being monitored, current value of the wells, the required measurement value, and the
        elapsed time since the last well was read. At any point the user can choose to bypass
        the monitoring process and continue forward with the read or cancel the operation,
        aborting the entire Procedure.

  How To:
          1.    Click Monitor Well to start the loop
                 Interval: enter the time interval between readings for the duration of the
                   well monitoring. Alternatively, check the Minimum Interval option (if you
                   have a reader attached) to let Gen5 determine the shortest possible interval
                   for monitoring
                 Stop Monitoring When: tells the reader when to conclude the monitoring
                   process. Use the drop-down list to select a conditional option and an
                   operator, and enter a measurement value to be met:

               Condition                  Operator                 Measurement Value

               At least one well          > greater than,          Absorbance valid range: -
                                          >= or equal to           1.000 to 5.000

               Average of wells           < less than,             Fluorescence/ Luminescence
                                          <= or equal to           valid range: 0 - 99998
               All wells

          2.    Define a read and shake step, if desired, for the Monitor Well loop:
                 Read: with End Monitoring highlighted in the Procedure, click Read and
                   define the Wells to Monitor:
                    Click             to select the wells to monitor for the "Stop Monitoring






              When" criteria. Single or multiple wells can be selected by clicking in the
              grid. Multiple wells must be contiguous.
            Define the reading parameters using the modified Read step dialog. .
            Add a Shake step, if desired, as normal.
      3.   Add the regular Procedure steps to follow the Monitor Well loop, i.e. an
           endpoint or kinetic reading and any associated activities. Gen5 always requires
           at least one actual read step. The "Monitor Read Step" does not fill this
           requirement.0.


         Important: Gen5 does not save the reading results (measurements) obtained during
     the Monitor Well step. Only measurements collected during a regular read step are
     retained for analysis and data reduction.




 Plate In/Out
     Add a Plate In/Out step to a Procedure to pause the run and change the position of the
     plate carrier. This command can be used to perform a manual task, like adding reagent
     to the plate between reads steps, for example. You can also use this step to change the
     behavior of the plate carrier, for example, if you want to move the carrier back into the
     reader at the end of a run.

       Unlike the Stop/Resume step, this command does not completely
         interrupt or end the run.

Select one:
            Move carrier out, Display dialog, Move carrier in



              Enter text in the Comment field. When the plate is ejected Gen5 will display
              the comment.
            Move carrier out (no dialog)
            Move carrier in (no dialog)

Results:
     Move carrier out, Display dialog, Move carrier in:



146 | Chapter 7: Defining the Procedure



            When the first option is selected, Gen5 displays
            the comment in a dialog like this when the plate
            carrier is moved out:
            When the user clicks OK, the plate carrier is
            moved back in. The plate can be handled in the
            interim.



        The other two options open or close the plate carrier without displaying a message.



    Stop/Resume
        Use this command to stop the experiment where it is inserted in the Procedure. It is
        typically used for long interruptions (such as incubation periods), and allows the
        reader to be used for other experiments. Gen5 will stop the experiment until you
        resume it. See how to resume below. Only then will it continue to perform the
        Procedure steps that follow the Stop/Resume step. You can close the experiment when
        it is stopped and reopen it when you're ready to resume.

            Set Temperature: Gen5 considers a Stop/Resume step the end point
              of the series of steps that precede it. If you want the steps following a
              Stop/Resume to be performed at a certain temperature you must add
              a Set Temperature step after the Stop/Resume step.

  Set up:
           Eject Plate Before Stop: Gen5 will open the plate carrier to eject the plate before
        stopping the experiment, unless you de-select this option. When this option is not
        selected, Gen5 lets the previous Procedure step determine the position of the plate
        carrier. Since most Procedure steps do eject the plate upon completion, to keep the
        plate inside the reader during the downtime, you may need to add a Plate In step
        before the Stop/Resume step.
        Comment: Enter a comment to be displayed on-screen

  Results:
         The Comment you enter, "Add reagent" in this example, is
         displayed in a message like this when the experiment is
         stopped. Users must click OK to acknowledge the message.
         The experiment is stopped, until it is resumed.




         Gen5 signals the experiment has been stopped using the
         plate-paused icon in the menu tree.






To Resume:
     1.   Open the experiment, if it was closed.

     2.       Click the Read button when you're ready to resume the experiment. The
          standard read screen changes, offering Resume instead of Read.

     3.                                Click the Resume button to continue with the
          Procedure. Note: If Re-Read is selected, Gen5 restarts the Procedure from its
          beginning (first step), reading the plate again and discarding the initial data.0.



148 | Chapter 7: Defining the Procedure
