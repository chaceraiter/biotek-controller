# Chapter 2: Getting Started

     This section provides a basic introduction to Gen5. It also includes
     contact information for obtaining technical support and tips for
     users of BioTek's KC4 software.


 Getting Started........................................................................ 28
 Gen5's Workspace.................................................................... 30
 Introducing the Protocol Workspace ........................................... 33
 Gen5's Wizard ......................................................................... 35
 Buttons and Icons Guide ........................................................... 36
 About the Menu Tree ................................................................ 38
 Tips for KC4 Users ................................................................... 39
 Getting Technical Assistance ..................................................... 41







Getting Started
         Welcome to Gen5TM! To make you feel comfortable with this very capable reader
         control and data analysis software, we've provided several learning tools. Tackle them
         progressively and you'll be a pro in no time. You'll find these tools in Gen5's Help.

           Important: these topics do not describe the Initial Setup
             requirements, like connecting a reader. Unless your System
             Administrator has already done so, complete the initial setup
             requirements before trying the lessons described here.

 Watch an Online Demonstration: select Help> Tutorials
            Basic #1: Intro to Gen5
            Basic #2: Setting up the Procedure
            Basic #3: Defining the Plate Layout (not for Gen5 Reader Control)
            Basic #4: Creating Data Reduction Steps (not for Gen5 Reader Control)
            Basic #5: Runtime Prompts
            Basic #6: Building Reports
            Data Views: Create a New View
            Intro to Power Export (to use Microsoft(R) Excel for reporting) (not for Gen5
              ELISA or Reader Control)
            How to create multiple standard curves
            Intro to Calibrator-Plate Protocols (not for Gen5 Reader Control)
            How to select the optimal PMT Sensitivity (for fluorescence and luminescence)
            Synergy 2 and Synergy 4: Filter-based FL Detection Methods


 Practice using Gen5 with the Learning Exercises:
            Refer to the Getting Started Guide shipped with the product CD or Gen5's Help
              system for step-by-step learning exercises











 Open a Sample Protocol:
        Gen5 ships with numerous protocols so you can load one up, customize it to fit your
        particular requirements, and run an experiment.
             1.   Select File>Open Protocol

             2.      At the top of the Open dialog, click the "Up One Level" button
             3.   In the Gen5 folder or the DB (shared database), select the Samples folder
             4.   Select the folder for the desired detection method: Absorbance,
                  Fluorescence or Luminescence
             5.   Open the Protocol (or Synergy 2_Synergy 4) folder and select one. 0.

          Recommendation: Before making any modifications to the sample
            protocols, we recommend selecting File>Save As after opening them
            and assigning a unique name to the protocol. This will preserve the
            original sample protocol for future use. Also recommended when
            saving a copy of the original protocol is selecting the most convenient
            location for it. You may want to use the Up One Level button a few
            times to get back to the Gen5/Protocol folder, a more likely location
            for your "in use" protocols. Note: the step-by-step instructions for
            opening a sample protocol are based on the default filenames and
            path.

          Important: The sample protocols must be considered as examples
            provided for demonstration and guidance purposes. If you plan to use
            these protocols or similar ones in a real application, it is your
            responsibility to validate the protocol parameters, including the report
            and export content (if applicable), before using them.

          One more thing: your reader may not support all of the sample
            protocols provided. Review the descriptions in the Sample Protocols
            and Experiments Guide to see if your reader is compatible with the
            defined steps. If you can read PDF files: click the Windows(R) Start
            button, select All Programs>Gen5>Sample Protocols and
            Experiments Guide










Gen5's Workspace
         Gen5 offers several controls and workspaces for developing protocols, running
         experiments, and viewing and reporting results:




           Gen5's Welcome screen is only available when Gen5 is initially
             launched. You restart Gen5 to get to the Welcome screen.

1 Protocol
     Every experiment is based on a protocol. The differences between a Protocol and an
     Experiment in Gen5 are described in the Essential Concepts chapter.

2 Plate View
     Gen5 provides a view or workspace for each plate processed (or to be processed) in an
     Experiment. You must have an Experiment, rather than a Protocol, open to have a Plate
     View:

   Opening the Plate View/Workspace
     In an Experiment, if it is not already open in the main view of Gen5TM:

            from the menu tree: Double-click the desired              item
            Or, select Plate> View











        Gen5 offers several ways to modify and customize the Plate View for on-screen display
        and reporting/outputting results, see the Viewing Results chapter to learn more.

3 Menu Tree
    The menu tree, docked at the left side of the workspace, provides a quick and easy way to
    open all the tools needed to create and run experiments.
               About the Menu Tree (page 38)

4 Toolbars and Menus
    Here is a reference guide to learn about Gen5's buttons and icons:
               Buttons and Icon Guide (page 36)

5 Running an Experiment
    All of the views and components come into play when running an experiment (File>New
    Experiment). The Protocol menu tree is the primary engine for an experiment and Plates
    (one for each plate processed or to be processed) are added to the menu tree. The Plate
    View and other plate components are made available:

        Information contains the text input at the Runtime Prompts when the plate is read
    and Bio-CellTM results when this pathlength-correction option is used

        Sample IDs are user-defined sample names or bar codes

        Calculation Log keeps track of and displays any data reduction errors

        Audit Trail logs changes (masking and editing) of data points for all levels of Gen5,
    and numerous other events for Gen5 Secure. Audit trail events can be included in reports
    and export files.










About the Plate Workspace
         The Plate View represents the microplates processed (or to be processed) in an
         Experiment. The following tabs are available depending on the Protocol definition:
                Matrix: a representation of the microplate layout. Each cell in the grid
                  shows the data-set results for the well it represents in the plate. The Layout
                  data set shows the current Plate Layout. You can use this view for masking
                  or editing results.
                Statistics: a standard set of statistical values are determined for you and
                  displayed in a table
                Graphs: when a standard curve is defined it is shown in the Graphs tab
                Cutoff Values: when a Cutoff Data Reduction step has been defined, this
                  tab displays the values or results of the cutoff formulas
                Validation Results: when a Validation Data Reduction step has been
                  defined, this tab displays the results of any calculations











Introducing the Protocol Workspace
    When you create a new protocol, Gen5 opens a special workspace limited to the protocol's
    components:




    The workspace is made up of the menu tree with a branch for each of the protocol's
    elements. The order of the protocol elements reflects the order to follow when defining
    most protocols:

         Defining the Procedure or reading parameters, like detection method, wavelength,
    and other factors, is the most important step to Gen5. The Procedure describes the data
    sets which are used in most subsequent steps to generate results output. The Plate Layout
    is the only other protocol element that is not affected by the Procedure.

         For most protocols, it's best to define the Plate Layout in your second step. Gen5
    automatically performs a blank-subtraction calculation when Blanks are defined in the
    plate layout. (You'll see this Transformation in the Data Reduction workspace.) Defining
    the standards and their concentrations in the plate layout is a prerequisite to generating a
    standard curve.

         Data Reduction is one of Gen5's most powerful features, and it requires the
    information provided by the two previous steps to logically offer you its capabilities.
    Automatically-generated transformations, like pathlength correction, and the ability to
    conduct well analysis, for example, depend on the Procedure. To plot a standard or titer
    curve, and to validate Transformation formulas requires knowing the Plate Layout.










          Runtime Prompts are user-defined text fields that are presented to users when they
     read a plate. The information obtained is stored in the Plate Information component of the
     experiment and can be included in reports and export files.


     Viewing and Reporting Results: the next four options (or three options if you're running
     Gen5 ELISA or Reader Control, which do not offer Power Export) are tools for selecting
     and customizing the appearance of data sets: raw data measurements and data reduction
     results. Data Views controls the on-screen appearance of data. Data Views also stores and
     makes available for reporting and exporting any customizations made to the data sets. For
     example, you can build your own matrix, table, or curve view of a data set by combining
     and formatting data elements. When you do this in Data Views, that user-defined data set
     is available for printing or exporting using the Report Builder, File Export Builder and
     Power Export Builder.

         Protocol Options provide several special features and preferences. Many of the
     options may be rarely used by your organization. Review the options provided and if your
     preferences vary from the default settings, use the Default Protocol to set them for all
     newly-created protocols. The exception to this rule occurs with multi-plate protocols:
     Calibrator-Plate Protocols and, for Gen5 and Gen5 Secure users, multi-plate assay
     protocols. These types of protocols begin by selecting the Protocol Type defined in the
     Protocol Options.











Gen5's Wizard
        Use Gen5's Wizard to create a new protocol. Then, you can run an unlimited number
        of experiments based on that protocol. Learn the difference between a Protocol and
        Experiment in Gen5, in the Essential Concepts chapter to make the most of Gen5.

  How to use the wizard:
             1.   On each screen of the wizard, click the button to define that protocol
                  element (each function is described in a subsequent chapter):

                      Defining the Reading Procedure

                      Defining the Plate Layout

                      Setting up Data Reduction

                      Building Reports

                      Using the File Export Builder

                      How to use Power Export

             2.   After defining a protocol element, click Next to proceed to the next one.
                  Gen5 displays a checkmark for an element that has been defined.
             3.   Click Finish to generate the protocol based on your selections.
             4.   Select File>Save and give the protocol a unique name.
                  Now you're ready to run an experiment.
             5.   Select File>New Experiment. The just-created protocol will be
                  highlighted, click OK to select it. 0











Buttons and Icons Guide

  Buttons Descriptions

             The 3-dot (three-dot) button is a tool for customizing or modifying the item's
             contents. In some report options, you must click in a field to activate its 3-dot
             button

             Open an existing Experiment

             Create a new Experiment or Protocol

             Add another plate to the current Experiment

             Read the plate (or Simulate, Manually Enter, or Import data)

             Save the Experiment

             Gen5's Wizard to help you create an Experiment

             Print the results, but first use Report Builder to select what to include

             Print Preview

             Reader Control: check the status, open the control panel

             Duplicate View: click the button in the upper-right corner of the Plate View
             to open a coincident display of the plate's results

             Gen5 Secure Only: Sign a protocol or experiment

             384- and 1536-well Plate View Toggle: zoom in to view the top-left
             section of the plate, zoom out to view the whole plate



  Menu Tree Icons

               Plate - Not read. Put the plate in the reader and click the Read button

               Plate read successful

               Plate read paused by Stop/Resume step. When you're ready, put the plate
               in the reader, click the Read button and select Resume to continue

               Plate read aborted. To begin again, put the plate in the reader, click the
               Read button and select Re-Read

               Plate read in progress









              Plate read error, which is always preceded by an error message

              Protocol

              Procedure: define the reading parameters

              Plate Layout: assign location of samples

              Data Reduction: set up calculations

              Runtime Prompts: define the information requested when a plate is read

              Report Builder: select the content to print

              File Export Builder: select the content to export

              Power Export Builder: select the content to export to Excel(R)

              Data Views: customize the appearance of data for online viewing and
              reporting

              Protocol Options: miscellaneous options for saving, naming, exporting and
              calculating results

              Plate Information: information obtained at runtime

              Sample IDs: user-defined names or IDs assigned to samples

              Calculation Warning Log: Data Reduction-related errors issued by
              unexpected curve or calculation results

              Multi-Plate plate view of data reduction statistics and curves

              Audit Trail displays any logged events



3-dot (Edit) Button
        The 3-dot button leads to editing features for the field or data point it is associated
        with. Click the button when it is next to or in a field to change the selection list or
        format of the field's items.

          Note: In Field Groups and in Headers and Footers you must click
            inside a field in the table to enable a 3-dot button.











About the Menu Tree

            In an experiment, the menu tree is docked at the left side of the workspace,
              unless its position has been previously altered. When you're working with a
              protocol file, the menu tree, like the toolbar, is limited to related operations.
              Learn the difference between Gen5's Protocols and Experiments in the next
              chapter
            The menu tree provides a visual cue of the steps to follow when creating a
              protocol
            All of the controls available from the menu tree can alternatively be accessed
              using toolbar buttons or the drop-down menus

                 and   icons next to an item expand or close it to reveal or hide its
                components
            Highlight an item in the menu tree and right click for a context-sensitive menu
              of options, including Read when a plate is selected, for example.
            * asterisks are displayed next to plate icons (and in the title bar) of an
              experiment when a change is made or an action is taken but the file has not yet
              been saved
                You can move the menu tree to another corner of the workspace or let it float
                undocked like the Plate workspace: click the undock button, drag the title bar
                and drop it in the desired location
            When you Add multiple plates to an experiment, highlight a plate and right-
              click for menu options to delete and renumber plates.











Tips for KC4 Users
        BioTek relied on input from KC4 users to develop this improved next-generation
        product. It may take a bit of practice to learn how to use them, but we think you'll find
        the new features worth it.
         1.   In Gen5, reading parameters are not defined in one dialog (screen), but set up
              as steps in the StepWiseTM Procedure. This gives you far more flexibility in
              defining an experiment. Depending on the level of Gen5 you're running, this
              includes multiple read steps and reading-related functions, like shaking and
              dispensing.
         2.   The filename extensions are slightly different and file formats are simpler.
              Gen5 replaces the .pla and .glb formats with one experiment file: .xpt. Gen5
              keeps the .prt filename for protocol files. The experiment file (.xpt) like its
              predecessor the .glb or global data file, contains the .prt or protocol as it was
              defined at runtime
                  KC4           Gen5
                  .pla          .xpt
                  .glb
                  .prt          .prt

         3.   Gen5 does not offer Power Reports for Microsoft(R) Word. Power Export to Excel
              is available and a full-featured, user-customizable Report Builder eliminates
              the need for Word for most users. In addition, a new Quick Export to Excel
              feature and a user-customizable File Export tool are offered, which can be used
              to port files to Word. Learn more: Reporting Results
         4.   Append to Kinetic File, a KC4 feature, has been replaced in Gen5 with new
              features:
               multiple read steps can be performed in one experiment, and Gen5 offers to
                 Append to previous Kinetic data when multiple kinetic loops are defined
                 in a Procedure
               a long, discontinuous-interval Kinetic analysis can be performed using the
                 Discontinuous Kinetic option
               multiple plates can be used to run a single assay, review Multi-Plate
                 Protocols
         5.   Eject Between Filter Sets, a KC4 option, is omitted from Gen5 because it is not
              needed. Instead, you can set up multiple read steps interspersed with a Plate
              In/Out or Stop/Resume step
         6.   Lag time defined in Reading Parameters in KC4 is accomplished with a Delay
              step in the Procedures in Gen5










          7.   In Gen5, add a Kinetic loop to the Procedure rather than ticking a checkbox in
               KC4. See Setting up a Kinetic Analysis. Also note that the Data Reduction
               options for kinetic analysis do not include KC4's "Formula" and individual
               reading point identifier "R." These calculations can be replicated using Gen5's
               Transformation dialog.
          8.   In Gen5, to "Pre-Read Blank Plate" you'll set up two Read Steps with a
               Stop/Resume step between them: for instructions see Subtracting a Blank
               Plate (This is not available for Gen5 ELISA)
          9.   Gen5 does not automatically generate dual-wavelength subtraction or Delta
               OD data reductions, for instructions see: How to perform Dual-Wavelength
               Subtraction
         10. Set up a Dispense step in the Procedures, rather than ticking a checkbox in
               KC4. Here are instructions for setting up Dispensing Protocols
         11. Luminescence reading parameters in Gen5 require definition of Integration
               Time rather than the number of samples per well and delay time before and
               after sampling. When selecting the Emission filter setting, Lum/E has been
               replaced with Hole.
         12. Don't confuse what was called "Multi-Plate Transformations" in KC4 with
               multi-plate protocols or multiple-plate experiments in Gen5. Multi-plate
               transformations have been replaced with the StepWiseTM Data Reduction
               steps, where an almost unlimited number of calculations can be performed
         13. Multi-Detection was called Multi-Mode in KC4
         14. Raw Data Correction options in KC4 are engaged differently in Gen5:

                Blank Plate Subtraction is described above
                Blank Wells Subtraction occurs automatically when there are Blanks
                  assigned to the Plate Layout. You'll find these automatically-generated
                  Transformations in the Data Reduction dialog
                Pathlength Correction can be enabled when defining an Absorbance Read
                  Step
         15. When viewing Well Analysis results in the Well Zoom view:

                Gen5 uses brackets [ ] to show the revised Calculation Zone, instead of
                  showing the data points in different colors as in KC4
                Setting "Scales for Kinetic Reads" and "Individual Well Auto Scaling" for
                  scanning reads is replaced with more feature-rich tools for editing the
                  results output, see Modify a Graph. When you combine these features with
                  the ability to define the calculation zone (select Calculation Options when
                  defining the Well Analysis step), you have enormous control over the
                  appearance of the results
         16. Monitoring Wells is more flexible in Gen5 because it is defined as a separate
               step in the Procedure. The read parameters are specific to the monitoring
               process and can be different than those defined to obtain measurements0.









Getting Technical Assistance
    Gen5TM is backed by a superior support staff. If the software fails to work perfectly, please
    contact BioTek's Technical Assistance Center (TAC). You can call, write, fax, or email your
    questions and concerns to BioTek:

Email Support: tac@biotek.com

Fax Support
          Send a fax with your questions or requests for help 24 hours a day:
              Technical Assistance Center (TAC): 802.655.3399
               European Coordination Center: +49 (0) 7136.968.111

Phone Support:
          You can telephone the Technical Assistance Center between 8:30 AM and 5:30 PM
          Eastern Standard Time (EST), Monday through Friday, excluding holidays.
          Customer Service:          (802) 655-4040
          Technical Assistance Center:
               In the US call: (800) 242.4685
               Outside the U.S. call: (802) 655.4740
          European Coordination Center: +49 (0) 7136.9680

Whichever method of contact you choose, please be prepared to provide the
following information:
        The software version and revision numbers displayed at Help>About Gen5...
        The license type or software level: Gen5, Gen5 Secure, Gen5 ELISA, or Reader
          Control
        The specific steps that produce your problem
        Any error codes displayed
        A daytime phone number
        Your name and company information
        An email address and/or a fax number, if available.
