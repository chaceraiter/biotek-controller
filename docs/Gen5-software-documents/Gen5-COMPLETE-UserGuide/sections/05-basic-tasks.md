# Chapter 5: Basic Tasks

     This section provides instructions for performing basic tasks in
     Gen5. It also describes the process for creating an Experiment
     (based on a protocol).


 Quick Read ............................................................................. 100
 Create a Standard Curve........................................................... 101
 View Results............................................................................ 102
 Print Results............................................................................ 104
 Quick Export ........................................................................... 105
 Quick Output Options ............................................................... 106
 Test the Reader ....................................................................... 108
 Setting up an Experiment ......................................................... 109
 Read a Plate ............................................................................ 110



100 | Chapter 5: Basic Tasks




Quick Read
        In Gen5, a Quick Read is using the microplate reader connected to the PC to read a
        plate and report the results. It's called quick because it is accomplished without taking
        the time to set up a protocol.

To perform a Quick Read:
          1.    Click Read a Plate from the Welcome page (and skip down to Step 4)
                or Click     or select File>New Experiment
          2.    Select Default Protocol

          3.    Click    (the Read button)
                The Procedures dialog opens.

          4.    Click               and enter the desired reading parameters, and any other
                needed steps. When you click OK to save and close the Procedure, the Plate
                Reading dialog opens.
          5.    Click Read0.

               When the reading is done you can report the results or select a view and click the
        Quick Export button to use Excel(R) to manipulate the data.







How to Create a Standard Curve
    Gen5 lets you create one or more standard or calibration curves for determining the
    concentration of test samples:
     1.   Select File> New Protocol
     2.   Select Procedure and define the Read step (and any other required steps)
     3.   Select Plate Layout:
           Define the Concentrations of the Standards
           Assign the location of the standards, samples, and blanks (if any) on the
             plate
     4.   Select Data Reduction> Curve Analysis
           Gen5 may have generated a "corrected" data set: if you assigned blanks to
             the plate or selected Pathlength Correction in the Read step, you'll want to
             select these data sets for Data In for the Y-Axis Data when plotting the
             curve

     5.      On the Data In tab, use the drop-down to select the Y-Axis Data
     6.   On the Curve Fit tab, choose a curve fit method
     7.   Other options and requirements when defining multiple curves:
           Curve Name: replace the default "Curve" with a more meaningful or unique
             name
           On the Data Out tab, replace the default "Conc" for the Data Set Name with
             a more meaningful or unique name
           On the Data Out tab, define interpolations to plot on the curve
     8.   Define the reporting or export requirements and Save the protocol. Now,
          you're ready to run an experiment: select File> New Experiment to read the
          plate and generate the curve.0.



102 | Chapter 5: Basic Tasks




Viewing Results

           Learn more in the Viewing Results chapter.

        You can instantly view the results of an experiment in Gen5's main workspace using
        the Plate View:




            After reading the plate (or otherwise acquiring data), in the Plate View use the
              drop-down list for Data to display the raw data and any data reduction results

                 Click the 3-dot button next to a data set to customize the view's
                appearance, including changing the numeric Format, e.g. number of decimal
                places, and the Font. (This feature is also available in the Data Views dialog.)
            ** Asterisks are used to signal a change: in Gen5's title bar an asterisk
              indicates the current file has been changed but not-yet saved. When asterisks
              enclose a data set it has been become invalid. Generally this is because a Read
              step or Data Reduction step has been altered. Edit custom-made data views to
              select valid data sets

                  384- and 1536-well plates require resizing to effectively see the data. Gen5
                adds a button to the Plate View to zoom in on the top-left quadrant of the plate
                and zoom out to view the entire plate. After zooming in, use the scroll bars to
                bring the other quadrants into focus. Find more on resizing the views in Gen5's
                Help

                  Click the Quick Export button to instantly open the current view in Excel(R).
                Learn more about Gen5's Export Options



            Multi-index readings offer another viewing option. Kinetic and scanning reads
              generate views based on the number of read intervals, wavelengths, or






            positions defined. Use the spin buttons or enter the desired read index and
            click Show to display it. Gen5 displays the time, wavelength, or position of the
            selected read number.

             Kinetic and Scanning protocols can generate Well Analysis data sets
            labeled Curves in the Matrix drop-down list, open the Curves data set and click
            on a well for a Well Zoom


          Starting at the Curves data set, you can display multiple well zooms
       simultaneously by holding down the Ctrl key while selecting (up to 8) wells


        You can also select Create new Matrix to define a new view
        Select the Statistics tab to view a table of data reduction results
        Select the Graphs tab (when available) to view any Curves, except kinetic
          analysis curves, which Gen5 calls Well Analysis and is described above
        Select the Cutoffs tab (when available) to view the values or results of the
          cutoff formulas
        Select the Validation tab (when available) to view the values and results of the
          validation formulas
        Review this description of Gen5's naming convention for the raw data/results:
          Data Set Naming on page 316


 Important Notes:
             Gen5 may not display some data points by default; to see them you must
               create your own Data Views. If you expected to see certain results that are
               not currently displayed, try creating your own views.
             All data views are also available for Reporting and/or Exporting
             Gen5 always uses your computer's Regional Settings to display and input
               data.
             Modify a data view to change the way results are reported, including the
               number of decimal places and significant digits. Learn more in the Viewing
               Results chapter, including the meaning of the Symbols and Notations
               displayed



104 | Chapter 5: Basic Tasks




Printing Results
     Gen5 offers numerous options for results output. It's report engine offers two primary
     outputs:

                  Click the Print button to print the results of an experiment AFTER you
                have created a report.
            QuickPrint instantly generates a print out of the current view or selection.
              After selecting the current view or specific content, right-click and select
              QuickPrint. Click and drag to select contiguous cells or hold down the Ctrl key
              and click to select non-contiguos cells.

Create a Report:

         Before you can print a report, you must select the report content using Gen5's Report
     Builder.
        Reporting in an experiment is done on a per plate basis:

                 Highlight a            in the menu tree and select Print/Print Preview.
                 In a multi-plate experiment: You can select multiple plates by holding the
                   Ctrl key while highlighting them, or to select contiguously-ordered plates,
                   highlight the first plate, hold down the Shift key and select the last plate.
                   Then, click the Print button.
            Gen5 offers enormous flexibility in report output. After defining the report
        elements, use the Print Preview option to view the report on-screen before printing it
        to paper. Unneeded columns and other individual report elements can be removed or
        modified to improve the appearance and usefulness of the report.

More Information:
        Find step-by-step instructions for creating and customizing reports in the Reporting
        Results chapter.







Quick Export

         Click the Quick Export button to instantly create a copy of the current screen in
     Excel(R).
  Where it works:
     Wherever you see the Quick Export button, you can export the view. Almost every
     Data View has a Quick Export button. For example, the Matrix, Statistics, Cutoff and
     Validation tabs offer it and the Graph tab has two, one for the curve and another for
     the Curve Results Table.


     Adjust the Quick Export Settings to select the target spreadsheet for the Quick
  Export. You can add items to the bottom of an existing Excel worksheet, for example.
  Select Protocol>Protocol Options>Quick Export Settings.



  If you don't have MS Excel:
     Use one of these options (described in the Exporting Results chapter) to select content
     and export it for use in another software application:
        File Export Builder: to export selected data to a text file
        Right-Click Menu Options - Copy to Clipboard and Save As: to copy or save
          the current selection for use in another software application



106 | Chapter 5: Basic Tasks




 Quick Output Options

     In addition to the      Quick Export option, Gen5 offers several ways to output data,
     results and current views. Use the right-mouse-click menu that is available in most views
     for instant printing or exporting content for use in other software applications.


         Simply right-click to select the entire current view for a quick output. Or, to limit the
     output: click and drag to select contiguous cells or hold down the Ctrl key and drag to
     select noncontiguous cells, then right-click for an option.


Copy to Clipboard




          1.   After selecting specific content or a current view, right-click and select the
               Copy to Clipboard feature
          2.   Open another software application, e.g. Microsoft(R) Word, WordPad, Paint,
               Outlook and similar products offered by other manufacturers, where you want
               to use the Gen5 content
          3.   Paste the selected content. Try:0.
                    Ctrl-V
                    Right-click and select Paste
                    From the menu, select Edit> Paste

Quick Print




        You can print the whole view or click and drag an area to select specific content for the
        QuickPrint.
            After selecting specific content or a current view, right-click and select the
              QuickPrint feature.






        It is similar to printing from the Report Builder, you can select a local printer. The
        current view or selected content is printed in formatted text with row and column
        headers.

Save As




        In any graph, i.e. Curve or Well Zoom, you can:
          1.   Right-click and select the Save As feature
          2.   Gen5 opens the standard Save As dialog so you can browse to any
               file/directory available to your PC to choose the Save In location



          3.   Use the drop-down list to select the Save as type: 0.
                   Portable Network Graphic (.png)
                   24-bit Bitmap (.bmp)
                   CompuServe Graphics Interchange Format (.gif)
                   JPEG Format (.jpg)
                   Windows Enhanced Meta File (.emf)

Export Multiple Plates to One File
       When you run multiple plates in an experiment you can export all the data to one text
       file:
          1.   In the menu tree, select/highlight multiple plates (by holding down the Ctrl
               key)
          2.   Right-click and select File Export0.

          Make sure the File Export Settings are defined to automatically append
            the data.



108 | Chapter 5: Basic Tasks



Reader System Test
     System> Diagnostics> Run System Test

           The System Test for the ClarityTM Microplate Luminometer must be
             performed using the Clarity PC software. Refer to the Clarity
             Operator's Manual for instructions.

Run the Test
     Most BioTek readers perform a self-test every time they're turned on, but when you want
     to view and/or print the results of a system (aka optics) test:
          1.   Select System> Diagnostics>Run System Test
          2.   When there is more than one reader attached to the PC, select the desired
               reader and click OK
          3.   When the test is completed:0.
               1.   Fill in the text fields, User, Company, Comments, to be included in the
                    report of the test results. Then, click OK.
               2.   Print the report to retain a hard copy for your records
               3.   Save As to convert the results to a text file. This is especially useful when
                    troubleshooting a reader. You can email the text file to BioTek TAC.0.

Test History
        Gen5 keeps the results of System Tests when they are performed using the menu
        controls. To review or print them, select System> Diagnostics> Test History...







Setting up an Experiment
   File> New Experiment

About Experiments
      In Gen5, all plates are processed in an Experiment, which is based on a protocol. The
      Experiment holds all the information: the Protocol as it was executed, the plate layout,
      the raw data, and the transformed data and calculation results from Data Reductions.
      An experiment is stored in a file with an .xpt extension.

How to:

          1.   Click the    button or select File>New Experiment
               This opens the Protocol selection dialog with the most recently
               opened/modified protocol selected
          2.   Select a protocol:
                You can select an existing one: double-click the desired protocol, or
                Select Default Protocol
          3.   Review (and modify as needed) the elements of the selected protocol, and
               when you're ready click the Read button

          4.   Select File>Save or click       and give the experiment file a unique name.0.


 In an experiment, you can:
                      Add Plates: to process additional plates using the same protocol

                Delete and Renumber Plates: When multiple plates have been added to an
                  experiment, highlight a plate in the menu tree, right click and select Delete.
                  After removing a plate, right click and select Renumber All, if needed

                      Read multiple plates: when multiple plates have been defined in an
                    experiment, highlight one and hold the Ctrl key to select others, then right
                    click for options: Read or Print

                      Use the Quick Export feature to instantly export the current view to
                    Excel(R)


     You can make changes to the Protocol when running it in an Experiment. Select
  File>Save Protocol As to save the changes for a future experiment. Otherwise, the
  Experiment's protocol and the original Protocol will be different.



110 | Chapter 5: Basic Tasks




Read a Plate

            Highlight the plate in the menu tree and click the Read button on the toolbar or
        right-click and select Read to read the plate.

Prerequisites and other issues:
            Minimally, you must define some reading directions, like wavelength. In Gen5
              this is a Quick Read
            If the reading is part of an experiment or assay that you'll perform numerous
              times, create a new protocol

            Click the Read button when an experiment is stopped and you want to begin
              again:
               you can Resume a reading procedure: continue from the stopping point, if
                  a Stop/Resume step has been defined
               or Re-Read the plate, starting from scratch, i.e. overwriting any previously
                 obtained measurements
            Define the Runtime Prompts: You can customize the "prompts" or text fields
              users see when they read a plate

Immediately before a read:
            Runtime Prompts: Fill in the fields defined in the Protocol as Runtime Prompts
            Set Temperature: Gen5 displays a warning message telling users to wait until
              the defined temperature is reached before proceeding with the read
            Load Plate: Gen5 displays the current reading-chamber temperature (if the
              reader has an incubator). If the temperature is too high, you can Cancel the
              read to wait until it cools down



Acquiring Data
        There are three ways for Gen5TM to acquire the data used in calculations and analysis:
            Reading a plate
            Manual entry
            Import a text file
        In Gen5 select Help>Help Topics to learn about the latter two options.
