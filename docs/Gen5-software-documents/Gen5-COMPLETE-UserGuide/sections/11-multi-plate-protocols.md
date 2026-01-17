# Chapter 11: Multi-Plate Protocols

     An overview and specific instructions for creating multi-plate
     protocols is provided in this chapter.


 Designing a Multi-Plate Protocol ................................................. 206
 About Multi-Plate Protocols........................................................ 207
 Running a Multi-Plate Protocol ................................................... 209
 Calibrator-Plate Protocols .......................................................... 212
 Multi-Plate Assay Protocols........................................................ 215



206 | Chapter 11: Multi-Plate Protocols



Designing a Multi-Plate Protocol
         There are numerous applications for multi-plate protocols, not to be confused with
         multiple-plate experiments described on page 208.
         Select the option that best meets your needs:
            Calibration Plate Protocols: Define a calibration or standards plate to
              determine concentrations of test samples on other plates
            Multi-Plate Assay Protocol: Use multiple plates to accommodate one assay.
              During processing and data reduction, Gen5 treats the multiple plates as if all
              samples and controls were on one plate
            Batch Processing: Process a batch of samples, using a limited number of
              standards, and incrementing continuous sample numbers across multiple
              plates.

           Important: All multi-plate protocols begin the same way, by first
             defining the number of plates required: Select File>New Protocol
             and set the Protocol Type as the first step.






About Multi-Plate Protocols
      For the numerous applications requiring multiple-plate processing, Gen5TM helps you
      conduct multi-plate assays or to process multiple plates in an experiment. The method
      you choose depends on the requirements of your protocol. This information is
      intended to help you select the most efficient method.
      The considerations include Plate Layout, Read Type, and data and kinetic analysis
      requirements:
         Do you need more than one plate layout to distribute samples,
           standards, controls, and blanks? If yes, then a multi-plate protocol is
           required. Otherwise, you can process multiple plates in any experiment, each
           containing unique Sample IDs to distinguish and track samples, but with the
           same plate layout (Well IDs).
         Do you need to perform calculations on the data across multiple
           plates that have the same plate layout? Multiple plates with the same
           layout can be processed in any experiment, but the results of each plate stand
           alone. Results are viewed, reported, exported and transformed individually per
           plate. If your assay requires determining means, ratios, or other factors across
           the multiple plates being processed, then you need a Multi-Plate Assay
           Protocol.

        Note: By default, Gen5 averages replicates when performing
          calculations. Blanks, controls, and any other identical Well ID that
          occurs across the multiple plates will be averaged in automatically-
          generated data sets. You can override this feature by creating your
          own transformations for individual plates.

         Can you set up a standards or calibration plate that can be used to
           determine the concentration of samples that will be processed on a
           different plate? If yes, the best option is the Calibration Plate Protocol, which
           lets you define (at least) two plate layouts, one for the calibration plate and one
           for all the other plates to be processed. The other plates can contain test
           samples, blanks, controls, etc. and like regular experiments, the results of each
           plate are viewed, reported, exported and transformed separately. Up to 10
           calibrator plates are supported.
         Does your assay require kinetic (or time course) analysis of the plate?
           If so, your options are more limited. Gen5 does not support kinetic reads for
           Multi-Plate Assay Protocols

Step-by-Step Instructions:
            Setting up a Calibration Plate Protocol on page 212
            Setting up a Multi-Plate Assay on page 215



208 | Chapter 11: Multi-Plate Protocols



Multi-Plate Protocol vs. Experiment

           For this explanation you should already know the difference between
             an Experiment and a Protocol in Gen5TM. If you haven't already done
             so, read Experiment vs. Protocol in the Essential Concepts chapter.


            Important: This feature is limited by the level of Gen5 you're running:
            Gen5 Reader Control cannot run multi-plate protocols, but can process up to
              1000 plates in an experiment. However, since Reader Control does not support
              Plate Layout or Sample IDs, the following explanation of Gen5's potential may
              not be applicable
            Gen5 and Gen5 Secure are full-featured software levels supporting both types
              of multi-plate protocols and up to 1000 plates in an experiment
            In an Experiment you can process a huge number of plates (up to 1000 plates) <<
              use the Add a Plate feature >>. Naturally, an experiment that processes more
              than one plate can be called "multiple plate." Regardless of the number of
              plates, running this kind of experiment means applying the protocol to each
              plate in the same manner, and transforming, reporting, and exporting data
              individually, on a per plate basis. Generally, every plate in a multiple-plate
              experiment has the same plate layout. But, you can distinguish one plate from
              another by assigning unique Sample IDs to each plate.
            A Multi-Plate Protocol allows the definition of up to 10 plates as distinct
              entities. Each plate in a multi-plate protocol may serve a different function,
              and/or have a different plate layout. It can be as simple as incrementing
              continuous sample numbers across multiple plates, or much more complex.
              Here are examples:
                Multiple plates are required to run one assay - for quality control or other
                  purposes it is necessary to distribute test samples, standards, and controls
                  across a series of plates
                Calibrator plates containing only the standards, not the test samples, are
                  used to determine the concentration of samples on other plates. This allows
                  for a one-time setup and processing of the calibrator plate(s), followed by
                  the processing of up to 1000 test-sample plates in an Experiment
                Processing a batch of samples spread over 10 plates, with incremented or
                  user-defined sample numbers or IDs







Running a Multi-Plate Protocol
       When you run a multi-plate protocol in an experiment (File>New Experiment), the
       menu tree, data views and reports are slightly different than a standard experiment.

Calibrator-Plate Protocols:
          Calibrator-Plate experiments add an additional set of Protocol elements to the
            menu tree for each calibrator plate and one set for all the Other Plates. In an
            Experiment, Gen5 sets up the standard Plate View for every plate, one for each
            calibrator and test/sample plate (Other Plates).
            When you Add a Plate to the experiment, it takes on the attributes of the Other
            Plates.


                 Reporting is the same as any multiple-plate experiment. After building the
            report, highlight a          in the menu tree and click Print/Print Preview.
            You can select multiple plates by holding the Ctrl key while highlighting them.

Multi-Plate Assay Protocols:
          Multi-Plate Assay experiments have one set of Protocol elements and a unique
            Data View called InterPlates to display the Statistics, Graphs, Cutoff Values
            and Validation tabs (if applicable). The Matrix for each plate is still displayed in
            the standard Plate View for viewing results in this format.
            Unlike other types of protocols, Gen5 does not let you "Add Plates" to this type
            of experiment. The total number of plates required to set up the assay must be
            defined in the first step of creating the protocol.



210 | Chapter 11: Multi-Plate Protocols



         InterPlates




                  Reporting results for a multi-plate assay is different from standard
                experiments in a couple of ways. When you wan to include the Matrix view in
                a report or export, each Plate must be added to the Content individually. And,
                unlike other multiple-plate experiments, all the plates are reported together in
                one output (instead of a separate report for each plate). Just as the InterPlates
                view (described above) displays the Statistics, curves, and other data for all the
                plates in one view, this data is reported/exported simultaneously for all the
                plates.


Plate Layout for Multi-Plate Protocols
         Defining the layout of test specimens for a multi-plate protocol is identical to single-
         plate protocol layouts, only more so, i.e., there are more plates to define.
            Calibration plate protocols have a unique set of protocol elements for each
              calibrator plate and one set of protocol elements for the test plates, called Other
              Plates in Gen5. So, there are additional Plate Layout options in the menu tree:
              one for each calibrator plate, and one for all the Other Plates
            Multi-Plate Assay protocols retain one Plate Layout option but provide a grid
              or matrix for each plate within the dialog:







      Select each Plate # tab individually to define its layout.


Data Reduction for Multi-Plate Protocols
      Special formula syntax is available for performing Transformations across multiple
      plates:

   <well>.<plate>         When referencing a well              B3.3 = well B3 on Plate 3
                          coordinate in a multi-plate          DS1.H6.2 = well H6 of data
                          experiment, identify the             set 1 on Plate 2
                          specific well and plate using a
                          period
      Review the Formula Syntax tables in the Data Reduction Options chapter for more
      information.



212 | Chapter 11: Multi-Plate Protocols




Calibrator-Plate Protocols

Creating a Calibration-Plate Protocol
         This procedure defines a multi-plate protocol using a calibrator or standards plate to
         generate a standard curve that is used to determine the concentration of samples
         processed on other microplates.
Create the Protocol:
          1.   Begin by creating a new protocol: File>New Protocol
          2.   Select Protocol> Protocol Options
          3.   Highlight Protocol Type and select the Calibration Protocol button. Enter the
               number of Calibrator plates, maximum 10. Enter the expected number of
               Other Plates: the number of plates with samples to be processed, maximum
               1000. Click OK to save and close the dialog




               The menu tree changes to correspond to your input. Each calibrator plate is
               identified as "Plate #", the samples plates are identified as Other Plates. In this
               example (click the binoculars), Plate 1, the calibrator plate, is moved to the top
               of the tree with its own Procedure and other protocol elements. The Other
               Plates represent the test-sample plates and have their own Procedure, Plate
               Layout and so on. Generally for calibrator-plate protocols, only the Procedure
               for reading the plates are the same. The Plate Layout and Data Reduction steps
               are different. When multiple calibration plates are defined, each calibration
               plate has its own protocol elements.
          4.   Define the Plate Layout for Plate 1 and the Other Plates in the normal manner:
               assigning Standards with their respective concentrations to the calibrator plate
               (Plate 1) and assigning unknown samples with the required number of
               replicates to the Other Plates






       5.   Set up Data Reduction for Plate 1 and the Other Plates: define a Standard
            Curve for Plate 1 in the normal way. Then, for the Other Plates define Curve
            Analysis using the option to Use Curve from Calibrator Plate
       6.   Define the Report output individually for Plate 1 and the Other Plates. This
            can be a real time saver when running the protocol in an experiment


             Like single-plate protocols, Calibration Protocols allow additional
          plates to be added for processing when you run the experiment. Each
          plate is processed and its results reported separately. In Calibration
          Protocols, newly added plates are always Other Plates, rather than
          calibrator plates.

       7.   Save the protocol with a unique name.0.


Run the Calibration Protocol in an Experiment
      When the protocol has been created, it is ready to run in an Experiment.
       1.   Select File>New Experiment.
       2.   Select the calibration protocol.

                   Plate 1, in the menu tree, is always the first calibration plate
          in this type of protocol. After Plate 1, Gen5 adds one plate icon in the
          experiment for each calibration plate, and, one plate icon for (all) the
          Other Plates.

       3.   Highlight one of the plates, click Read and follow the online prompts.
            Continue this pattern, until all the plates are read.0.


        Each plate generates its own report (based on the user-defined report parameters).
      To simultaneously generate a report of all the plates, highlight the first plate in the
      menu tree, hold the Shift key and highlight the last plate, then click Print



214 | Chapter 11: Multi-Plate Protocols



Using Curve from Calibrator Plate
         For Calibration Protocols, Gen5 makes available a standard curve generated from a
         calibration plate, to plot the concentrations of test samples on the current plate.

           Prerequisite: You must first define the Procedure, Plate Layout, and
             Curve Analysis for the Calibrator or standards plate. Secondly, define
             the Procedures and Plate Layout for the sample plate (Other Plates).




          1.   Select Data Reduction>Curve Analysis
          2.   Enter a unique Curve Name
          3.   On the Data In tab, select Use Curve from Calibrator Plate and select the
               previously defined calibration-plate curve
          4.   On the Data Out tab, select the Y Data. You can also apply Interpolations, if
               applicable
          5.   Also on the Data Out tab, enter a unique name for the Concentration data set.
               If applicable, select the Concentration x Dilutions calculation and give this
               resulting data set a unique name.0.

           Options on the Curve Fit tab are disabled (grayed out) because they
             are owned by the "Curve from the Other Plate."






Multi-Plate Assay Protocols

Creating a Multi-Plate Assay Protocol
       This procedure creates a multi-plate protocol for an assay that requires the samples,
       standards and controls to be distributed to multiple plates. This method does not
       support kinetic analysis.
Create the Protocol:
        1.   Begin by creating a new protocol: File> New Protocol
        2.   Select Protocol> Protocol Options, highlight Protocol Type (at the top of
             the tree) for the multiple-plate options.
        3.      Select Multi-Plate Assay Protocol, and enter the number of plates required
             to layout the assay in the Number of Plates field (up to 10).
        4.   Accept or alter the default setting for identical plate layout. Selecting All plates
             have identical layout provides only one Plate Layout grid. Leaving it
             unselected provides one grid for each plate.
        5.   Define the Plate Layout as you would for any protocol, using the plate-
             numbered tabs to bring each grid into focus. Learn more on page 210.


           Keep in mind Gen5's default behavior is to determine and use the mean of like-
       named samples in data reductions. This applies to multi-plate protocols that distribute
       like-named items across the plates.


        6.   Define the Procedure: Read Steps and any other necessary activities.
        7.   Define the Data Reduction steps: the calculations will be performed for all the
             plates at once. Gen5 will automatically create data sets for Blank subtractions if
             the Plate Layout and Procedures suggest them.
        8.   Now you're ready to define your Report and/or Export requirements.

         Note: In this type of multi-plate assay, Gen5 treats the samples from
           all the plates as if they were on one plate, and reports the results from
           all the plates together in one report. To report results in the Matrix
           format in reports and exports, you must add one Matrix item for each
           plate to the Report/Export Content. See Designing multi-plate
           reports

        9.   Save the protocol. And, you're ready to run it in an experiment: File> New
             Experiment. 0.



216 | Chapter 11: Multi-Plate Protocols



Running a Multi-Plate Assay Experiment




         If you've already created a multi-plate single-assay protocol, here are a few tips for
         running it in an experiment.

                  Read each plate individually, as you would in any other experiment:
                highlight the plate in the menu tree and click Read

                   Inter-plates is a special view provided only for this type of protocol.
                Since data reductions are performed across the plates, the inter-plate view
                combines the statistics from all the plates into one table and shows any curves
                plotted from all the data points.

                   Designing the Reports and Export parameters for these kinds of assays
                requires extra attention: when adding Matrix items to the output content you
                must designate which plate it represents. Gen5 opens the Edit dialog to
                facilitate the process:
                1.   Add a Matrix item in the Available Data Views to add it to the Content box.




                2.   Now, double-click the matrix in the Content box to open its Edit dialog.
                     Change the Plate number in the Selection tab to identify the Plate.






    3.   Repeat Steps 1 and 2 until there is one Matrix item in the Content for each
         plate.0.


  You can fine tune the protocol while running it in an experiment, but if you like the
changes, be sure to select File>Save Protocol As to save the changes to the original
protocol for future use in another experiment.



218 | Chapter 11: Multi-Plate Protocols




Processing a Batch of Samples
         Gen5TM offers several ways to process a large batch of samples. The method you
         choose depends on the requirements of your protocol.
         The procedure described here use's Gen5's Multi-Plate Assay feature to define a
         protocol to process a batch of samples with one method. Gen5TM lets you assign up to
         10 plates to an experiment. Plates can have the same or different layouts, but all other
         Protocol elements are the same.

           Note: This is one of several options for achieving the same goal. You
             may want to try other methods to determine which approach best
             meets your needs. Check out Gen5's Help to learn more.

How to:
          1.   Begin by creating a new protocol: File>New Protocol

          2.       In the menu tree, open the Protocol Options and highlight Protocol Type
          3.   Select the button next to Multi-Plate Assay Protocol. Enter the number of
               plates required in the field, maximum 10. In this example, each plate has a
               different layout to distribute standards to some plates, and to continue sample
               numbering across several plates.
          4.   Define the Plate Layout for each plate. (See Plate Layout for Multi-Plate
               Protocols on page 210.)
          5.   Define the Procedures for reading the plates.
          6.   Define the Data Reduction steps.
          7.   Define the Report requirements.0.
When these steps have been completed the protocol is ready to run in an Experiment.
