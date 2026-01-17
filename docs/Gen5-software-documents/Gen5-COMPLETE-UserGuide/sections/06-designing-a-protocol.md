# Chapter 6: Designing a Protocol

     This chapter covers the steps required to create a protocol. It also
     provides instructions for using the Default Protocol.


 Define the Procedure ................................................................ 113
 Define the Plate Layout............................................................. 111
 Define the Data Reduction ........................................................ 116
 Define the Reporting Requirements ............................................ 118
 Using the Default Protocol......................................................... 119



112 | Chapter 6: Designing a Protocol




Design a Protocol
         The menu tree provides a visual clue to the steps involved in creating most protocols
         (File>New Protocol... opens only the Protocol section of the menu tree):
          1.   Define the Procedure (or Reading Parameters)
          2.   Define the Plate Layout (for all except Gen5 Reader Control software)
          3.   Define the Data Reduction Requirements (for all except Gen5 Reader Control)
          4.   Define the Runtime Prompts to collect user input at runtime (plate reading)
          5.   Define the Reporting Requirements
          6.   Save the Protocol0.

           Important: follow this sequence of tasks, when developing a protocol
             to take advantage of Gen5's automatically created data reduction
             events. For example, when you add Blanks to the Plate Layout, Gen5
             automatically creates a Blank-Subtraction data set.

         You can find specific, step-by-step instructions for numerous types of protocols in
         Gen5's Help system.
     Protocols are run or executed within an Experiment. Learn more about the differences
     between Experiments and Protocols in the Essential Concepts chapter

           Alternatively, you may want to begin with one of Gen5's Sample
             Protocols described in Chapter 4. They can give you a head start.






Defining the Reading Procedure
    Protocol> Procedure

      Set up the Procedure to control the reader: define the                   reading
      parameters and related activities of the Protocol/Experiment.

          Grayed out? Once a reading has been done in an experiment, the
            Procedure cannot be changed for the current experiment. If this isn't
            the case, your System Administrator may have restricted your ability
            to modify the protocol elements.

          Grayed out buttons mean the action cannot be performed by the
            current reader or because previously defined steps, e.g. kinetic loop,
            limit the function.

How to:
          1.   Click a button to add that step to the procedure. Most buttons open a screen for
               defining the parameters of that step, e.g. Read lets you define wavelengths, etc.
               When defining a kinetic or synchronized well/plate mode analysis, add the
               Kinetic or Synchronized Mode steps first. Kinetic and Synchronized Mode
               steps form a loop or block. Put the Read and other valid steps to be performed
               inside the loop, between the Start and End. Monitor Well is similar, first add
               the Monitor Well step and then, add a Read step inside the monitor-well loop.
          2.   Define the details of the step and click OK
          3.   Click Validate to check the selection and sequence of the steps

          Your reader must be communicating with Gen5 for it to fully validate
            the Procedure: make sure your reader is turned on, not busy, and
            properly connected to the PC.




         More details and a Validation Checklist are provided in the Defining a Procedure
      chapter beginning on page 121.



114 | Chapter 6: Designing a Protocol




Modify a Protocol
     Gen5 does not restrict your ability to change a protocol, but other factors may:
            the Procedure cannot be changed in an Experiment after more than one plate
              has been read. Other protocol elements, like Data Reduction and reporting
              parameters can be changed at any time.
            Gen5 Secure's System Administrator can prohibit a user's ability to modify a
              protocol.
            All Gen5 System Administrators can limit users' ability to modify the Default
              Protocol.

To change the Procedure, you can:
                When only one plate has been read in an Experiment, you can modify the
                  Procedure and then re-read the plate, but this requires deleting the data
                  originally obtained from the reader,
                Alternatively, create a new Experiment based on the Protocol, then change
                  the Procedure and re-read the plate,
                Or, open the original Protocol, revise and save it, then create a new
                  Experiment based upon it.

           Gen5 tracks plate deletions in the Audit Trail

Changing the protocol is easy:
          7.   Open the protocol element you want to modify. For example, double-click
               Procedure in the menu tree.
          8.   Make the required changes:
                In the Procedure and Data Reduction dialogs, double-click an already-
                  defined step to open it for editing
                For other protocol elements, use the controls to make the needed changes.
          9.   When you're happy with the changes, save the file (File>Save or File>Save
               Protocol As). 0.







Defining the Plate Layout
  Protocol> Plate Layout
  It's easy to define the plate layout with Gen5's tools for identifying samples, standards,
  controls and blanks. Follow these steps:

       1.        In the Well Settings box in the top-left corner, select the Type of specimen

       2.      Customize the ID or Well Identifiers, if necessary, by clicking the 3-dot
            button.

       3.      Define the Concentration or Dilution, if applicable, by clicking the 3-dot
            button.
       4.   Assign the well IDs to their corresponding locations in the plate grid by
            clicking in the wells in the matrix.0.

                          When you select a corresponding starting # the ID changes
                 accordingly for assignment to the plate.
             Use the Auto Select and Replicates options to speed up your work: set the
               options and click and drag to fill multiple wells at once. Click a column or
               row header to fill it.

        The type of plate, e.g., 96-well, is defined in the Procedure and
          displayed in a representative matrix or grid format in the Layout and
          Transformation screens.

        More details are provided in the Plate Preparation chapter beginning
          on page 219, and Gen5's Help offers an instructive animated demo of
          the process: Select Help>Tutorials.



116 | Chapter 6: Designing a Protocol




Setting up Data Reduction
     Protocol> Data Reduction
         There are several options available for interpreting the results of your experiment.
         Gen5TM automatically creates the most commonly applied data reduction steps (based
         on previously-defined Protocol parameters). You can design your own or modify the
         calculations.

           Find more details and the Top 6 Things You Should Know about
             Data Reduction in the chapter beginning on page 245.

Data Reduction Options
      Find details about each option in the Data Reduction Options chapter.

                 Define a Transformation

                 Define a Curve Analysis

                 Define a Well Analysis

                 Define Cutoffs

                 Define Validation criteria

                 Fluorescence Polarization


               Gen5 shows an invalid data reduction step by blocking out its icon.
             Changing the Procedure, e.g. reading parameters or sequence of
             events, renaming a Read step or data set, or making other Protocol
             changes can invalidate a data reduction step. Generally, it is easiest to
             delete the invalid step and recreate it, selecting valid options.







Customizing Data Views, Reports, and Exports
      Gen5TM provides several tools for changing the appearance of views and reports. All
      selections and customizations to views and to report and export elements can be saved
      with the protocol, (File>Save Protocol As) so they are retained for all future
      experiments based on that protocol.
      Check out the tips and rules for customizing the views and output format of data
      elements:

 Best Practice:
         A good habit to develop when setting up a Protocol is customizing the content
           and format of the Data Views: the on-screen presentation of data. The settings
           defined in Data Views become available for selection in the Report Builder and
           Export definition screens, so it is most efficient to begin with Data Views (after
           defining the Procedures, Plate Layout, and Data Reduction details)
         Important: Attributes applied to data items and field groups in the Data Views
           dialog take effect going forward. They do not replace, update, or overwrite an
           item that has previously been assigned to a Report or Export output. You must
           refresh the Report/Export contents after making any changes to a data element,
           to capture them in the report. Any previously saved Experiment will not reflect the
           content or formatting changes.
         Gen5 limits the ability to customize system-provided views, but creating new
           ones offers enormous flexibility. For example, if you do not use Sample IDs,
           you'll always have an empty Name column in the system-provided Statistics
           tables. But, you can create your own view that excludes the Name/Sample ID
           data point.
         You can choose the way Gen5 formats data/text that is too long to fit
           completely in a field or column by Changing the Font settings for a data
           elements.
         Protocol Summary report sections can be added to the Default Protocol so that
           all future protocols will include them. These are the only Data Views you
           cannot view on-screen, so they are only available in the reporting tools: Report
           and Export Builders. Unlike most of the other data views, these report elements
           are always available, even before you have defined the Protocol.
         Field Groups (for use in reports) can only be created in the Data Views dialog,
           but they can be modified in the Report Builder and Export dialogs



118 | Chapter 6: Designing a Protocol




Reporting Results
         Gen5 offers several tools for reporting results from experiments.
         You can use:
                Gen5's full-featured report engine: begin with the Report Builder described
                  in the Reporting Results chapter beginning on page 333.
                or Export the results and use Excel(R) or another software application to
                  generate a report; its described in the Exporting Results chapter.







Using the Default Protocol
      Use the default protocol to work more efficiently in Gen5.

About the Default Protocol
   System> Preferences> Default Protocol...
   Gen5 provides a mirror-image of the Protocol menu tree to create a Default Protocol, a
   template, to help you save time when creating new Protocols. If some protocol elements
   remain the same from experiment to experiment in your lab, you can make them default
   settings that are applied to all new protocols. Any aspect of the Default Protocol can be
   overridden in a newly-created protocol or experiment using the regular menu options.
   There is a limiting factor controlling the use of the Default Protocol for most users,
   defining the Procedure or read parameters is a prerequisite to defining Data Reduction
   and selecting Report and Export content. Since reading parameters generally vary from
   experiment to experiment, the role of the Default Protocol is somewhat limited. However,
   it can still be used to define numerous settings that you're likely to apply to all
   experiments.
   The Default Protocol is stored in Gen5's database: SharedDB. When this is stored on a
   network drive that all your Gen5 users can access, they can also share the Default Protocol.

         Unless the reading parameters, like wavelengths, remain the same for
           all experiments in your lab, it is best to NOT define a Procedure for the
           Default Protocol. Users can alter the Procedure when they define a
           new protocol, but this action will invalidate any Data Reduction steps
           and report content, which may go unobserved by the user.

Customize Well IDs
      A major advantage of the Default Protocol is to customize the Well IDs (see next page)
      used in the Plate Layout. You may also be able to define the concentration values and
      location of Standards, and Blanks on the plate. Similarly, for Sample Identification
      fields. The customized IDs become available for selection in new protocols. Find
      instructions for defining customized Well IDs and Sample Identification fields in the
      Plate Preparation chapter beginning on page 219.

Common Default Settings
      You may want to define Runtime Prompts, Report Headers and Footers, and Export
      Options, which are commonly static elements in an organization's protocol design. The
      pre-built Protocol Summary data views, Procedure Summary and Data Reduction
      Summary, can be added to the Report and/or Export Builder in the Default Protocol so
      they are automatically included in reports for every experiment.

         Important: Defining the default protocol settings takes effect going
           forward, i.e. they are only applied to newly created protocols and have
           no effect on existing protocols or experiments.



120 | Chapter 6: Designing a Protocol



Default Protocol Setup
     System> Preferences> Default Protocol...
         Use these controls to define the default settings for newly created protocols.

How To
         Define the Default Protocol as you would a standard protocol, keeping in mind that
         your selections will be applied to all newly created protocols.


            As with standard protocols, you cannot define Data Reduction steps until the
         reading Procedure has been defined. Conversely, altering the Procedure can
         invalidate any previously defined Data Reduction steps.


Reset
         Use the Reset button to clear the Default Protocol settings, erasing any selections or
         customizations. Reset returns the Default Protocol to its out-of-the-box definition.


Customizing IDs in the Default Protocol
         Gen5 ships with certain abbreviations for the various well types, but they may not
         match your organization's naming convention. Customizing the Well IDs in the
         Default Protocol's Plate Layout makes them available for all newly created protocols.
         This can be a real timesaver for your users.

Common Changes
           Well Type         Default ID      New Default ID

           Sample            SPL             SMP

           Assay             CTL1            PC (Positive Control)
           Control

                             CTL2            NC (Negative Control)

                             CTL3            HPC (High Pos)
