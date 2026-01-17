# Chapter 12: Preparing Plates

     This chapter describes Gen5's tools for defining the Plate Layout,
     including assigning concentration values to samples, standards, and
     controls, and how to customize their Well IDs. It also covers
     assigning Sample IDs or names to associate test samples with
     specific test subjects.


 Defining the Plate Layout .......................................................... 221
 Assign Standards, Controls, and Blanks ...................................... 223
 Customize Well IDs .................................................................. 223
 Assign Concentrations/Dilutions ................................................. 226
 Custome Plate Layout............................................................... 229
 Plate Information ..................................................................... 230
 Runtime Prompts ..................................................................... 231
 Assign Sample IDs ................................................................... 231



220 | Chapter 12: Preparing Plates




Overview
        Gen5TM needs to know the layout of samples, standards, controls, and blank wells on
        the actual microplate(s) of your experiment to perform data reduction, curve analysis,
        and other calculations. It is not necessary to define a plate layout to simply read the
        plate and report the measurements. But to take advantage of Gen5's full array of data
        reduction features, define the plate layout, including any concentrations or dilutions of
        samples, controls or standards, before defining the data reduction calculations.

           Plate Type for a protocol or experiment is defined in the Procedure.
             Plate Type is selected from the Plate Types Database (covered in a
             System Management chapter)

        Gen5 supports 6-, 12-, 24-, 48-, 72-, 96-, 384- and 1536-well microplates. However, your
        reader may not support all of these configurations. Select the Plate Type when defining
        the Procedure and then open the Plate Layout to see how Gen5 formats the plate map:
        all columns are numbered and all rows are designated with a letter(s). Well A1 is
        always in the top left corner of the grid, for example:
            96-well plates are mapped as 8 rows A-H and 12 columns 1-12
            1536-well plates are mapped as 32 rows A-Z, AA, AB, AC, AD, AE, AF and 1-48
              columns

  Adding a new plate to an Experiment

           Click the     button to add another plate to an experiment. The plate takes on the
           currently-defined plate attributes. Right-click on the plate and select Custom
           Layout to create a unique plate map.







Defining the Plate Layout
   Protocol> Plate Layout
   It's easy to define the plate layout with Gen5's tools for identifying samples, standards,
   controls and blanks. Follow these steps:

        1.        In the Well Settings box in the top-left corner, select the Type of specimen

        2.        Customize the ID or Well Identifiers, if necessary:

        3.        Define the Concentration or Dilution, if applicable:
        4.   Assign the well IDs to their corresponding locations in the plate grid by
             clicking in the wells in the matrix. 0.

                           When you select a corresponding starting # the ID changes
                  accordingly for assignment to the plate.
              Use the Auto Select and Replicates options to speed up your work: set the
                options and click and drag to fill multiple wells at once. Click a column or
                row header to fill it.

         The type of plate, e.g., 96-well, is defined in the Procedure and
           displayed in a representative matrix or grid format in the Layout and
           Transformation screens


 Helpful Hints:
          Set up your preferred default Well IDs in the Default Protocol. For example,
            you can define PC (for Positive Control) instead of CTRL1 for Assay Controls.
            Well IDs defined in the Default Protocol are available when defining the Plate
            Layout for all newly-created protocols/experiments
          Use the Undo button at the bottom of the screen to undo the last action. Up to
            10 previous actions can be undone
          To clear the grid and start over, right click and select Empty Layout, or to
            clear selected cells, set the Type of Well Settings to Empty and select the cells
            you want to clear.
          You can Print the plate layout. 384-well plates print out in two sections,
            columns 1-12 and 13-24. 1536-well plates print in eight sections to fit all 48
            columns and rows from A to AF.
          To copy the contents of the grid to Windows' virtual clipboard to paste into a
            text/external file, right click and select Copy Layout. Open the receiving file,
            e.g. Word(R) or Excel(R) and right click and select Paste. Generally, plates larger
            than 96-wells do not fit completely in a standard-sized Word or text file, a
            spreadsheet is required.



222 | Chapter 12: Preparing Plates



            For Samples - unknown test specimen - Gen5 lets you assign and track data
              points in addition to the Sample ID. You can create "Additional Identification
              Fields."
            To copy the contents of the grid to Windows' virtual clipboard to paste into a
              text/external file, right-click and select Copy Layout. Open the receiving file,
              e.g. Word(R) or Excel(R) and right-click to select Paste. Generally, plates larger than
              96-wells do not fit completely in a standard-sized Word or text file, a
              spreadsheet is required.
            Each instance of a Sample and Sample Control Well ID, and each Assay Control
              group can have a unique concentration/dilution value. Gen5 assigns a dilution
              index to the Well ID to keep track each instance.
            Use the Dilutions Only/Concentrations Only button to apply only dilution
              or concentration values (that you have previously defined) to selected wells
              without altering the well's identifier. See Assign Concentrations or Dilutions to
              Samples, Standards, Controls on page 226.
            Use the shortcut for filling the entire plate with the selected Well Settings: click
              in the top-left (unlabeled) corner of the matrix, i.e. between A and 1.
            When assigning concentrations/dilutions, well selection must be compatible
              with the Replicate, Auto Select, and Filling option settings
            You can resize the plate view in the standard Windows(R) way: click and drag
              the outer borders of the view, or click the maximize button in the top-right
              corner. You can resize the rows and columns: hover your mouse over a grid
              line between two numbered columns or alpha-labeled rows until the cursor
              changes to a separator, then, click and drag.







Assigning Well IDs
   Protocol> Plate Layout
      Gen5TM recognizes the significance of commonly-used elements in an experiment:
           Standards or calibrators for generating a standard/calibrator curve
           Blanks for blank wells subtraction
           Controls for multiple purposes: Assay Control generally used as controls, cut-
             offs, or for validating the assay, and Sample Control generally used in
             association with a specific sample, e.g., spiked or known-concentration
             samples.
           Samples represent the test specimen or unknowns to be processed.
      When defining the Plate Layout, you can customize the Well ID and on-screen
      appearance, and you can assign concentration or dilution values to Standards, Controls
      and Samples.




      Use the drop-down lists and 3-dot buttons in the upper-left corner of the Plate Layout
      dialog to select, customize and assign standards, controls and blanks to the plate. For
      details see:
           Customize Well IDs (below)
           Customize Sample IDs or assign them additional ID fields on page 224
           Assign Concentrations or Dilutions to Samples, Standards, Controls on page
             226


Customize Well IDs
      To save the customized IDs for use in all newly-created protocols/experiments,
      perform these steps in the Default Protocol at System> Preferences> Default
      Protocol

1. Type
         Use the drop-down list to select the Type of specimen,
      (except for the Empty option, which is used to clear a previously assigned well).



224 | Chapter 12: Preparing Plates



2. ID

        Gen5 displays the default label or name for the selected Type. Click      (3-dot button)
        to customize the name and color code. Click in the fields to replace the text and select
        the color.
        Depending on the Type, one of three dialogs opens, here are two examples:




            ID for Standards, Assay Controls and Blanks can be up to 10 characters, the ID
              Prefix for Samples and Sample Controls can be up to 6 letters, numbers and
              underscores, without any blank spaces. It cannot end in a number, nor be
              identical to a formula operand, e.g., X, MIN, MAX, and so on, and cannot be
              identical to a well coordinate, e.g., A1, H12. Click in the field, and enter text to
              edit it. The ID can be used in data reduction formulas.
            Name can be up to 20 alphanumeric characters and can be used in reports
            The selected Color or Color Sequence will be applied to the matrix view of the
              plate. Click in the field to activate the drop-down list of color choices


Customizing Sample Wells
           With Sample selected, click the 3-dot button next to the ID field to access these
        controls.
        Sample wells are the unknown samples to be processed. To save customized IDs for
        use in all newly-created protocols/experiments, perform these steps in the Default
        Protocol at System> Preferences> Default Protocol

About Sample Identification Fields
      Identification Fields provide a way to assign and track additional data points related to
      an unknown sample. For example, in a clinical trial you may have a patient number,






      age, gender, and other information to be analyzed for trends. This data must be kept
      with the measurement results. There are numerous scenarios for assigning additional
      data to a sample. Use an Identification Field to create a category or class for this data.
      Then, collect the data in the experiment.
      In the Gen5 Experiment, data, like Name, Age, etc., can be assigned to each sample on
      the plate. When you create Identification Fields in this dialog, they become data fields
      in the Plate's Sample ID table. You can also display the data in custom data views for
      online viewing and reports.
      Gen5's system-generated views: the Layout matrix, Statistics and Well IDs tables
      automatically include all Identification Fields marked as "Show." This facilitates the
      Matrix data-entry option.

How to customize Sample wells:

       1.      In the Plate Layout, set Well Type to Sample, click the 3-dot button next to
            the ID field.
       2.   On the Display tab, click in the field to overwrite the default Samples ID
            prefix: SPL.
            The ID can contain letters, numbers, and underscores, up to 6 characters. IDs
            cannot end in a number and cannot contain spaces. IDs cannot conflict with
            well coordinates, A1, H12, etc.
       3.   Click in a Color Sequence field to enable the drop-down options, click on the
            desired color to select it. The first color selected is applied to SPL1, the second
            color is applied to SPL2, and so on. Gen5 reapplies the colors, starting with the
            first one, when the entire list has been used.




       4.   Click the Identification Fields tab to create or modify these data categories.



226 | Chapter 12: Preparing Plates



          5.   For each "Add. Field#" or additional identification field, enter a Title or name
               for this data category.
          6.      Mark the field to Show in Gen5's system-generated data views. This enables
               the Matrix data-entry option referenced below.

To populate the Identification Fields
      The Title of the Identification Field becomes a category for data input. For every
      Sample assigned in the Plate Layout, you can collect the data for each category when
      you run an experiment. There are two ways to input the data:
                Fill in the Samples ID Table on page 236
                Edit the Matrix to Input Data on page 237
                Use the Batch IDs creator to "Apply to Fields," see page 239



Assign Concentrations or Dilutions to Standards, Samples, Controls
        In the Plate Layout screen, under Well Settings, the label changes to either Conc. or
        Dil. (for Concentration or Dilution) depending on the Type selected and your input.

                                                                      This is a must-do
                                                                      for plotting a
                                                                      Standard Curve:
                                                                      assign the
                                                                      expected
                                                                      concentrations of
                                                                      the Standards


        First, define the concentrations or dilutions, then, assign them to the plate.

Define the Concentrations or Dilutions

            After selecting the Type and the ID, click the 3-dot button next to Concentrations
        or Dilutions. When Standards are the selected Type, the cells in this table are labeled
        accordingly, e.g. STD1 (or STDB1 when multiple standard curves are created [see the
        Data Reduction Options chapter]). Gen5 applies an indexing notation for all other
        Types of Well ID, e.g. CTL1:1
          1.   In ascending or descending order, enter the values in the consecutively-
               numbered fields. For a shortcut, select one of the two Auto entry tools:
                Increment when the dilutions are based on a fixed number to increment
                  your starting entry by. For example, starting at 10, increment by 10 to define
                  concentrations as 20, 30, 40.
                Factor when the dilutions are based on a fixed number to multiply your
                  starting entry by. For example, starting at 1, factor by 10 to define them as
                  10, 100, 1000 and so on.






         In the first field, enter the starting number
         Click in (or use the down arrow key to move to) each successive field to
           apply the incremented or factored value
2.   When the well type is other than Standards, select Concentrations or Dilutions
     with the buttons underneath Conc./Dil. Type.
3.   If applicable, enter an abbreviation for the measurement Units.
4.   Assign the location of concentrations or dilutions to the plate, in the same
     manner as assigning Samples. Set the Well Settings and click the well to assign
     that ID and Conc/Dil value to. Or, use the Replicates and Auto Select options
     and select a row, column, or click and drag over the area of the plate to assign
     the IDs.0.



228 | Chapter 12: Preparing Plates




 Helpful Information:
            Important: You can assign unique concentration/dilution values to individual
              Sample, Sample Control Well IDs, and Assay Control groups. For example,
              SPL1 can be defined as dilutions of 5, 15, and 45, while, SPL2 is defined as
              dilutions of 10, 25, and 50. Change the ID and click the 3-dot button for
              Conc/Dil to define a unique concentration/dilution-values table for each
              individual ID. The values table is not saved for that Well ID until they have
              been assigned to the plate
            You can define multiple standard curves: described in the Data Reduction
              Options chapter
            In the Plate Layout dialog, you can use the Dilutions Only/Concentrations
              Only button to apply only dilution or concentration values to selected wells
              without altering the well's identifier
            When assigning concentrations/dilutions, the well selection must be
              compatible with the Replicate, Auto Select, and Filling option settings
            Set up your preferred default IDs and define regularly used
              concentration/dilution values for Samples, Standards and/or Controls in the
              Default Protocol







Custom Plate Layout
      Gen5 let's you create individual custom layouts for experiments with multiple plates >>
      not to be confused with Multi-Plate Protocols. Exercise judgement when using this
      option, keep in mind any Data Reduction formulas that reference Well IDs. You cannot
      set up Data Reduction steps that reference the custom layout only.

How to create a custom layout:

       1.    After adding plates, select the          in the menu tree, and right click
       2.    Select Custom Plate Layout from the pop-up menu.
             A new Custom Layout icon is added to the menu tree for that plate.
       3.    Double click the plate's Custom Layout icon to open the Plate Layout screen,
             for that plate only!0.


 Helpful Info:
                         In the menu tree, Gen5 highlights plates with an asterisk to
             indicate the plate varies from the protocol in some way
         Keep in mind the differences between the Protocol's plate layout in Data
           Reduction steps, Data Views and Report Builder. For seamless integration of a
           custom layout, make sure any Well IDs referenced by a Data Reduction step are
           included in the custom plate



230 | Chapter 12: Preparing Plates




Plate Information
     Plate> Information




About the Plate Information
        Every plate added to an experiment comes with an Information component. The
        Information is collected when the plate is read. Runtime Prompts (described on the
        next page), set up for the Protocol, define the information requested when the plate is
        read.

Reviewing the Plate Information
        Double click the Information element under the Plate in the menu tree to review or
        modify the information collected when the plate was read.

Printing the Plate Information
        You can include the Plate Information in a report or export file using Field Groups







Runtime Prompts
    Protocol> Runtime Prompts
        Use these controls to set up the Runtime Prompts presented to users when they Read
        a plate in an Experiment based on this Protocol. The Prompts you define become the
        labels for input fields in the "Plate Reading" screen Gen5 presents when a plate is read.
        The Plate Reading data is retained in the experiment as Plate Information.




        The Runtime Prompts become input fields in the Plate Reading dialog. Example:
        When the Prompt Name is "Name" for prompt 1, users are prompted to enter their
        name when they read a plate.
           Clear the default text from any unused prompts for the best appearance at run
             time.

How to:
      Find descriptions of these prompt attributes:
           Prompt Name on page 232
           Prompt Type on page 232
           Data Reduction Variable Names on page 233
           Remember Recent Values on page 233
           Skip runtime prompts on page 234



232 | Chapter 12: Preparing Plates



Reviewing the Plate Information




                            You can review (and modify) the Information entered when the
        plate was read in the Information component of the Plate in the menu tree

Printing the Plate Information
        You can include the Information in a report or export file using Field Groups


           Bar-Code Scanning the Plate ID: If you have a compatible bar-code scanner, you
        can use it to input the plate's barcode and any other prompts. Replace the keyboard
        with the scanner and use it to capture the information just before reading the plate.



Creating a Runtime Prompt:

Prompt Name
      When defining Runtime Prompts the Prompt Name becomes the data-input field name
      in the Plate Reading dialog. Up to 6 prompts can be defined. Prompt Names must be
      unique or empty, independent of case. LOT and Lot are not acceptable variations, for
      example.
        Field names are limited to 32 characters. Their corresponding data-entry fields support
        up to 255 characters.
        When a prompt is defined as "required" its Prompt Name is marked with an asterisk in
        the Plate Reading dialog.



           Delete unused "Prompt #'s" for the best appearance in the Plate Reading dialog.
        The fields will appear blank instead of displaying the prompt number.


Prompt Type
      When defining Runtime Prompts use the drop-down list to select the Prompt Type:
               Optional: gives the user an opportunity to enter data, but the field can be
                 skipped. When all prompts are optional, the Plate Reading dialog can be
                 turned off, blocked from appearing before a plate read.
               Required: requires the user to enter data in the field before reading the
                 plate. Required "Prompt Names" are marked with an asterisk in the Plate
                 Reading dialog. Required fields disable the ability to "Skip the Plate
                 Reading dialog."






               Data Reduction Variable: requires the user to enter a numeric value for use
                 in data reduction formulas. The entered value replaces the Variable Name,
                 which is used as a placeholder when writing the formulas. Numeric values
                 can be decimal or scientific notation in accord with the computer's Regional
                 Settings. Data Reduction Variables, also called "runtime variables" can be
                 used in these data reduction steps:
                   Transformation
                   Curve Interpolation
                   Cutoff
                   Validation
                   Well Analysis Formula

Data Reduction Variable Names
      When defining Runtime Prompts for Data Reduction Variable Prompt Types, the
      Variable Name is used when writing formulas. The Variable Name is a placeholder for
      the numeric value Gen5 users are prompted to enter before reading the plate.
      Although, the value can be modified in the Plate Information dialog at a later time.
        At the Plate Reading dialog, Gen5 verifies the user has entered a valid numeric value
        for the variable. They can be integers, decimals or scientific notation in accord with the
        computer's "Regional Settings."
        Gen5 gives you a headstart when defining a variable name. It repeats the Prompt
        Name text preceded by an exclamation point (!), because this is the required syntax.
        Syntax for Variable Name:
               Must start with "!"
               Other characters must be alphanumeric (a-z; A-Z; 0-9); they are character
                 case dependent
               Up to 32 characters can be used
               Must be unique (to the protocol)

           Data Reduction Variable prompts are "required" entry fields.


Remember Recent Values
     When defining Runtime Prompts this option lets you give users a shortcut for data
     entry. It remembers the last 5 values entered for the prompt and provides them in a
     drop-down list for easy selection. Gen5 retains the values with the Protocol, so the list
     is available in any experiment based on that protocol.

           Recent Values are managed with the Database Maintenance tools.



234 | Chapter 12: Preparing Plates



Skip Runtime Prompts
       You can speed up plate reading by skipping the "Plate Reading" dialog when:
               it is not necessary to collect miscellaneous data about each plate
               none of the Prompts are "Required" entry fields
              none of the Prompts are Data Reduction Variables
        Open the Runtime Prompts screen, empty the table is necessary and select
           Skip Plate Reading dialog during plate read







Assigning Sample IDs
   Plate> Sample IDs
     Gen5 provides tools for pairing labeled patient/test samples with their reading and
     data reduction results. This feature reflects the customization and definition of
     unknown "Sample" wells in the Plate Layout, e.g. SPL1. For each Sample well assigned
     in the Plate Layout you can attach an ID or Name, and when you have defined
     "Additional Fields" you can input related data for each Sample well.
     The Samples IDs (Names) and other Identification Fields are unique to each test plate.
     They provide the ability to explicitly relate a test sample to a test subject. Learn more
     about the Identification Fields that are created in the Plate Layout.

       You must be in an Experiment, not a Protocol, to assign Sample IDs.
         And, the Plate Layout must be defined before Sample IDs can be
         defined and applied to the plate.

     You can:
        Import Sample IDs from a Text File (page 242)
        Manually Enter Sample IDs (page 235)
        Batch Sample IDs (page 239)
        Create a replicate of a previously defined plate (page 242)
        Use a BarCode Scanner to enter Sample IDs (page 237)
        Export Sample IDs to a text file (page 243)
        Print the Sample IDs after entering them, in list or matrix format. Matrix
          depicts the plate layout. To include them in a report or export file, add the Well
          IDs table to the Report Content or Export Content in the respective Report or
          File Export Builder, or using the Power Export toolbar.
        Clear/Remove Sample IDs from a plate after they've been assigned: Select
          Plate>Sample IDs and click Clear All
        Delete a column of data: highlight column in the Samples ID table and press
           Delete


Manually Enter Sample IDs
     Gen5 provides three ways to manually enter Sample IDs and data for "Additional
     Identification Fields:
            Fill in the Sample IDs table (described below), or
            Edit the Plate View Matrix (described on page 237), or
            Barcode Scan Sample IDs to enter data (described on page 237)



236 | Chapter 12: Preparing Plates




 Helpful Hints:
            Use the Batch Sample IDs feature for more advanced sample naming described
              next
            When Sample well identifiers are not consecutively numbered in the Plate
              Layout, Gen5 does not skip them in the Sample IDs table, but indicates their
              absence by graying out and putting an asterisk at their label. When automated
              methods are used to ID samples, Gen5 skips the missing SPL identifiers.

Fill in the Sample IDs Table

           This data-entry method is an alternative to editing the Matrix.




             1.                        Locate Sample IDs under the Plate in the menu tree
                   and double-click to open it.
             2.    Gen5TM lists the consecutively numbered Sample well identifiers (SPL) from
                   the Plate Layout. Enter their corresponding IDs or names or other data:0.

                                    Select Auto Numbering to automatically increment a
                   numeric suffix or a standalone number. For example, enter ABC10 in the
                   first cell of the table and using your down-arrow key or a mouse click,
                   select the next downward cell to assign the next samples ABC11, ABC12,
                   and so on.
               Use the buttons to print the Sample IDs in a List or Matrix format
               Select the contents of a cell and use Ctrl+C to Copy and Ctrl+V to Paste
               Use the Clear All button to empty the table: contents of all columns and
                 rows will be deleted. Click Cancel to recover data.


                   To delete rows, columns or blocks of contiguous cells, select them and click
              Delete. To select a row or column click on its header. Click and drag over a
              block of contiguous cells to select them.


               Copy Sample IDs from Another Plate: Instead of manually entering or
                 importing IDs, when you have multiple plates in an experiment, use the
                 spin buttons or enter the number of the plate you want to copy IDs from
                 and click Copy.







Edit the Matrix to Input Sample Data
       Gen5 lets you enter Sample Identification Fields data in the Matrix:

  Prerequisite:
        There are two ways to display the Sample Identification Fields in a Matrix view so they
        can be input/edited:
               they must be defined to Show in the Identification Fields dialog, this makes
                 them automatically appear in the Layout view
               or, they have been included in a custom Data View

  How to:
             1.   With the experiment open and the desired plate selected in a multi-plate
                  experiment, open the Plate View.
             2.   Select the Matrix tab and from the Data drop-down list select Layout or a
                  custom data view that contains Name or Additional Identification fields.

             3.        Click the Edit button.
             4.   Click in a well to reveal placeholders for the fields (if data has not yet been
                  entered). Replace the placeholders or previously entered data with your
                  desired input. Multiple wells can be changed in a session.

             5.       To apply the changes, click the OK (green check mark) button.
                      Click the cancel button to ignore your entries, and restore the original
                  values.0.

          Use the right-click options to copy and print the matrix.

          This data-entry method is an alternative to filling in the table.


Barcode Scanning Samples IDs

  Prerequisite
        You must have a wedge-type bar-code scanner that replaces or mimics keyboard input.
        Follow the manufacturer's instructions for installing and setting up the scanner for
        carriage return line feed.

          Added Bonus: If you do have a compatible bar-code scanner you can
            also use it to input a Plate ID and other Plate Information collected
            by Gen5 when the plate is read.



238 | Chapter 12: Preparing Plates



  How to



          1.                       Open the experiment and locate Sample IDs under the
               Plate in the menu tree, and double click to open it.
          2.   Gen5TM lists the consecutively numbered Sample well identifiers (SPL) from the
               Plate Layout. Use your mouse to select the starting point, e.g. SPL1, and make
               sure Auto Numbering is de-selected, i.e. unchecked.
          3.   Operate the scanner according to the manufacturer's instructions to enter the
               corresponding IDs or names.0.







Assign Sample IDs for Multiple Plates (Batch)
   Plate> Batch Sample IDs
      Use the Batch Sample IDs screen to assign sample IDs or names to multiple plates
      simultaneously. Samples IDs or names are specific to each test plate, and are intended
      to relate a test sample processed by Gen5 to a test subject. The batch process offers
      more advanced auto-numbering methods than the single-plate Sample IDs tool.




        The Plate Layout must be defined before Sample IDs can be applied to
          the plates.

Auto Number
      Select Auto Number to manually create a naming/numbering convention for samples
      for one or more plates:



240 | Chapter 12: Preparing Plates




                                      When you have created additional Sample ID Fields
        during the Plate Layout, you can use this Batch ID feature to populate these fields. Use
        the Apply to Field drop-down list to select the ID field you want to auto-number.


          1.   In the Base Name text field, enter text that Gen5 will append with a numeric
               suffix, if desired. Leave the field blank to consecutively number samples
               without additional text.
          2.   Enter the Initial Suffix - the number to apply to the first sample (of the first
               plate)
          3.   Set the Increment for sample IDs. Gen5 will leave the defined number of
               numbers unassigned between each sample. For example:
          4.   If desired, set the Minimum Suffix Width to enforce a uniform appearance to
               the numbering convention
          5.   Optionally, set the Start next plate at the next multiple of number. Gen5 will
               increase the next plate's Initial Suffix by the defined "next multiple," as long as
               that number has not already been used in a plate.
               For example: For a 96-well plate, if samples are numbered consecutively with
               an increment of 1, and the next multiple is 100, the second plate's samples will
               be numbered 101, 102, 103, ..., and the third plate's samples will be numbered
               201, 202, 203, and so on.
               For a 384-well plate, in the same scenario, the next plate's samples will be
               numbered 401, 402, and the third plate must begin with 801,
               More on Next Multiples: Applying the Next Multiple prefix is determined by
               the number of samples on the plate and the Increment factor. When sample
               numbering for the plate exceeds 100, and the "next multiple" is set to 100, Gen5
               applies the next unused multiple to start numbering the next plate. Thus, for
               384-well plates the default next multiple is 1000, which produces the best
               results for large numbers of samples.


                  Watch the effect of your choices in the Example space of the screen.


          6.   In the Plates section, define which plates to apply the naming convention to:0.
                All currently defined plates. This feature will not automatically apply the
                  naming convention to plates added to the experiment after it has been
                  executed. You must execute the feature again when more plates are added
                  to the experiment.






               Selection is filled by Gen5 when you select plates in the menu tree before
                 initiating this feature: hold the Ctrl key while clicking multiple plates, they
                 will be highlighted. Then, select Plate>Batch Sample IDs to see this option
                 selected.
               Range to define a contiguous selection of plates

          All plates selected for sample naming will be affected, even if Sample
            IDs have already been defined for them, i.e. the batch process will
            overwrite existing IDs.


Use Same IDs for each plate
        This option assigns the same Sample IDs or names to all selected plates:
         1.   Click the Edit Sample IDs button and enter IDs
         2.   Define the plates to apply sample IDs to in the Plates section (see step 6 above
              for details).0.

Import From File
      Gen5 lets you import a text file of Sample IDs. The file can contain the IDs or names of
      samples, each one separated by a hard return, and any "Additional" sample
      identification fields you've defined. When the additional ID fields are included in the
      text file they must be separated from the Name or Sample ID by the symbol defined in
      the Read From File Settings.
        The text file format requires data for each sample to be in a separate row: Name; ID
        field; ID field, when the "read from file" separator is a semi-colon (;), for example. Use a
        hard return or "carriage return" to separate each sample's data..

         1.   File Name        Enter the full path and filename or click the 3-dot button to
              locate the text file containing the Sample IDs for this plate and click Open.
         2.   Define the plates to apply sample IDs to in the Plates section (see step 5 above
              for details).0.
        Beginning with the first text item, Gen5 fills the Samples ID table of the first plate with
        the corresponding number of IDs. Additional plates are subsequently processed. Extra
        text is ignored, and insufficient text to fill all the sample cells results in blank name
        spaces.

Clear Sample IDs from Multiple Plates
        You can use the Batch Sample IDs feature to clear or erase the sample names applied to
        multiple plates:
         1.   In a multiple-plate experiment, highlight the plates in the menu tree (hold the
              Ctrl key while selecting the plates with Sample IDs you want to remove)
         2.   Select Plate> Batch Sample IDs, under Sample Names, select Use Same
              IDs for each plate



242 | Chapter 12: Preparing Plates



          3.   Click the Edit Sample IDs button, Gen5 opens the Samples dialog.
          4.   Click Clear All and click OK. Gen5 returns to the Batch Samples ID screen.
         5. Click OK. Click Yes at the warning message that all IDs will be cleared.0.
        erase sample names clear sample IDs for multiple plates


Create a replicate of a previously defined plate
        Gen5 automatically creates a replicate of a plate, when you add a plate to the
        experiment. The currently-defined Plate Layout is applied to the new plate. Gen5 also
        provides tools for copying Sample IDs from another plate.
        Choose your preference:
                Adding (a replicate) plate to an Experiment (see below)
                Copy Sample IDs from one plate to another on page


               Perform both steps to create an identical copy of the plate!



Import Sample IDs from a Text File
        Gen5 lets you import a text file of Sample IDs and "Additional" sample identification
        fields.

           These instructions are for a single plate, for more than one plate see:
             Batch IDs

        The file can contain the IDs or names of samples, each one separated by a hard return,
        and any "Additional" sample identification fields you've defined. When the additional
        ID fields are included in the text file they must be separated from the Name/Sample
        ID by the symbol defined in the Read From File Settings.



          1.                        Locate Sample IDs under the Plate in the menu tree and
               double click to open it.
          2.   Click Import. Gen5 opens the standard Windows(R) open file screen.
          3.   Locate the text file containing the Sample IDs or names for this plate and click
               Open.0.
        Gen5 assigns the first text item to the first sample well, and fills the Samples ID table
        with the exact number of IDs. Extra text (i.e. for undefined SPL wells) creates
        additional cells in the table to hold the extra data. Similarly, when the samples were
        not consecutively numbered in the Plate Layout, Gen5 does not skip them in the






      Sample IDs table, it assigns them an ID. Both extra text and "missing" samples are
      indicated in the table as grayed out fields.

        Gen5 offers to delete the extra or "invalid" data/IDs when you modify
          or review the Samples ID table. Answer No to the question: Do you
          want to keep this data? to delete it.

 Import File Format
      The import file format requires data for each sample to be on a separate line: Name; ID
      field; ID field, when the "read from file" separator is a semi-colon (;), for example. Use a
      hard return or "carriage return" to separate each sample's data. Leave the row/line
      blank to skip the sample identifier.
      When the "Read from File Setting" is a Tab and one additional ID field is defined the
      text file for the first 5 samples should look like this, without the title row:

            Well Identifier      Sample ID       Additional ID

            SPL1                 S4532           F

            SPL2                 S8765           F

            SPL3                 S2310           M

            SPL4                 G5876           M

            SPL5                 T4326           F

       The title row is only shown for illustration purposes. It should be omitted from the
      import file.


Export Sample IDs
      Gen5 lets you export a text file of Sample IDs. The file will contain only the IDs or
      names of samples, each one separated by a hard return.



       1.                        Locate Sample IDs under the Plate in the menu tree and
            double click to open it.
       2.   Click Export. Gen5 opens the standard Windows(R) save file screen.
       3.   Locate the directory where you want to save the text file containing the Sample
            IDs for this plate and click Save.0.



244 | Chapter 12: Preparing Plates
