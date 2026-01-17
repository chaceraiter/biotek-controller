# Chapter 16: Exporting Results

     Learn about Gen5's numerous data-exporting options in this
     chapter. You must have Microsoft Excel 2000 or higher installed
     on your computer to run the Quick Export and Power Export
     features. If you do not have Excel your options are limited to the
     File Export or Right-Click options.


 Exporting Results ..................................................................... 352
 Quick Export ........................................................................... 354
 Right-Click Options................................................................... 356
 Export to File........................................................................... 358
 Power Export........................................................................... 362



352 | Chapter 16: Exporting Results




Exporting Results
     Gen5 provides these exporting tools:

                 Quick Export: to instantly export the current view to a Microsoft(R) Excel
                worksheet
            Power Export: to export selected data to Microsoft Excel
            File Export: to export selected data, excluding curves, to a text file (for use in
              another software application)
            Right-Click Menu Options - Copy to Clipboard and Save As: to copy or save
              the current selection for use in another software application

Prerequisites
           For the Quick Export and Power Export features, you must have Microsoft Excel
           2000 or higher installed on your PC. Use the File Export or Right-Click options if
           you do not have Excel.

  About the Export Tools:
            The Power Export and File Export methods require selecting the content you
              want included in the output file before executing the export for a designated
              plate
            You can save your export selections with the Protocol, to reuse them every time
              you run an experiment based on that protocol
            Exporting data is like generating a report, it is done individually for each
              plate*. While you can select the export content in a protocol, you must run (or
              execute) the export in an Experiment (after selecting a plate or multiple plates)
            In an experiment, to run the export, you can select a plate in the menu tree and
              right click for a menu that offers the Power Export and File Export options
                [* except in multi-plate assays: refer to the Multi-Plate Protocol chapter]


           To preview the export-file output on-screen before generating an export file, use the
        Report Builder and Print Preview: add the same elements to a report as you do to
        the export, then click Print Preview to view the results online.






Export Multiple Plates to One File
       When you run multiple plates in an experiment you can export all the data to one text
       file:
         1.   In the menu tree, select/highlight multiple plates (by holding down the Ctrl
              key)
         2.   Right-click and select File Export0.

          Make sure the File Export Settings are defined to automatically
            append the data



354 | Chapter 16: Exporting Results



Quick Export

            Click the Quick Export button to instantly create a copy of the current screen in
        Excel(R).

   Where it works:
        Wherever you see the Quick Export button, you can export the view. And almost
        every Data View has a Quick Export button. For example, the Matrix, Statistics, Cutoff
        and Validation tabs offer it and the Graph tab has two, one for the curve and another
        for the Curve Results Table.

   If you don't have MS Excel:
        Use one of these options to select content and export it for use in another software
        application:
            File Export Builder: to export selected data to a text file (see page 356)
            Right-Click Menu Options - Copy to Clipboard and Save As: to copy or save
              the current selection for use in another software application (see page 356)



    Quick Export Settings
     Protocol> Protocol Options> Export Options> Quick Export Settings
     System> Preferences> Default Protocol> Protocol Options> Export Options>
     Quick Export Settings

        You can define default settings for Quick Export, which can be overridden in
        individual protocols. Use the controls in the Default Protocol to base all new Protocols
        on them. Override the default settings in individual protocols using the Protocol
        Options.

           Important: Default Protocol settings are applied "going forward,"
             they do not override existing protocol settings. They effect only newly
             created protocols.

   Export Row and Column Headers
 Select this option to include the Matrix and Statistic table row and column headers with the
 data exported to ExcelTM

Text Options
            Formatted Text: exports text as defined in Gen5, retaining the selected font and
              any customizations
            Text Only: exports text as characters only, without an associated font or any
              customization performed in Gen5






Excel Target
      Select a method for positioning the exported content in Excel:
         New Workbook and Target Cell: opens a new workbook and aligns the
           content starting at the target cell
         New Worksheet and Target Cell: creates a new worksheet (within a workbook)
           and aligns the content starting at the target cell
         Current Worksheet: adds content to the current worksheet
            Gen5 will launch Excel with a new worksheet if necessary. When multiple Excel
            sessions are open, Gen5 will prompt you to select a worksheet before
            performing the Quick Export.
            Target Cell: aligns content beginning at the target cell, fill the Target Cell
              field when you select this option
            Current Selection: places content beginning at the currently selected cell
            Append to Bottom: places content beginning at the next available row

          Ask me when I export: This option lets you determine the Excel Target every time
      you use Quick Export. Gen5 will prompt you for a placement option prior to executing
      the Quick Export.



356 | Chapter 16: Exporting Results




Right-Click Menu Options
         In addition to the Quick Export option available in most views, Gen5 offers three other
         features for "exporting" the current view for use in other software applications.


              Simply right-click to select the entire current view for a quick output. Or, to limit
         the output: click and drag to select contiguous cells or hold down the Ctrl key and click
         to select noncontiguous cells, then right-click for an option.


Copy to Clipboard




          1.   Right-click in almost any view and select the Copy to Clipboard feature
          2.   Open another software application, e.g. Microsoft(R) Word, WordPad, Paint,
               Outlook and similar products offered by other manufacturers, where you want
               to use the Gen5 content
          3.   Paste the selected content. Try:
                  Ctrl-V
                Right-click and select Paste
                From the menu, select Edit> Paste

Quick Print
       After selecting specific content or a current view, right-click and select the QuickPrint
       feature.
         It is similar to printing from the Report Builder, you can select a local printer. The
         current view or selected content is printed in formatted text with row and column
         headers.

Save As




         In any graph, i.e. Curve or Well Zoom, you can:
          1.   Right-click and select the Save As feature






2.   Gen5 opens the standard Save As dialog so you can browse to any
     file/directory available to your computer to choose the Save In location



3.   Use the drop-down list to select the Save as type: 0.
      Portable Network Graphic (.png)
      24-bit Bitmap (.bmp)
      CompuServe Graphics Interchange Format (.gif)
      JPEG Format (.jpg)
      Windows Enhanced Meta File (.emf)



358 | Chapter 16: Exporting Results




Export to File (File Export Builder)
       This option creates a text (.txt) file of the selected content for use in another software
       appliation.

     Protocol> File Export Builder

 Using the File Export Builder

   Select the Content to Export
        Highlight items in the Available Data Views and Add them to the Export Content
        box:
                You can Drag and Drop items into the Export Content box
                Drag and drop to change the sequence order of export items in the output
                  file
                Change the format and data sets associated with an item in the Export
                  Content box: Highlight an item and double click, or right click and select
                  Edit
                Highlight an item and click Remove, to remove it from selection
                In multiple-read (multi-index read) protocols, like kinetic analysis, it is
                  necessary to select a range of reads or a range of wells to include in an
                  export item. Certain data elements, like Well Data, Well Results, and Well
                  Zoom, require manual selection of the specific wells to include. Except for
                  area scan results, you can select multiple wells for simultaneous reporting
                  in the resulting table or graph. For details see Reporting Well Analysis
                  Results in the (previous) Reporting Results chapter


          Gen5 opens report items in Edit mode when a selection is required. For example,
        when you select a Matrix item to report a multi-index/kinetic read, you must select a
        Range of read numbers. One matrix or grid will be reported for each read number.


           Limitation: "Curves" and "Scan" data sets, created from kinetic
             analysis and area scans, cannot be exported with this feature. If you
             have Excel(R), use the Quick or Power Export options.

  Export Multiple Plates to One File
        When you run multiple plates in an experiment you can export all the data to one text
        file. After defining the export content, (and making sure the File Export Settings do not
        prevent it):
          1.   In the menu tree, select/highlight multiple plates (by holding down the Ctrl
               key)






        2.   Right-click and select File Export0.
       You can also use the File Export Settings to do this automatically:
              make sure the plates do not result in unique filenames,
              set the "prompt before saving" option to Never and Append

         ** Items marked with asterisks indicate 1 of 3 conditions:
           1. You must select specific data points from a very large (multi-read)
           data set or
           2. The experiment did not generate the expected results, an error
           occurred or
           3. The Procedure and/or Data Reduction steps that generated the item
           have been changed making it invalid **

  Using the Default Protocol
       You can define default settings for File Export, which can be overridden in individual
       protocols:
          Use the controls in the Default Protocol to base all new Protocols on them.
          Override and refine the default settings in individual protocols using the File
            Export Builder

         Content options in the Default Protocol may be limited by the lack of a
           defined Procedure.

         Important: Default Protocol Settings are applied "going forward,"
           they do not affect existing protocols. They are applied only to newly-
           created protocols.


File Export Settings
   Protocol> Protocol Options> Export Options> File Export Settings
   System>Preferences>Default Protocol>Protocol Options>Export Options>
   File Export Settings
       You can define default settings for File Export, which can be overridden in individual
       protocols:
          Use the controls in the Default Protocol to base all new Protocols on them
          Override the default settings in individual protocols

  File Naming Convention
       Set up a naming convention to apply to the export file:
          File Name: use the text field to build a naming convention. You can put any
            combination of text and Gen5-provided data points in the field to become the
            name applied to consecutively-saved files:



360 | Chapter 16: Exporting Results



                    Click the options arrow at the end of the field to select from the Gen5-
                   provided data points.
               Add or replace default text with your own text
               Notice the underscores Gen5 places between data points, they can be
                 retained or removed according to your preferences. Generally, it is good
                 practice to use filenames without spaces.
               Example: Gen5 displays an example of the file name you create

           The filename must comply with Microsoft(R) filename conventions, e.g. it
             must not contain so-called offending characters: \ / : # ? " < > |

  Separator
           Export files contain "delimited" data, i.e. data separated by a user-defined symbol
           or character. Select or enter the desired Separator using the buttons for Tab, semi-
           colon, comma or Other. If Other, enter the symbol or character in the text field.

  File Location
        Specify the location for Saved files:
            Last folder used: puts the Excel file in the folder last used by Gen5's File Export
              engine
            Folder: select an existing folder or define a name to apply to a newly-created
              folder

                    Use the 3-dot button to browse to the desired location for file storage

                    Use the options arrow to name a newly-created folder using the Gen5-
                   provided data points.
               You can add text for naming a newly-created folder, if desired
               Example: Gen5 displays an example of the folder name you create

  When Exporting, prompt before saving file:
               Always prompt users by opening the Save As screen whenever they export
                 a plate file, allowing users to alter the file name and location on-the-fly
               Only if the file already exists: open the Save As screen for saving export
                 files only if Gen5 generates a filename that already exists
               Never, if it the file already exists: never open the Save As screen
               Append: add this plate's data to the bottom of the existing file
               Overwrite: replace the existing data with this plate's data

  Include:
        Use the checkboxes to include any of the items offered:






 Headings: includes the Name of selected data elements as a section heading
   in the export file (just like the section headings in a Gen5 report)
 Matrix ...: includes the well location column and row labels, e.g. A-H and 1-
   12
 Statistics ...: includes column headers of the tables, e.g. Well ID, Name,
   Well, Conc/Dil.



362 | Chapter 16: Exporting Results




Power Export

  Prerequisite
           You must have Microsoft(R) Excel 2000 or higher installed on your PC to use Power
           Export.

  Power Export Explained
        Gen5 joins forces with Microsoft Excel to give you high-powered results reporting.
        Gen5 compiles all the data and customizations made in an experiment and exports it to
        Excel, along with a Gen5 toolbar.
        In Excel, you design the report using the Gen5 toolbar to select the desired experiment
        content. Then you can use Excel's native tools to perform complex calculations and
        customize the report's appearance.
        Using Power Export is a two step process: first, ideally when setting up a protocol, you
        select the content for export. Second, after running an experiment, you execute the
        Power Export for each plate.
        Whenever you select a Power Export option, Gen5 launches Excel. Initially, to select
        the content of the export, which inserts placeholders in the worksheet for the data to be
        generated in the experiment. Later, when you execute Power Export in the experiment,
        the selected data fills the placeholders.

  With Power Export you can:
               Take full advantage of Excel's document customization features to generate
                 publication-quality reports
               Include pictures, drawings, and company logos in reports
               Create custom formulas in Excel to perform additional calculations on the
                 Gen5 experiment data
               Take advantage of Excel's charting capabilities to create bar graphs, pie
                 charts, etc.


           Before defining the Power Export, customize the Data View elements in Gen5 that
        you'll include in the Excel report. While, you can make changes to Gen5's data
        elements when using Power Export in Excel, it is faster and easier to make the bulk of
        your choices first in Gen5.


           Watch the Tutorial for a demonstration on how to use Power Export






About the Power Export Toolbar
       Gen5's Power Export Builder launches Excel(R) with a custom toolbar:




        The selection buttons of the toolbar mirror the categories in Data Views (except
        Protocol Summary, which is only offered in the reporting tools). Use the buttons to
        select the content you want included in the Power Export. When you make a selection,
        Gen5 puts a "Results Object" or placeholder for the information in the Excel worksheet.
        The placeholder is filled in with results data (after the plate is read) during Power
        Export execution.

          In Office 2007 the Power Export Toolbar is placed in the Add-Ins
            tab/ribbon, which is added to the default ribbons when Excel is
            launched by the Power Export Builder.

              Protocol Summary = two pre-defined listings of the Procedure and Data
                Reduction steps defined in the protocol
              Matrix = a grid that represents the microplate
              Table = a columnar presentation of the data
              Graph = a standard curve or well zoom generated from a Curve or Well
                Analysis
              Field Groups = user-selected or defined data points useful for reports

   Power Export Execution
        When you execute the Power Export in an experiment (i.e. highlight a plate in the
        menu tree, right click and select Power Export) , Gen5 launches Excel with the data
        from the experiment filling in the placeholders selected with the Builder. You can run
        Excel as you normally do. he connection between Gen5 and Excel is severed. To
        modify a report element use the Power Export Builder.


            BioTek recommends customizing the Data View elements in Gen5 before
        selecting them for the Excel report. You can make changes to Gen5's data elements
        using the Power Export toolbar in Excel, but it is faster and easier to make the bulk
        of your choices in Gen5 first.



364 | Chapter 16: Exporting Results



How to use Power Export
          1.   When setting up the protocol, after customizing the Data Views, select Power
               Export Builder from the Protocol menu tree. This launches Excel with Gen5's
               Power Export Toolbar.

           In Office 2007 the Power Export Toolbar is placed in the Add-Ins
             tab/ribbon, which is added to the default ribbons when Excel is
             launched by the Power Export Builder.

          2.   In Excel, use the Power Export toolbar to select the content you want to import
               from each plate (described below).
          3.   Define the Power Export Settings (page 365).
          4.   When you run an experiment based on the protocol, highlight a plate in the
               menu tree, right click and select Power Export.0.
        Whenever you select Power Export, Gen5 launches Excel. Initially, to select the export
        content, inserting placeholders for the data in the Excel worksheet. When you run
        Power Export in the experiment, the selected data fills the placeholders. Then, you can
        use Excel's native toolset to prepare the report for publication.

           To modify a report element you must use Power Export Builder.



           Do NOT "protect" the worksheet in Excel when building the report with Power
        Export Builder; that is do not engage Excel's Tools>Protection settings.


Using the Power Export Toolbar in Excel



        Gen5's Power Export Builder launches Excel(R) with a custom toolbar for selecting
        content for the export.

How to select content:
          1.   Select the starting cell in the Excel worksheet where you want the Gen5 content
               to begin.
          2.     Click the down arrow of a selection button: Protocol Summary, Field group,
               Matrix, Table, or Graph on the Power Export toolbar and select an item. Gen5
               presents a Selection/Data/Format dialog specific to the selected item.
          3.   Make selections and/or modifications to the data format, as required for the
               item. Just like Customizing Gen5 Data Views and Reports. You can limit the
               Range of data points or change the Format/Font, as needed.






          Certain data elements, like Well Data, Well Results, and Well Zoom,
            require manual selection of the specific wells to include in the
            export. Except for Area Scans, you can select multiple wells for
            simultaneous reporting in the resulting table or graph.

         4.   Repeat steps 1-3 to select all the specific data items you want included in the
              Power Export, filling the worksheet with the required placeholders.

         5.   Click        to return to the Gen5 workspace. 0.
              Now you're ready to execute Power Export in an experiment: highlight a plate
              in the menu tree, right click and select Power Export.

How to modify selected content:
      When you select content for the Power Export, Gen5 puts a button above each data
      view in the Excel spreadsheet, right next to the starting cell for the content.




        Click the button to modify the selected content, i.e. open it in Edit mode

Running Power Export
    Highlight the plate in the menu tree> right click> Power Export
           After you've selected the content to export using the Power Export Builder
           And read the plates in an experiment

            Highlight the plate in the menu tree and click the Power Export button on the
        toolbar or right click and select Power Export. Gen5 launches Excel(R) with the selected
        content. You can then use Excel as normal.


Power Export Settings
    Protocol> Protocol Options> Export Options> Power Export Settings
    System>Preferences>Default Protocol>Protocol Options>Export Options>
    Power Export Settings



366 | Chapter 16: Exporting Results



        You can define default settings for Power Export, which can be overridden in
        individual protocols. Use the controls in the Default Protocol to base all new Protocols
        on them. Override the default setting in individual protocols using the Protocol
        Options.

Select method:
           Save after Export: select this option to enable Gen5's file naming and saving routine,
        then define your preferences below. They will be executed when the Excel file is saved.
        When this option is not selected, Power Export performs as expected but does not save
        or name the resulting file.
           Close after Export: select this option to run Power Export in the background. This
        feature creates, saves, and closes the Excel file using the defined settings after
        obtaining the content selected with the Power Export Builder. If you do not select this
        option, Gen5 will keep Excel open until you close it.

File Naming Convention
        Set up a naming convention to apply to the Excel files created with Power Export:
            File Name: use the text field to build a naming convention. You can put any
              combination of text and Gen5-provided data points in the field to become the
              name applied to consecutively-saved Excel files:

                    Click the options arrow at the end of the field to select from the Gen5-
                   provided data points
               Add or replace default text with your own text
               Notice the underscores Gen5 places between data points, they can be
                 retained or removed according to your preferences. Generally, it is good
                 practice to use filenames without spaces.
               Example: Gen5 displays an example of the file name you create

           The filename must comply with Microsoft(R) filename conventions, e.g. it
             must not contain so-called offending characters: \ / : # ? " < > |

File Location
        Specify the location for Saved files:
            Last folder used: puts the Excel file in the folder last used by the Power Export
              engine
            Folder: select an existing folder or define a name to apply to a newly-created
              folder

                    Use the 3-dot button to browse to the desired location for file storage

                    Use the options arrow to name a newly-created folder using the Gen5-
                   provided data points






            You can add text for naming a newly-created folder, if desired
            Example: Gen5 displays an example of the path and folder name based on
              your input

When Exporting,
      Prompt the user to confirm the path and filename by showing Excel's Save dialog:
            Always: whenever the save occurs
            Only if the file already exists: when the same name is applied to an
              existing file
            Never (overwrite the file if it already exists): do not show the Save dialog,
              replace the existing file with the current one when a file with the same
              name exists

  Export Row and Column Headers
        Select this option to include the Matrix and Statistic table row and column headers
        with the data exported to ExcelTM

Text Options
         Formatted Text: exports text as defined in Gen5, retaining the selected font and
           any customizations
         Text Only: exports text as characters only, without an associated font or any
           customization performed in Gen5

        Important: Default Protocol settings are applied "going forward,"
          they do not override existing protocol settings. They effect only newly
          created protocols.



368 | Chapter 16: Exporting Results
