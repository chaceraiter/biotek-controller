# Chapter 15: Reporting Results

     This chapter describes Gen5's Report Builder for generating print-
     ready data output for your experiments. Instructions for creating
     Field Groups to report inherent data points, how to change the
     Font, and other useful tips are provided.


 Building Reports ...................................................................... 334
 How to create and customize a report ........................................ 336
 Customizing Reports ................................................................ 338
 Reporting Well Analysis Results ................................................. 340
 Change the Font ...................................................................... 344
 Edit Report Items..................................................................... 344
 Fields and Field Groups............................................................. 346
 Create a Header and Footer ...................................................... 349



334 | Chapter 15: Reporting Results




Building Reports
     Protocol> Report Builder

About the Report Builder
       Gen5TM provides this tool to define exactly:
                what to include in the report
                how to format an item in the report
                where to place the item in the report.


           Define the Data Views and Default Protocol to speed up this step! Create Headers
        and Footers and add the Protocol Summary report sections in the Default Protocol so
        they appear in all newly-created protocols.


Report elements should be defined for each Protocol:
          1.   In the menu tree, under Protocol, select Report Builder
          2.   Highlight Available Data Views and Add them to the Report Content box
                You can also Drag and Drop items into the Report Content box
                Drag and drop to change the sequence order of items in the Report Content
                  box
                Edit an item in the Report Content box with a double click or use the right-
                  click menu
                Highlight an item in the Report Content box and click Remove to de-select
                  it (or use the Delete key)
                To clear the slate and start over, click Remove All to de-select all items.
                In multiple-read (multi-index read) protocols, like kinetic analysis, it is
                  necessary to select a range of reads or a range of wells to include in an
                  export item. Certain data elements, like Well Data, Well Results, and Well
                  Zoom, require manual selection of the specific wells to include. Except for
                  area scan results, you can select multiple wells for simultaneous reporting
                  in the resulting table or graph. For details see Reporting Well Analysis
                  Results on page 340.


          Gen5 opens report items in Edit mode when a selection is required. For example,
        when you select a Matrix item to report a multi-index/kinetic read, you must select a
        Range of read numbers. One matrix or grid will be reported for each read number.






        3.     Highlight an item in the Report Content box and click Page Break to add a
               page break to the report. Gen5 inserts it just above the highlighted item. You
               can drag and drop the Page Break to move its sequence order. (This step often
               works best after you've read the plate and can use Print Preview to assess the
               layout of the report.)
        4.     Set up Headers and Footers, if desired. (page 349)

        5.        When the report is defined, in an experiment, click the Print button to
               generate the report.0.

         ** Items marked with asterisks indicate 1 of 3 conditions:
           1. You must select specific data points from a very large (multi-read)
           data set or
           2. The experiment did not generate the expected results, an error
           occurred or
           3. The Procedure and/or Data Reduction steps that generated the item
           have been changed making it invalid **



             Click Print Preview to assess the report layout!


Using the Default Protocol
       Using the controls in the Default Protocol, you can input text and select protocol and
       experiment data to be included in all your reports. Your selections can be modified,
       removed, or replaced in individual protocols without affecting other experiments.
    System> Preferences> Default Protocol > Report Builder

         Content options in the Default Protocol may be limited by the lack of a
           defined Procedure.

         Important: Default Protocol Settings are applied "going forward,"
           they do not affect existing protocols. They are applied only to newly-
           created protocols.



336 | Chapter 15: Reporting Results



How to create and customize a report
        These step-by-step instructions are intended to introduce you to Gen5's tools and
        method for outputting results. While this example uses the Report Builder, the options
        and process is the same when building export files.

  Important first step
        You must define the Procedure (read parameters) and the Plate Layout before you can
        define Data Reduction steps. Likewise, you must define these and other elements of
        the Protocol (to generate the content of reports and export files) before you can create
        and customize the report.
        After you've defined the Procedure, Plate Layout, Data Reduction, and Runtime
        Prompts, you're ready to build the report.

  Create a Field Group to report details
        Field Groups can be used to report all of the details affecting your experiment:

          1.       Open Data Views from the menu tree
          2.   Highlight the Field Group label at the bottom of the tree and click New
          3.   Enter a Name for the field group at the top of the Edit dialog. For this exercise,
               we'll name it Read Step.
          4.   Click in the first cell of the table to enable a 3-dot button, and click the 3-dot
               button. The Fields dialog opens.

          5.      Use the drop-down list to set the Category to Procedure for this exercise.
          6.   At Field: use the drop-down list to select a data point. Select Measurement 1 for
               this exercise.
          7.   At Label: click in the text field, and overwrite the default label with a more
               fitting label for this data point. For this exercise, we'll call it Wavelength 1
               because we have multiple wavelengths.
          8.   Click OK to close the Field dialog.
          9.   Repeat steps 4-8 for the other cells in the table, adding Rows and Columns as
               needed. Explore the fields offered in the other Categories, like Plate
               Information, to find all the details you want to include. When you've added all
               the desired fields, click OK to save and close the Field Group.
         10. At Data Views, click Close.0.






     Here's an example of the Field Group:




Build the Report

      1.       Open the Report Builder from the menu tree
      2.   Locate the Field Group category at the bottom of the tree and highlight the
           just-made field group (Read Step for this exercise). User-defined field groups
           appear in bold text. Click Add to include it in the Report Content.
      3.   Scroll up the tree of Available Data Views, selecting and adding the desired
           items to the Report Content. The order of the items listed in Report Content is
           their order in the printed report. Drag and drop items to change their position.
      4.   After adding an item to the Report Content, double-click it to open it in Edit
           mode. Now you can customize the output. For example, on the Data tab, in the
           Format column, click in the cell to enable a 3-dot button that lets you change
           the number of decimal places or time format; on Selection or Well tabs define
           the range of data to report. Editing Curves lets you define the X- and Y-Axis
           titles. You can even combine multiple curves in one graph, if applicable.


          In Edit mode, change the Name at the top of the screen to customize the section
       heading in the report


      5.   Click OK to save your work and close the Report Builder.

      6.       If you're performing these steps in an experiment, click Print Preview to
           assess the report layout. If you're performing these steps in a protocol, save the
           protocol and create a new experiment based on it. Then use Print Preview to
           judge the output. Return to Report Builder to make any changes to the selected
           content.0.



338 | Chapter 15: Reporting Results




Customizing Reports
        Gen5TM offers extraordinary flexibility in customizing reports and export files. Almost
        everything you can view in Gen5 can also be reported. And, once you learn a few basic
        steps, you'll be able to define exactly what to include and exclude from reports and on-
        screen views.

Basic Rules:
               Data elements that are created or modified in Data Views become available
                 for selection when defining the Report and Export parameters. This
                 includes hiding a data set, which removes it from selection. Setting up the
                 views in the Default Protocol (if possible) makes them available in all
                 newly-created protocols.
               Create your own Data View for the most precise control over content and
                 appearance. You can create a matrix, table or graph that displays and
                 reports the information you've selected. You can include multiple data sets
                 in one view, for example. And, exclude default data points that do not
                 apply to your experiment.
               Include the Protocol Summary options: Procedure and Data Reduction
                 Summary to report protocol elements used to obtain the measurements
                 being reported. They are a good candidate for the Default Protocol.
               Create Field Groups to include miscellaneous information and data
                 points in your reports/export files. Gen5 captures numerous details like
                 temperature and shake duration, Plate ID and other run-time entries, and
                 print date and page count. Virtually all of the details affecting your
                 experiment can be reported.
               In multiple-read protocols, like kinetic analysis, it is necessary to select a
                 range of reads, or a range of wells to include in a report item. Certain data
                 elements, like Well Data, Well Analysis Results, and Well Zoom, require
                 manual selection of the specific wells to include in the report. You can
                 select multiple wells for simultaneous reporting in a table or graph.
               Select the Font option when editing content to define the "clipping"
                 method to apply to data points that are too long to fit completely in a report
                 column. Several choices are available to hide, truncate, or display as much
                 as possible of an extra-long data point.
               Select the Format option when editing content to define the number of
                 decimal places or significant digits to report or to change the time format of
                 a report item.
               Attributes applied to data elements in Data Views and the Report and
                 Export Builders take effect going forward. They do not replace, update, or
                 overwrite an item that has been previously assigned to a Report/Export.
                 You must refresh the selected contents after making any changes to a data






               element. And, any previously-saved Experiment will not reflect the content
               or formatting changes.
             When you Edit data elements in the Report Builder, your changes only
               apply to the Report. They will not be reflected in the Data Views or Export
               options. And, unless you use the File>Save Protocol As option, your
               changes will not be applied to any future experiments based on this
               protocol.
             384- and 1536-well plate matrixes are reported in segments that best fit the
               data to the page. Generally, the first 12 columns are reported in one matrix,
               the next 12 columns in another and so on, unless the page orientation is
               changed to landscape or the font size is reduced. Unless otherwise directed,
               Gen5 reports the entire matrix on as many pages as needed to display all
               the data.

Best Practices:
             Create your own Data Views for the most freedom-of-choice in reporting
               and online viewing.
             Print Preview your reports to make sure you're happy with the layout
               before printing them.
             Curve Results tables work best just below or above the curve they describe.
               Drag and drop the Curve or the Curve Results in the Report Content to
               arrange them this way.
             Limit the number of wells in a Well Zoom graph to 8 for best results.
             Changing the page orientation from "portrait" to "landscape" may be the
               best use of the space and improve the appearance and readability of the
               report, especially when reporting 384-well and larger plates.

 To change the page orientation:
       1.   Select File>Print Setup...
       2.   Select the desired Orientation 0.

        You must be have the experiment file open to change the Print Setup



340 | Chapter 15: Reporting Results



Reporting Well Analysis Results
     Protocol> Report/Export Builder> for the selected Content
        By its nature, the individual well results of Well Analysis make reporting them a bit
        tricky. Well Analysis results, like Well Zoom graphs and Well Data tables, require an
        extra step when defining reports and exports. See Report Examples on page 342.
        In the Report Builder and for applicable export routines, in the Export Builders, when
        you select any of the following:
                Well Data table
                Well Data 2D table (for area scans)
                Well Analysis Results table
                Well Zoom graphs
                Area Scan Zoom graphs
          Be sure to open (Edit) the item to select one or more wells as the content to
        report/export.

In the Report or Export Builder:
          1.   Add a well analysis item from Available Views to Report/Export Content
          2.   If the item doesn't open in Edit mode, double click it
          3.   Select the Wells tab or the Curves tab (depending on the type of report item)
          4.   Select one well at a time to report on: enter a well location in the Well field;
               Gen5 displays the Well ID and concentration or dilution assigned to the
               location, or
               Select multiple, adjacent wells using a hyphen to define the range, A1-H12,
               for example, would include all wells in a 96-well plate
               Important: Some report items require limiting the number of wells that can be
               successfully included in an instance of it. You may need to add multiple
               instances of the item to report all the desired wells. Use Print Preview to
               determine how many wells can fit on the page.
          5.   Click Add to move the well into the Selected box. Except for Area Scan results,
               you can select multiple wells for each report item. (See Tip for Area Scan
               below.)






     Tables and Curves respond differently to this treatment. Curves: Well
       Zoom graphs, overlay the results for each well in one curve. (Limit the
       number of wells to 8 for the best results.) Well Data tables present
       the data for each well in a column or row, adding another column/row
       to the table for each well. To best fit the data in a report it is often
       necessary to add multiple instances of an item. And, for each
       instance select the maximum number of individual data points that fit
       cleanly. Likewise, to report well zoom graphs individually, rather than
       overlaying them, you must add multiple instances of the Well Zoom
       graph. Use Print Preview (after the plate is read) to determine the
       best fit for your data. It's a "trial and error" process, selecting and
       revising the Report Content, and assessing the layout with Print
       Preview, until the report is satisfactory.

     Exporting the data does not require the same level of precision when
       selecting content. Gen5's File Export Builder delimits data points
       without restriction (and does not support curves) and Power Export
       exploits Excel's spreadsheet capabilities to handle limitless data
       transfer.

    6.   (Optional when available) Highlight a well in the Selected box and click the
         Edit button to modify its formatting.0.



                    You can remove multiple wells from the Selected box
         simultaneously: hold the Ctrl key while selecting non-contiguous wells or hold
         the Shift key while selecting adjacent wells, then click Remove

Tip for Area Scans
         You must add multiple instances of the Area Scan Well Zoom and Well Data 2D table
         to the Content to report /export multiple area scan wells. For best results, identify the
         selected well in the Name field when adding each well, one well at a time, to the report
         content. The Name becomes a sub-heading in the report output, so you can easily
         distinguish between reported wells, e.g. Scan: B3.



342 | Chapter 15: Reporting Results



Report Examples
Here are some sample report outputs of well analysis results:
        Using Gen5's Report Builder to output well analysis results involves some trial and
        error to determine the maximum number of wells that can fit neatly on the page. Here
        are some examples of the offerings:

Well Zoom Graph




        Limit the number of wells to 8 when reporting a well zoom graph for the best results

Well Data Table




Well data tables report each well in a column. The number of wells that can be successfully
included depends on the number of digits in the results and the paper orientation (portrait or
landscape).






Well Analysis Results Table




Well Analysis results tables are generally easy to include, i.e. all wells can be safely selected,
because each well is reported in a row.



344 | Chapter 15: Reporting Results




Edit Report Items
     Protocol> Report Builder
   In the Report Builder, double click an item in the Report Content window to edit its format,
   font and other attributes specific to the selected item. The editing options available are
   context sensitive, depending on the attributes of the selected item: matrix, table, or graph.


Change the Font

       Clicking the 3-dot button in the Font column of a Data View or Report Builder Edit
   screen leads to a standard Windows(R) Font selector (watch the Report Builder Tutorial for a
   demonstration):
            In Data Views, highlight the item and click Edit
            In Report Builder, add the item to the Report Content, then double click to
              open it in Edit mode
        Selecting the Font, Style, Size, and Effects is the same as any Windows program. The
        fonts available for selection are set by your PC's operating system.




Select method for displaying extra-long text items:
           In the lower-right corner of the Font screen, use the drop-down lists:
            Clipping to select the way to format data points that have too many characters
              to fit completely in a report or table column and in the cells of a Matrix:
               None fits as much text as possible, using the selected Alignment method






    text... fits as much text as possible and truncates it using the ellipsis
    ### replaces all the content with the pound sign or hash mark
    c:\...\file.ext only applies to path and filename content, it fits as much text
      as possible beginning with the filename and extension and progressively
      truncates the directory's path
 Alignment to define the text alignment: left, center, right

Font settings are not retained by the File Export Builder because
  they are not supported in the resulting text file



346 | Chapter 15: Reporting Results



Fields and Field Groups
        For reporting and exporting data, Gen5TM automatically provides data fields and field
        groups based on inherent information. You can create your own field groups, as well.
            Learn About Field Groups (below)
            Create New Field Groups on page 347
            Assign Fields to Reports on page 350


About Fields and Field Groups
      For reporting and exporting purposes, Gen5TM provides data fields based on inherent
      information. You can create your own Text field, as well, to add custom information to
      a report header or to create a report title, for example.
        The responses to Runtime Prompts, the steps in the Procedure, and the Reading Date
        and Time (logged by Gen5 your computer's calendar and clock) are examples of the
        numerous data points Gen5 turns into Fields that can be added to a Field Group for
        reporting or inserted in a report header or footer. One field group is installed with
        Gen5: an empty Field Group is available in the Data Views, and the report and export
        builders. You can modify this Field Group and/or create your own in Data Views.

Basic Rules
            Field Groups are a collection and arrangement of fields
            Creating and modifying Field Groups is done in Data Views; however, field
              groups can be modified for individual instances after they are included in
              Report or Export content
            Field Groups can be included in Reports and Export files and Fields can be
              added to report Headers and Footers in the Report Builder
            Once Field Groups are added to reports and export content their properties are
              fixed. Changes made to field groups only take effect going forward, i.e. when
              you edit a field group in Data Views, the changes are NOT applied to those
              field groups that are already included in Report and Export Content. You must
              Remove the original and Add the updated field group in the Report Builder,
              Power Export Builder and File Export Builder to capture the changes.
            Field Categories include Text for user-created information/text and Blank for
              use when editing a field group, header or footer to remove a field.
            A Field Categories reference table is provided on page 348
                how to clear remove a field from a field group







Creating and Modifying Field Groups
      To create a new field group:

      1.        Open Data Views (Protocol>Data Views)
      2.    Highlight the Field Group label at the bottom of the tree and click New
      3.    Enter a Name for the field group in the Edit dialog. Follow the instructions
            below to define the content of the group.0.
      To modify a field group:
      1.    Open Data Views
      2.    Highlight the Field Group you want to modify and click Edit. Follow the
            instructions below to define the content of the group.0.

       You can also Edit a field group in the Report Builder, but your
         changes will only apply to the Report for the current experiment. They
         will not be reflected in the Data Views, will not be available for Export,
         and will not be applied to any future experiments based on this
         protocol. Keep this in mind when you're formatting a field group - in
         most cases it is more efficient to work in Data Views than in Report
         Builder.

      To define the content of a field group:
      1.    Use the Add Row or Add Column buttons as needed to set up the desired
            number of rows and columns.
      2.    Click in a cell in the table to enable a 3-dot button that leads to the Fields dialog
            to select and format the content of the field. Click the 3-dot button, and select
            the Category and Field you want to add to the group.




      3.    You can insert, delete, and merge rows, and insert and delete columns using a
            right-click: select the row or column by clicking its number, then right-click for
            a menu.0.
           Another shortcut: you can drag and drop rows and columns to change
           their position. Click in the column/row you want to move until the pointer
           changes to drag and drop mode, drag it into place, watching for the red
           location indicator, and release to drop it into the desired position.



348 | Chapter 15: Reporting Results



Field Categories Reference

       Category              Field                   Hint

       Text                  User-defined Text       Use this option to define your own
                                                     report titles

       Experiment            Experiment File Name    .xpt file must be saved to have a file
       Information                                   and path name
                             Experiment Path Name    -Plates per Assay is only applicable to
                                                     multi-plate protocols.
                             Plates per Assay

       Procedure             Read step and related   These fields are created by the steps
                             data, examples:         you define in the StepWise Procedure.
                                                     If there is more than one Read step
                             Plate Type              the fields will be numbered
                                                     accordingly, i.e. every read-related
                             Reading Zone            field will be numbered to correspond
                                                     with its read step. When multiple
                             Kinetic Interval
                                                     Kinetic loops are defined, they are
                                                     similarly numbered.
                             Measurement #
                                                     Plate size reports the number of
                             Sensitivity             columns x rows

                             Temperature

                             Step 1 Description

       Protocol Options      Protocol Type

                             Std Dev Weighting

       Plate Information     Experiment-specific     Reports user inputs at read time
                             details, examples:

                             Reading Date and
                             Time

                             Plate ID

                             Runtime Prompts

                             Barcode

                             Reader Serial Number

                             Reader Basecode

                             Plate Comment

       Printing Options      Print Date/Time         Especially useful for Headers or
                                                     Footers
                             Page Number






     System                 User Name                  User information is only useful for
     Information                                       Gen5 Secure users
                            User Group                 Software version reports Gen5's
                                                       version number
                            Software version

     Blank                  Empty                      Use to delete a previously-added field



Creating a Header and Footer
      You can set up a default header and footer that will be applied to all reports, and/or
      you can create a header and footer for each protocol individually. (Modify the
      header/footer for individual experiments to override the Default Protocol settings.)
              To assign headers and footers to the Default Protocol (for all newly-created
                protocols/experiments), select System> Preferences> Default Protocol
                Setup
              To create headers and footers in a Protocol/Experiment (only for the
                current protocol/experiment): in the menu tree, select Protocol> Report
                Builder

To create a header or footer:
       1.    In the Report Builder, select the appropriate tab: Header or Footer
       2.    Use the Add Row or Add Column buttons as needed to set up the desired
             layout
       3.    Click in a cell in the table to enable a 3-dot button that leads to the Fields
             dialog to select and format the content of the field
       4.    You can insert, delete, and merge rows, and insert and delete columns using a
             right-click: select the row or column by clicking its number, then right click for
             a menu
       5.    As needed, select the option to "use custom header/footer on first page" to add
             another tab to this dialog. If unselected, all pages of the report will have the
             same header and footer. 0.
         Another shortcut: you can drag and drop rows and columns to change their
         position. Click in the number of the column/row you want to move until the
         pointer changes to drag and drop mode, drag it to the new place, watching for
         the red location indicator, and release to drop it into the desired position. Note:
         when a row has been merged, columns cannot be moved.



350 | Chapter 15: Reporting Results



Assigning Fields to Reports

  Fields can be used in two ways:
            Used in a header or footer when defining reports, see Creating Headers and
              Footers (described above)
            Used to define a Field Group to include in a report or export file
        In Report or Export Builder:

          1.      In any of the Header or Footer tabs or after adding a Field Group to the
               Report or Export Content and opening it to Edit, click in a cell in the table to
               enable a 3-dot button, and click it.
          2.   In the Category field, use the drop-down list to select either Text or a category.
          3.   In the Field field, use the drop-down list to select a field, unless you selected
               Text.
          4.   In the Label field, enter the text you want included in the report. You can
               customize the label by typing over the default text or remove the label by
               deleting the text.
          5.   Use the 3-dot buttons at the Font and Format fields (if applicable) to modify the
               default settings. You can replace the default content for the field Value the
               same way:
                Use the Font dialog to define the Alignment of the content in the field: left,
                  center, right. And, if there's a chance the text will overrun the length of the
                  field, choose a Clipping format to replace the missing text. Your choices are
                  not displayed in the header or footer table, use Print Preview to assess the
                  effects.
          6.   Click OK to save and apply your choices.0.
