# Chapter 4: Assay Examples

    This section contains step-by-step instructions for programming
    commonly known assays using Gen5. Gen5 also ships with Sample
    Protocols for most of these assays. Both the Sample Protocols and
    the assay descriptions are learning tools. It is your responsibility to
    customize and validate them to meet your needs. Find a list of the
    assays described in this chapter in the "How do I set up my assay"
    section.


 Sample Protocols and Experiments............................................. 52
 How do I set up my assay? ....................................................... 54



52 | Chapter 4: Assay Examples




Sample Protocols and Experiments
        Numerous sample protocols are shipped with Gen5. You can use the protocols to learn
        more about Gen5 and as a timesaver, customizing them to meet your needs and then
        running them in an experiment to obtain results.

          Recommendation: Before making any modifications to the sample
            protocols, we recommend selecting File>Save As after opening them
            and assigning a unique name to the protocol. This will preserve the
            original sample protocol for future use.

        A matching experiment file is also shipped with Gen5 for use as a learning tool. Many
        of the experiment files contain actual data so you can see how Gen5 presents the
        results on-screen and in reports.

         Find the sample protocols and experiments shipped with Gen5 in the default file
     storage locations. A folder for each detection method is available: Absorbance,
     Fluorescence, Luminescence and and for Synergy 2 and Synergy 4 users, there is a Synergy
     2_Synergy 4 folder within each detection method folder:
        Gen5 Secure (and database users): Select File>Open Protocol, in the DB
          directory select the Samples folder.
        All other levels of Gen5: Select File>Open Protocol and browse to C:/Program
          Files/BioTek/Gen5/Samples.


           Tip: Select File>Open Protocol and use       (the Up One Level button).


        Gen5's Welcome screen also offers the option to open a Sample File.

          Important: The sample protocols must be considered as examples
            provided for demonstration and guidance purposes. If you plan to use
            these protocols or similar ones in a real application, it is your
            responsibility to validate the protocol parameters, including the report
            and export content (if applicable), before using them.

          Notes: Your system administrator can change the path and filenames
            described above. If you cannot find the Samples folder, contact your
            system administrator. Also note, your reader may not support all of
            the sample protocols provided. Review the descriptions in the Samples
            Protocol Listing to see if your reader is compatible with the defined
            steps.

Sample Protocols and Experiments Guide
     You can review a complete description of samples in the Sample Protocols and
     Experiments Guide.PDF shipped with Gen5: click the Windows(R) Start, select All
     Programs>Gen5>Sample Protocols and Experiments Guide






  Gen5 installs a copy of the Sample Protocols and Experiments Guide in
    the Samples folder of the main Gen5 directory. (By default this is
    C:\Program Files\BioTek\Gen5\Samples)

You can also find a summary listing and brief description of the sample protocols in
Gen5's Help. Review the description of the sample protocol to make sure it is
compatible with your reader.



54 | Chapter 4: Assay Examples




How do I set up my assay?
        Here are step-by-step instructions for creating Gen5 Protocols to run common assays.
        (More Assay Examples can be found in Gen5's Help.) We hope that by following the
        instructions, making some changes to names and other details, you can adapt them for
        use in your lab. Also see the Kinetic Analysis chapter.

Absorbance
           Quantitative ELISA Example on page 55
           Subtracting Blank Plate Reads on page 58
           Pathlength Correction Example on page 60
           Dual Wavelength Absorbance Endpoint on page 62
           Basic Spectrum Analysis on page 64
           Protein Quantification Assay on page 66
           Max Binding Determination on page 83
           Toxicity/Cytotoxicity Assay on page 86
           Endotoxin Test on page 89
           ss-Galactosidase Kinetic Assay on page 92

Fluorescence
           Basic Fluorescence Assay on page 69
           Kinetic Fluorescence Assay on page 71
           Fluorescence Assay with Injection on page 74
           Fluorescence Area Scan Example on page 77
           Fluorescence Polarization on page 79

Luminescence
           Basic Luminescence Glow Assay on page 81
           Luminescence Flash Assay with Injection on page 82

Dispensing Reagent
           Dispensing Reagent in a Kinetic Analysis on page 94
           Dispensing Reagent in an Endpoint Analysis on page 95
           Fast Kinetics with Injection for Absorbance on page







Quantitative ELISA Example
      To help you set up your own assay here is an example of the steps required to run a
      quantitative ELISA assay. In this example we set up an endpoint Absorbance read,
      subtract Blank wells from all others, plot a standard curve, and define a Control to
      express the samples as a percentage of the control.


          It may be easier to follow these instructions if you have already watched the Gen5
      Basic series of online tutorials: select Help>Tutorials or if you've completed the
      learning exercises described in the Getting Started Guide.


      To set up the protocol, we'll define the:
            1.   Reading Procedure
            2.   Plate Layout
            3.   Data Reductions0.

        Reporting Results is the same process for all types of experiments

1. Defining the reading Procedure
   This assay example has the simplest read Procedure: a single-wavelength Absorbance
   endpoint read:
       1.   Select File>New Protocol
       2.   Select Protocol>Procedure
       3.   Click the Read button and select the wavelength. Use the drop-down list or
            type the wavelength in the text field (overwrite the current value).
       4.   Click OK twice to save the Procedure0.



56 | Chapter 4: Assay Examples



2. Defining the Plate Layout
        This step is critical for the data reduction steps to be defined later. Here's the plate
        layout we need:




        The critical factor is using the Well IDs, not their location on the plate. We did not need
        to customize the Well IDs for this example. We simply selected the Type, defined the
        known concentration of the standards and assigned them to the plate:

              Well ID      Type                Description

              BLK          Blank               DI water only

              STD          Standard            Known concentrations

              CTL1         Assay Control       Known Control

              SPL          Sample              Unknown samples

        Find specific instructions in the Preparing Plates chapter.

3. Defining the Data Reduction Steps
        Now that we've defined the reading parameters and plate layout, we can define the
        data reduction steps: blank-well subtraction, standard curve, and expressing samples
        as a percentage of the control. Gen5 creates the blank-subtraction step for you
        automatically.
         1.   Select Protocol> Data Reduction
              Notice that one Transformation, named "Blank nnn" where nnn is the
              wavelength, has already been created. We'll use the results of this calculation to
              plot the standard curve.
         2.   Click Curve Analysis






 3.   Notice on the Data In tab, the Well ID is set to STD and X Axis Data to <Plate
      Layout Settings>. The known concentrations entered for Standards are plotted
      on the X Axis. Use the drop-down list for the Y Axis Data to select Blank nnn
      (wavelength)
 4.   Click the Curve Fit tab: depending on your assay, you may want to change the
      curve fit method to 4 Parameters or another option, or use Log values on the X
      or Y axis. For now, retain the defaults and click the Data Out tab. Take note
      that the Data Set Name produced from the standard curve is called Conc (by
      default. You can change it.). Click OK to save and close the curve.
 5.   Click Transformation
      1.   For the Data In use the drop-down list to select Conc.
      2.   Enter a New Data Set Name for the results of this calculation, e.g.
           %Control
      3.   In the Formula field enter: (X/CTL1)*100
           Retain the default setting to Use single formula for all wells. X represents
           the value of the current well. CTL1 is the well ID for the control we
           assigned in Plate Layout.


   After the plate is read, you can return to the Data Reduction dialog to make any
needed changes, like the Curve Fit Method. Do not change the Data Out or Data Set
Names, this would invalidate the data reduction steps that use those data sets.


 6.   Save the protocol.0.
Now you're ready to define your reporting requirements, and run the protocol in an
experiment.



58 | Chapter 4: Assay Examples




Subtracting Blank Plate Reads
        To perform a blank-plate subtraction in your experiment, set up an additional Read
        Step for the blank plate, and then, create a Data Reduction Transformation to subtract
        the measurements of the blank plate from the samples plate.
        You can insert a Plate in/Out step in the Procedure sequence to first read the blank
        plate, pause the experiment to pipette samples to the plate, and then, read the samples
        plate.

Step-by-step procedure:
         1.   Select File>New Protocol
         2.   Double click Procedures to set the reading parameters:
                 1   First, create a Read Step for the blank plate: enter Blank for the Step
                     Label to easily identify the raw data.




                 2   Add a Plate In/Out step to eject the plate to pipette samples, standards,
                     etc. Optionally, enter "Load Samples" in the comment field.
                 3   Finally, create a Read Step for the samples plate. 0

          Other steps can be included in the sequence, like Set Temperature and
            Shake, if required.

         3.   Set up the Plate Layout to match the distribution of samples and standards or
              controls.
         4.   Double click Data Reduction to define a transformation: Blank Plate Data
              Reduction
                 1   The dialog will contain any automatically generated data reductions.
                     Highlight the top-most one and click Transformation, to position the
                     blank subtraction as the first calculation.

                 2   Click
                 3   In the Multiple Data Sets screen, use the drop-down lists to select the
                     Blank plate read data for DS1 and the samples plate data for DS2.

          In multiple wavelength protocols there may be several data sets to
            choose from. If you've used the Step Labels for each Read Step, it's
            easy to match up the blank plate with the samples plate.







                 4   Enter a New Data Set Name for the resulting data set, e.g. Blanked 390
                 5   Enter DS2-DS1 in the Plate Formula field and click OK.
                 6   Repeat steps 2-4 to create as many blank-plate subtraction
                     Transformations as needed, e.g. one per wavelength.
                 7   Now you're ready to create other Data Reduction steps using the
                     blanked data sets. For example, select Curve Analysis to generate a
                     standard curve based on the blank-subtracted test plate.0
         5.   Customize the Data Views and fine-tune the Report Builder as needed before
              saving and closing this protocol. File>Save0.
              Now you're ready to run the protocol in an experiment: File> New
              Experiment

Running the experiment:
      After reading the blank plate, Gen5 ejects the carrier so you can load the samples




                                     If you entered a comment, e.g. Load Samples in the Plate
              In/Out step, it is displayed on screen. Here's how to proceed:
           Click OK after loading the samples, when you're ready to continue reading the
             plate



60 | Chapter 4: Assay Examples




Pathlength Correction Example
        Here is an example of the steps required to perform pathlength correction in an ELISA
        assay. In this example we set up an endpoint Absorbance read, subtract Blank wells
        from all others, and transform the data to determine the concentrations of the
        unknown samples. This is the process used to create the Direct Oligo Quantification
        assay shipped as a sample protocol with Gen5.


            It may be easier to follow these instructions if you have already watched the Gen5
        Basic series of online tutorials: select Help>Tutorials or if you've completed the
        learning exercises described in the Getting Started Guide.


        To set up this protocol, we'll define the:
         1.   Reading Procedure
         2.   Plate Layout
         3.   Data Reductions0.

          Reporting Results is the same process for all types of experiments

1. Defining the reading Procedure
     This assay example has the simplest read Procedure: a single-wavelength Absorbance
     endpoint read:
         1.   Select File>New Protocol
         2.   Select Protocol>Procedure
         3.   Click the Read button and keep the default settings for Detection Method,
              Read Type and Read Speed
         4.     Fill in the checkbox next to Pathlength Correction. [Optionally, click the 3-
              dot button to view (and modify if desired) the test and reference wavelengths
              used in the process.]
         5.   Set the Wavelength. Use the drop-down list or type the wavelength in the text
              field (overwrite the current value). For this example, enter 260.
         6.   Click OK twice to save the Read step and the Procedure0.

2. Defining the Plate Layout
        For this assay example, the plate layout is very simple, comprising two blank wells and
        94 unknown samples:

         1.       Select Protocol> Plate Layout






       2.   In the Well Settings box, select the Type of specimen, first Blanks, then
            Samples
       3.   Assign the blanks to cells A1 and B1
       4.   Change the Type to Sample, make sure Next ID is enabled, click and drag over
            the remaining wells to assign the unknown samples0.

3. Defining the Data Reduction Steps
      After defining the reading parameters and plate layout, we can define the data
      reduction steps. Gen5 creates the blank subtraction and the pathlength correction for
      you automatically.
       1.   Select Protocol> Data Reduction
            Notice the two Transformations, "Blank 260" and "Corrected [Blank 260]", Gen5
            first subtracts the blanks and then applies the Pathlength Correction
            Calculation.
       2.   Click Transformation to add anther Data Reduction step
       3.   For the Data In use the drop-down list to select Corrected [Blank 260] data set
       4.   Enter a New Data Set Name for the results of this calculation, e.g.
            Concentration
       5.   In the Plate Formula field enter: X*32.5
            Retain the default setting to Use single formula for all wells. X represents the
            value of the current well. The extinction coefficient for ssDNA oligonucleotides
            (1 mg/ml) at 260 nm is 13 ODs for a 1 cm pathlength; this can be recalculated to
            mean 1.0 OD has a concentration of 32.5 ug/ml.
       6.   Save the protocol.0.
      Now you're ready to define your reporting requirements, and run the protocol in an
      experiment.



62 | Chapter 4: Assay Examples




Dual Wavelength Absorbance Endpoint
   Here are step-by-step instructions for setting up a dual-wavelength absorbance read with
   known concentrations of standards against which a linear regression curve is plotted.

Create the protocol:
         1.   Select File>New Protocol

         2.      Double-click Procedure in the menu tree:
               Click Read to set the reading parameters: Keep the default settings for
                 Detection Method and Read Type: Absorbance Endpoint
               For Wavelengths, click the button for 2 and use the drop-down list to
                 select (or enter) the test and reference wavelengths: 410 and 630 for this
                 example.
               Click OK twice to close the Read Step, and then, the Procedure dialogs.

         3.       Double-click Plate Layout to define the location of standards, samples,
              and blanks on the microplate. For this example, the standards are placed in the
              center of the plate, modify the instructions to match the distribution of samples
              and standards on your plate:
               Set the Well Settings Type to Standard and click the 3-dot button next to the
                 Conc. field to enter the expected concentrations. For this example, leave 0 in
                 the STD1 cell at the top of the table. Select Incr. with a tick mark, and enter
                 10 in the field, then click in the STD1 cell, then in the STD2 cell, and each
                 subsequent cell in the table until STD8. Click OK to save and close the
                 concentrations.
               At the grid, set the Number of Replicates to 2, and select Next Conc. under
                 Auto Select. Click and hold as you roll the mouse over the 5 and 6 columns,
                 (the cursor changes to a black, down-facing arrow) to fill the entire
                 columns.
               Set the Well Settings Type to Blank, keep the Number of Replicates at 2,
                 and click and drag over wells A1 and A2.
               Set the Well Settings Type to Sample, keep the Number of Replicates at 2,
                 and select Next ID under Auto Select. Click and drag the cursor over the
                 remaining wells in columns 1 and 2, and then 3-4, and then 7-12, to assign
                 samples to all the other wells of the plate.

         4.      Double-click Data Reduction
              Gen5 automatically creates the Blank-Subtraction transformations.
               Click Transformation to set up the calculation:

         5.   Click






        6.    For DS1 (selected by default) use the drop-down list to select Blank 410
        7.         Select DS2 and use the drop-down list to select Blank 630
        8.    Click OK to close the Multiple Data Set dialog
        9.    For this example, we'll call the New Data Set Name: Dual Wavelength. Enter
              the name in the text box. Dual wavelength is also known as Delta OD, you may
              want to use this name instead .
        10. In the Plate Formula field enter: DS1-DS2 to subtract the reference
              wavelength (630) measurements from the test (410) measurements. Retain the
              default: Use single formula for entire plate.
        11. Click OK to save and close the Transformation

               Click Curve Analysis. In the Data In tab, use the drop-down list to select Y
                 Data: Dual Wavelength and click OK.

         For this simple protocol, the remaining default settings are acceptable.
           More options are available, like customizing the names of data sets,
           plotting interpolations in the generated curve, and so on. See Plotting
           a Curve in the Data Reduction Options chapter.

               Click OK to close the Data Reduction dialog.

        12.      Set the Report parameters and Data Views as desired. For instructions, see
              Viewing Results.
        13. Save the protocol: select File>Save and name it DualWave1 for this example.
              0.

Run the protocol:
Now, you're ready to run the DualWave1 protocol in an experiment.
        1.    Select File>New Experiment. By default, Gen5 highlights the DualWave1
              protocol in the dialog, making selection quick and easy.
        2.    If the reader is all set up, you're ready to go: Click Read and follow the online
              prompts.



64 | Chapter 4: Assay Examples




Basic Absorbance Spectrum Analysis
        Numerous applications can profit by a preliminary spectral screening. Here are
        instructions for setting up a basic spectrum protocol in Gen5.


            It may be easier to follow these instructions if you have already watched the Gen5
        Basic series of online tutorials: select Help>Tutorials, or if you've completed the
        learning exercises described in the Getting Started Guide.


1. Defining the reading Procedure
        This assay example uses a kinetic read for analysis.
         1.   Select File>New Protocol
         2.   Open the Procedure (double click Procedure in the menu tree)
         3.   Click Read and change the Read Type to Spectrum
         4.   Set the Wavelength range: for this exercise set Start to 200 and Stop to 550
         5.   Set the Step to 3, and close the Read step
         6.   Click OK to save and close it.0.

2. Defining the Plate Layout
        Define the plate layout in the usual way to reflect the arrangement of unknown
        samples, standards and blanks on the microplate.

3. Defining the Data Reduction Steps
        Now that you've defined the reading parameters and plate layout, you can define the
        data reduction steps:
         1.   Select Protocol> Data Reduction
              Gen5 automatically sets up the a Well Analysis for Min/Max OD. If Blanks
              have been assigned to the plate, it will be preceded by and based on a blank-
              subtraction Transformation step.
         2.   Click Well Analysis to add another step
         3.   Enter a unique name for this step in the Label field
         4.   Select one of the offered Calculation Types: Integral or Formula
         5.   Click OK to save and close the step
         6.   Click OK to save and close Data Reduction0.







4. Save the Protocol
       1.   Define the Reporting Requirements using the Report Builder or export options

       2.       Save the protocol0.
      Now you can run it in an experiment: select File>New Experiment

5. Viewing the Results
      After you read the plate, you can take advantage of Gen5's Well Zoom to examine the
      results. This feature is described in the Kinetic Analysis chapter.



66 | Chapter 4: Assay Examples




Protein Quantification: Endpoint Absorbance
        Here are instructions for the Gen5 portion of running this type of assay - the easy
        part. Correctly mixing and dispensing the standards, and pipetting reagents to the
        plate is the tricky part. Follow the assay instructions closely and modify these steps, as
        needed. Click the links for instructions at each step.
         1.   Select File>New Protocol
         2.   Define the Procedure




                1.        Select Protocol>Procedure
                2.   Click Read to add one read step
                3.   Keep the default settings:
                      Detection Method = Absorbance
                      Read Type = Endpoint
                4.   Set the Wavelength using the drop-down or enter 650 in the nm field
                5.   Click OK twice to close and save the Read step and the Procedure0






 3.   Define the Plate Layout




Set up Gen5's plate layout to match your placement of samples and standards on the
plate, for example:

        1.       Select Protocol> Plate Layout
        2.   In the Well Settings box, select the Type of specimen, first Standards,
             then Blanks, then Samples

        3.      Define the Concentration of the Standards:
        4.   Set the Replicates to 4
        5.   Assign the well IDs to their corresponding locations in the plate matrix
             by clicking in the respective wells in the matrix. Use the Auto Select
             options to speed up your work. 0

 4.   Define the Data Reduction:




Gen5 creates a Blank Subtraction data set when you put blanks on the plate, as defined
above. Click in the white space below the Transformation step:
       Click Curve Analysis to create a standard curve:
       Data In: Well ID is set to STD. Set the Y Axis = Blank [650]



68 | Chapter 4: Assay Examples



               Curve Fit: Method is set to Linear Regression

         5.   Define the Reporting Requirements 0.

Save the Protocol
      Select File> Save when you're finished setting up the protocol. You'll be able to use
      this protocol repeatedly to run this assay in an experiment.
        Select File> New Experiment and select the protocol when you're ready to run it, i.e.
        reagents are reconstituted, the plate is prepared, etc.







Basic Fluorescence Assay Example
       To help you set up your own assay in Gen5 here is an example of the steps required for
       nucleic acids quantitation using a fluorescent stain, such as the dsDNA specific
       PicoGreenTM.

1. Defining the reading Procedure
    This assay example defines a single-filter-set Fluorescent endpoint read:
        1.   Select File>New Protocol
        2.   Select Protocol>Procedure
        3.   Click the Read button and change the Detection Method to Fluorescence
        4.   To set the Filter Set: filter-based reads use the drop-down list to select the
             filter for Excitation and Emission, for this exercise 485/20 and 528/20,
             respectively; monochromator-based reads enter 485 and 528 in the text fields.
        6.   Keep the Optics Position set to Top and if applicable select a mirror, e.g. Top
             510, that corresponds to the selected filters. Top 50% works with any filter.
        7.   Enter 65 for the Sensitivity setting when using filters or enter 100 for the
             setting when using the monochromator
        8.   Click OK twice to save and close the Procedure0.

2. Defining the Plate Layout
       Define the plate layout in the usual way to reflect the arrangement of unknown
       samples, standards and blanks, if any, on the microplate. For the sample protocol
       shipped with Gen5, we set up the plate this way:



70 | Chapter 4: Assay Examples



        Defining the expected concentration of the standards is the required to plot a curve.
        Find specific instructions in the Preparing Plates chapter.

3. Defining the Data Reduction Steps
        With the reading parameters and plate layout defined, Data Reduction steps can be
        created: a standard curve for determining the concentrations of the unknown samples:
         1.   Select Protocol> Data Reduction
         2.   Click Curve Analysis
         3.   Notice on the Data In tab, the Well ID is set to STD and X Axis Data to <Plate
              Layout Settings>. The known concentrations entered for Standards are plotted
              on the X Axis. Use the drop-down list for the Y Axis Data to select
              485/20,528/20 (or 485,528).
         4.   Retain the default settings for Curve Fit and the Data Out tab. Take note that
              the Data Set Name produced from the standard curve is called Conc (by
              default. You can change it.). Click OK to save and close the curve.
         5.   Click OK twice to save and close Data Reduction0.


           After the plate is read, you can return to the Data Reduction dialog to make any
        needed changes, like the Curve Fit Method. Do not change the Data Out or Data Set
        Names, this would invalidate the data reduction steps that use those data sets.


4. Save the Protocol
         1.   Define the Reporting Requirements using the Report Builder or export options

         2.       Save the protocol
        Now you can run it in an experiment: select File>New Experiment







Kinetic Fluorescence Assay Example
      To help you set up your own assay in Gen5 here is an example of the steps required to
      measure antioxidant capacity based on the free radical damage to a fluorescent probe,
      as in the Oxygen Radical Absorbance Capacity (ORAC) Assays. This protocol deploys
      Gen5's Synchronized Plate Mode for precise timing of the measurements.

1. Defining the reading Procedure
   This assay example defines a single-filter-set Fluorescent endpoint read:




       1.   Select File>New Protocol
       2.   Select Protocol>Procedure
       3.   Click Set Temperature and enter 37 for the temperature
       4.   Click Plate Out/In and select Move plate in
       5.   Click Delay and enter 0:30:00 minutes to let the reader warm up
       6.   Click Plate Out/In and select Move plate out
       7.   Under Synchronized Modes, click Plate for a synchronized-plate mode block
       8.   Click Shake and change the Intensity to Fast and the Duration to 0:15 seconds
       9.   Click Kinetic and set the Run Time to 1:00:00 hour and the Interval to 0:01:00
            minute
       10. Click the Read button, change the Detection Method to Fluorescence and set
            the Filter Set: filter-based reads use the drop-down list to select the filter for
            Excitation and Emission, for this exercise 485/20 and 528/20, respectively;
            monochromator-based reads enter 485 and 528 in the text fields.
       11. Keep the Optics Position set to Top and if applicable select a mirror, e.g. Top
            510, that corresponds to the selected filters. Top 50% works with any filter.
       12. Enter 65 for the Sensitivity setting when using filters or enter 100 for the
            setting when using the monochromator
       13. Click OK twice to close and save the Read step and the Procedure0.



72 | Chapter 4: Assay Examples



2. Defining the Plate Layout
       Define the plate layout in the usual way to reflect the arrangement of unknown
       samples, standards, controls and blanks on the microplate. For the sample protocol
       shipped with Gen5, we set up the plate this way:




        Defining the expected concentration of the standards is required to plot a curve. Find
        instructions in the Preparing Plates chapter.

3. Defining the Data Reduction Steps
        Now that we've defined the reading parameters and plate layout, we can define the
        data reduction steps: two well analysis steps and a standard curve.
         1.   Select Protocol> Data Reduction
              Gen5 automatically creates two steps: the Blank Subtraction Transformation
              and Well Analysis for Max V
         2.   Click Well Analysis to add another step to perform a calculation on the results
              of individual read intervals:
                6.   Enter a unique Label for this step, e.g. AUC
                7.   Select Formula and enter it in the text field:
                     (R1/R1)+(R2/R1)+(R3/R1)+(R4/R1)+(R5/R1)+(R6/R1)+(R7/R1)+(R8/
                     R1)+...(R61/R1). This formula normalizes the AUC (area under the
                     curve), the results are used to plot the standard curve to determine
                     unknown concentrations
                8.   Click OK
         3.   Click Curve Analysis to plot a standard curve:0.
                 1   On the Data In tab, select the Y-Axis Data. In this example, choose the
                     Well Analysis "AUC: Formula Result [Blank 485/20, 528/20]" or [Blank
                     485,528]"






              2    Click OK twice to save and close the Curve and the Data Reduction
                   dialog


         After the plate is read, you can return to the Data Reduction dialog to make any
      needed changes, like the Curve Fit Method. Do not change the Data Out or Data Set
      Names, this would invalidate the data reduction steps that use those data sets.


4. Save the Protocol
       1.   Define the Reporting Requirements using the Report Builder or export options

       2.       Save the protocol
      Now you can run it in an experiment: select File>New Experiment



74 | Chapter 4: Assay Examples




Fluorescence Assay with Injection
        To help you set up your own assay in Gen5 here is an example of the steps required to
        develop an ion channel assay and similar FRET assays which are well suited for
        sodium, potassium, calcium and ligand-gated ion channel research. This protocol
        deploys Gen5's Synchronized Well Mode to quickly switch between two emission
        filters in well kinetic mode.

1. Defining the reading Procedure
     This assay defines a kinetic dual-filter-set Fluorescent read:




          1.   Select File>New Protocol
          2.   Select Protocol>Procedure
          3.   Under Synchronized Modes, click Well for a synchronized-well mode block
          4.   Click Kinetic and set the Run Time to 0:40.00 and the Interval to 00.15 second
          5.   Click the Read button and change the Detection Method to Fluorescence
                  1   Define the Filter Set using the filter wheels, for this exercise set the first
                      filter set to 360/40 and 460/40, and the second filter set to 360/40 and
                      590/35
                  2   Set the Optics Position set to Bottom and enter 65 for the Sensitivity
                      setting
                  3   Click OK to close and save the Read step
          6.   In the Procedure workspace, highlight the End Mode step and click Dispense.
               Define the parameters for injecting the wells with 100 ul of a High K+ solution
               to initiate depolarization. Select Tip priming
          7.   Click Kinetic and again set the Run Time to 0:40.00 and the Interval to 00.15
               second
          8.   Click the Read button. Gen5 offers the limited-form read step because the
               parameters must match the first read step. De-select Append to previous
               Kinetic data and click OK (We're going to compare the before and after
               injection data sets, so we do not want them combined into one.)
          9.   Click OK to save and close the Procedure0.






2. Defining the Plate Layout
       Define the plate layout in the usual way to reflect the arrangement of the cells and
       blanks on the microplate. For this assay we set it up the plate this way:




        Find instructions in the Preparing Plates chapter.

3. Defining the Data Reduction Steps
        Now that we've defined the reading parameters and plate layout, we can define the
        data reduction steps. This type of FRET assay supports a direct comparison between
        the 590-nm and 460-nm fluorescence results via a ratiometric data reduction.
          1.   Select Protocol> Data Reduction
               Gen5 automatically creates four Blank Subtraction Transformation steps and
               four Well Analysis for Max V (one for each data set)
          2.   Click Transformation to add another step to determine the ratio of the pre-
               injection (polarized) reads:
                 1    Click the Select multiple data sets button: click the button for DS2,
                      use the drop-down lists to select DS1: Blank Read 1:360/40,460/40 and
                      for DS2: Blank Read 1: 360/40,590/35
                 2    Enter a New Data Set Name, e.g. Polarized Em Ratio
                 3    In the Plate Formula field enter DS1/DS2
                 4    Click OK
          3.   Repeat Step 2 selecting Read 2 data sets to calculate the post-injection
               (depolarized) ratio: DS1: Blank Read 2:360/40,460/40 and for DS2: Blank Read
               2: 360/40,590/35. For this assay we called the New Data Set: Depolarized Em
               Ratio
          4.   Create one more Transformation to calculate the response ratio:



76 | Chapter 4: Assay Examples



                 1   Click the Select multiple data sets button: click the button for DS2,
                     use the drop-down lists to select the previously calculated ratios, we
                     named them DS1: Depolarized Em Ratio and for DS2: Polarized Em
                     Ratio
                 2   Enter a New Data Set Name, e.g. Response Ratio
                 3   In the Plate Formula field enter DS1/DS2
                 4   Click OK
         5.   Perform additional Data Reduction steps, as needed, for further analysis
              outputs.
         6.   Define the Reporting Requirements using the Report Builder or export options

         7.       Save the protocol0.
        Now you can run it in an experiment: select File>New Experiment







Fluorescence Area Scan Example
       To help you set up your own assay in Gen5 here is an example of the steps required to
       perform a fluorescent area scan.

          The Synergy 2's and Synergy 4's probe size limits its ability to
            perform Fluorescence area scan in plates with a small well diameter.
            Generally, this means you must use a plate with fewer than 96 wells.

1. Defining the reading Procedure
    This assay example defines a single-filter-set Fluorescent area scan read on four wells:
         1.   Select File>New Protocol
         2.   Select Protocol>Procedure
           Synergy 2/4 users must change the Plate Type
         3.   Click the Read button and change the Detection Method to Fluorescence
         4.   Set the Read Type to Area Scan
         5.   Click the Full Plate button in the upper right corner of the screen
         6.   Turn off the Use all wells by clicking the checkbox
         7.   Click and drag over the matrix to select four adjacent wells to read
         8.   Define the Filter Set
         9.   Keep the Optics Position set to Top and if applicable select a mirror, e.g. Top
              510, that corresponds to the selected filters. Top 50% works with any filter.
        10. Enter 65 for the Sensitivity setting when using filters or enter 100 for the
              setting when using the monochromator
        11. Click OK twice to save and close the Procedure0.

2. Defining the Plate Layout
       Define the plate layout to reflect the arrangement of unknown samples, standards and
       blanks, if any, on the microplate. Find instructions in the Preparing Plates chapter.

3. Defining the Data Reduction Steps
       Gen5 automatically creates a Well Analysis Data Reduction step to determine the
       Mean, Standard Deviation and CV% of the scanned wells. You can additional
       calculations as needed: Protocol> Data Reduction



78 | Chapter 4: Assay Examples



4. Viewing the Results




                                         To view the results on-screen:
         1.   Open the Plate View, and select the Scans data set in the Data field.
         2.   For a Well Zoom click on a well
        Area scans can be used to determine the optimal settings for an assay.







Fluorescence Polarization Example
     To help you set up your own assay in Gen5 here is an example of the steps required to
     perform a fluorescent polarization experiment.


         It may be easier to follow these instructions if you have already watched the Gen5
     Basic series of online tutorials: select Help>Tutorials or if you've completed the learning
     exercises described earlier. Learn more about Fluorescence Polarization in Gen5's Help.


     To set up the protocol, we'll define the:
          1.   Reading Procedure
          2.   Plate Layout
          3.   Data Reductions 0.

           Reporting Results is the same process for all types of experiments

1. Defining the reading Procedure
       This assay example defines a single-filter-set Fluorescent area scan read on four wells:
          1.   Select File>New Protocol
          2.   Select Protocol>Procedure
          3.   Click the Read button and change the Detection Method to Fluorescence
          4.      Select Polarization by clicking the checkbox
          5.   Optionally, you can change the default settings for Light Source and Read
               Speed
          6.   To set the Filter Set, use the drop-down list to select the filter for Excitation
               and Emission, for this exercise 485/20 and 528/20, respectively
          7.   Gen5 automatically sets the Optics Position to Top and selects the mirror in
               position 3 because the polarizers are located above this mirror in the mirror
               holder. Since the mirror position is fixed for FP analysis, you must select a filter
               set that corresponds to the mirror in position 3.
          8.   Enter 65 for the Sensitivity setting
          9.   Click OK twice to save and close the Procedure0.

2. Defining the Plate Layout
     Define the plate layout to reflect the arrangement of unknown samples, standards and
     blanks, if any, on the microplate.



80 | Chapter 4: Assay Examples



3. Defining the Data Reduction Steps
    Gen5 automatically creates the Fluorescence Polarization steps, preceded by the blank-
    subtraction transformations if Blanks were assigned to the plate layout. You can add other
    Data Reduction steps as needed: Protocol> Data Reduction

4. Save the Protocol
         1.   Define the reporting requirements using the Report Builder or export options

         2.       Save the protocol. 0.
        Now you can run it in an experiment: select File>New Experiment







Basic Luminescence Glow Assay Example
       To help you set up your own assay in Gen5 here is an example of the steps required to
       use reporter genes, such as luciferase, for studying gene expression. The step-by-step
       instructions provided here mirror the sample protocol shipped with Gen5 for Glow
       Luciferase Assay.

1. Defining the reading Procedure
    This assay example defines a single-filter-set Luminescent endpoint read:
        1.   Select File>New Protocol
        2.   Select Protocol>Procedure
        3.   Click the Read button and change the Detection Method to Luminescence
        4.   Set the Integration Time to 1.0 SS.ss
        5.   To set the Filter Set, use the drop-down list to select the Hole for Emission
        6.   Keep the Optics Position set to Top and enter 200 for the Sensitivity setting
        7.   Click OK twice to save and close the Procedure

2. Defining the Plate Layout
       Define the plate layout in the usual way to reflect the arrangement of unknown
       samples, standards and blanks on the microplate. For the sample protocol shipped
       with Gen5, a Blank well and 47 unknown Sample wells in duplicate were defined.
       Find instructions in the Preparing Plates chapter.

3. Defining the Data Reduction Steps
       With the reading parameters and plate layout defined, Data Reduction steps can be
       created. Gen5 automatically creates the Blank Subtraction transformation. You can add
       additional calculations as needed.

4. Save the Protocol
        1.   Define the Reporting Requirements using the Report Builder or export options

        2.       Save the protocol
       Now you can run it in an experiment: select File>New Experiment



82 | Chapter 4: Assay Examples




Luminescence Flash Assay with Injection
        To help you set up your own assay in Gen5 here is an example of the steps required to
        use automated injection and luminescence detection for studying gene expression. The
        step-by-step instructions provided here mirror the sample protocol shipped with Gen5
        for Flash Luciferase Assay.

1. Defining the reading Procedure
     This assay example defines a single-filter-set Fluorescent endpoint read:
         1.   Select File>New Protocol
         2.   Select Protocol>Procedure
         3.   Click Well to set up a Synchronized Well Mode block
         4.   Click Dispense and set the Volume to 100 and the Rate to 300
         5.   Click Delay to define a Delay Time of 0:02.00 (two seconds)
         6.   Click the Read button and change the Detection Method to Luminescence
                 1    Set the Integration Time to 5.0 SS.ss
                 2    To set the Filter Set, use the drop-down list to select the Hole for
                      Emission
                 3    Keep the Optics Position set to Top and enter 180 for the Sensitivity
                      setting
                 4    Click OK twice to save and close the Procedure

2. Defining the Plate Layout
        Define the plate layout in the usual way to reflect the arrangement of unknown
        samples, standards and blanks on the microplate. For the sample protocol shipped
        with Gen5, 48 unknown Sample wells in duplicate were defined.

3. Defining the Data Reduction Steps
        With the reading parameters and plate layout defined, Data Reduction steps can be
        created. Gen5 automatically creates the Blank Subtraction transformation. You can add
        additional calculations as needed.

4. Save the Protocol
         1.   Define the Reporting Requirements using the Report Builder or export options

         2.        Save the protocol
        Now you can run it in an experiment: select File>New Experiment







Max Binding Determination/Competitive Assay
       To help you set up your own assay in Gen5 here is an example of the steps required to
       run a competitive ELISA assay to determine maximum binding. In this example we set
       up an endpoint Absorbance read, subtract Blank wells from all others, subtract NSB
       (non-specific binding) wells from all others, plot a standard curve, and define B/B0 as a
       percentage of bound sample and identify the Total Activity (TA) wells.

1. Defining the reading Procedure
    This assay example has a simple read Procedure: a single-wavelength Absorbance
    endpoint read:
        1.   Select File>New Protocol
        2.   Select Protocol>Procedure
        3.   Click the Read button and select the wavelength. Use the drop-down list or
             type the wavelength in the text field (overwrite the current value).
        4.   Click OK twice to save the Procedure

2. Defining the Plate Layout
       This step is critical for the data reduction steps to be defined later. Here's the plate
       layout we need:




       The critical factor is using the Well IDs, not their location on the plate. We customized
       the Well IDs for this example, changing the first three Assay Control IDs to NSB, Bo,
       and TA. Then, defined the known concentration of the standards and assigned all of
       them to the plate:



84 | Chapter 4: Assay Examples



              Well ID Type               Description

              BLK        Blank           DI water only

              NSB        Assay Control Assay-specific

              Bo         Assay Control Assay-specific

              TA         Assay Control Assay-specific

              STD        Standard        Known concentrations

              SPL        Sample          Unknown samples



3. Defining the Data Reduction Steps
        Now that we've defined the reading parameters and plate layout, we can define the
        data reduction steps: blank-well subtraction, NSB subtraction, determine the percentage
        bound and plot a standard curve. Gen5 creates the blank-subtraction step for you
        automatically.
         1.   Select Protocol> Data Reduction
              Notice that one Transformation, named "Blank nnn" where nnn is the
              wavelength, has already been created. We'll use the results of this calculation to
              build the next step.
         2.   Click Transformation
                   1   For the Data In use the drop-down list to select Blank nnn.
                   2   Enter a New Data Set Name for the results of this calculation, e.g.
                       B/Bo
                   3   In the Formula field enter: (X-NSB)/(Bo-NSB)*100
         3.   Click Curve Analysis
                   1   Notice on the Data In tab, the Well ID is set to STD and X Axis Data to
                       <Plate Layout Settings>. The known concentrations entered for
                       Standards are plotted on the X Axis. Use the drop-down list for the Y
                       Axis Data to select B/Bo (or whatever you named the New Data Set
                       Name in the previous step.)
                   2   Click the Curve Fit tab: depending on your assay, you may want to
                       change the curve fit method to 4 Parameters or another option, or use
                       Log values on the X or Y axis. For now, retain the defaults and click the
                       Data Out tab. Take note that the Data Set Name produced from the
                       standard curve is called Conc (by default. You can change it.).
                   3   Click OK to save and close the curve.
         4.   Save the protocol.
        Now you're ready to define your reporting requirements, and run the protocol in an
        experiment.






More Advanced Options
        Monitor Wells: Sometimes it is necessary/desirable to wait until a certain
          amount of activity has occurred in the plate before reading it. Gen5 will
          periodically check designated wells until they've reached a certain
          measurement when the Monitor Wells option is used. When the criterion is
          met, Gen5 continues the Procedure, i.e. the regular plate reading is performed.



86 | Chapter 4: Assay Examples




Toxicity/Cytotoxicity Assay
        To help you set up your own assay in Gen5 here is an example of the steps required to
        run a Toxicity or Cytotoxicity assay to determine LD50 (lethal dose). In this example
        the Read step is straightforward, but the Plate Layout takes full advantage of Gen5's
        ability to customize Well IDs. We'll create two samples with six dilutions each, and a
        control and blank for each sample. Then, we'll plot a standard curve based on blank-
        subtraction and toxicity percentage. We'll use Gen5's Curve Interpolation to identify
        LD50. toxicology

1. Defining the reading Procedure
     This assay example has a simple read Procedure: a single-wavelength Absorbance
     endpoint read:
         1.   Select File>New Protocol
         2.   Select Protocol>Procedure
         3.   Click the Read button and select the wavelength. Use the drop-down list or
              type the wavelength in the text field (overwrite the current value).
              Alternatively, you may want to perform a kinetic analysis.
         4.   Click OK twice to save the Procedure


2. Defining the Plate Layout
This step is critical for the data reduction steps to be defined later. Here's the plate layout we
need:






      The critical factor is setting up the Well IDs and dilution values. For the Samples,
      (notice there are only two samples on the plate) we defined the known dilution values
      and assigned them to the plate using the Auto Select features Next ID and Next Dil for
      3 Replicates. We customized the Well IDs for the Sample Control IDs to BLK to have
      sample-specific blanks and assigned them to plate without using the Auto Select
      features. Assay Controls were assigned to the plate in the same way as the BLK1 and
      BLK2.

            Well ID Type               Description

            SPL      Sample            Unknown samples with dilution values

            CTL      Assay Control     Sample-specific

            BLK      Sample Control Customized to be sample specific



3. Defining the Data Reduction Steps
      Now that we've defined the reading parameters and plate layout, we can define the
      data reduction steps: blank-well subtraction, toxicity percentage determination and a
      standard curve.
       1.   Select Protocol> Data Reduction
       2.   Click Transformation
              1    For the Data In only one data set, the raw data from the Read step is
                   available.
              2    Enter a New Data Set Name for the results of this calculation, e.g.
                   %Toxicity
              3       De-select the Use single formula for all wells
              4    In the Current Formula field enter: (X-BLK1)/(CTL1-BLK1)*100
              5    Click and drag over the SPL1 wells to assign the formula to them
              6    Change the Current Formula for SPL2 wells: (X-BLK2)/(CTL2-
                   BLK2)*100 and assign the formula to them
              7    Click OK to save and close the Transformation
       3.   Click Curve Analysis
              1    On the Data In tab, the Well ID is set to SPL- All IDs and X Axis Data
                   to <Plate Layout Settings>. The known dilutions entered for Samples
                   are plotted on the X Axis. Use the drop-down list for the Y Axis Data to
                   select % Toxicity (or whatever you named the New Data Set Name in
                   the previous step.)
              2    Click the Curve Fit tab and change the curve fit method to 4 Parameters
                   (unless you prefer another method).



88 | Chapter 4: Assay Examples



                 3   Click the Data Out tab, in the Interpolations table enter 50 (and 90, if
                     desired). 50 represents 50% toxicity and it will be plotted on the curve.
                     Click OK to save and close the curve.
         4.   Save the Data Reduction steps (click OK)

         5.       Save the protocol
        Now you're ready to define your reporting requirements, and run the protocol in an
        experiment.







Endotoxin Test
       Here are some guidelines for setting up a protocol to detect endotoxins in test samples
       using a Limulus Amebocyte Lysate assay kit.

         There are numerous variables when running this type of experiment.
           This example uses a kinetic analysis rather than an endpoint, for
           instance. Modify these procedures to comply with your assay kit
           instructions.

First, create a new Protocol: Select File>New Protocol

Set up the Procedure




        1.   Begin with Set Temperature
        2.   Add a Delay step to incubate the plate
        3.   Add a Shake step to mix the ingredients in the well
        4.   Add a Monitor Well step to delay the start time for collecting actual
             measurements until selected wells reach an OD of 0.05.
             Gen5 sets up well monitoring as a loop in the Procedure.
               1    Click Monitor Well to add the loop to the Procedure.
               2    Define the criteria that must be met before the reader moves onto the
                    next step
               3    With the End Monitoring step highlighted, click Read to define the
                    reading parameters for well monitoring.
               4    Select the wells to monitor and define the same reading parameters as
                    the actual read step: Absorbance read at 405 nm.
        5.   Add Kinetic and set the Run Time to 50 minutes and the Interval to 15
             seconds
        6.   Set the Read step to Absorbance at 405 nm.
        7.   Click OK twice to save and close the Procedure.



90 | Chapter 4: Assay Examples



Define the Plate Layout




        Take note of some of the conditions particular to this type of assay: Standards with
        decreasing concentration values, and only one Sample, with known dilution values, is
        assigned to the plate using the Auto Select features Next ID and Next Dil, in duplicate.
        For the "Spiked Samples" we customized the Well ID of Sample Controls (SPLC),
        changing it to Spike and assigned a concentration value. The Assay Control IDs were
        customized to Pos and Neg.

              Well Type          ID

              Standard           STD

              Sample             SPL

              Sample Control     Spike

              Assay Control      Pos & Neg

              Blanks             BLK


Set up Data Reduction
      Data reduction, in this endotoxin example, requires a blank-subtraction, an onset OD
      well analysis, a standard curve and a transformation for % Recovery determination.
      Gen5 creates the blank-subtraction data set and a Max V Well Analysis step
      automatically.
         1.   Select Protocol>Data Reduction
              Gen5 created the Blank 405 data set (if you defined this wavelength for the
              Read step) and used Blank 405 as the Data In for the Well Analysis step. (You
              can retain or replace the Max V step.)






       2.   Click Well Analysis to determine the Onset OD (if this is the second Well
            Analysis step, give it an unique Label):
              1    Set the Data In to Blank 405
              2    Select the button for Onset OD
              3    Enter 0.03 for the value.
       3.   Click Curve Analysis to create a standard curve:
              1    On the Data In tab: set the Well ID to STD and the Y Axis Data to t at
                   Total OD [405]
              2    On the Curve Fit tab: select Linear Regression for the method and
                   change the X Axis Data and Y Axis Data Transformation to Log
              3    On the Data Out tab: select both Calculate Concentrations options.
                   Enter a Data Set Name for the Concentration X Dilution results: Conc
                   X Dil.
       2.   Click Transformation to calculate the percentage recovery:
              1    For the Data In select Conc X Dil
              2    Enter a New Data Set Name: % Recovery
              3       De-select the Use single formula for all wells
              4    In the Current Formula field enter: (Spike1-SPL1:1)/(.125)*100
              5    Click in the Spike1 wells to assign the formula to them
              6    Change the Current Formula for SPL1:2 wells: (Spike2-
                   SPL1:2)/(.125)*100 and assign the formula to the Spike2 wells
              7    Change the Current Formula for SPL1:3 wells: (Spike3-
                   SPL1:3)/(.125)*100 and assign the formula to the Spike3 wells
       3.   Repeat the process for all the spiked samples
       4.   Create two Validation steps:
              1    Click Validation and set the Data In = t at Total OD [Blank 405]
                    enter the Formula = Neg>STD5*1.1

              2    Click Validation and set the Data In = % Recovery
                    enter the Formula = 50%<Spike#<200%


Set up the Report
      Define your reporting requirements as with all other types of experiments.

Save the Protocol
      Select File>Save when you're finished setting up the protocol. You'll be able to use
      this protocol repeatedly to run this endotoxin assay in an experiment. Select
      File>New Experiment and select the endotoxin protocol when you're ready to run it,
      i.e. reagents are reconstituted, the plate is prepared, etc.



92 | Chapter 4: Assay Examples




ss-Galactosidase
        Quantitation of ss-galactosidase (ss-gal) enzymatic activity is a commonly used
        determination in cellular and molecular biology. A colorimetric assay using o-
        nitrophenol-B-D-galactoside (ONPG) as the substrate for ss-gal is described in an
        Application Note on BioTek's website. Here are instructions for setting up this type of
        assay in Gen5.

1. Defining the reading Procedure
        This assay example uses a kinetic read for analysis.
         1.   Select File>New Protocol
         2.   Open the StepWise Procedure
         3.   Click Kinetic. Gen5 opens the Kinetic Step controls. Define the timelines:
               Enter 0:30:00 minutes for the Run Time
               Set the Interval to 0:00:30 seconds
         4.   With the End Kinetic step highlighted, click Read and set the Wavelength to
              420
         5.   At the Procedure dialog, click OK to save and close it.

2. Defining the Plate Layout
        This assay requires 12 standards are decreasing concentration. The plate layout is
        critical to the data reduction steps defined later:




        The Standard concentrations can be defined in Gen5 using the Auto entry tools:






                                                     1.   Set the Well Type to Standard
                                                          and click the 3-dot button next to
                                                          the Conc. field
                                                     2.   Enter 10 in the table for STD1
                                                     3.   Fill the checkbox next to Fact. and
                                                          enter .5 in the text field
                                                     4.   Click in the STD2 cell in the table
                                                          to apply the factor
                                                     5.   Click in or use the down arrow
                                                          key to move to each next cell
                                                          until STD12
                                                     6.   Change STD12 to 0




      Assign the location of the standards and unknown samples to the plate.

3. Defining the Data Reduction Steps
      Now that we've defined the reading parameters and plate layout, we can define the
      data reduction steps: two well analysis steps and a standard curve.
       1.   Select Protocol> Data Reduction
            Gen5 automatically sets up the first Well Analysis for MaxV
       2.   Click Well Analysis to add another step
              1    Enter a unique name for this step in the Label field, e.g. Mv for this
                   exercise
              2    Select the Mean V Calculation Type
              3    Click OK to save and close the step
       3.   Click Curve Analysis to define a standard curve
              1    On the Data In tab set the Y-Axis Data to Mv: Mean V[420]
              2    On the Curve Fit tab select 4 Parameters
              3    Click OK to save and close the curve step
       4.   Click OK to save and close Data Reduction0.

4. Save the Protocol
       1.   Define the reporting requirements using the Report Builder or export options

       2.       Save the protocol0.
      Now you can run it in an experiment: select File>New Experiment



94 | Chapter 4: Assay Examples




Dispensing Reagent
        Dispensing reagent during an experiment is affected by the type of analysis. Select the
        option that most closely fits your requirements:
           Dispensing Reagent in a Kinetic Analysis
           Dispensing Reagent in an Endpoint (non-kinetic) Analysis



Dispensing Reagent in Kinetic Analysis Protocols
        If dispensing is required during a kinetic read, here are two options:

Manually Dispensing Reagent:
        Create a protocol with an extended kinetic interval; add enough time to dispense
        reagent to the plate between readings. During an interval, when the reader is idle:
         1.   Push the carrier eject button on the front of the reader to eject the plate
         2.   Perform the dispense using a pipette
         3.   Push the carrier eject button to draw the plate back in
         4.   The read will continue as scheduled0.




Readers with Injectors:

Standard Mode:
        Define two kinetic read steps around a dispense step in the Procedures:
         1.   Set the Kinetic timelines, define the Reading parameters, and End the loop.
         2.   After the loop, add a Dispense step to dispense the reagent. (You can add a
              Delay and/or Shake step after dispensing and before the next kinetic loop.)
         3.   Add a second Kinetic loop, kinetic settings can differ. Add a Read step to the
              loop, and check Append to Previous Kinetic Data. Selecting this option copies
              the previous defined reading parameters, e.g. wavelength/filter set, to this
              step. 0.







Synchronized Mode:
      For Fluorescence or Luminescence analysis select Plate or Well Mode to most precisely
      control the timing of your experiment. Learn About Synchronized Modes in Gen5's
      Help.
       1.   Add a Plate or Well mode block to the Procedure
       2.   Create a Dispense step to dispense the reagent. (You can add a Delay, and in
            Plate mode a Shake step, after dispensing and before reading.)
       3.   Add a Read step to the block, defining the reading parameters as needed.
       4.   Within the block you can repeat any or all of the options: Dispense, Delay,
            Shake in Plate mode, and Read, again. Note: the first Read step in the block sets
            the parameters0.


Dispensing Reagent in Endpoint Analysis

Manually Dispensing Reagent:
      Add a Plate In/Out step to the Procedure:
       1.   You might want to incubate the plate before adding the reagent. If so, and your
            reader is capable, add a Set Temperature step.
       2.   Add a Plate In/Out step. Enter "Add Reagent" in the Comment field.
       3.   Add a Read Step.0.




Readers with Injectors:
      Define a dispense step in the Procedure:
       1.   Create a Dispense step to dispense the reagent.
       2.   Add a Delay and/or Shake step after dispensing, if desired.
       3.   Add a Read step.0.



96 | Chapter 4: Assay Examples




 Other Options
        Multi-Detection Methods
        For readers capable of performing multiple detection methods, like BioTek's Synergy
        models, Gen5 supports multi-detection kinetic protocols.

        Discontinuous Kinetic Procedure
        A Discontinuous Kinetic Procedure can be defined to execute a sequence of readings
        over an extended time period. Use the Procedure's Advanced Options to conduct an
        experiment that requires long periods of downtime (for rest or incubation) between
        reads. Learn more in the Gen5 Help.







Fast Kinetics with Injection for Absorbance




                       for Synergy HT with Injectors, Synergy 2, and Synergy 4



 BioTek's multi-detection readers Synergy 2 and Synergy 4 can perform
   absorbance reads in Synchronized Mode, providing more ways to perform fast
       kinetics. You may need to experiment with the various options to determine the
       best method for your assays. Generally, for the shortest kinetic intervals, < 2
       seconds, use Well Mode. For intervals > 15 seconds, use Synchronized Plate
       Mode. Alternatively, copy the procedure described here, it is a work-around for
       Synergy HT.

    Gen5 lets you dispense fluid to wells when performing a kinetic absorbance analysis, but
    the Synergy HT cannot perform Absorbance reads in Synchronized Mode. Here is a way to
    mimic this fast kinetic behavior: define the Procedure to dispense and read one row at a
    time, like this:




        3.   Add a Dispense step
             1.   Click the Full Plate button and change it to read the first row, A1-A12
             2.   Select Priming and set the Volume to 20 ul
             3.   Set the Dispense Volume
             4.   Click OK0.
        4.   Click Kinetic, set the Run Time and click Minimum Interval



98 | Chapter 4: Assay Examples



         5.   Add the Read step
              5.   Click the Full Plate button and change it to read the first row, A1-A12
              6.   Set the Read Speed to Sweep
              7.   Select the wavelength
              8.   Click OK0.
         6.   Now, repeat steps 3-5 selecting the next row (e.g., B1-B12, then, C1-C12 ...) for
              each series of steps. Note: Highlight the empty space beneath the End Kinetic
              step before adding the next Dispense step. When defining the subsequent Read
              steps, de-select Append to previous Kinetic data to enable the reading
              parameters controls.
         7.   When you've defined a Dispense step and Kinetic read for each row of the
              plate, click Validate to obtain the minimum kinetic interval for each read and to
              make sure the reader can perform the Procedure. 0.
