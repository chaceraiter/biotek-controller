# Chapter 14: Viewing Results

     Learn Gen5's naming conventions and the meaning of symbols and
     notations in this chapter. Instructions and suggestions for
     customizing online views and report outputs are provided also.


 Plate View ............................................................................... 313
 Data Views.............................................................................. 315
 Gen5's Tables.......................................................................... 320
 Data Set Naming Conventions ................................................... 316
 Symbols and Notations ............................................................. 317
 Modify/Customize Views/Data ................................................... 323
 Change the Time Format........................................................... 326



310 | Chapter 14: Viewing Results




Viewing Results
        You can instantly view the results of an experiment in Gen5's main workspace using
        the Plate View:




            After reading the plate (or otherwise acquiring data), in the Plate View use the
              drop-down list for Data to display the raw data and any data reduction results

                  Click the Quick Export button to instantly open the current view in Excel(R).
                Learn more about Gen5's Export Options

                 Click the 3-dot button next to a data set to customize the view's appearance.
                This feature is also available in the Data Views dialog.
            ** Asterisks are used to signal a change: in Gen5's title bar an asterisk indicates
              the current file has been changed but not-yet saved. When a data set is enclosed
              by asterisks it has been become invalid. Generally this is because a Read step or
              Data Reduction step has been altered. Edit custom-made data views to select
              valid data sets

                  384- and 1536-well plates require resizing to effectively see the data. Gen5
                adds a button to the Plate View to zoom in on the top-left quadrant of the plate
                and zoom out to view the entire plate. After zooming in, use the scroll bars to
                bring the other quadrants into focus. Find more on resizing the views below.



            Multi-index readings offer another viewing option. Kinetic and scanning reads
              generate views based on the number of read intervals, wavelengths, or
              positions defined. Use the spin buttons or enter the desired read index and
              click Show to display it. Gen5 displays the time, wavelength, or position of the
              selected read number.






                Kinetic and Scanning protocols can generate Well Analysis data sets
              labeled Curves, in the Matrix tab, open the Curves data set and click on a well
              for a Well Zoom. (Note: 384- and 1536-well plates show a magnifying glass in
              the well instead of a curve.)


            Starting at the Curves data set, you can display multiple well zooms
         simultaneously by holding down the Ctrl key while selecting (up to 8) wells


          You can also select Create new Matrix to define a new view
          Select the Statistics tab to view a table of data reduction results
          Select the Graphs tab (when available) to view any Curves, except kinetic
            analysis curves, which Gen5 calls Well Analysis and is described above
          Select the Cutoffs tab (when available) to view the values or results of the
            cutoff formulas
          Select the Validation tab (when available) to view the values and results of the


 Important Notes:
            validation formulas



               Gen5 may not display some data points by default; to see them you must
                 create your own Data Views. If you expected to see certain results that are
                 not currently displayed, try creating your own views.
               All data views are also available for Reporting and/or Exporting
               Modify a data view to change the way results are reported, including the
                 number of decimal places and significant digits (page 323)
               Gen5 always uses your computer's Regional Settings to display and input
                 data
               Learn the meaning of the Symbols and Notations displayed on page 317.


Opening the Plate View/Workspace
   In an Experiment, if it is not already open in the main view of Gen5TM:

          from the menu tree: Double-click the desired               item
          Or, select Plate> View



312 | Chapter 14: Viewing Results



Resizing the Plate View




        Use the standard Windows(R) Maximize and Minimize buttons to resize the Plate View

             For more precise control, hover your mouse at the corner of the window, and with
        the two-headed arrow click and drag it to the desired size

            You can also resize the columns and rows: hover your mouse on a border and
        drag the two-arrowed pointer to the desired column/row size

           Changing the window, column & row size typically enables the
             standard Windows(R) scroll bars, which you'll need to use to see all of
             the wells







Resize columns




           Hover your cursor over the division between columns until the cursor turns into a
      two-arrow I-beam. Then click and drag the column to the desired size. Just like Excel(R)
      and other programs! In some Gen5 views this option works for rows, as well.


Plate View (Workspace)
   Plate> View
      Use the Plate View or Plate Workspace to instantly view the results of an experiment
      and, if needed, to mask or alter the results.

About the Plate View
      Gen5 always provides the Matrix and Statistics tabs, and when applicable, adds a
      Graphs, Cutoff Values and Validation tab

What you can do:



              After reading the plate (or otherwise acquiring data), in the Plate View use
             the drop-down list for Data to select the data set (raw data or data reduction
             results) to display

              Click the 3-dot button next to a data set to customize the view's appearance.
             This feature is also available in the Data Views dialog.

               Click the Quick Export button to instantly open the current view in Excel(R).
             Learn more about Gen5's Export Options, including the right-click options:
             Copy to Clipboard and Save As



314 | Chapter 14: Viewing Results



                  In the Matrix and Curve tabs, use the Edit and Mask buttons to change or
                mask selected data

                  In the upper-right corner, below the minimize, maximize, and close
                buttons, click the duplicate view button to open another instance of the Plate
                View. Use this feature to view the raw data results of a reading in one window
                and simultaneously display a curve plotted from the results in another
                window, for example

                                 Use the read index spin buttons to consecutively advance the
                view of a Kinetic or Spectrum read, or enter a read/wavelength index in the
                field and click the Show button

How to set the default view
     To determine the first data set or data view to open for each tab of the Plate View:

          1.        Select Data Views from the menu tree
          2.    For each category, Matrix, Table, Graph, ..., highlight the data set you want to
                be shown first, i.e. during and immediately after reading the plate, when its
                corresponding tab is selected in the Plate View
          3.    Click Set as default0.
        The Set as default button only appears when an eligible data set is highlighted. The
        button appears grayed-out when the current default is selected, and it disappears
        when a non-eligible data set or another item in the Data Views is selected.







Data Views
  Protocol> Data Views
    Gen5TM offers this menu-tree control box for selecting and modifying the way data is
    presented on-screen and in reports and export files. The selections and modifications
    made for on-screen viewing (Data Views) become the settings for the Report Builder,
    Power Export Builder, and File Export Builder.


      Create your own Data Views for the most precise control of content and
    appearance.


    Gen5 lists all the data sets available for viewing under a display category:
           Matrix = a grid that represents the microplate
           Table = a columnar presentation of the data
           Graph = a standard curve or well zoom generated from a Curve or Well
             Analysis
           Field Groups = user-selected or defined data points to include in reports

      Protocol Summary is another category offered for reports and
        exports only. You'll find it in the Report Builder, File Export Builder,
        and Power Export Builder.



    The function buttons: New, Edit, and Hide/Show are enabled or disabled in sync
    with your selections in the menu tree.
       Highlight an item in the tree and click Edit to modify its appearance.
         Depending on the type of item, you can change its:
           Numeric Format and Font, e.g. number of decimal places,
           Range of data/wells to include in views and reports,
           Sort order, layout and other characteristics.
       Highlight a display category to enable the New button. Modifying the system-
         provided views is limited, but you can create your own views to display
         exactly the data elements of interest, in the most pleasing format.

                The Set as default button only appears when an eligible data set is
    highlighted. The button appears grayed-out when the current default is selected, and it
    disappears when a non-eligible data set or another item in the Data Views is selected.
    Use the button to determine the first data set to open in the Matrix tab of the Plate
    View. Gen5 displays the first raw data set (measurements obtained from the reader),
    unless another data set has been set as the default.



316 | Chapter 14: Viewing Results




Data Set Naming Convention
        Gen5TM names the data sets it creates this way:

    Name                  Meaning                              Example

    wavelength            Absorbance wavelength                450

    wavelength[#]         When 2 or more identical read        450[2]
                          steps are defined in the same
                          Procedure, the wavelengths are
                          numbered

    ex/bw & em/bw         Fluorescence filter sets:            360/40, 580/40
    ex, em                excitation/bandwidth and             485,528
                          emission/bandwidth or excitation
                          and emission wavelengths for
                          mono reads

    em/bw                 Luminescence emission                460/40
                          wavelength/bandwidth

    Lum                   Luminescence using Hole/empty        Read 3:Lum
                          position in the filter wheel

    Spectrum              Absorbance Spectrum scan             Read 1:Spectrum
    EX Spectrum           Fluorescence Monochromator-          Read 1: EX Spectrum
    EM Spectrum           based spectrum scans                 Read 2: EM Spectrum

    Curves [nm]           Kinetic curves are automatically     Curves [490]
    Curves                generated during kinetic analysis;   Curves [360/40, 460/40]
    [ex/bw,em/bw]         they lead to Well Zooms
                                                               Curves [EM Spectrum]
    [Spectrum]            Spectrum scans also plot curves
                          for each well: OD*/wavelength;       *OD also represents
                          they lead to Well Zooms              RFU/RLU

    Read #:nm             When more than one read step is      Read 2:410
                          defined, the Read number names
                          the data set

    Blank nm              Blank well subtraction data set      Blank Read 2:360/40
                          (created automatically by Gen5)

    Corrected [nm]        Pathlength corrected data set        Corrected [405]
                          (Absorbance read option)

    Polarization          Data transformed per                 Polarization
                          fluorescence polarization formula






  Parallel Intensity      Raw/ blanked data from parallel         Parallel Intensity
                          measurement

  Perpendicular           Raw/ blanked data from                  Perpendicular Intensity
  Intensity               perpendicular measurement x G
                          Factor

  ex/bw,em/bw             Raw data from parallel or               485/20, 590/35 [Parallel]
  [Parallel] or           perpendicular measurement               485/20, 590/35
  [Perpendicular]                                                 [Perpendicular]

  Anisotropy              Data transformed per anisotropy         Anisotropy
                          formula

  Data Reduction steps produce data sets named with the type of calculation and the
  raw data set name. For example, Well Analysis steps could generate: Mean V [340/40,
  520/40] and Onset [Blank Read 2:490]



  When a Step Label is entered for the Read or Data Reduction Step, the label is
  included in the name of the data set. For example: a Step Label in an Absorbance read
  step of Test1 would result in a raw data set of "Test1:450" and an automatically-
  generated blank-subtraction data set would be "Blank Test1:450".




Symbols and Special Notations
        Depending on the current view, report, or exported text you may see any of the
        various symbols and notations that Gen5 applies to call your attention to special
        conditions:

Symbol               Description

>(highest conc.)     After fitting a standard curve and calculating the concentrations,
<(lowest conc.)      Gen5 denotes wells falling outside the abscissa range with >(upper
                     limit concentration) or <(lower limit concentration); <0.00 is
                     displayed rather than negative concentrations, unless it's called in
                     an interpolation

?????                ????? appears in a well in certain Matrix and Statistics views when
                     data for that well has not been obtained; cannot be calculated; is
                     based on out-of-range values; or has been failed by the reader

####                 #### appears in a well when the size of the grid is not large
                     enough to show the value in the well. Resize the view to see the
                     contents. Or, change the Font used to display the value, choosing a
                     different "clipping" method

[ ]                  In Well Zoom views when the original read range is reduced, Gen5



318 | Chapter 14: Viewing Results



                      plots the revised Calculation Zone with brackets: [ ]

 *1234*               Gen5 displays Masked values in data views and reports between
                      asterisks

 !1234!               When Gen5 uses an out-of-range value in statistics calculations, it is
                      considered a biased result and will be reported between exclamation
                      points

 *                    Asterisks are displayed next to plate icons and in the title bar of an
                      experiment when a change is made or an action is taken but the file
                      has not yet been saved

 **dataset**          Asterisks identify invalid data sets. This is generally caused by
                      changing the source Read step or Data Reduction step after the
                      data set was initially created

 #N/A                 Indicates an invalid data reduction item

 INJECT               Synchronized Mode Procedures with multiple, appended kinetic
                      loops and one or more dispense steps, use this symbol to identify
                      when dispensing occurred

 OVRFLW               Measurements are not being collected, most likely due to
                      inappropriate read parameters for the test specimen (overflow)

 MISSED               The reader did not capture a value for every Xenon flash
                      measurement taken for this well. The reader missed a measurement
                      and cannot report a reliable value.


           Note: Biased values may appear in a Statistics table when
             Calculation Options are set to include out-of-range values. If, for
             example, the concentration for one of three standard replicates is
             reported as >40, the Standard Deviation and CV% values are
             considered suspect. Gen5 surrounds the values with exclamation
             points to indicate that it is the user's responsibility to determine
             whether or not the results are valid.

Well Analysis Results Table
        When a Well Analysis Data Reduction step is defined, Gen5 shows the calculation
        results in a table beneath the curve. The "Curves" or "Scan" data set that leads to a well
        zoom, must be the subject of a Well Analysis step; raw data well zoom views do not
        include a Well Analysis Results table.

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



Data Points Reference
      When customizing or creating a new view in Gen5, the following data points may be
      available depending on the Procedure (reading parameters) and Data Reduction steps:

       Data                            Description

       Well ID,                         Plate Layout well assignments

       Conc/Dil, Conc/Dil type          Concentration or dilution values and setting
                                        in Plate Layout

       Unit                             User-defined in Plate Layout

       Name                             Sample IDs

       Bitmap [nnn]                     Kinetic/Spectrum Curves or Area/Linear
                                        Scan image

       Formula [nnn]                    Transformation formula

       Label: nnn [nnn]                 User-defined labels for read and data
                                        reduction steps



320 | Chapter 14: Viewing Results




Gen5's Tables

About Gen5's Tables
      Based on the type of plate reading and the data reduction steps defined, Gen5
      automatically creates tables to display, report, and export the data. You can make
      slight modifications to the system-generated tables, like changing the font and numeric
      format of an item. And, you can create your own -custom-made- tables.
        You can view the tables in the Plate View:
               Statistics tables can be viewed using the Statistics tab,
               Curve Fitting results are shown below the curve in the Graphs tab,
               Well Data and Well Results tables can be viewed in the Well Zoom.
        Some tables, like Validation results, can only be printed (or Print Previewed) and
        exported.

Curve Results Table






Potential Tables
        Depending on the protocol, specifically the type of read and data reduction steps,
        and the level of Gen5 software, the following tables may be available for viewing,
        reporting and exporting data.
         Statistics - show the results of a data reduction step. The system-generated
           tables display the Well (well coordinate), Well ID, and
           Concentration/Dilution assigned in the Plate Layout; the Sample IDs or Name
           assigned to the Well ID; the Count or number of replicates; and the Mean,
           Standard Deviation and Coefficient of Variation percentage (%), if available.
         Curve Results - Gen5 generates three tables to show the curve fitting
           Parameters and Values of a curve. The "Curve Fitting Results" table includes
           the curve name, formula, parameters, and R2. The "Curve Interpolations" table
           shows the interpolation data. And, the "Curve Fitting Details" table lists the
           parameters and their calculated value, standard error and 95% confidence
           interval. You can display these tables underneath a curve in the Graphs tab of
           the Plate workspace when viewing them online. You should review the details
           to assess the goodness-of-fit of your curve. Depending on the Curve Fit
           Method, numerous other parameters and values can be displayed/reported in
           a custom-made table.
         Well Data - show the well-specific details for multiple-reading Read Steps
           like kinetic analysis, spectrum, and linear scans. Well Data 2D is the Area Scan
           rendition. They are used in Well Zooms to toggle the display between View
           Data and View Chart. When adding this kind of table to a report or export file,
           it is necessary to select the specific wells, by their well coordinate, e.g. A1, that
           you want reported.
         Well Analysis Results - show the generated data of a Well Analysis Data
           Reduction step. They are viewed in a related Well Zoom, beneath the curve.
           Note: The "Curves" or "Scan" data set that leads to a well zoom, must be the
           subject of a Well Analysis step; raw data well zoom views do not include a Well
           Analysis Results table. When adding this kind of table to a report or export file,
           it is necessary to select the specific wells, by their well coordinate, e.g. B2, that
           you want reported.
         Cutoff Results - show the cutoff formula as defined and the value of the
           formula. While the results of the cutoff criteria can be viewed online, using the
           Symbols data set, the Cutoff Results table can only be reported and exported.
           You can use the Print Preview feature to view this report component online.
         Validation Results - show the validation Formula as defined and the Value
           result of the formula. The Validation Results table can only be reported and
           exported. You can use the Print Preview feature to view this report component
           online.
         Audit Trail - shows the entries, i.e. change history, logged in the Audit Trail.
           Depending on your level of Gen5, one or more types of audit trails are
           maintained and can be reported: Data, Protocol, and Calculation Warning. This



322 | Chapter 14: Viewing Results



              table is only used for reporting and exporting, as Gen5 offers the Audit Trail
              viewer in the menu tree for online viewing. The audit trails tables list date,
              user, event and user's comment logged at the time of the event.
            Signatures - shows the date, time, reason and signatory of each signing event.
              Also included is a "Document modified" record whenever the protocol or
              experiment is changed after a signing event. Refer to the audit trail to
              determine how the file was changed.
            Procedure Summary - lists the steps, in sequence, defined in the StepWise
              Procedure for reports and export files


           When building reports, using the Report Builder, group together related items, like
        the Curve and its Curve Results table, and a Well Zoom and its Well Data, for the best
        results.



Print Preview to see Tables




        This is a sample report of the Cutoffs, Validation, and Audit Trail tables, using Print
        Preview.






Modify/Customize Views/Data

Numeric Format for Results
      Gen5 provides controls for changing the numeric format for results. You can choose
      between Scientific notation, Decimal and Best Fit formats. Then you can define the
      number of significant digits or decimal places to display/report. Scientific notation is
      also known as Standard index notation.

  How to change the numeric format:
      The numeric format is set individually for each applicable data set.

      After defining the protocol, open Data Views (select Protocol>Data Views):
       1.   Highlight the data set you want to format in the tree and click Edit
       2.   Select the Data tab
       3.   In the Format column, click inside the applicable table cell (row) to enable a 3-
            dot button that leads to the Numeric Format control for that data point
       4.   Click the 3-dot button and use the controls to define the format. Select a
            Format and define the level of Precision. The Samples section of the control
            shows the affect of your selections on sample data.0.

        Data views/data sets can also be Edited in the Plate View and after
          they have been added to report and export content. Click the 3-dot
          button next to the Data field of the Plate View. Double click an item
          added to the Report/Export Content in the respective builder.

  Gen5's Numeric Formats explained:
      Gen5 provides these display options for numeric results in reports and on-screen.
      "Display options" being the operative description. When performing data reduction
      operations, Gen5 uses all the digits (up to 15) regardless of the numeric format applied
      for display. Use the Round(x;y) and Truncate(x;y) functions to control the number of
      digits used in/generated by a calculation.

        Format options:

        Decimal                   Standard, unmodified numeral

        Scientific                A way to write very small or large numbers. Numbers
        Notation                  are separated into two parts, a real number with an
                                  absolute value between 1 and 10 and an order of
                                  magnitude value written as a power of 10. The '10' is
                                  omitted and replaced by the letter E or e, which is
                                  short for exponent.

        Best Fit                  Gen5 determines, based on the size of the display
                                  area, the format, Decimal or Scientific



324 | Chapter 14: Viewing Results



        After selecting the format, define the level of precision for the display of numeric
        results. Select and set the number of Decimal places or Significant digits:

           Example            Decimal places = 3           Significant digits = 3

           0.000123456        0.000                        0.000123

           12.34567           12.345                       12.4

           123456             123456.000                   123456



Modify Data Files
     After data has been retrieved from the reader (or entered manually, or imported from a
     file), Gen5TM permits authorized users to edit or mask measurement values. Gen5
     automatically logs an event in the experiment's Data Audit Trail any time data is changed
     or masked.

           Important! Changing or masking wells may significantly alter or even
             invalidate results.

                Only raw measurement values can be changed. Data sets generated from
                  Data Reduction calculations cannot be changed, only masked.
                When a well is masked, Gen5 excludes its value from further calculations.
                In most views and reports, masked values appear sandwiched between
                  asterisks, e.g. *6879* and edited values are shown in parenthesis, e.g. (6879)


Change a Measurement Value
        After data has been retrieved from the reader, Gen5TM permits authorized users to edit
        or mask measurement values. Gen5 automatically logs an event to the file's Data Audit
        Trail any time values are changed.
          1.   With the experiment open, and the desired plate selected in a multi-plate
               experiment, open the Plate workspace
          2.   In the Plate workspace, select the Matrix view and from the Data drop-down
               list, select the desired data set (it must contain raw measurement values); or in
               Well Zoom view, click the View Data button

          3.        Click the Edit button

           The System Administrator can protect the use of this function. If the
             button is grayed out, you may not be authorized to use it.

          4.   Click on and change the value of one well at time in the grid. Multiple wells
               can be changed in a session.






       5.        To apply the changes, click the OK (green check mark) button. Gen5 will
            recalculate results.
                Click the cancel button to ignore your entries, and restore the original
            values.0.



Mask (Exclude) a Data Point
   Most data views let you mask or ignore one or more data points:
       1.   With the experiment open, and the desired plate selected, open the Plate
            workspace
       2.   In the Plate workspace, select the desired view, Matrix or Graph. Depending on
            the view, click the Data or Curve drop-down list to select a data set. Or go to
            the Well Zoom view, where you can either View Data or View Chart

       3.        In the Matrix/View Data view, click the Mask button. (This is not
            necessary in Curve/Chart view.)

        The System Administrator can restrict the use of the Mask function. If
          the options are grayed out, you may not be authorized to use it.

       4.   Click a well in the matrix or a point in a curve to mask it. (Click again to
            unmask.) Multiple data points can be masked in a session.

       5.        To apply the changes, click the Apply (green check mark) button to
            recalculate results.
                Click the Cancel button to ignore your entries, and restore the original
            values.0.


         In curve views, right click or click & drag for more masking options: you can mask and
      unmask multiple points simultaneously



             Mask and Edit functions are done in a "session." If you change
          the view, e.g. change the Read Index in a kinetic analysis, or close the
          plate view, experiment, or Gen5, without first applying the changes,
          Gen5 prompts you to Apply or Cancel the modifications you've made,
          before it can close the session.



326 | Chapter 14: Viewing Results




Change the Time Format
        For viewing and reporting Kinetic or Well analysis results, you can change the time
        format using Gen5's Edit tool for data views.
        In the Report and Export Builders:




        (Not shown: In Data Views, highlight the item and click Edit.)
        On the Data tab, in the Format column for the data point,




        After defining a Procedure and Data Reduction steps based on a time format:
          1.   Open the Data View, Report Builder, or Export file builder, and locate the
               Matrix, Table or Curve that contains the data you want to modify and click
               Edit or double-click to open the item. (In Report & Export Builders, first
               Add the view to the selected Content box.)
          2.   In the Edit dialog:
                for a Matrix or Table select the Data tab and locate the time format you
                   want to change in the Format column, then, click inside the cell to enable a
                   3-dot button
                for a Curve select the X-Axis tab, locate the Format field under Labels

          3.      Click the 3-dot button in the Format column/field to open the Time Span
               Format selector.
          4.     Fill the checkboxes to select the desired time-format options. 0.






Modify protocol parameters in an experiment:
      After a plate is read, the Procedure cannot be changed. Other changes to the
      experiment are permitted:
       1.   With the experiment open, select an option from the Protocol menu tree, other
            than Procedure. Double-click the element you want to modify, such as Plate
            Layout, Data Reduction, Report, and so on.

        Warning: Making changes to the Protocol elements may have an
          unintended effect that ripples through your protocol. For example,
          deleting or altering a Data Reduction step whose results are used in a
          subsequent step, could invalidate the subsequent step.

       2.   Within the appropriate protocol dialog, make the desired change and click OK
            to recalculate results.0.

        The System Administrator can protect some or all protocol parameters
          from being modified. If you are trying without success to modify these
          parameters, you may not be authorized to do so.

            Gen5 Secure automatically updates the Audit Trail to reflect any changes made.



328 | Chapter 14: Viewing Results




Modify the Matrix View
   You can change the number of decimal places or significant digits expressed and customize
   the font used, among other options.
     There are two ways to access this feature:


   Select Protocol> Data Views, highlight
                                                      In the Matrix tab of the Plate View,
   the desired data set under Matrix in the
   menu tree and click Edit                       select the Data to modify and click the
                                                  3-dot button




             Report and Export Builders offer the same options. Generally, it is more efficient to
         modify the matrix using these approaches, so you see the changes both on-screen and
         in the Report and Export outputs.


  Edit
         Except for custom-made matrix views (Create New Matrix), modification options are
         limited to Format, Font, and Selection

  Format

                                                   Click inside a cell in the Format column
                                                   to enable a 3-dot button, and click on
                                                   the 3-dot button to open the Numeric
                                                   Format dialog.
                                                   You can select the desired Format
                                                   using the drop-down list and set the
                                                   number of Significant digits or
                                                   Decimal places
                                                   Use the Samples window to judge the
                                                   effect of your selections on the
                                                   appearance of the data






Font
        To change the font used to display and report values: click inside a cell in the Font
        column to enable a 3-dot button that leads to the Font dialog. Use this standard
        Windows(R) Font option to make selections.

Title
        Customize the Title of the data set by clicking in the field and typing over the Auto or
        default text. The title appears as a Tool Tip when the mouse is hovered on a data point
        in the Matrix view.

Selection
        Modifying a matrix via Data Views and the Report/Export Builders offers the
        Selections tab. It is most useful in multiple-read experiments, e.g. kinetic, that produce
        multiple results sets. Use the Selections tab to define a range of results sets to include
        in reports and export files.



330 | Chapter 14: Viewing Results




Modify a Graph
     Gen5TM provides tools to change the appearance of a graph. You can display or hide the
     legend and change the title, labels, font, and colors.
     There are two ways to access this feature:


  Select Protocol> Data Views, highlight
                                                      In the Graphs tab of the Plate view,
  the desired curve (under Graph in the
  menu tree) and click Edit                       select the curve to modify and click the
                                                  3-dot button


           The Report Builder offers the same options. Generally, it is more efficient to modify
        the graph using these approaches, so you see the changes both on-screen and in print.


  Layout
     Select the Layout tab to:
             Define a Title for the curve; position the title on the page/screen; and select the
               font
             Display or hide the Legend; and select the font for the legend

  X Axis/Y Axis
     On the X Axis and Y Axis tabs, you can:
             Define a Title or label for the axis; select the font; Show (or hide) Gridlines for
               the axis;
             Change the Scale of the display using Linear (1, 2, 3) or Log (10, 20, 30)
               numbers; Auto applies the method selected when the curve was created in the
               Curve Analysis step of Data Reduction
             Change the numeric Format and Font of the Labels, i.e. the numbers/data
               displayed on each axis. Try out the various options to determine which
               combination works best for your reporting and viewing requirements.


               Click the 3-dot button for Format to change the scientific notation, decimal
            places or significant digits displayed in the view/report/export


  Plots/Curves
        Select the Plots tab to further modify the appearance of the graph. You customize the
        appearance of the error bars and fitting line, for example. (The Curves tab is displayed
        for user-created curves, select a curve and click Edit after to enable these functions):






      Click in a cell in the table to enable a 3-dot button that leads to formatting
     options for the selected item (line, marker, text, or pattern):
      Automatic is the default setting. It is most useful in Well Zooms, when
        more than one well is selected for simultaneous viewing. Gen5 displays a
        different color scheme for each well selected.
      Select Hide (or None) to remove the item from the view.
      Select Custom to modify it. Use the drop-down options to apply different
        colors, symbols, styles and/or line weight.




    Select the Plot tab to turn-off the Text that may be obscuring the details in a
Well Zoom curve: select the table cell containing the offending text, click the
activated 3-dot button. At the Text tab, select Hide



332 | Chapter 14: Viewing Results
