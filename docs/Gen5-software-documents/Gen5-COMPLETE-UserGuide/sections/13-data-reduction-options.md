# Chapter 13: Data Reduction Options

     Gen5's robust and flexible Data Reduction options are described in
     this chapter.


 Setting up Data Reduction ........................................................ 246
 How to use a Runtime Variable in a Formula................................ 248
 Define Transformations............................................................. 249
 Plotting a Curve ....................................................................... 261
    Multiple Curves ................................................................... 282
 Kinetic Analysis ....................................................................... 288
    Well Analysis ...................................................................... 290
 Define Cutofs .......................................................................... 296
 Validation Criteria .................................................................... 301



246 | Chapter 13: Data Reduction Options




Setting up Data Reduction
     Protocol> Data Reduction
        There are several options available for interpreting the results of your experiment.
        Gen5TM automatically creates the most commonly applied data reduction steps (based
        on previously defined Protocol parameters). You can design your own or modify the
        calculations.

Top 6 Things to Know about Data Reduction
         1.   Reductions are StepWiseTM, they can be built one upon another, based on their
              sequence in the Data Reduction dialog: a data set created in a previous step can
              be used in a later transformation, curve, cutoff, validation or well analysis, if
              applicable.
         2.   Gen5 creates four types of data reduction steps automatically:
               When blanks (BLK) are assigned to the plate, Gen5 automatically creates a
                 Blank Subtraction data set. Gen5 subtracts the mean of the blanks from all
                 other wells on the plate.
               A Well Analysis step is created when a multi-read index Read step is
                 defined: Kinetic, Spectrum, Area or Linear Scan. If applicable, blank-
                 subtraction results are used to perform the well analysis.
               A Pathlength-Corrected data set is created when this option is selected in
                 an Absorbance read step.
               The Fluorescence Polarization (FP) transformation is performed
                 automatically when this reading mode is selected in the Read step. If
                 applicable, blank-subtraction results are used to perform the FP reduction.
                 In kinetic experiments, well analysis is based on the FP transformation
                 results.
         3.   Important! Once the Data Reduction dialog is opened and saved, (i.e. OK is
              selected to close it) Gen5-created reductions are no longer added, deleted, or
              changed. Keep this in mind when modifying a protocol or experiment.
         4.   Plate-specific Data Reduction Variables can be collected from users when they
              read the plate so Gen5 can use them in data reduction calculations. First, you
              define the variable in the Runtime Prompts, then, write a formula using the
              variable name as a placeholder. At runtime, when the measurements and
              variables are obtained, Gen5 performs the calculation using the input value.
         5.   Raw data sets used in Data Reduction steps are named according to Gen5's
              Data Set Naming Convention, which is based on the number of Read steps
              defined in the Procedure. When the number of read steps is changed, any
              previously defined Data Reduction steps are voided, because the data set name
              is also changed. When you add or remove a Read step, you must update the
              effected Data Reduction steps.






       6.    In the Data Reduction dialog, you can:0.
              Drag and drop Data Reduction steps to change their sequence order,
              Select a step and right-click to delete it,
              Double click an event to open it for modification or deeper review (or right-
                click and select Edit).


Data Reduction Options

                Transformation

                Curve Analysis

                Well Analysis

                Cutoffs

                Validation

               Fluorescence Polarization


           Gen5 shows an invalid data reduction step by blocking out its icon.
          Changing the Procedure, e.g. reading parameters or sequence of
          events, renaming a Read step or data set, or other changes can
          invalidate a data reduction step. Generally, it is easiest to delete the
          invalid step and recreate it, selecting valid options.



248 | Chapter 13: Data Reduction Options



How to use a Runtime Variable in a Formula
      You can acquire a plate- or assay-specific variable for use in data reduction formulas
      using the Runtime Prompts. When the plate is read, users will be prompted to enter
      a value that will be used in the calculations.
        Follow these steps to write a formula using a Data Reduction Variable:
         1.   Create the Data Reduction Variable in the Runtime Prompts:
                 1.   Select Protocol>Runtime Prompts
                 2.   Enter a Prompt Name for the variable: this is the name of the field users
                      will see in the Plate Reading dialog when they read a plate
                 3.   Set the Prompt Type to Data Reduction Variable
                 4.   Assign it a Variable Name0
         2.   Write the formula: create the applicable Data Reduction Step and include the
              Variable Name in the formula
         3.   Save the protocol and create a new experiment based on it.

         4.       Read the plate. Enter the value for this runtime variable in the Plate
              Reading screen that opens just before the plate is read. Gen5 will calculate the
              formula using the entered value.0.

          In Calibrator-Plate Protocols, Data Reduction Variables created for
            and populated by the calibrator plate(s) can be used in data reduction
            steps defined for the Other Plates. The converse is not true: variables
            created for the Other Plates cannot be applied to a calibrator plate.
            Any variable defined for a calibrator plate can be used to create
            formulas applied to the Other Plates. Variable names must be unique
            in a protocol, they cannot be reused from plate to plate.

          In Multi-Plate Assay Protocols, Gen5 only recognizes the
            variable(s) collected for the first plate (Plate 1). Users will be
            prompted to enter the data reduction variable(s) for every plate, but
            only the data entered for Plate 1 will be used in the calculation(s).






Define Transformations
   Protocol> Data Reductions> Transformations

About Transformations
           In Gen5TM, the Transformation dialog is the workspace to define plate- and well-
           level calculations. If you are familiar with spreadsheets, like Excel, you can write
           formulas in a similar way.

      You can perform calculations using:
            any previously-defined raw data, e.g. measurements obtained from the
              reader
            already-transformed data sets,
            concentrations determined from standard curves,
            well-analysis results
            up to 4 valid data sets

      Gen5's StepWise Data Reduction lets you perform a Transformation on the results of
      any previous data reduction step.
      The sequence of data reduction steps determines the availability of the data sets:
      previous steps provide input for subsequent steps. So you can build a series of
      calculations, defining new calculations to be performed on the results of a previous
      one.
      Well IDs, like blanks (BLK) and standards (STD), etc., must be defined in the plate
      layout before they can be used in a formula. The matrix in the Transformation dialog
      reflects the current Plate Layout

        ????? - This symbol in Transformation results indicates a value could
          not be determined, or an out-of-range or biased value was used in the
          calculation. Check the Protocol Options>Calculation Options
          settings.



250 | Chapter 13: Data Reduction Options



Basic Steps




        In the top left corner of the Transformation dialog:
          1.     Select Data In
          2.     Enter a name for the resulting data set in New Data Set Name
          3.     Enter the formula in the Plate Formula field to apply it to the whole plate (all
                 wells) or
                 de-select Use single formula for all wells and define the Current Formula
                 field for individually selected wells: click in the matrix cell to apply the formula
                 to that well of the plate0.

           Note: When formulas are applied to individual wells you can right
             click and Copy the formula, then Paste it into the Current Formula
             field to see it, reuse it, or modify it. You can also resize the columns to
             view formulas.

For more details about setting up data transformations:
            Selecting Multiple Data Sets on page 251
            Formula Syntax and Examples on page 252
            Apply calculation to entire plate on page 256
            Apply calculation to individual wells on page 256


               Don't forget to update your Report to include your transformations.






Multiple Data Sets
        In the Transformation dialog, click the Select multiple data sets... button:




      Use these controls to select the data sets for the Transformation. Click the radio button
      to enable selection of a data set, and use the drop-down lists to select the content of the
      data set.
         Plate: When multiple plates have been defined for a protocol, you can create a
           data set using other than the default value of Current Plate
         Data In: The drop-down list offers any raw data, or results of previously-
           defined calculations or curves
         Read(s): Kinetic and scanning raw data offers All or the results of a specific
           reading or sampling number to define the data set. Selection is limited in two
           ways:
             If you want to use a combination of All and individual reads, set DS1 to
               All, and the subsequent data sets to the individual reads, otherwise,
               individual read points can be selected for all four data sets
             When more than one kinetic or other multiple-index data set is available
               you can only select All for more than one data set when their read counts
               (indexes) exactly match. Otherwise, individual readings from different data
               sets can be selected.


       When selecting multiple data sets with read indexes, the first data set selected: DS1,
    determines the read index count of the resulting data out: New Data Set produced by the
    transformation.



252 | Chapter 13: Data Reduction Options



 Transformation Formula Syntax and Examples
        Here are the Symbols and Functions that can be used in Transformations, in formulas
        applied to the whole plate or individual wells.

    Symbol                     Description                         Example

    x or X                     Represents the current well
                               value

    Well Coordinates           Represent the value of a            A2 or H12
                               particular well

    Multiple Data Sets         When referencing multiple           DS1.H6 = well H6 of
    (DS#)                      data sets use the DS#. To           data set 1
    <data set>.<well>          identify a specific well within a   DS1.X or DS1 = current
                               data set, use a period to           well of DS1
                               separate the data set and the
                               well coordinate

    <well>.<plate>             When referencing a well             B3.3 = well B3 on Plate
                               coordinate in a multi-plate         3
                               experiment, identify the specific   DS1.H6.2 = well H6 of
                               well and plate using a period       data set 1 on Plate 2

    Well Identifiers           The value of a specific well. The   SPL3
    wellID_ALL                 ID assigned to a specific well,     SPL_ALL
                               including a Conc/Dil index
                               value, if applicable:               SPLC_ALL:3 = the mean
                               <ID><index>:<Conc/Dil               of SPLC at the 3rd conc
                               Index> The last number is the       value
                               Conc/Dil index, not the             STD3.3 = STD3 on Plate
                               concentration/dilution value.       3
                               The well index can be replaced
                               by _ALL for Samples and
                               Sample Controls, which returns
                               the mean of all indexes of the
                               well type. Does not apply to
                               STD, BLK or Assay Controls

    <wellID>:<conc             Use : as a separator to identify    CTL2:3 = the average
    index>                     individual well IDs of a specific   value for all CTL2 at the
                               concentration/dilution level.       third concentration or
                                                                   dilution level

    Data reduction             Represents a value collected        !KitFactor
    variable                   with the Runtime Prompts

    Function Operators         Add +, subtract -, divide /,        CTL3+H5, STD3-25,
                               multiply *, combine ( )             DS1/DS2, SPL_ALL*2,
                                                                   (STD1/STD6)*100






Figures/Scientific       Any numeral, including those        2.45E-08
notation                 expressed with scientific
                         notation



Function             Description                           Example

Mean(<ID>)           Represents the mean of the            Mean(SPL1;SPL2;SPL3)
Mean(x;y;z;...)      specified well identifier or           Note: Gen5 automatically
                     variables; the mean of any set of     uses the mean of all like-
                     variables can be expressed            named wells on the plate

SD(<ID>)             Represents the standard               SD(SPL10)
SD(x;y;z;...)        deviation of the specified well ID    SD(23;75;45)
                     or variables

CV(<ID>)             Represents the coefficient of         CV(CTL2)
CV(x;y;z;...)        variation for the specified well ID   CV(1;2;3)
                     or variables, expressed as a
                     percent

DIL(<ID>) or         Returns the defined dilution or       Dil(CTL3)
Dil(X); CONC(X)      concentration of the specified well   CONC(STD2)
or Conc(<ID>)        ID or current well
                                                           Conc(X)

Round(x;y)           Rounds x to the y number of           Round(X;2)
                     significant digits. x can be any      (X represents the value of
                     valid symbol or expression.           the current well)

Truncate(x;y)        Truncates x to the y number of        Truncate(CTL3;3)
                     significant digits. x can be any
                     valid symbol or expression.

Log(x)               Represents the Log10 function         Log(SPL_ALL)

POW(x;y)             Represents the value of x raised      POW(STD1;2)
                     to the power of y

POW(10;x)            Calculates the Anti-Log of the        POW(10;x)
                     current well

SQRT(x)              Represents the square root of x       SQRT(A1*B1)

MIN(x;y;z;...)       Returns the minimum of the            Min(CV(SPL1);CV(SPL2))
                     defined variables.

MAX(x;y;z;...)       Returns the maximum of the            MAX(A1;B1;C1)
                     defined variables.



254 | Chapter 13: Data Reduction Options



    Functions allow a      (x;y) Any expression that represents a single value, including
    combination of         well identifiers, locations, numerals, a function that results in a
    expressions            single value, can be included in the formula, if it's a valid
                           expression. Functions described with the ellipsis (x;y;z;...) allow
                           up to 10 expressions.




          Well IDs are case sensitive, i.e. they must be entered exactly as they
            are defined in the plate layout. Other symbols and the functions are
            case insensitive.

Formula Examples

     Formula                      Description

     X+(A5+A6)/2                  The result of this formula is the sum of the current well
                                  value and the mean of the A5 and A6 wells.

     DS1/DS2                      This is the ratio calculation of data set 1 and data set 2.

     Log(X/PC)                    The result of this formula will log the ratio of the current
                                  well over the mean of PC (user-defined identifier).

     MAX(A1;A2;A3)-               This formula calculates the difference between the
     MIN(B1;B2;B3)                maximum value of A1, A2, A3 and minimum value of B1,
                                  B2, B3.

     CTRL1-3*SD(CTRL1)            The result of this formula is the mean of the wells
                                  containing the identifier CTRL1 minus three Standard
                                  Deviations of these wells. It is the equivalent of
                                  MEAN(CTRL1)-3*SD(CTRL1)

     X*Dil(X)                     The result of this formula is the current well value times
                                  its dilution factor

     ((SPL4-BLK)/(SPLC4-          This formula can be used for toxicology assays, in this
     BLK))*100                    example to calculate the toxicity percentage of SPL4.



More on Min/Max
      The MIN/MAX calculations are limited to 10 arguments, but by combining them you
      can apply up to 100 arguments:
               1 level: MIN(A1;B2;C3;D4;E5;F6;H7;A8;B9;C10) works for 2 to 10 arguments
               2 levels:
                 MIN(MIN(A1;B2;C3;D4;E5;F6;H7;A8;B9;C10);MIN(F1;G2;H3;A4;B5;C6;D7;E
                 8;F9;H10);...) works for up to 100 arguments if you use 10 MIN statements
                 inside a higher level one.






          Note: you cannot use Min/Max for one Well identifier, like Min(STD1)
            or Max(NC). You must use the well locations to determine the min and
            max of a well ID's replicates.
            For example: If you use "MIN(NC;POS)", this translates as
            "MIN(MEAN(NC);MEAN(POS))" and does not return the value that
            corresponds to the minimum value of all wells where you either put NC
            or POS. It returns either MEAN(NC) or MEAN(POS), whichever is lower.

Round or Truncate to control results
      While Gen5 provides a way to control the number of significant digits or decimal
      places to display in reports and on-screen, when performing data reduction operations,
      Gen5 uses all the digits (up to 15) regardless of the numeric format applied for display.
      Use the Round(x;y) and Truncate(x;y) functions to control the number of digits used in
      and/or generated by a calculation.


Adding and Selecting Data Sets
     Protocol> Data Reduction> Transformation
        Gen5TM provides enormous flexibility in designing data reductions by letting you build
        up a series of data sets. The variables or data sets for your calculations can be raw data
        or the results of a previously-defined Data Reduction step.




              When one or no data sets selected




              Multiple data sets already selected

        The Transformation dialog changes when multiple Data In data sets have been
        selected, as demonstrated above. Initially, the dialog offers the Select multiple data
        sets button. Use the drop-down list to select one data set. Click the button to select
        multiple data sets.
        When multiple data sets have been selected, the selected data sets (DS1, DS2, up to 4)
        are displayed with a three-dot button.



256 | Chapter 13: Data Reduction Options



           Both buttons lead to the Multiple Data Sets dialog, where you can select from raw
        data or results data from previously defined transformations, well analysis formulas
        and curves.

Apply calculation to entire plate
       Select Protocol> Data Reduction> Transformation and retain the default settings
       to apply a formula to all the wells of the plate:




        In the Formula section of the Transformation dialog, affirm with a check mark "Use
        single formula for all wells."
     In the Plate Formula field, enter the calculation formula to apply to all wells.

Apply calculation to individual wells
       Select Protocol> Data Reduction> Transformation and de-select "Use single
       formula for all wells." This changes the input-field label from Plate Formula to
       Current Formula.
          1.   First, de-select Use single formula for all wells by clicking the checkbox to
               remove the check mark.
               The formula field label changes to Current Formula and additional auto-entry
               options are enabled:
                Current Formula, selected by default, refers to the formula entered in the
                  field
                Difference Between Columns
                Difference Between Rows
          2.   In the Current Formula field, enter a formula to apply and then select (click
               in) one or more wells to apply that formula to them.0.


 Helpful Hints:
            Right click a well or field for tools: Copy, Paste, Cut, Undo
            Use the Undo button (which retains 10 past actions) to reverse an action
            Resize the window and/or the grid's columns to see the formula written to a
              well; (the formula is truncated when it is too long to display):
                Hover the mouse between two columns to engage             (the resize tool), click
                  and drag to the desired column width
                Resize the window using standard Windows(R) tools: click and drag the two-
                  headed arrow icon at the window's corners or edges






            Reference specific wells in a formula: often, after creating a data set based on
              individual-well formulas, it is necessary to reference the specific well or wells
              in a subsequent transformation using that data set.


Correcting a formula
       Use the right-click pop-up menu if you need to make small corrections to a previously-
       applied formula:
          1.   Right click as you're highlighting or selecting the well to be fixed
          2.   From the pop-up menu select Copy
          3.   Paste the formula in the Current Formula field, with a right click or Ctrl+V
          4.   Make the needed changes to the formula
          5.   Apply the revised formula to the desired cell with a regular left click.0.

Individual-Well Formula Example 1
        Here's an example of the need to reference a specific well in a transformation formula.
        An assay kit requires subtracting the average of the "non-specific binding" wells (NSB)
        from the "maximum binding" wells (MB) to determine the corrected maximum
        binding, which is used in a subsequent transformation.
        The wells to be referenced are assigned to the first column of the plate layout:

                      1

          A           BLK

          B           BLK

          C           NSB

          D           NSB

          E           MB

          F           MB

          G           MB

          H           SPL1

     Transformation 1: MB - NSB = DS1 (data set 1). This formula can be applied to the whole
     plate, even though only the specifically referenced wells will be affected by it. Viewing the
     output data set shows the results, the corrected maximum binding, are assigned only to
     the applicable wells: C1, D1, E1, F1, G1.
     Transformation 2: X-NSB/DS1.C1*100 can be applied to the whole plate or individually to
     the sample wells. Notice the reference to well C1 of the data set (DS1), this could have been
     any of the relevant wells, i.e. referencing F1 would also work.



258 | Chapter 13: Data Reduction Options



How to perform Dual-Wavelength Subtraction
        A common way to improve the accuracy of your results is to read the plate at two
        wavelengths and perform a dual-wavelength subtraction data reduction. Here are
        step-by-step instructions for endpoint and kinetic (multi-index) reads:

Endpoint Analysis
        First define the Read step with two wavelengths:
         1.   Select Protocol>Procedure and add steps as needed, e.g. Set Temperature
         2.   Click Read and select 2 wavelengths
         3.   Define the Plate Layout of samples, blanks, standards, etc.

         4.       Select Protocol>Data Reduction and click Transformation

         5.                         Gen5 opens the Multiple Data Set dialog
         6.      Select the button for DS2

         7.      Use the drop-down list to select Data In for DS1 and DS2, the first read
              measurement for DS1 and the second read data set for DS2. Click OK when
              you're done.
         8.   In the Transformation dialog, enter a name for the New Data Set Name in
              the text field, e.g. Delta OD
         9.   Define the dual wavelength subtraction formula in the Plate Formula text
              field, e.g. DS1-DS20.
        Now you can use the results of this calculation, Delta OD, in subsequent data
        reduction steps, if desired.

Kinetic Analysis




        First define the Read step with a kinetic loop and two wavelengths:






        1.   Select Protocol>Procedure and add a Kinetic loop and other steps as
             needed, e.g. Set Temperature
        2.   Click Read and select 2 wavelengths
        3.   Define the Plate Layout of samples, blanks, standards, etc.

        4.      Select Protocol>Data Reduction. Gen5 opens the StepWiseTM Data
             Reductions dialog
        5.   Highlight the first Well Analysis step and click Transformation.
             StepWise Data Reductions let us use the results from all previous calculations
             in subsequent steps. By making the dual-wavelength subtraction the first step
             we can use the results in all other steps. (Later, we can modify the Gen5-
             generated Well Analysis steps to use the dual-wavelength results.)

        6.                        Gen5 opens the Multiple Data Set dialog
        7.     Select the button for DS2

        8.     Use the drop-down list to select Data In for DS1 and DS2, the first read
             measurement for DS1 and the second read data set for DS2.

        9.      Set the Read(s) for both DS1 and DS2 to All. Click OK when you're
             done.
       10. In the Transformation dialog, enter a name for the New Data Set Name in
           the text field, e.g. Delta OD
       11. Define the dual wavelength subtraction formula in the Plate Formula text
           field, e.g. DS1-DS20.
       Now you can use the results of this calculation, Delta OD, in the Well Analysis data
       reduction steps, if desired. In the StepWise Data Reductions dialog, to modify the
       Gen5 generated steps, double click a step to open it in edit mode, and change the
       Data In to Delta OD. Or, create a new well analysis step.


Subtracting Blank Wells
       When there is one or more Blank defined in the Plate Layout, Gen5TM automatically
       creates a Transformation or "blanked" data set.

         Gen5 uses the "blank" (blank-subtracted) data sets in any subsequent
           system-generated data reduction steps, like Pathlength Correction and
           Well Analysis calculations in kinetic experiments.

  For single- and multi-wavelength reads:
       For each raw data set, Gen5:
        1.   Calculates the mean of the raw measurement values in wells identified as blank
        2.   Subtracts the mean from the raw measurement value in each well on the plate
             to generate a "Blank" data set containing each well's measurement result after
             blank well subtraction



260 | Chapter 13: Data Reduction Options



         3.   Displays the Blank well Mean in the Statistics data view.0.

  For Specific Read Types:
        Within any protocol, if one or more wells are defined as 'Blank' in the Plate Layout,
        Gen5 automatically generates Blank-Wells Subtraction data sets for each wavelength:
           Endpoint read: For each wavelength defined in the protocol, the average of the
             blank well(s) is subtracted from every well on the plate
           Kinetic analysis: For each wavelength defined in the protocol, within each
             kinetic read, the average of the blank wells is subtracted from every well on the
             plate
           Spectrum scan: A blank average is calculated for each wavelength in the
             spectrum reading range. The blank average for each wavelength is then
             subtracted from the absorbance read at the corresponding wavelength in each
             well
           Linear and Area scan: For each wavelength defined in the protocol, within each
             read index, the average of the blank wells is subtracted from every well on the
             plate







Plotting a Curve
  Data Reduction> Curve Analysis
      Select Curve Analysis in the Data Reduction dialog to create a standard or titer curve
      for your experiment. Other than kinetic curves, there are two scenarios for using a
      curve to determine the concentration of samples:
      Gen5TM provides two general ways to use its curve plotting feature:
         Standards, Controls, and/or Samples, for which concentrations or dilutions
           have been defined, are read on one or more microplates, along with the
           test/unknown samples.
         A Multi-Plate Calibration Protocol defines one plate as the calibrator
           (containing the Standards or Controls), and plots a curve against the calibrator
           plate to determine the concentration of test/unknown samples on one or more
           other plates. Refer to the Multi-Plate Protocols chapter for details.


            Gen5 lets you generate multiple standard curves (up to 6) from one plate


 Prerequisites for generating a Curve:
       1.    Define Standards (STDn), Controls (Assay or Sample), and/or Sample
             Dilutions (SPL) in the Plate Layout with corresponding concentrations or
             dilutions (Learn about Multiple Standards on page 282)
       2.    Define the minimum number of standards/dilutions for the desired Curve Fit
             (Minimum STDs on page 269)
       3.    Create at least one read step in the Procedure. 0.

 To View a Curve:
        After you've defined the Curve Analysis, and acquired the data, e.g. read the plate,
        open the Plate View, and select the Graph tab.
              Curve Fitting Results: The default table displays the parameters used to
                plot the curve including the Curve Formula, its elements and the R2
                coefficient (for all curve fits except point-to-point).
              Curve Fitting Details: Select the Details table to view best-fit results for
                each parameter, including standard error (SE) and 95% confidence
                intervals.
              Curve Interpolations: When one has been defined for the curve, Gen5
                builds a table listing the interpolation formula and the X and Y values for
                that point on the curve.



262 | Chapter 13: Data Reduction Options



  To Output a Curve:
          Gen5 provides several ways to print a curve:

                     Click Quick Export to instantly send the current curve to Excel
               Add it to the Content in Report Builder
               Right-click to copy or save it as an image for use in a word-processor
                 application
               Export it to Excel(R) using Power Export


How to Create a Standard Curve
        Gen5 lets you create one or more standard or calibration curves for determining the
        concentration of samples:
         1.   Select File> New Protocol
         2.   Select Procedure and define the Read step (and any other required steps)
         3.   Select Plate Layout:
               Define the concentrations of the Standards (see below)
               Assign the location of the standards, samples, and controls and blanks (if
                 any) on the plate
         4.   Select Data Reduction> Curve Analysis
               Gen5 may have generated a "corrected" data set: if you assigned blanks to
                 the plate or selected Pathlength Correction in the Read step, you'll want to
                 select these data sets for Data In for the Y-Axis Data when plotting the
                 curve
               For Kinetic reads, Gen5 creates a Well Analysis step. The default kinetic
                 well analysis is "Mean V," which can be easily changed to any of the wells
                 analysis options. The output of the well analysis step is typically used as the
                 Data In for the Y-Axis in quantitative assays.

         5.        On the Data In tab, use the drop-down to select the Y-Axis Data
         6.   On the Curve Fit tab, choose a curve fit method
         7.   Other options and requirements when defining multiple curves:
               Curve Name: replace the default "Curve" with a more meaningful or unique
                 name
               On the Data Out tab, replace the default "Conc" for the Data Set Name with
                 a more meaningful or unique name
               On the Data Out tab, define interpolations to plot on the curve
         8.   Define the reporting or export requirements and Save the protocol. Now,
              you're ready to run an experiment: File> New Experiment to read the plate
              and generate the curve.0.






Define Standards

      In the Plate Layout dialog:
       1.    Set the Type to Standard
       2.    Gen5 sets the ID to STD:
              You can change the abbreviation using the 3-dot button
              Use the drop-down list to define multiple standards.
       3.    Click the 3-dot button at the Conc. field to enter the expected concentrations for
             the Standards:
              In ascending or descending order, enter the values in the consecutively-
                numbered fields: STD1, STD2... For a shortcut, select one of the two Auto
                entry tools


            Be sure to assign the Minimum Number of Standards: see page 269


       4.    Assign the location of the Standards on the plate, in the same manner as
             assigning unknown Samples.0.



264 | Chapter 13: Data Reduction Options



Curve Fit
     Data Reduction> Curve Analysis> Curve Fit tab




         Curve Name: assign each curve a unique alpha-numeric name that does not include
         spaces or symbols used as mathematical operators (+, *, -, /). Characters must be
         alphabetic, numeric, or the underscore.
     Select the Curve Fit Method that will best model the data for your experiment. The
     parameters selected for Curve Fit can be modified at any time without invalidating the
     data. You may want to experiment with the options to assess the best method for your
     experiment.

           If the options on the Curve Fit tab are disabled (grayed out), Data In
             is set to "Use Curve from Calibrator Plate," which is only applicable to
             Calibration Plate Protocols.

         Gen5 offers several curve fit methods and lots of flexibility in defining or influencing
         the best-fit calculation. All the options are intended to fit data to a model that defines Y
         as a function of X, i.e. X values must be known. Gen5's StepWiseTM Data Reduction
         feature lets you transform the data prior to fitting the curve, if necessary. And, you can
         apply constraints to the parameters or weighting to the sum-of-squares after viewing
         the curve, as well as before it is plotted.

Linear Regression
       Linear Regression is a simple, best-fit, straight line. See page 265.
         Polynomial Regression is an extension of the Linear Regression equation. See page 268






Non-Linear Regression
      4 Parameter is characterized by a symmetrical sigmoidal plot that eventually becomes
      asymptotic to the upper and lower standard values. See page 266.
         5 Parameter is similar to 4P but it is better able to model data that is asymmetrical at
         the upper and lower asymptotes. See page 267.
         Logit-Log is a restricted form of 4P that has been offered in BioTek readers' onboard
         data reduction (PDR) software and KCjuniorTM. See page 268.

Other
         Point-to-Point follows each standard point with no averaging of the values to smooth
         the curve. Minimally two standards are required.
         Spline with Smoothing is a curve defined piecewise by polynomials, joining a set of
         data points by a series of straight lines, which is then smoothed by the Smoothing
         Factor.
         The curve will appear smoother as the Smoothing Factor is increased. The zero factor
         will force the curve fit through all data points.
         This curve is most useful when you have a very large data set. Minimally 4 standards
         are required to plot a Spline curve.


Linear Regression
         Linear regression: y = ax + b (or Y = intercept + slope x X).
           y represents unknown response
           x represents theoretical concentration (in this context should we be using the word
           expected?)
           a represents the slope of the linear regression
           b represents the intercept to the y axis
         The linear regression fit uses the least squares technique. The better the quality of
           the fit the more the absolute value of R tends to 1. This type of curve fitting
           technique can be used when you think the data will fall in a predictable linear
           pattern. It may be necessary to transform the x and/or y components using
           Logarithmic axes.
         You can enable or disable Use average of replicates in the curve calculation. By
           default, the mean of replicates is used. This is recommended when the replicates
           are not independent. Contrarily, when the source of experimental errors is the
           same for all replicates, you should consider plotting each point separately.
         You can apply Parameter Constraints, but generally, linear regression determines
           the best-fit curve without constraints.



266 | Chapter 13: Data Reduction Options



Nonlinear Regressions are Iterative
        Nonlinear regression is performed in a series of steps, each adjusting the parameters to
        improve the goodness-of-fit.
        Here are the steps that every nonlinear regression program follows:
         1.   Start with an initial estimated value for each variable in the equation.
         2.   Generate the curve defined by the initial values. Calculate the sum-of-squares
              (the sum of the squares of the vertical distances of the points from the curve).
         3.   Adjust the variables to make the curve come closer to the data points. There are
              several algorithms for adjusting the variables. Gen5 uses the Newton-Rapshon
              method.


         4.   Adjust the variables again so that the curve comes even closer to the points.
         5.   Keep adjusting the variables until the adjustments make virtually no difference
              in the sum-of-squares.
         6.   Report the best-fit results. The precise values you obtain will depend in part on
              the initial values chosen in step 1 and the stopping criteria of step 5. This means
              that repeat analyses of the same data will not always give exactly the same
              results.


4 Parameter Curve
        The four parameters are left asymptote, right asymptote, slope, and the value at the
        inflection point. Gen5 performs an iterative series of calculations (using the Newton-
        Raphson algorithm) to determine the best curve fit - the least squares method to
        minimize the residual error. The iterations stop when no further improvement to ERR
        is detected. You can refine the calculation using Parameter Constraints and/or
        Weighting.
          4 Parameter logistic fit:




          a = (theoretical) response at concentration = 0
          b = measure of slope of curve at its inflection point
          c = value of x at inflection point
          d = (theoretical) response at infinite concentration
          x = concentration
          y = response (OD)
        The minimum number of standards is 4.

          IC50/EC50: typically, the c parameter is equal to the IC50 or EC50 value






     It is recommended that:
        at least one standard is not far from each asymptote
        at least 2 standards fall within the linear area of the curve, one either side of the
          inflection point


      You can plot the IC50/EC50 value on the 4P curve by updating Gen5's Curve
    Analysis step before reporting the results.



5 Parameter Curve
     As you would expect, the five parameter curve is nearly identical to the 4 Parameter
     except for an additional parameter e (which is equal to 1 in a 4P curve and makes the
     curve symmetrical). With e, the 5P curve fit is better able to model asymmetric
     experiment results. You can refine the calculation using Parameter Constraints and/or
     Weighting. Gen5 ends the iterative calculations when no further improvement to ERR
     is detected.

       This five-parameter logistic is also called the Richards equation.




       a = minimal curve asymptote; (theoretical) response at concentration = 0
       b = measure of slope of curve at its inflection point
       c = value of x at inflection point
       d = maximal curve asymptote; (theoretical) response at infinite concentration
       e = quantifies the asymmetry
       x = concentration
       y = response (OD)
       The minimum number of standards is 5.
     It is recommended that:
        at least one standard is not far from each asymptote
        at least 3 standards fall within the linear area of the curve, one at the inflection
          point and one on either side of it.


       You can calculate and plot the IC50/EC50 value on the 5P curve by manually
    performing the calculation and then updating Gen5's Curve Analysis step before
    reporting the results.



268 | Chapter 13: Data Reduction Options



Polynomial Regression Curve Fit
        The calculation of the Polynomial fit parameters is based on a least squares method
        that results in a series of equations. Then, a Gaussian Elimination algorithm is applied
        to the augmented matrix of the series to calculate the parameters.




        n represents the Degree of the polynomial regression.
           The Degree must be less than or equal to the number of standards minus 1. If
             this condition is not met, Gen5 automatically reduces the degree of the
             polynomial to the number of defined standards having different X values
             minus one.
           The unknown concentrations are calculated by using an approximate
             calculation method, linear interpolation between 1000 points evenly spaced on
             the X axis.
           When a Y Axis Intercept value is defined it determines the coefficient a of the
             polynomial equation:
             y = g*x6 + f*x5 + e*x4 + d*x3 + c*x2 + b*x + a
             This is equivalent to defining an advanced parameter constraint with a fixed.


Logit-Log Curve
        Gen5's Logit-Log curve is identical to the 4 Parameter Curve except it is does not
        perform an iterative series of calculations to minimize residual error. Instead, the
        asymptotes of the curve (parameters a and d) are determined from experimental data
        (y values). And, the inner portion of the curve (b and c) is solved using a logit-log
        linear regression. This prohibits the application of Parameter Constraints and
        Weighting.

          Gen5's logit-log algorithm is derived from BioTek readers' onboard
            data reduction (PDR) software and KCjuniorTM.







Curve Fit: Minimum Number of Standards
      Here are the minimum number of standards that must be defined for each Curve Fit
      Method:

            Curve Fit Method         Minimum STDs

            Linear Regression        2

            4-Parameter              4

            5-Parameter              5

            Logit-Log                4

            Point-to-Point           2

            Spline with Smoothing 4

            Polynomial Regression Degree +1

            Degree: 2                3

            Degree: 3                4

            Degree: 4                5

            Degree: 5                6

            Degree: 6                7



More Curve Fit Controls:

Axis Transformation:
      In the bottom left corner of the Curve Fit tab, you can alter the default Transformation
      for the X and Y axes used to calculate the curve.
         None - the default value, retains the Formula displayed at the bottom of the
           dialog to calculate the curve (no transformation is applied to the selected data,
           X or Y.)
         Log (logarithmic) - alters the formula used to calculate the curve by applying
           log10 (10x) to the selected data, X or Y. Any change is reflected in the Formula
           displayed at the bottom of the screen. Log transformations fail when the data
           includes a negative or null value. And, they are not applicable to the Nonlinear
           Regression curves.

Y Axis Data:
        Use average of replicates
      This check box offers a Yes or No option to calculate and apply the average of
      replicates when plotting the curve or to calculate each data point individually. The



270 | Chapter 13: Data Reduction Options



        default setting is yes, to average the replicates, but some types of assays consider
        results to be more accurate when each sample is plotted separately. This option is
        disabled for Point-to-Point and Spline curves.

           Weighting: Use the drop-down list to apply a weighting factor to the curve fit
        formula. (See below for more info.)

              Extrapolation Factor: The extrapolation factor range must be between 1 and 3.
        (See below for more info.)

Parameter Constraints:
           None (Estimate All)
           Y Axis Intercept is limited to Linear and Polynomial Regression fit methods.
             This option forces the curve to intercept the Y axis at the value you input. See
             page Error! Bookmark not defined..

           Advanced        : Click the 3-dot button to define constraints for the curve. See
             page 272.


Weighting in a Curve Fit
        Gen5 offers three options for weighting the curve fit to normalize or minimize-the-
        effect of an uneven distribution of data points from the curve. Select the most
        appropriate option for your experimental data:
        1/Y - Poisson Weighting
        This weighting option is available to refine data that follows a Poisson distribution.
        Where the standard deviation among the replicates is almost equal to the square root
        of their mean.




        1/Y2 - Relative Weighting
        When you expect (or discover) the average distance of the points from the curve to
        increase as Y increases, you can use this weighting option to minimize the sum-of-the-
        square of the relative distances. Relative weighting can ensure that all points have an
        equal influence on goodness-of-fit.




        1/Std Dev Y2 - Reciprocal-Variance Weighting






      When you have a large range of data values, variable error in the data or a relatively
      large error in the data you have good reason to consider applying a weight to each
      data point. This method of "weighting by observed variability" assumes that the mean
      of replicates with a large standard deviation (std dev) is less accurate than the mean of
      replicates with a small std dev. This is not always true.
      This method is only reliable when you have a large number of replicates.




        The setting: Protocol> Protocol Options> Calculation Options>
          Standard Deviation Weighting N-1 or N is used to determine SD
          prior to its use in this weighting scheme.

        At times Gen5 may not be able to calculate one or more weights.
          Calculation Warning messages will alert you to the situation and
          describe the remedy Gen5 implemented, e.g. the highest valid weight
          was used


Extrapolation Factor in Curve Fitting
      For all curves except Spline and Point-to-Point, you must define an Extrapolation
      Factor in the Curve Fit tab or use the default setting: 1.1. The Extrapolation Factor must
      be between 1-3.
      Using a factor of 1 eliminates the extrapolation, using the upper and lower Standards
      as the limits for concentration/dilution interpretation. An Extrapolation Factor >1 lets
      you extend the upper and lower limits of the calculation.
         Example: Assuming a linear X axis, we wish to extend the upper and lower
           limit by 20%. The lower limit denoted by the first standard is 50 units. The
           upper limit denoted by the last standard is 150 units. The dynamic range
           therefore is 150-50 = 100 units. Imposing the 20% extension means that the new
           range will be: 100 x 1.2 = 120 units. This represents an increase in the dynamic
           range of 10 units at the lower limit and 10 units at the upper limit. Therefore
           the new lower limit will be 50-10 = 40 units. The new upper limit will be 150 +
           10 = 160 units.

        Important: Exercise caution when using extrapolation (Factor >1), as
          the implied assumption is that the relationship of the x and y variables
          is valid outside the range defined by the standards. This type of
          extrapolation should only be applied when prior knowledge of the
          relationship is known. Typically this feature is used in assays where
          linear relationships are known. Inappropriate use of the
          Extrapolation Factor may invalidate results generated from
          data falling into the extrapolation zone.



272 | Chapter 13: Data Reduction Options



          FYI: Gen5 calculates the values that fall into the new limits. Those
            that fall outside these limits will be assigned > than or < than,
            respectively. Negative concentrations shall not be reported for any (y)
            value through extrapolation. If a value intersects the curve below 0 on
            the x-axis, Gen5 shall report a concentration of <0 for the well.


Advanced Parameter Constraints
           Gen5 lets you apply one of two types of constraint on your curve parameters to
        produce a more informative curve. (Detailed information about parameters is provided
        below.)

Select a constraint for a parameter:
         1.   Click in the Mode field of a parameter to enable a drop-down list to select:
               Start from: is offered for the nonlinear regressions that use an iterative
                 calculation process to determine the best fit. For 4P and 5P curve fits you
                 can tell Gen5 to start the iteration process with a given value.
               Fixed: lets you assign a fixed parameter value for Gen5 to use in the
                 calculation. When you fix certain parameter values Gen5 will use them to
                 determine the best-fit values for the other parameters.
               Estimate: does not apply a constraint. It lets the curve fit determine the
                 parameter value.
         2.   Enter a Start From or Fixed value in the Value field when applicable. 0.

 Helpful Information
           Constraints can be useful when you have not collected sufficient data to map
             all the parameters in your model and you know or expect a parameter to equal
             a certain value.
           4P and 5P regressions require that B, C, and E parameters are positive (non-
             negative) integers. Gen5 prevents input of a negative or null value for these
             parameters with an error message.
           For Linear and Polynomial Regressions, fixing the B or A parameters
             (respectively) to 0 is similar to setting the Y Axis Intercept to 0
           Constraints can be added or modified at any time, before or after the data has
             been collected. When the regression calculation using initial, non-constrained
             values generates a curve that is far from the data, you may be able to generate a
             better fit using a Start From or Fixed constraint.






About Curve Parameters and Values




         Depending on the curve fit method, Gen5 calculates and reports the values for these
         parameters. They can also be used in a Validation formula to test the results of your
         experiment.

Fitting Parameters
        The coefficients used in the equation to calculate the curve are the fitting parameters,
        potentially: A, B, C, D, E, F, G. These values can be constrained or determined by the
        curve fit. Gen5 reports SE and 95% CI for each parameter, except when Parameter
        Constraints have given them fixed values.
         For example, A, B, C, D are the 4 parameters in the 4P curve formula:




Goodness of Fit
         R2 - Coefficient of Determination
         The value R2 quantifies goodness of fit. The coefficient of determination of the
         regression ranges from 0.0 -1.0. It is computed by comparing the sum-of-the-squares
         distances from the best-fit curve and from a model defined by the null hypothesis, e.g.
         horizontal line through the origin.
                When R2 = 0.0 the curve does not come close to the data. Knowing X does
                  not help you predict Y.
                When R2 = 1.0 all points lie exactly on the curve with no scatter. If you know
                  X you can calculate Y exactly.



274 | Chapter 13: Data Reduction Options



        R2 is one criterion for determining if your curve fit is reasonable. Review the other
        Curve Data, like confidence intervals, to confirm the value of a high R2.


        Standard Error (SE)
        Gen5 constructs a "Hessian Matrix", evaluates the WSS and DoF to calculate the
        asymptotic Standard Error of Estimate of each parameter. A low Standard Error
        indicates one or more of these conditions:
               the curve fit models the data well
               lots of data points
               less scattered data
               narrow confidence intervals

          SE is not reported for fixed parameters.

        95% Confidence Interval: Min and Max
        Review the 95% CI range for each parameter to evaluate the curve's goodness-of-fit. A
        narrow range assures you of a true best fit, but a wide range signals a weakness in the
        experiment or in the model selected to fit the data.
        If you plotted the minimum and maximum CI values that Gen5 reports for each
        parameter it would produce a confidence band on equal sides of the curve. This
        standard statistics calculation tells you, with 95% certainty, the best-fit curve falls
        within the confidence band.
        See Calculating the Confidence Interval using t-distribution on page 276.

          SE and 95% CI are not reported for fixed parameters.

General Metrics
        R - Correlation Coefficient
        Gen5 calculates R by taking the square root of the coefficient of determination: R2.
        The correlation coefficient ranges from -1 to 1. A value of 1 shows that a linear
        equation describes the relationship perfectly and positively, with all data points lying
        on the same line and with Y increasing with X. A score of -1 shows that all data points
        lie on a single line but that Y increases as X decreases. A value of 0 shows that a linear
        model is inappropriate - that there is no linear relationship between the variables.


        Err - Error
        ERR, also known as the "root mean squared error" (RMSE), is the difference between
        the actual measurements and the values predicted by the model. It can be used to
        determine whether the model fits the data or not.






      SS - Sum of Squares
      The sum of the squares of the vertical distances of the points from the curve. It is useful
      when comparing curve fits. The less scattered the data the smaller the SS and Std Err.
      When weighting is applied to minimize the relative distance squared, the WSS is used
      to assess goodness-of-fit.



Covariance Metrics
      Degrees of freedom (DF)

        DF = p - n
        where p is the number of data points
        and n is the number of parameters


      t-Distribution (T)
        t-distribution is a statistic whose values are given by:
        t = [ x - `i> ] / [ s / sqrt( n ) ]
        where x is the sample mean, `i is the population mean, s is the standard deviation
        of the sample, n is the sample size, and t is the t score.
        See Calculating the Confidence Interval using t-distribution on page 276.


      Weighted Sum of Squares (WSS)
        When you apply a weighting factor to the curve, Gen5 calculates the weighted sum
        of squares (WSS), then uses it to determine the SE for a parameter ak:




        where wi is the weight of (xi,yi)
        and p is the number of data points
        and n is the number of parameters

Interpolations
        Gen5 reports the user-defined interpolations Y Formula and the values it produces
        for X and Y.



276 | Chapter 13: Data Reduction Options



Calculating the 95% Confidence Interval using t-Distribution
        The 95% Confidence interval for a parameter ak is calculated with the following
        formula:



        Where t0.025,df is the 97.5th percentile of the Student t distribution, given in the following
        Upper Tail Probability table:

        Degrees of           Pr(T > t)              Degrees of           Pr(T > t)
        Freedom                                     Freedom
         1                  12.706                31                     2.040
         2                  4.303                 32                     2.037
         3                  3.182                 33                     2.035
         4                  2.776                 34                     2.032
         5                  2.571                 35                     2.030
         6                  2.447                 36                     2.028
         7                  2.365                 37                     2.026
         8                  2.306                 38                     2.024
         9                  2.262                 39                     2.023
         10                 2.228                 40                     2.021
         11                 2.201                 41                     2.020
         12                 2.179                 42                     2.018
         13                 2.160                 43                     2.017
         14                 2.145                 44                     2.015
         15                 2.131                 45                     2.014
         16                 2.120                 46                     2.013
         17                 2.110                 47                     2.012
         18                 2.101                 48                     2.011
         19                 2.093                 49                     2.010
         20                 2.086                 50 to 59               2.009
         21                 2.080                 60 to 69               2.000
         22                 2.074                 70 to 79               1.994
         23                 2.069                 80 to 89               1.990
         24                 2.064                 90 to 99               1.987
         25                 2.060                 100 to 119             1.984






      Degrees of          Pr(T > t)             Degrees of              Pr(T > t)
      Freedom                                   Freedom
      26                  2.056                120 to 139               1.980
      27                  2.052                140 to 179               1.977
      28                  2.048                180 to 199               1.973
      29                  2.045                200 to 499               1.972
      30                  2.042                500 to 999               1.965
                                                1000 and greater        1.962



Data In for Curve Analysis
   Data Reduction> Curve Analysis> Data In tab




Generate Curve from Current Plate
      A prerequisite for this option is defining in the Plate Layout:
         Standards, Controls, or Dilution Samples
           and
         Concentrations or Dilutions for the standards, controls or samples



278 | Chapter 13: Data Reduction Options



        In each of the three fields, use the drop-down options to select the parameters for the
        curve:
           Well ID is the Standards, Controls or Dilution Samples to plot on the X axis
           for SPL (samples) and SPLC (sample controls), select All or one ID (see page
             283)
           X Data is the source for the values to plot on the X-axis, by default it is set to
             use the map of the selected Well IDs <Plate Layout>
           Y Data is the source for the values to plot on the Y-axis

Use Curve from Calibrator Plate
        This option only applies to Other Plates in a Calibrator Plate Protocol described in the
        Multi-Plate Protocol chapter


Data Out for Curve Analysis
     Data Reduction> Curve Analysis> Data Out tab
        The data sets created here will be available for viewing, reporting, and exporting. You
        may also be able to use them to perform additional data reductions.




  Options Grayed Out?
          Data Out options are only available when the curve is plotted for standards,
          controls or samples with Concentration values (not Dilution values).






  For Calibrator-Plate Protocols Only

            Y-Data: Select the data set to use for plotting the curve, based on the standard
         curve from the Calibrator Plate.

  Concentrations
         Gen5TM lets you define multiple curves for an experiment or protocol, the only
         requirement is defining a unique name for each one in the Data Set Name and
         Curve Name fields.

  Calculate Concentration x Dilution
         If sample dilutions have been defined for this protocol in the Plate Layout, you can
         use this feature to perform the common Titer Curve requirement of calculating the
         actual concentration of diluted samples. You must define a unique name, Data Set
         Name, for each data output generated based on a different curve.

  Interpolations
         In the Interpolations table, you can enter up to 20 Y-Axis values or formulas to
         view and report the results. Well IDs (that have been previously) defined in the
         Plate Layout can be used. Review the Formula Syntax for Interpolations. Gen5
         plots the interpolations in the generated curve if possible, Example.


Interpolation Formula Syntax

   Symbol/Function Definition                                 Example
            -            Subtraction or negation              BLK-0.010
            /            Division                             CTL1/CTL2
            *            Multiplication                       STD1*0.10
           ()            Represents inclusion                 (CTL1/CTL2)*100
     Numeric value       Represents y value                   0.500, 54000
   Well coordinates      The location of a specific well      A1/B1
        Well ID          The value of a specific well. The    STD3
        Well_All         ID assigned to a specific well,      CTL1:2
                         including a Conc/Dil index value,    SPL_ALL
                         if applicable:
                                                              SPLC_ALL:3
                         <ID><index>:<Conc/Dil
                         Index> The last number is the
                         Conc/Dil index, not the
                         concentration/dilution value. The
                         well index can be replaced by
                         _ALL for samples and sample
                         controls, which returns the mean
                         of all indexes of the well type.



280 | Chapter 13: Data Reduction Options



       MEAN(<ID>)         The mean of the specified well        MEAN(POS1)
      Mean(x;y;z;...)     identifier, well coordinates or       MEAN(A1;A2)
                          variables
        SD(<ID>)          The standard deviation of the         SD(BLK)
       SD(x;y;z;...)      specified well identifier or          SD(22;33;44)
                          variables
        CV(<ID>)          The coefficient of variation of the   CV(STD1)
       CV(x;y;z;...)      specified well identifier or          CV(A1;SPL3;50)
                          variables
        Round(x;y)        Rounds x to the y number of           Round(SPL3;4)
                          significant digits
      Truncate(x;y)       Truncates x to the y number of        Truncate(STD2;5)
                          significant digits
       Dil(<ID>) or       Returns the defined dilution or       DIL(SPL1)
       Conc(<ID>)         concentration of the specified        Conc(CTL2)
                          well ID
          LOG(x)          Represents the LOG10 function         LOG(SPL10)
         POW(x;y)         The value of x raised to the          POW(STD1;3)
                          power of y

         SQRT(x)          The square root of <x>                SQRT(A1*B1)
       MIN(x;y;z;...)       The minimum of the defined            MIN(CV(CTL1);CV(CTL2))
                          variables
       MAX(x;y;z;...)       The maximum of the defined            MAX(A1;B1;C1)
                          variables
      Data reduction      Represents a value collected with     !Lot#
         variable         the Runtime Prompts
     Functions allow a     (x;y) Any expression that represents a single value,
      combination of       including well identifiers, locations, numerals, a function
       expressions         that results in a single value, can be included in the
                           formula, if it's a valid expression. Functions described with
                           the ellipsis (x;y;z;...) allow up to 10 expressions.






Interpolation Example




Interpolate the IC50 or EC50
      When using the 4 Parameter or 5 Parameter curve fit methods, you can show the IC50 or
      EC50 value in the curve results using Gen5's Interpolate function.
       1.   First, define the Gen5 protocol and run the experiment as you normally would
            to capture the measurement results.
       2.   After Gen5 has calculated the best fit curve, locate and make note of the Curve
            Parameters:
             4P: C
             5P: A and D. Then, calculate the IC50/EC50 value using this formula: ((A-
               D)/2)+D
       3.   Return to and edit the Data Reduction>Curve Analysis step: select the Data
            Out tab and enter the value determined in the previous step in the
            Interpolations table under Formula.
      In the Plate View select the Graphs tab to see the interpolated IC50 or EC50 value. You
      will also see the value plotted when you include the curve in a report or PowerExport.



282 | Chapter 13: Data Reduction Options




Multiple Curves

 Gen5's Multiple Curves Options
        Gen5 offers several methods for generating multiple curves in an experiment. Follow
        the link for the method that best fits your needs:
           Generating Multiple Standard Curves: you have two or more standards and
             want to plot a standard curve for each
           Generating Curves based on Sample Dilutions: you have samples with
             multiple dilutions and want to plot curves based on the expected dilution
             values
           Plotting Sample Dilutions on a Standard Curve: you have unknown samples
             of various dilutions and want to determine their concentration from a standard
             curve
           Kinetic curve for each well: you are conducting a kinetic or time-course
             analysis and want to plot kinetic curves to determine Max V, Integral, etc.



Generating Multiple Standard Curves
        Gen5 lets you create up to six standard curves in an experiment. The standards can
        have the same or different concentration values.

  How to:
        Generating multiple standard curves requires applying multiple standards to the plate:
         1.   Create a new Protocol and define its Procedure in the usual way. When
              defining the Plate Layout, assign the first set Standards to the plate as usual



                                             You can change the default IDs for
                                             the Standards, learn how in the
                                             Preparing Plates chapter




         2.   Use the ID Prefix drop-down list to select the next standard, e.g. STDB, to
              assign to the plate
         3.   Optionally, click the 3-dot button for Conc. to define different concentration
              values for the next standard. Overwrite the first set of concentration values,






           with those for the current standard. Skip this step to use the same
           concentrations
      4.   Assign the location of the additional standards on the plate
      5.   Assign the location of the test samples and any controls to the plate
      6.   Go to Data Reduction> Curve Analysis to set up the curves. Create a Curve
           Analysis step, in the usual way, for each set of standards defined (one curve for
           each standard group).0.

 To View Multiple Standard Curves:
           As with a single standard curve, after you've acquired the data, e.g. read the
       plate, open the Plate workspace, and select the Graph tab. Use the drop-down list
       in the Curve field to select the curve to view.
       Curve Fitting Results: In addition to displaying the curve, Gen5 displays, in a
       table beneath the curve, the data points used to calculate all the standard curves.
       Combine the Curves in One View: Gen5 lets you create a new curve to overlay
       multiple curves in one graph.

 To Report Multiple Curves:
       Gen5 lets you report/print the curves separately or combined:
            Create a New Graph to overlay curves and add the new curve to the
              Content in Report Builder/Power Export Builder or add each curve
              independently to report them separately
            For any curve, display it in the Graph tab of the Plate workspace and Right-
              Click to copy or save it as an image for use in a word-processor application
            Export it to Excel(R)


Samples and Sample Controls Curves
   Data Reduction> Curve Analysis> Data In
     Gen5 will plot a curve for each sample ID or sample control ID, using the expected
     dilutions/concentrations for the X-Axis and the user-selected measurement values for
     the Y-Axis. Titer assays, for example, use this feature to plot a titer curve.




 Well ID
     After setting the Well ID to SPL or SPLC (assuming the default IDs were retained), tell
     Gen5 to generate one curve for All (each of) the IDs for which a concentration or
     dilution has been defined, or for only one particular ID:



284 | Chapter 13: Data Reduction Options



               Keep the check mark for All IDs to generate one curve for each ID
               Or, de-select All and enter the number of the Sample ID or Sample Control
                 ID group for which you want only one curve plotted.

  Viewing
        Just like standard curves, after you've read the plate, open the Plate View and select the
        Graph tab. Use the Curve drop-down list to select the curve to display. Gen5 appends
        the Well ID (e.g. SPL1) group name to the curve name: Curve_SPL1 for example, to
        name the curves.

  Reporting
        You can report/print the curves just like standard curves, repeating the procedure for
        each curve generated, as needed.

          If the Samples or Sample Controls used to plot the curves are
            assigned Concentrations, rather than Dilutions, you can elect to
            Calculate Concentrations and Concentrations x Dilutions. When
            the Well ID to plot the curves is set to All IDs, the results will only be
            calculated for the samples used in generating each single curve. For
            example, concentrations for SPL1 will be calculated using the SPL1
            curve, concentrations for SPL2 will be calculated using the SPL2 curve,
            and so on.


How to generate Sample-Dilution Curves
        When you have multiple dilutions of your samples, Gen5 makes it easy to plot a curve
        for each sample based on the known dilution values. The critical factor is assigning the
        dilution values to the Samples in the Plate Layout. Gen5 recognizes sample dilutions
        as valid X-axis values.

  How to:
         1.   Select File>New Protocol
         2.   Select Protocol>Procedure and define the Read step (and any other required
              steps)
         3.   Select Protocol>Plate Layout:
               Define the Sample Dilutions
               Assign the location of the sample dilutions, and blanks (if any) on the plate






For example:




This example shows three samples with the same dilution values. Gen5 will create
three curves, one for each sample. Gen5 assigns a dilution index to keep track of the
multiple instances of a sample, e.g. SMP2:3 is the third dilution index of Sample 2.
 4.   Select Protocol>Data Reduction
       When Blanks (BLK) are assigned in the Plate Layout, Gen5 automatically
         creates the Blank-Subtraction transformation
       Depending on your assay requirements you may need to define another
         transformation or data reduction to normalize the data used in the curves,
         as in this Toxicity/Cytotoxicity assay
 5.   Click Curve Analysis0.
       On the Data In tab, set the Well ID to SPL (or the customized Well ID) for
         sample dilutions
       Select the Curve Fit tab to select the best curve fit method



286 | Chapter 13: Data Reduction Options



Viewing and Reporting Sample Dilution Curves
        You can overlay multiple sample dilution curves in one graph for viewing and
        reporting. After defining the Procedure, Plate Layout, and Data Reduction steps,
        Create a New Graph in Data Views. The data views become Available Data Views in:
               Report Builder to generate a print out
               Power Export Builder for transfer to Excel(R)

                    To view the new curve online, select the Graph tab and use the Curve:
                   drop-down list to select it







Plotting Sample Dilutions on a Standard Curve
      When you have unknown samples and want to determine their concentration, it may
      be most efficient to test them in various dilutions/concentrations against a standard. In
      Gen5, you can take advantage of multiple features to accomplish this task.

  How to:
       1.   Select File>New Protocol
       2.   Select Protocol>Procedure and define the Read step (and any other required
            steps)
       3.   Select Protocol>Plate Layout:
             Define the Sample Dilutions
             Define the Standards and their expected concentrations
             Assign the location of the sample dilutions, standards and blanks (if any) on
               the plate
       4.   Select Data Reduction> Curve Analysis to create the standard curve
             Gen5 may have generated a "corrected" data set: if you assigned blanks to
               the plate or selected Pathlength Correction in the Read step, you'll want to
               select these data sets for Data In for the Y-Axis Data when plotting the
               curve

       5.      On the Data In tab, set the Well ID to STD and use the drop-down to select
            the Y-Axis Data
       6.   On the Curve Fit tab, choose a curve fit method
       7.   On the Data Out tab, define Interpolations to plot select Sample dilutions on
            the curve. For example, in the Interpolations Formula table enter SPL1:1,
            SPL1:5, SPL2:1, etc. to easily identify them in the graph0.


         Viewing results: Select the Graphs tab, after reading the plate, to view the curve.
      Use the drop-down for the Results field (at the top, right corner) to select the
      Interpolations table to enhance the view



288 | Chapter 13: Data Reduction Options




Troubleshooting Curve Fits
        Gen5 gives you a lot of flexibility in curve fitting, some of them can be used to improve
        a curve fit:
               Collect more data: the most certain way to improve a curve fit is to collect
                 more data: widen the range of X values, for example.
               Simplify the model: Linear regression and 4P fits are easier to calculate and
                 have fewer unknowns than a 5P fit, your data may better fit a simpler
                 model. (You can also use constraints to simplify the model, i.e. reduce the
                 number of unknowns.)
               Apply constraints when the curve is far from the data: by constraining the
                 initial values (Start From) or assigning a Fixed value you may be able to
                 generate a better fit.
               Constraints can also be useful when you have not collected sufficient data
                 to map all the parameters in your model and you know or expect a
                 parameter to equal a certain value.


            Gen5 lets you modify the settings used to plot the curve, as suggested above, so
        you can experiment with the different options. Alternatively, you can create multiple
        curves using the same data but with variant settings (add more Curve Analysis steps
        to the Data Reduction), so it is easier to compare the various results. Then, you can
        overlay the curves in one view, if that is helpful: see Create a New Graph.







Kinetic Analysis Options

        Learn more about the Well Zoom in the Kinetic Analysis chapter.

      Gen5 offers a full complement of options for analyzing your Kinetic Reading raw data
      results.

 Data Reduction Options
      In the Data Reduction> Well Analysis dialog, you can set up multiple steps, taking
      advantage of some or all the available options:
            Mean V
            Max V (Gen5 creates this Data Reduction step automatically. It also
              calculates the Y Intercept, R & R2, time at Max V, and Lag time)
            Mean Min/Max OD/RFU/RLU
            Onset OD/RFU/RLU
            Onset OD%/RFU%/RLU%
            Integral

 Combine Data Sets
      Gen5 lets you combine the measurements collected from multiple kinetic readings
      performed in one experiment. When multiple kinetic loops are defined in the
      Procedure, Gen5 offers the Append to previous Kinetic data option in the second and
      subsequent kinetic read steps.



      The read steps in the kinetic loops must be identical, and Gen5 enforces this rule when
      the Append option is selected. In a Synchronized Mode block, this feature is
      mandatory and Gen5 automatically applies it to the second and higher kinetic read
      steps.
      Append to previous Kinetic data results in one data set containing all the
      measurement values acquired from the reader during the all the kinetic loops. Do not
      use this option if you want separate data sets for data reduction purposes.

 Dispensing Reagent in a Kinetic Analysis
      Gen5 lets you include dispensing in a kinetic analysis: learn about Dispensing Reagent
      in a Kinetic Analysis Protocol in Gen5's Help.



290 | Chapter 13: Data Reduction Options



Perform Well Analysis
     Data Reduction > Well Analysis

  About Gen5's Well Analysis
           Well Analysis is available as a Data Reduction option when a Kinetic analysis
             has been set up in the Procedure
           Well Analysis is also available when Spectrum, Area Scan, or Linear Scan is
             defined as the Read Type
           Well Analysis produces a special data view that lets you zero-in on each
             individual well to see the measurement values and analysis results: Well Zoom
           Well Analysis also produces a special table of results for viewing, reporting and
             exporting the calculation results of each well
           In the StepWise Data Reduction dialog, you can create multiple Well Analysis
             events to obtain multiple types of results. Assign a unique Label/name to each
             well analysis step.

  How to:
         1.   Label - Identifies the results for data views, report building, etc. Enter a unique
              name/ID to be used in the resulting data set name. Data Set Name Rules. You
              must enter a unique Label when a data set is used in more than one Data
              Reduction step.
         2.   Data In - Click the down arrow to select a data set, e.g. raw data or results of
              previously-defined Transformation (based on All Reads)
         3.     Calculation Type - Use the buttons to select the type of computation to
              conduct. Each option displays the results it will produce in the Generated Data
              box on the right side of the screen (see below)0.
               Calculation Options correspond to the Calculation Type selected. Click the
                 Calculation Options button to alter the default settings for the selected
                 Calculation Type.
               Formula Syntax for Well Analysis: describes the symbols and functions
                 supported to perform a calculation using the individual read points of each
                 well (on page 292).







Kinetic and Scanning Data Reduction Outputs Listing
     Set up the Well Analysis option that generates the desired data output

   Read Type           Calculation Type           New Data Sets
   Kinetic            Mean V                      Mean V
                                                  R (correlation coefficient)
                                                  R2 (coefficient of
                                                  determination)
                                                  Y Intercept
                      Max V                       Max V
                                                  R (correlation coefficient)
                                                  R2 (coefficient of
                                                  determination)
                                                  t[1] at Max V
                                                  Lagtime
                                                  Max V Calc - t min
                                                  Max V Calc - t max
                                                  Y Intercept
                      Mean Min/Max OD             Mean Min OD[2]
                                                  t at Mean Min OD
                                                  Mean Max OD
                                                  t at Mean Max OD
                      Mean, Std, CV               Mean OD
                                                  Std Dev OD
                                                  CV OD
                      Onset OD                    Onset Time
                                                  Onset OD
                                                  Basis Time
                                                  Basis OD
                      Integral                    Integral


   Spectrum           Min / Max OD                Mean Min OD
                                                  W[3] at Mean Min OD
                                                  Mean Max OD
                                                  W at Mean Max OD



292 | Chapter 13: Data Reduction Options



       Read Type          Calculation Type          New Data Sets
       Linear Scan       Mean, Std, CV              Mean OD
                                                    Std Dev OD
                                                    CV OD
                         Mean Min/Max               Mean Min OD
                                                    Read Pos[4] at Mean Min OD
                                                    Mean Max OD
                                                    Read Pos at Mean Max OD
                         Integral                   Integral
       Area Scan          Mean, Std, CV             Mean OD
                                                    Std Dev OD
                                                    CV OD
        OD assumes absorbance reads. Substitute RFU or RLU/sec as appropriate.
        [3] W = Wavelength
        [4] Pos = Horizontal Reading Position


 Formula Syntax for Well Analysis
        The Well Analysis Formula lets you perform calculations using the individual read
        points or indexes in "multi-index" readings: kinetic and spectral scan. Formulas can be
        written similar to Transformations, using the symbols and functions listed below. Also
        see some Examples on page 295.

          Symbols and functions are not case sensitive.







Symbol/Function Description                          Example

       R#          Read point or index of a          R1
                   kinetic read

       W#          Read point or index of spectral W2
                   read

   Function        Add +, subtract -, divide /,      R2+R4, R6-R10,
   Operators       multiply *, combine ( )           W3/W8, R1*R15,
                                                     (R4/R1)*100

 Numeric value     Any numeral, including those      2.45E-08
                   expressed with scientific
                   notation

Mean(R#/W#;...) The mean of a set of read            Mean(R2;R4;R8)
                   points or variables               Mean(1;2;3)
 Mean(x;y;z;...)

 SD(R#/W#;...)     The standard deviation of         SD(R12;R22)
                   specified read points or a set    SD(23;75;45)
  SD(x;y;z;...)    of numerals

 CV(R#/W#;...)     The coefficient of variation of   CV(W5;W6;W7)
                   specified read points or any      CV(1;2;3)
  CV(x;y;z;...)    set of numerals, expressed as
                   a percent

   Round(x;y)      Rounds x to the y number of       Round(W2;5)
                   significant digits.

 Truncate(x;y)     Truncates x to the y number of Truncate(R3;3)
                   significant digits.

     Log(x)        Represents the Log10 function Log(R3)

   POW(x;y)        Represents the value of x         POW(W10;2)
                   raised to the power of y

   POW(10;x)       Calculates the Anti-Log of the    POW(10;R4)
                   current well

    SQRT(x)        Represents the square root of     SQRT(R1*R5)
                   x

  MIN(x;y;z;...)   Returns the minimum of the        Min(R5;R6;R7;R8)
                   defined variables.

 MAX(x;y;z;...)    Returns the maximum of the        MAX(W1;W2;W3)
                   defined variables



294 | Chapter 13: Data Reduction Options




     Symbol/Function Description                               Example

        Functions allow a    (x;y) Any expression that represents a single value,
         combination of      including well identifiers, locations, numerals, a function
          expressions        that results in a single value, can be included in the
                             formula, if it's a valid expression. Functions described
                             with the ellipsis (x;y;z;...) allow up to 10 expressions.



Using individual Kinetic read points in a Formula
        In addition to Gen5's Transformation option, you can perform calculations using the
        individual reading points of a well in a Kinetic or Spectral analysis with the Well
        Analysis Formula function. The formula will generate a single value for each well.
        Gen5 names the resulting data set "Formula Result [nm]", where nm is the wavelength
        or filter set defined in the read step. When a Label is defined it precedes the naming
        convention: "Label: Formula Result [nm]"
        After setting up the Kinetic loop or spectrum read step in the Procedure:
         1.   Select Data Reduction>Well Analysis
         2.   Select the multi-index data set to use for Data In
         3.      Select the Formula button and write the calculation in the text field0.







  Examples:
      1. For an ORAC Antioxidant Test:
      0.5+(R2/R1)+(R3/R1)+(R4/R1)+(R5/R1)....+(Rn/R1)
      Where R1 is the reading at initiation of the reaction and Rn is the last measurement. A
      step-by-step description for using this formula in an experiment is described in the
      Kinetic Fluorescence Assay Example in the Assay Examples chapter.
      2. To determine the mean of certain read points: (r1xr2xr3xr4)/4

  Viewing/Reporting Results
      Gen5 automatically generates a Matrix view and two tables when a Well Analysis
      Formula is created. In Data Views, and the Report Builder and export options, you'll
      find:
             Matrix: Formula Result [nm]
               Statistics: Formula Result [nm]
               Well Analysis Results: Formula Result [nm]



Well Zoom during a Kinetic Read
      Learn more about the Well Zoom in the Kinetic Analysis chapter.
       1.     Select the Curves data set from the Data drop-down list before Reading the
              plate.
       2.     Zoom into a specific well: click on the desired well to display the Well Zoom
              screen. It will display the results as they're measured.0.

         Tip: If necessary, drag the progress dialog out of the way for an unobstructed view:
      click and drag the title bar of the dialog to move it out of the way.

         Caution: In some cases, displaying the Curves data set during a Kinetic read can
      consume excessive resources resulting in computer-performance degradation. Learn
      more in the Troubleshooting chapter. You can follow the steps above to monitor the
      progress of one well, then, leaving the Well Zoom open, change the Matrix Data to a
      numeric view



296 | Chapter 13: Data Reduction Options




Define Cutoffs
     Protocol> Data Reduction> Cutoffs

About Cutoffs
        Gen5TM lets you define cutoffs as fixed or variable margins against which results are
        compared. Gen5 creates a Symbols data set based on your definition of cutoffs that
        shows how each well fits into the defined categories. Gen5 also adds another tab to the
        Plate View to show the Cutoff Values, the results of cutoff formulas. Up to 40 formulas
        (of increasing value) can be defined for each data set and multiple Cutoff steps, one
        Cutoff step per data set, can be defined in the StepWise Data Reduction.
        In the Cutoffs dialog, notice that the number of Symbols fields exceeds the number of
        cutoff formula fields by one. During data reduction, if the value of a well is less than
        the first cutoff, the first symbol is applied to it. If the value of a well is greater than or
        equal to the first cutoff but less than the second cutoff, the second symbol is assigned
        to the well, and so on.
        Out-of-Range Symbols are applied to concentration values (calculated from a
        standard curve) when the concentrations are outside the extrapolation range of the
        curve: below the minimum or above the maximum. You can change the OUT+ and
        OUT- labels applied to these values by clicking in the text fields and replacing the
        content.
        Data In data sets presented for selection are determined by the current protocol
        excluding multi-index data sets. Cutoffs cannot be determined in multiple-read
        measurements like kinetic analysis and scanning results. For these types of analysis a
        transformed or processed data set must be used.
        ????? - This symbol in Cutoff results, i.e. the Symbols data set, indicates an out-of-
        range or biased value was used in the calculation. Check the Protocol
        Options>Calculation Options settings.

          See an example and explanation of cutoffs on page 298


How to set up cutoffs:
         1.       Begin by selecting the Data In data set on which to apply the cutoffs.

          Hint: The Data In drop-down list offers the data sets resulting from all
            previously defined reads (raw data) and calculations, except for multi-index
            readings, e.g. kinetic. Cutoffs cannot be evaluated against multiple-index reads.

         2.   Define the cutoffs, beginning with the lowest value, by entering a formula or
              data point in the Cutoff Formula 1 field. In the Symbols fields that straddle the
              cutoff formula field, in the top field, enter a symbol (or call) to apply to wells
              with values less than the formula. In the next Symbol field, enter the symbol to






            apply to values greater than or equal to the Formula. (See the Formula Syntax
            table on page 298.)

       Important: Cutoffs must be defined in increasing order, from the
         lowest value to the highest. Gen5 will issue a Calculation Warning and
         will be unable to assign Symbols to wells if the reading results do not
         affirm the increasing values of the cutoff formula


       3.       Customize the appearance of the symbols, change the font and color, by
            clicking the 3-dot button next to the Symbol field.
       4.   Continue defining cutoffs and symbols in the same manner, always defining a
            higher value cutoff formula.0.


How to view the cutoffs:
       1.   After reading the plate (or otherwise acquiring data), open the Plate View and
            select the Matrix tab
       2.   At the Data field, use the drop-down list to select the Symbols data set
       3.   Select the Cutoff Values tab to view the values (formula results) upon which
            the Symbols data set was based0.


 Important Information:
        When cutoffs, or calls, are defined, Gen5 adds a tab to the Plate View to
          display the values or results of the cutoff formulas

             Up to 40 cutoff formulas can be defined for one data set. Use the scroll controls at
            the top of the dialog to display additional cutoff formula and symbol fields.
        Multiple Cutoffs can be defined (in the Data Reduction dialog) for a protocol: one set of
            cutoffs per data set, i.e. you can only reference a data set one time for cutoffs
        Gen5's rounding function in Data Views may cause unexpected results in the
          Cutoffs' reporting. Gen5 does not round the values before applying the cutoff
          formula, so it's possible to see conflicting outputs. More:



298 | Chapter 13: Data Reduction Options



Cutoffs Example




        For this example, we customized the Assay Control well type in Plate Layout to put
        Positive (PC) and Negative (NC) controls on the plate. Then, setting up the cutoffs as
        shown in this image, Gen5 will apply NEG to any well with a value less than the NC.
        It will apply the EQV symbol to any wells that are greater than or equal to the NC but
        less than the PC. It will assign POS to any wells equal to or greater than the PC. Any
        wells with values considered out-of-range will be assigned OUT- if the concentration is
        below the minimum, and OUT+ if the concentration is higher than the maximum.
        To view the cutoffs, after reading the plate, in the Plate workspace, select Symbols
        from the Data field drop-down list.


  Formula Syntax for Cutoffs

    Symbol/Function Description                                 Example

        +-*/                Mathematical operators               CTL1+0.100

        ()                  Represents inclusion                 (CTL1/CTL2)*100
        Numeric value       Any numeral, including those       0.500, 54000, 1e10
                            expressed with scientific notation







Symbol/Function Description                               Example
     Well ID        The value of a specific well. The     A1
 Well coordinates   ID assigned to a specific well,       STD3
   wellID_ALL       including a Conc/Dil index value,     CTL1:2
                    if applicable:
                    <ID><index>:<Conc/Dil
                    Index> The last number is the         SPL_ALL
                    Conc/Dil index, not the               SPLC_ALL:3
                    concentration/dilution value.
                    The well index can be replaced
                    by _ALL for Samples and
                    Sample Controls, which returns
                    the mean of all indexes of the
                    well type. Does not apply to
                    STD, BLK or Assay Controls.
   MEAN(<ID>)       The mean of the specified well        MEAN(SPL1)
  Mean(x;y;z;...)   identifier or variables               Mean(A1;22;SPL2)
    SD(<ID>)        The standard deviation of the         SD(BLK)
   SD(x;y;z;...)    specified well identifier or          SD(4;H12;CTL2)
                    variables
    CV(<ID>)        The coefficient of variation of the   CV(STD1)
   CV(x;y;z;...)    specified well identifier or          CV(SPL10;33;B2)
                    variables, expressed as percent
   DIL(<ID>);       Returns the defined dilution or       Dil(CTL3)
   Conc(<ID>)       concentration of the specified        CONC(STD2)
                    well ID
   Round(x;y)       Rounds x to the y number of           Round(SPL1;4)
                    significant digits. x can be any
                    valid symbol or expression.
                    (Learn more below)
  Truncate(x;y)     Truncates x to the y number of        Truncate(CTL3;3)
                    significant digits. x can be any
                    valid symbol or expression
     LOG(x)         Represents the LOG10 function         LOG(SPL10)
    POW(x;y)        The value of x raised to the          Pow(STD1;3)
                    power of y
     SQRT(x)        The square root of x                  SQRT(A1*B1)
  MIN(x;y;z;...)      The minimum of the defined            Min(CV(CTL1);
                    values                                 CV(CTL2); 45)

 MAX(x;y;z;...)       The maximum of the defined            MAX(A1;B1;C1)
                    values

Data reduction      Represents a value collected with
                                                      !KitFactor
variable            the Runtime Prompts



300 | Chapter 13: Data Reduction Options




    Symbol/Function Description                                    Example
      Functions allow a (x;y) Any expression that represents a single value, including
       combination of   well identifiers, locations, numerals, a function that results in a
        expressions     single value, can be included in the formula, if it's a valid
                        expression. Functions described with the ellipsis (x;y;z;...)
                        allow up to 10 expressions.



Rounding Issue with Cutoffs
        It's possible to see apparent discrepancies in the cutoff results:
          For Example: a value of .9998 will be rounded to 1 when the numeric format for the
          view is set to 3 Decimal places (the default setting). In the Matrix view you'll see 1
          for the well, but if Cutoffs are set to identify values less than 1, it will be reported
          as <1 in the Symbols view/report.
          Two ways to avoid this inconsistency:
               Create a Transformation that rounds the data set, and apply the cutoffs to
                 the new data set. Transformation formula: Round(X;3) for example. The
                 resulting reports and views of the data set and cutoffs will be consistent.
               Revise the numeric Format, i.e., the number of decimal places or significant
                 digits, of the Data View to more precisely view and report the values. Find
                 instructions at Numeric Format. In the above example, increasing the
                 number of decimal places to 4 would eliminate the inconsistency. This
                 option may or may not be appropriate for your results.







Validation
    Data Reduction> Validation
       Many assay kits define conditions which must be met to validate the results of an
       experiment. The Validation dialog lets you set up these conditions to compare to
       selected results (data sets). The Validation Formulas can be fixed thresholds or
       algebraic formulas.

Top 5 Things to Know about Validation Criteria:
        1.   Multiple Validation steps can be defined in the StepWise Data Reduction, but
             only one set of criteria for each data set is permitted
        2.   Up to 50 conditions or formulas can be defined in a Validation step
        3.   When data points that cause a Validation failure are masked or changed, the
             Validation can change from fail to pass
        4.   Validation results can be included in reports and/or export content
        5.   Most often, validation formulas combine well IDs with a less than, greater than,
             or equal sign, e.g. STD1>=1.5:0.
               <          less than
               <=         less than or equal to
               >          greater than
               >=         greater than or equal to



Setting up Validation Criteria
        1.   Select Data Reduction>Validation
        2.   Use the drop-down list to select a Data In data set against which the criteria
             are evaluated
        3.   In the Formula fields, enter conditions (up to 20) that must be met for the
             experiment's results to be considered valid.




        4.   Optionally, in the text fields on the right-side of the screen, e.g. Valid Text, click
             inside the field and overwrite the default text to change it for the results output
             and reports.0.



302 | Chapter 13: Data Reduction Options



Formula Syntax for Validation
        In conjunction with a conditional operator: <, <=, =, >, >=, you can use the following
        elements to define a formula as a validation or quality control condition:

    Symbol/Function             Description                      Example

        +                        Addition                        CTL1+0.100<3.5

        -                        Subtraction or negation         BLK-0.010

        /                        Division                        CTL1/CTL2
        *                        Multiplication                  STD1*0.10
        ()                       Represents inclusion            (CTL1/CTL2)*100
    Numeric value                Any numeral, including          0.500, 54000, 2.45E-08
                                 those expressed with
                                 scientific notation
    Well ID                      The value of a specific         A1
    Well coordinates             well. The ID and index          STD3
    wellID_ALL                   assigned to a specific well.
                                 The well index can be
                                 replaced by _ALL for
                                                                 SPL_ALL
                                 samples and sample
                                 controls, which returns the     SPLC_ALL:3
                                 mean of all indexes of the
                                 well type.
    WellID#                      To evaluate all of the          STD# performs the
    WellID:#                     specified wells individually,   evaluation on each STD
    WellID#:#                    returns the mean value of       group, e.g. STD, STDB,
                                 each separate well index.       STDC, etc.
                                 The Conc/Dil index can          SPLC2:# performs the
                                 also be represented with        evaluation on each SPLC2
                                 #.                              dilution
                                 SPL#:# performs the             STD:# performs the
                                 evaluation on each dilution     evaluation on each
                                 of each sample group.           concentration of the STD
                                                                 group, e.g. STD1, STD2
    wellID:conc index           Use : as a separator to          CTL2:3 the average value for
                                identify individual well IDs     all CTL2 at the third
                                of a specific concentration      concentration value
                                or dilution, if applicable:
                                <ID><index>:<Conc/Dil
                                Index> The last number is
                                the Conc/Dil index, not the
                                concentration or dilution
                                value.







Symbol/Function              Description                      Example
The difference between the two "all" identifiers extends to their results output: using
_ALL produces a one line result for all wells: valid or invalid (if one well is invalid, the
report is invalid); the # produces individual invalid results: if one or more wells are
invalid, each well result is reported; if all wells are valid a one line report is given.
_All does not apply to STD, BLK or Assay Controls
SD(<ID>)                   The standard deviation of the      SD(BLK)
SD(x;y;z...)               specified well identifier or       SD(A1;STD3;45)
                           expression
CV(<ID>)                   The coefficient of variation of    CV(STD1)
CV(x;y;z...)               the specified well identifier or   CV(SPL12;33;B2)
                           expression
ROUND(x;y)                 Rounds x to the y number of        Round(SPL1;4)
                           significant digits
Truncate(x;y)              Truncates x to the y number        TRUNCATE(STD1;5)
                           of significant digits
Conc(<ID>)                 Returns the defined                CONC(CTL4)
                           concentration of the specified
                           well ID
DIL(<ID>)                  Returns the defined dilution       Dil(SPL3)
                           of the specified well ID
SQRT(x)                    The square root of x               SQRT(A1*B1)
LOG(x)                     Represents the LOG10               LOG(SPL10)
                           function
POW(x;y)                   The value of x raised to the       POW(STD1;3)
                           power of y
MIN(x;y;z;...)            The minimum of the defined          MIN(CV(CTL1);CV(CTL2))
                          variables
MAX(x;y;z;...)              The maximum of the defined          MAX(A1;B1;C1)
                          variables

Curve(<x>;<y>)            Returns the value of the            Curve(CurveA;R2)>8.8
                          selected curve result

Curve(<x>;<y>;<z>) Returns the value of the curve Curve(CurveB;C;SE)<=1
                   result for the selected
                   parameter. See explanation
                   below.

Data reduction            Represents a value collected
                                                              !KitFactor
variable                  with the Runtime Prompts



304 | Chapter 13: Data Reduction Options




    Symbol/Function               Description                  Example
    Functions allow a         (x;y) Any expression that represents a single value,
    combination of            including well identifiers, locations, numerals, a function that
    expressions               results in a single value, can be included in the formula, if
                              it's a valid expression. Functions described with the ellipsis
                              (x;y;z;...) allow up to 10 expressions.


Defining curve results and parameters
    When you have generated a standard curve, Gen5 lets you define validation criteria using
    the Parameters and Values calculated by the curve as the variables in the validation
    formula. For example, you can define a validation condition specifying the value of R2:
     0 < Curve(CurveC;R2) < 1.0
     Two types of curve formula are possible:
           Curve(Curve_name;y) to express a whole curve variable, such as R2, DF, or SS
           Curve(Curve_name;y;z) to identify a parameter and parameter-specific
             variable, like SE or 95% CI

          Note: you can select any data set in the experiment for this curve
            formula application; but, keep in mind Gen5's limitation of one
            Validation step per data set.

          Find more details in Gen5's Help. Look for Validation: Curve Formula


Validation Examples
         1.   From an assay kit: "The absorbance of the Negative Control (NC) must be less
              than 70% of the cutoff (CO) value. The mean absorbance of the cutoff should be
              greater than 1. The ratio Positive Control (PC)/CO should be greater than or
              equal to 1.3."




         2.   Another assay kit says: "Individual negative control (NC) absorbance values
              must be less than or equal to 0.150 and greater than or equal to -0.005.
              Individual positive control (PC) absorbance values must be greater than or






              equal to 0.600. Individual positive control values must be within the range of
              0.5 to 1.5 times the mean of the positive control."




         3.   In a kinetic analysis, during the first of several readings, the mean value of
              STD1 must fall between 0.200 and 0.300 OD. The mean value of STD2 must fall
              between 0.900 and 1.300 OD.




              And, the Mean OD of every sample replicate group must be greater than 0.




Viewing the Validation Results
      Gen5 applies a status to each formula defined in the Validation step:
           Valid if the condition was met
           Not Valid if the condition was not met (i.e. failed).
           Unable to Evaluate, if:



306 | Chapter 13: Data Reduction Options



               The selected data set was not available,
               A well ID in the formula was not found in the Plate Layout,
               A value could not be determined for a cited Well ID (e.g., all wells with that
                 ID are masked, or over-ranged).

          You can change the status labels, replacing them with terms that have
            more meaning for your organization.

          Gen5 issues a Calculation Warning when out-of-range or biased values
            are used in a validation formula, see Calculation Options

               Gen5 adds a tab to the Plate View to display Validation results




               Failed validations or when Gen5 was "Unable to Evaluate" a criteria are
                 reported immediately after a plate is read in the Calculation Warning pop-
                 up. You can reopen the message anytime by selecting Calculation Log
                 under the respective Plate in the menu tree. If the condition is Verified,
                 Gen5 does not present a message.

Reporting Validation Results

                    Add the Validation table to Report Content in the Report Builder.
                   Similarly, you can export the results.







Fluorescence Polarization
    Data Reduction> Polarization

About Fluorescence Polarization Data Reduction
      Gen5 automatically performs data reduction when Fluorescence Polarization (FP) is
      the selected read type. You can retain, modify, or delete the auto-generated data
      reduction step.
      When Blanks are assigned to the Plate Layout, Gen5 performs a blank-subtraction
      before calculating polarization. When FP is performed in a kinetic loop, Gen5 uses the
      polarization results to automatically perform a Max V Well Analysis determination.
      Blank subtraction is performed before the Well Analysis, if applicable.

Polarization and Anisotropy
      The basic polarization formulas use:
            Parallel Intensity (raw or blanked data from parallel measurement
            Perpendicular Intensity (raw/ blanked data from perpendicular
              measurement x G Factor
            G Factor: a coefficient used to calculate the polarization value. It corrects for
              the optical variations between the parallel and perpendicular emission
              paths unique to each reader. Gen5's default value is 0.87.

      Gen5 automatically performs the Polarization calculation option. You can modify the
      automatically-generated FP data reduction step to change the output to Anisotropy, or
      to select both options.
      The raw and transformed data sets created by FP are available for selection/use in all
      other applicable data reduction options, e.g. Transformations, Curve Analysis.



308 | Chapter 13: Data Reduction Options



FP Formulas




           Parallel Intensityraw data from parallel measurement
           Perpendicular Intensityraw data from perpendicular measurement X G
             Factor
           G Factor: coefficient used to correct for the optical variations between the
             parallel and perpendicular emission paths. Gen5's default value is 0.87
           spl = test sample; blk = blank




        The G Factor is used in the FP calculation to normalize the polarization value obtained
        on fluorescein to 20 mP (known reference value of unbound fluorescein). Gen5 ships
        with a "G Factor Determining Protocol" that you can run to determine your reader's
        specific G Factor for fluoroscein.
