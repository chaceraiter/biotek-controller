# Chapter 21: Troubleshooting

     This chapter is intended to help you resolve or recover from error
     messages or other system trouble. The Fluorescence and
     Luminescence chapter also contains troubleshooting suggestions
     particular to those detection methods.


 Communication Errors .............................................................. 437
 Error Messages ........................................................................ 438
 Calculation Warnings ................................................................ 439
 Restoring Optimal Performance.................................................. 442
 System Administrator's Password............................................... 442



436 | Troubleshooting




Troubleshooting
     Here are some guidelines for error recovery, find additional information in Gen5's Help:
           First Response: Run a System Test on the reader to restore the reader's initial
             settings and computer communication capability. Note: to stop the alarm on
             readers without keypads (e.g. Synergy) press the plate-carrier button
           Reboot your Computer and Reader: When you can't run a system test, e.g.
             Gen5 is not responding, or when running a system test doesn't resolve the
             issue, turn off your computer and reader, check all the cabling, i.e. make sure
             your serial or USB cable is in good condition and is properly connected to the
             PC and reader, and then, power on your computer and reader. This should
             refresh the devices and reset communication parameters
           Communication Errors: PC to Reader on page 437
           Database Error Recovery in the Managing Files chapter
           Calculation (Data Reduction) Warnings on page 439
           Reader Error: #### on page 438
           Handling Other types of Error Messages refer to Gen5's Help
           Unknown System Admin's Password on page 442
           Computer Performance Slowdown on page 442
           Troubleshooting Fluorescence/Luminescence Measurements in a previous
             chapter on page 169
           Excel(R) errors refer to Gen5's Help


           Visit BioTek's website for useful suggestions on getting the most from your reader:
        http://www.biotek.com/products/technotes.php.


           Other Known Issues
              Gen5 installs a Read Me file in the root directory, the default path is
              C:\Program Files\BioTek\Gen5 (software level)\ReadMe.txt. It lists known
              issues you may have encountered. Locate and review the file and contact
              BioTek TAC for additional information or support.
           Synergy 2/4 to non-Synergy 2/4 readers (and vice versa)
              Protocols created with a Synergy 2 or Synergy 4 reader are not instantly
              compatible with other readers, and vice versa. You must re-validate the
              Procedure with the current reader: open the Procedure and click Validate.
              Generally, this corrects the error. If not, open each step in the Procedure and
              review it for compatibility with the current reader.






Communication Errors: Reader to Computer

Important Information:
         To prevent damage to the reader, always turn OFF the reader or the computer
           before removing or inserting a communications (serial or USB) cable
         Gen5TM and the reader-communication parameters will supersede the
           Windows(R) settings. Windows communication port configuration settings
           should not need adjustment to enable proper communications

When the computer (PC) won't communicate with the reader:
       1.   Confirm that the reader passes its system self test. Most readers perform a self
            test when turned on. Refer to the reader's user guide for more details. The
            reader will not communicate if it fails an internal system test. If the reader fails,
            refer to the user's guide to resolve the failure.
       2.   Make sure the serial or USB cable is in perfect condition and properly
            attached to the port defined in the Reader Configuration dialog (e.g. COM 1).
            Correct and reboot both PC and Reader. Test communication.
       3.   Confirm the Baud rate (or transmission speed) defined in Gen5's Reader
            Configuration matches the reader's settings. Consult your reader's user guide
            for the correct rate. Correct Gen5's Reader Settings to match the reader and
            reboot both PC and Reader. Test communication.
       4.   Disable the Calculation Option: Perform data reduction after each read to
            give Gen5 sufficient time between obtaining measurements to perform
            calculations
       5.   Confirm that the serial cable was obtained from BioTek. Serial cables are not
            universal. Consult the reader's user guide for proper cable configuration or
            contact BioTek customer service to purchase a factory tested cable. After
            installing a known, good cable, reboot both PC and Reader. Test
            communication.
       6.   Confirm with your computer supplier or a local PC technician that the serial
            port has been enabled. For example, the IBM Thinkpad(R) was originally
            shipped with the serial port disabled. Correct and reboot both PC and Reader.
       7.   For advanced PC users, the serial port of the reader and PC can be
            independently tested using an independent serial-communication software
            package such as Windows TerminalTM, Hyper TerminalTM, or ProComTM.
            BioTek does not support or sell these programs. 0.
             Select flow control for "XON/XOFF" and send an ASCII asterisk symbol (*)
               to the reader. The reader should initiate a self test and return the results to
               the PC. If the reader fails to communicate, test the reader on an alternative
               PC to confirm which device is at fault. Please contact BioTek if the reader is
               diagnosed to be faulty.



438 | Troubleshooting




Error Messages
        Here are some guidelines to help you quickly resolve an error:
         1.   Make note or take a "print screen" of the error message
         2.   Locate and follow the specific instructions/suggestions for the error provided
              in the reader's operator's manual
         3.   Call BioTek's Technical Assistance Center (TAC) if you are unable to resolve
              the issue yourself. 0.

Potential Error Messages and their Resolutions
           Reader Error ###: refer to the reader's Operator's Manual to identify the
             specific error. You may be able to resolve it yourself.
           File Not Found: there are several potential causes for this error. In a shared
             database environment, another user may have the file open. Check with your
             colleagues to eliminate this as the cause. When using the Windows(R) File
             System for file storage, use Windows Explorer to verify the location of the file.
           Bandpasses overlap: the selected Excitation and Emission filters are too close.
             Change one of the selected filters. Learn more in the Fluorescence and
             Luminescence chapter.
           Baud rate settings can cause "serial read" errors: when the baud rate is set to a
             non-default setting for Synergy and PowerWaveXS readers, Gen5 may be
             unable to communicate with them if they are turned off and then turned on
             again while Gen5 is running. Gen5 may reset the baud rate to the default
             setting in this scenario. Run a System Test to return readers to their initialized
             state






Calculation Warnings
      When Data Reduction steps generate an error or cannot be calculated, Gen5 displays
      and logs a Calculation Warning. Here are some guidelines for pinpointing and
      correcting the source of the error.

Curve Fit
         Not enough data points to fit
            If the plate was read successfully, i.e. all the data points obtained, make sure
            you have defined the minimum number of X-Axis points, e.g standards, for the
            selected curve fit. See Curve Fit: Minimum Number of Standards in the Data
            Reduction chapter.
         Too many data points
            The Spline curve fit is the only option with a limit on the number of X-axis
            points. Either change the curve fit method or reduce the number of standards,
            dilution samples, or calibrators, i.e. the number of X-data points.
         The selected curve fit method does not accept data points with identical X
            values
            The Spline and 4-P curve fits cannot be plotted when X-axis values are
            identical. Either:
             select a different curve fit
             change the Data In selected for the X-axis
             if the selected X-axis data is based on a Transformation, rewrite the formula
               to suppress duplicate values in the results
         The degree of the polynomial regression fit has been reduced
            If desired, you can either:
             Reduce the Degree



             Add more X-axis points, e.g. standards
         Math overflow error
            Check the Extrapolation setting



440 | Troubleshooting



              or Interpolation formulas (on the Data Out tab) to make sure they are not
              raising values to too high a value.
           Curve fit generic error
              Is the curve fit 4-P?
              Formula: Y = (A-D)/(1+(X/C)^B) + D
              If so, this error may be indicating that the calculated B parameter <=0


           Curves do not support multi-indexed data sets
              It is possible the Procedure was changed from an endpoint read to a kinetic
              analysis (or other multi-index option) without revising the curve generator.
              Review the Data Reduction steps and make the necessary adjustments, e.g.
              Well Analysis may be a better fit.
           The 4-parameter fit is not convergent. It is probably not the best fit
              Gen5 performs multiple approximations to plot a 4-P curve. It is expected that
              the err (error) will decrease with each approximation, indicating a better fit is
              being determined during each iteration. Gen5 displays this message when the
              err does not decrease.
              Select another curve fit method.
           Error during calculation. Data to fit not compatible with axis type
              Review the Data Reduction> Curve Analysis definition, is the Axis Data set
              to Log? and some of the Data In values are <0?




              If yes, change these settings to eliminate the error.

Validation
           At least one validation condition failed
              This message alerts you to the results of a Data Reduction>Validation
              formula. A criterion of your experiment may not have been satisfied. Review
              the results.

Cutoff
           Cutoffs do not support multi-indexed data sets
              It is possible the Procedure was changed from an endpoint read to a kinetic
              analysis (or other multi-index option) without revising a Data Reduction>
              Cutoff step.
              Review the Data Reduction steps and make the necessary adjustments, e.g. it
              may be possible to use a Validation formula in place of Cutoff results.







         Cutoffs are not in increasing order. Symbols can not be determined
           Review the Data Reduction> Cutoff formulas. They must be input in
           ascending order, from the lowest (obtained or calculated) value to the highest.
         Some cutoffs could not be calculated. Symbols cannot be determined
           Review the Data Reduction> Cutoff formulas. Try rewriting them, making
           sure to reference valid Well IDs, non-masked data values and logical formulae.

Well Analysis
         Well Analysis requires multi-indexed data set
           It is possible the Procedure was changed from a kinetic analysis (or other multi-
           index option) to an endpoint read without revising the Well Analysis step.
           Review the Data Reduction steps and make the necessary adjustments or
           update the Procedure to define kinetic or scanning analysis to generate a multi-
           index data set.



442 | Troubleshooting




Restoring Optimal Performance
        Numerous factors can affect your computer's performance. If you notice a slowdown
        in Gen5's performance, follow these suggestions:
               Close all other applications, including Internet browsers, when running
                 Gen5
               Do not display Gen5's "Curves" data in the Plate View while performing a
                 kinetic analysis. Wait until the read step is finished before viewing the
                 "Curves" data set. Displaying the Curves data set during a Kinetic read can
                 consume excessive resources resulting in performance degradation. You can
                 drill down to a Well Zoom to monitor the progress of one well, then,
                 leaving the Well Zoom open, change the Matrix Data to a numeric view
               Disable the Calculation Option "Perform data reduction after each read"
                 to give Gen5 sufficient time between obtaining measurements to perform
                 calculations
               Disable the auto-Save options for interim reads: Save Options can be set to
                 free up resources.




System Administrator's Password
        Contact BioTek Customer Care if you've lost or forgotten the System Administrator's
        password: BioTek Customer Care
        The System Administrator's password does not expire, but if a change in personnel, or
        some other cause has resulted in your team not knowing the password, you can
        contact BioTek for a new one.
        Gen5 ships with the System Administrator's password set to "admin."



       Index

                           Symbols
                                                                              individual wells.......................................... 256
                                                                            Applying calculation to raw data............. 256
!exclamation points!....................................317                 Area Scan ..................................... 127, 191, 200
* Asterisks explained ..........................102, 310                    Assay Control.............................................. 223
.glb...................................................................39   Assay Description....................................... 346
.pla...................................................................39   Assign Calibrators ...................................... 223
.prt ...............................................39, 45, 47, 376         Assign Concentrations ............................... 226
.xpt...............................................39, 45, 47, 376          Assign Sample Names
?????...............................................................317       Multiple Plates........................................... 239
[brackets] ................................................39, 317          Assign Standards ........................................ 223
ss-Galactosidase............................................112              Audit Trail Notification ............................. 391
                                                                            Audit Trails

                                   A
                                                                              About ......................................................... 391
                                                                              Exporting ................................................... 392
A260/A280...................................................112
                                                                              User Comments ......................................... 391
                                                                            Audit Trails.................................. 394, 395, 396
About
                                                                            Automatic Sensitivity Adjustment
  Audit Trails ................................................391
                                                                              Fluorescence/Luminescence .............. 159, 169
                                                                            Automatic Sensitivity Adjustment........... 156
  AutoSensitivity ..........................................159
  Data Reductions .................................116, 246
  Fields and Field Groups .............................346                  Automatically-generated data reduction 246
  Fluorescence Analysis ...............................150                                                    B
  Gen5's Tables.............................................320
  Luminescence Analysis .............................153                    Backup files.................................. 374, 379, 380
  Multi-Plate Protocols .................................207                Bandwidth Verification.............................. 169
  Plate Workspace.........................................313               Bandwidth Verification Failed.................. 169
  the Menu Tree..............................................38             Basics .............................................................. 28
Access rights ................................................401           BioTek's Technical Assistance Center........ 41
Acquiring data.............................110, 116, 246                    Bitmaps......................................................... 319
Add                                                                         Blank Read1 ................................................. 316
  Buttons to the toolbar.................................430                Blanks
  New Plate Type..........................................432                 In plate layout ............................................ 223
  New User .............................................15, 400               Subtracting blank plates............................... 58
  Text to a report...........................................346
Adding fields to a report............................349
                                                                              Subtracting blank wells ..................... 246, 259
                                                                            Blanks ..................................................... 58, 223
Administrator, Power User .................18, 399                          Block light between reads.......................... 129
Aligning text in views and reports ...........344                           Build
Append to kinetic file .................................189                   Export File ................................................. 358
Apply calculation                                                             Report ........................................................ 334
  entire plate..................................................256         Buttons



444 | Index



   explained......................................................36       Customize IDs ........................................... 223
   rearrange toolbar ........................................430           Quality or Validation ................................. 301
                                 C
                                                                           Reader Control Panel................................. 417
                                                                         Controls........................................................ 223
Calculation Options                                                      Copying
  Linear Scan ................................................202          Copy and Paste images .............................. 356
Calculation Zone                                                         Copyright information................................ vii
  Defining in Well Analysis .........................196                 Corrected...................................................... 316
  Symbols .....................................................317       Corrected data sets ..................................... 259
Calculation Zone .........................................191            Creating
Calculations                                                               Header and Footer for Reports .................. 349
  formula syntax ...........................................252            New Experiment ........................................ 109
Calibration Curve................................101, 262                  New Protocol ............................................. 112
Calibrator Plates ..................206, 208, 212, 214                     Standard Curve .................................. 101, 262
Calibrator/Standards Plate Protocol112, 212                              Current Password............................... 385, 428
Cell growth studies.....................................189              Curve
CFR Part 11 ....................................................44         4 Parameter ................................................ 266
Change the Format of data values                                           Change the appearance .............................. 330
  In a curve....................................................330        Generate multiple standard curves............. 282
  In a report...................................................344        Minimum number of standards.................. 269
Change the Time Format............................326                      Polynomial................................................. 268
Changing
                                                                           Remove/hide text....................................... 330
                                                                           Standard............................................. 101, 262
  Filter Cartridges/Wheels ............................173
                                                                           Titer ........................................................... 283
  Filter Wheel ...............................................416
                                                                           Using curve from another plate ................. 214
                                                                         Curve ............................................................ 320
  Font ............................................................117
                                                                         Curve Analysis
  On-screen appearance ........................117, 315
  the Procedure/Protocol...............................114
                                                                           Data In ....................................................... 277
                                                                         Curve Analysis.................................... 116, 246
  User's Permissions .....................................398
  Well IDs .....................................................223
  Your Password...................................385, 428               Curve Fit Method........................................ 269
  Your Startup preferences ...........................429                Custom Plate Layout.................................. 229
Check wells periodically ............................144                 Custom Plate Type ..................................... 431
Clarity                                                                  Customize Well IDs.................................... 223
  Controlling .................................................409       Customizing
  Setup ............................................................23     Data Views ................................................ 117
Clipping text ................................................344          Reports....................................................... 338
Close light between reads ..................129, 416                       Toolbar....................................................... 430
Comments                                                                   Well IDs..................................................... 223
  Audit Trail..................................................391         Well Zoom View ....................................... 194
Communication errors ...............................437                  Cutoffs
Concentrations                                                             About ......................................................... 297
                                                                           Formula Syntax.......................................... 298
                                                                         Cutoffs Example.......................................... 298
  Assigning ...................................................226
  Determine by Curve Fit .............101, 262, 278
Concentrations/Dilutions..........................278                                                      D
Connecting a Reader.....................................21
Continuous Shake .......................................139              Data
Controlling the reader ................................123                Change or mask raw data........................... 324
Controls                                                                  Mask/unmask values.................................. 324
  Assign ........................................................223     Data Audit Trail .......................................... 394





Data Files                                                                Plates from an Experiment................. 109, 114
 File Storage ................................4, 12, 47, 371            Delta OD ...................................................... 258
 Maintaining Files ...............................370, 376              Design
 Organizing your Files ..........................10, 372                  Export ........................................................ 352
Data In for Curve Analysis ........................277                    Protocol...................................................... 112
Data points                                                             Difference Between Columns.................... 256
 not showing................................................344         Difference Between Rows.......................... 256
Data Reductions                                                         Digital signature ......................................... 390
 How to set up .....................................116, 246            Dilution Factor ............................................ 252
 Top 5 things to know .................................246              Dilutions............................................... 226, 278
 Validation/Quality Control ........................301                 Dispense reagent
Data Reductions ..................................116, 246                Dispense Rate ............................................ 141
Data Set Naming Convention....................316                         in a Kinetic Analysis.............................. 94, 97
Data Views                                                                in an Endpoint Analysis............................... 95
 Customizing ...............................................117         Dispenser control
 Modifying ..................................................330          Priming ...................................................... 420
Data Views ...................................102, 310, 315               Purging....................................................... 421
Database Configuration .............................374                 Dispenser control........................................ 419
Database Management                                                     Display measurements....................... 102, 310
 Database Utilities .......................373, 376, 379                DNA Purity.................................................. 169
 Error recovery ............................................379         Dual Wavelength
 Maintaining files ........................................376            Data Reduction .................................. 116, 246
 Optimize performance ...............................377                  How to perform dual-wavelength subtraction,
 Plate Types Database .................................431                   Endpoint................................................. 258
 Reduce the size ..........................................381          Duration
 Setting up ...................................................374        Kinetic time course.................................... 186
 Test connection ..........................................374            Long/discontinuous kinetic........................ 189
Decimal places                                                            Pre-Heating................................................ 417
 in Data Reduction ......................................255              Shake Step ................................................. 139
 Setting number of...............315, 323, 328, 330
Default data reduction ...............................246                                                E
Default Protocol...................................120, 223             Edit Report Items ........................................ 344
Default Report .....................................338, 349            Editing
Define method to display data when it's too                               Procedure................................................... 114
 long............................................................344      Report elements ......................................... 338
Defining                                                                Electronic Signature............................ 389, 390
 Concentrations/Dilutions ...........................226                Email............................................................. 356
 Filter cartridges ..........................................175        Email Support................................................ 41
 Procedures..........................................113, 122           Endotoxin Analysis ...................................... 89
                                                                        Endpoint Absorbance
 Reporting requirements..............................334
 Timelines .............................................69, 186
                                                                          Protein Quantification.................................. 66
                                                                        Error bars ..................................................... 330
 User's Permissions .....................................398
Delay .....................................................143, 146
                                                                        Error Messages
Delay before integration (Time-Resolved
 Fluorescence) ...........................................156
                                                                          Communication Errors .............................. 437
Delay Before Sampling...............................156
                                                                          Database Errors.......................................... 379
                                                                        Error Messages............................................ 438
Delay Between Samples .............................156
                                                                        Essential Concepts ........................................ 44
Delete
                                                                        Excel(R)
 Files............................................................376



446 | Index



  Shortcuts not working ................................436               Change ....................................................... 344
Excel(R) ...................................................105, 363        Changing.................................................... 117
Experiment                                                              Font ....................................................... 117, 344
  multiple plates............................................208        Force the curve through the origin........... 268
  printing results ...........................................104       Formula
  setting up....................................................109       Data point .................................................. 319
Experiment vs Protocol ................................45                 Easily Make Corrections............................ 256
Export Builder                                                          Formula ........................................................ 256
  Using..........................................................358    Formula Syntax
Export Builder .....................................117, 359              Cutoffs ....................................................... 298
Export Content ............................................358            Transformations......................................... 252
Export File Settings .....................................359             Validation/QC criteria ............................... 302
Export Multiple Plates................................353                                                G
Exporting
  Results........................................................352    Gen5 Secure ................................................. 398
  Sample IDs.................................................243        Gen5TM Secure Only ............................. 18, 399
  System Audit Trail.....................................396            Getting Technical Assistance ...................... 41
                                 F                                      Getting to Know Gen5 ........................... 28, 44
                                                                        Glow Luminescence ................................... 112
Fast Kinetics ...................................................97     Graph
FDA Electronic Records Compliance .44, 388                                Change the appearance .............................. 194
FDA requirements                                                          Modify ....................................................... 330
      Signature ................................................389     Graph.................................................... 117, 194
Fields and Field Groups .....................347, 350                   Groups
File locations ..................................................47       change........................................................ 398
File Management...................10, 370, 372, 376                     Groups............................................ 18, 398, 399
File Storage...........................4, 12, 47, 370, 371
                                                                                                         H
File types ........................................................47
Filter Cartridges                                                       hash mark..................................................... 344
   Changing a filter cartridge .........................173             Header/footer ............................................. 349
Filter Cartridges ..................................173, 416            Help>About Gen5TM..................................... 41
Filters ....................................................175, 415    Hide the Legend.......................................... 330
Fluorescence Analysis ................................150               How to
Fluorescence Experiment                                                     Set up Kinetic/Time course analysis........ 69
   Filter Set Options .......................................156            Set up kinetic analysis ............................. 69
   Monochromator-based ...............................133                   Create a standard curve.......................... 101
   Processing Modes Comparison..................166                         View results ........................................... 102
   Read Step ...................................................129         Print results ............................................ 104
   Time Resolved ...........................................154             Set up Data Reduction ........................... 116
Fluorescence/Luminescence                                                   Resume a Stop/Resume step.................. 146
   Automatic Sensitivity Adjustment .............159                        Set up Kinetic/Time course analysis...... 186
   Background too high..................................169                 Set up kinetic analysis ........................... 186
   Measurement Options ................................156                  Use the minimum kinetic interval.......... 188
   Readings too low........................................169              Determine kinetic rate............................ 196
   Troubleshooting measurements .................169                        Set up Data Reduction ........................... 246
Fluorescence/Luminescence .....................159                          Perform dual-wavelength subtraction.... 258
FLx800.....................................................21, 419          Create a standard curve.......................... 262
Font                                                                        View results ........................................... 310
                                                                            Mask or change data points/values ........ 324





       Create and customize reports .................336                                                   L
       Change your password...........................385
       Change your password...........................428                 Lag time........................................................ 196
                                                                          Lamp
                                  I                                         tungsten...................................................... 422
Icons                                                                     Lanthanide ions........................................... 154
  explained......................................................36       LD50........................................................ 86, 112
Import Sample IDs......................................242                Learn About
Importing data.............................................110              Buttons......................................................... 28
Improve the transfection............................169                     FDA Electronic records submission .......... 388
Incubation ....................................................417
                                                                            Gen5 Databases ......................................... 373
Individual Well Auto Scaling......................39
                                                                            Plate Workspace ........................................ 313
                                                                          Legend
Industry-standard microplates .................431
Initial Setup Tasks...........................................8
                                                                            show/hide in graphs ................................... 330
                                                                          Light shutter ................................................ 129
Initialize the dispenser ...............................419
                                                                          Linear Scan................................................... 127
INJECT..........................................................317
                                                                          LocalDB ........................................................ 370
Injection assays..............................................97
                                                                          Login
Injectors ..........................................................94
Install Gen5 Secure..........................................8
                                                                            changing another user's password........ 15, 400
                                                                            changing your password .................... 385, 428
Instrument Not Achieving Desired                                            controls/parameters.............................. 17, 386
  Fluorescence Detection Limit ................169                        Long-period kinetic analysis..................... 189
Instrument Over-ranging...........................169                     Low UV Applications................................. 112
Interpolations                                                            Lowry Protein Assay............................ 66, 112
  Curve Analysis...........................................278            Lum............................................................... 316
  Example .....................................................281        Lum/E............................................................ 39
  Formula syntax...........................................279            Luminescence
Introduction ...................................................28          About Luminescence ................................. 153
                                  K                                         Read Step................................................... 135
                                                                            Troubleshooting......................................... 169
KC4..................................................................39
Kinetic                                                                                                    M
  Fast Kinetics for Absorbance.......................97                   Maintain Files .............................................. 401
  Long Interval, Discontinuous.....................189                    Manually entering data.............................. 110
  Monitoring in real time ..............................295               Matrix
Kinetic...................................................191, 295
Kinetic Absorbance Assays........................112
                                                                           Modify ....................................................... 330
                                                                          Matrix ................................................... 102, 310
Kinetic Analysis.....................................69, 186              Max V ........................................................... 196
Kinetic Data Reduction Options listing ..196,                             Mean Maximum OD................................... 196
  291                                                                     Mean Minimum OD ................................... 196
Kinetic Fluorescence .............................69, 186                 Mean V ......................................................... 196
Kinetic Multi-Detection Protocols                                         Measurement Mode.................................... 162
  Restrictions ................................................183        Measurement Options........................ 150, 156
Kinetic Multi-Detection Protocols ............184                         Menu Tree...................................................... 38
Kinetic reads
                                                                          Microplate
  How to create a protocol ......................69, 186
                                                                           Layout samples .................................. 115, 221
  Setting the minimum time interval.............188
Kinetics Time format ..................................326
                                                                           Plate Types ................................................ 431
Known-concentration samples..................223
                                                                           Quick Read ................................................ 100
                                                                           Read........................................................... 110



448 | Index



 Read a blank plate........................................58          Optics Position .................................... 150, 169
Microsoft Word .............................39, 352, 356               Optics Test ........................................... 108, 423
Microsoft(R) Excel 2000 ..........................39, 352                Optimize the database................................ 377
Minimum kinetic interval ..........................188                 OUT+/OUT-................................................ 297
Minimum Number of Standards ..............269                          Outlook......................................................... 356
Minimum Requirements ............................426                   Out-of-range values.................................... 317
Mirrors                                                                Overflow (OVRFLW) ................................. 317
 Dichroic .....................................................177     Overlay multiple curves in one view....... 191
                                                                                                         P
 Mirror Holder Library................................180
 Setting up a mirror .....................................178
Mixing...........................................................123   Page Break
Modify                                                                   add to report............................................... 334
 Fields and Field Groups .............................347              Password
 Graph .................................................194, 330         expired ......................................................... 18
 Matrix View...............................................328         Password, Changing your ................. 385, 428
                                                                       Pathlength Correction ................................ 246
 Reports .......................................................338
Monitor Wells ..............................................144
                                                                       Perform
Monochromator-based reads
                                                                         Calculation................................................. 256
 About Fluorescence Monochromator.........151
Monochromator-based reads ....................133
                                                                         Kinetic analysis.................................... 69, 186
Multi-detection kinetic ...............................183
                                                                         Multiple detection methods ......... 69, 182, 186
                                                                         Quick Read ................................................ 100
Multi-Detection Protocols                                              Performance degradation .......................... 436
 Examples....................................................184       Periodically check wells............................. 144
Multi-Detection Protocols ..........................182                Permissions.................................... 18, 399, 401
Multi-index reads................................102, 310              Plate In/Out ................................................ 146
Multi-Mode Reading                                                     Plate Information ........................................ 230
 See                                                                   Plate Layout................................. 223, 226, 229
                                                                       Plate Reading....................................... 100, 110
    Multi-Detection......................................182
Multi-Plate Protocols
                                                                       Plate Types................................................... 431
                                                                       Plate types currently stored....................... 431
 Plate Layout for..........................................210
                                                                       Plate Types Database.......................... 431, 432
 Running a...................................................209
 Using calibrator/standard curve .........212, 214
Multi-Plate Protocols ..........................207, 208               Plate Workspace
Multiple curves in one view ..............191, 330                       Resizing ............................................. 312, 313
Multiple plates.............................................229        Plate Workspace.......................................... 313
Multiple reads..............................................123        Plate#
Multiple standard curves...................226, 282                      About the workspace ................................. 313
                                                                         Information ................................................ 230
                                N                                        Viewing results .................................. 102, 310
                                                                       Plate>Audit Trail ........................................ 394
Naming                                                                 Plots
 Data points .................................................319        Curves........................................................ 330
 Data Sets ....................................................316
New User Accounts ..............................15, 400
                                                                         Select ......................................................... 330
                                                                       Plots .............................................................. 330
Numeric Format                                                         PMT Sensitivity........................................... 159
 Scientific, Decimal, Best Fit ......323, 328, 330                     Polynomial Regression............................... 269
                                O                                      Polynomial Regression Curve Fit............. 268
                                                                       Positive Control........................................... 223
Onset OD......................................................144      Pound sign ................................................... 344





Power Export                                                            Question marks ........................................... 317
  Run.............................................................365   Quick Read .................................................. 100
Power Export ...............................................365
                                                                                                         R
Power Export Designer ..............................363
Power Export toolbar..................................363               R and R Squared ......................................... 320
Power User.............................................18, 399          Read Step
Preferences                                                               About the Procedures................................. 123
  Startup..........................................15, 400, 429           Fluorescence .............................................. 129
Pre-Heating ..................................................417         Luminescence ............................................ 135
Pre-Read Blank Plate ..............................39, 58                 Spectrum Analysis..................................... 136
Pre-read for specific value .........................144                Read Step ..................................... 100, 135, 136
Print Preview ...............................................334        Read Type .................................... 127, 150, 153
Printing                                                                Reader
  Defining the Report....................................334              Connecting................................................... 21
  Headers and Footers...................................349             Reader............................................................. 21
  Quick Print .................................................104      Reader Control .............................. 44, 123, 417
  Reader test results ......................................424         Reader System Test............................. 108, 423
  Results........................................................118    Reader Test History.................................... 424
Printing.................................................104, 334       Reading Parameters.................................... 123
Privileges                                                              Reading Procedure
  User Permissions........................................401             Defining..................................... 100, 113, 122
Procedure                                                               Read-only permission ................................ 401
  Delay..........................................................143    Reagent dispensing................................. 94, 95
  Discontinuous Kinetic................................189              Reduce database size.................................. 381
  How to change ...........................................114          Reduce photo bleaching............................. 129
                                                                        Reduction Requirements ................... 116, 246
  Monitor wells .............................................144
                                                                        Remove buttons .......................................... 430
  Read Step ...................................................200
                                                                        Repair/compact the database ........... 377, 381
  Validating...................................................125
Procedure .....................................113, 122, 123
Procedure Summary ...................................320                Report Builder ............. 117, 334, 338, 344, 349
Procedure, set up.........................113, 122, 123                 Report Content.................................... 334, 344
Protein Quantification                                                  Reporting
                                                                          method to display data when it's too long.. 344
                                                                        Reporting Engine ........................................ 334
  Endpoint Absorbance...................................66
Protein Quantification ..................................66
Protein Quantitation ...................................112             Reports
Protocol                                                                  Adding fields to ......................................... 350
                                                                          Customizing....................................... 117, 338
  Applying Signature ....................................389
                                                                          Defining..................................................... 334
  Default Setup .............................................120
                                                                          Headers and Footers .................................. 349
  Protocol Folder...............................................5
Protocol.........................................................389
                                                                          Include Sensitivity value............................ 161
Protocol Type
                                                                          Meaning of symbols, asterisks................... 317
                                                                          Rules and Best Practice ............................. 117
  Default Protocol .........................................119           Well Analysis Results................................ 340
  Multi-Plate .................................................206      Reports ......................................................... 334
Protocol vs Experiment ................................45
                                                                        Requirements for plotting a curve.... 101, 262
Protocol's Procedure ...........................113, 122
                                                                        Reset Connection button............................ 374
                                 Q                                      Resize columns and rows .......................... 313
                                                                        Resize the windows.................................... 312
Quality Controls..........................................301           Resolutions .................................................. 438



450 | Index



Restrictions and liabilities........................... vii                Sensitivity
Results                                                                      Determine optimal setting.......................... 159
  Meaning of symbols, asterisks ...................317                       Lower/Raise............................................... 169
  Viewing......................................102, 117, 310                 Report the Sensitivity setting..................... 161
Results...........................................316, 317, 320            Sensitivity............................................. 156, 169
Results Object ..............................................363           Serial read errors......................................... 438
Resume button.....................................110, 146                 Set Temperature Procedure............... 145, 417
Rights and privileges..................................401                 Setting
RNA Quantitation.......................................112                   Start-up Preferences................................... 429
Running                                                                      User's Permissions ..................................... 398
  Multi-Plate Experiment..............................209                  Shake the plate ............................................ 139
Run-Time Prompts                                                           Shared Database.................................... 10, 372
  Creating......................................................231        SharedDB ............................................. 370, 374
  In experiments............................................230            Show
  Include in reports .......................................346              Plate Layout............................................... 313
                                  S
                                                                             Reading results .................................. 102, 310
                                                                           Sign a protocol or experiment................... 390
Sample Control Wells                                                       Sign off.......................................................... 389
  Spiked or Known-concentration ................226                        Signature Reasons....................................... 389
Sample Control Wells.........115, 221, 223, 283                            Signatures .................................................... 389
Sample Dilutions.........................115, 221, 283                     Significant digits ......................................... 323
Sample IDs                                                                 Slow response time from Gen5 ................. 437
  Batch creation ............................................239           Software performance degradation ......... 437
  Erase/Clear IDs ..........................................239            Spectrum ...................................................... 316
  Export.........................................................243       Spectrum Analysis
  Import.........................................................242         Read Step................................................... 136
Sample IDs ...................................235, 242, 243                  Viewing ..................................................... 191
Sample naming............................................235               Spectrum Analysis...................................... 203
Sample Protocols...............................28, 58, 66                  Spiked samples.............................................. 89
Samples.........................................................223        Stand-Alone Multi-Detection Protocol .... 182
Save                                                                       Standard Curve ... 101, 212, 214, 223, 262, 313
  Curves/Graphs as pictures..........................356                   Standard User........................................ 18, 399
  Experiment...................................................45          Standards
  Protocol......................................109, 112, 125                Assigning........................................... 223, 263
Save .................................................................48     Minimum Number ..................................... 269
Scales for Kinetic Reads................................39                 Startup Preference ...................................... 429
Scan Options ........................127, 191, 200, 203                    Statistics
Scanning Data Reduction Options listing291                                   Inter-Plates................................................. 209
Scientific notation and significant digits                                 Statistics................................................ 102, 310
  in Data Reduction ......................................255              StepWiseTM................................................... 123
Scientific notation and significant digits.323,                            Stop/Resume............................... 110, 143, 146
  330                                                                      Subtracting a blank plate read .................... 58
Security                                                                   Symbols and special notations.................. 317
  Audit Trails ................................................391         Synergy 2...................................................... 131
  Digital Signatures.......................................389             Synergy 4...................................................... 133
  File Storage ......................................4, 12, 371            Synergy HTTR............................... 21, 182, 183
                                                                           Synergy HTTR w/Injectors ......... 94, 416, 419
  User Accounts......................................15, 398
Selecting Data Sets ......................................255
                                                                           Syntax





  in formulas                                                              Tutorials ......................................................... 28
                                                                                                            U
     Cutoffs....................................................298
     Interpolations .........................................279
     Transformations .....................................252              Upgrade utility............................................ 374
     Validation/Quality Control ....................302                    Use first filter set sensitivity.............. 156, 159
System Administrator
                                                                           User Groups
  Changing password......................................14
                                                                             Defining/Modifying................................... 401
                                                                           User Groups................................... 18, 398, 399
  To Do List ......................................................8
System Audit Trail
                                                                           Users ..................................... 5, 15, 18, 398, 399
                                                                           User's Permissions
  Exporting ...................................................396
  Viewing......................................................396
System Test ..........................................108, 423               Changing your password ................... 385, 428
System> Security.........................................384
                                                                             Setting................................................ 398, 401
System-generated data reduction .............246
                                                                             User's Account..................................... 15, 400
                                                                           User's Permissions ...................................... 401
                                  T
                                                                                                            V
Table..............................................................320
                                                                           Validate
TAC .................................................................41
Technical Assistance.............................41, 438
                                                                             Procedures ................................................. 125
                                                                             Set up quality controls for experiment....... 301
Temperature                                                                Validation Criteria ...................................... 301
  Incubation during an experiment ...............145                       Validation Examples .................................. 304
  Pre-heading the Reader ..............................417                 Viewing
Temporary Files...........................................373
Text
                                                                             Audit Trails................................ 394, 395, 396
                                                                             AutoSensitivity .......................................... 161
  not fully displayed......................................344               Excel(R) ....................................................... 358
Time                                                                         Results ............................................... 102, 310
  hours, seconds format ................................326                  System Audit Trail..................................... 396
Time to Peak ................................................196             Well Analysis ............................................ 191
Time-Resolved Fluorescence .....................154                        Viewing Data
Titer Assay ...................................................112           Customizing views ............................ 117, 194
Titer Curve ...................................................283           Defining Data Views ................................. 315
Toolbar                                                                      Masking data point .................................... 325
  Buttons and Icons Guide..............................36                    Modify views..................................... 328, 330
  Customize ..................................................430            Well Zoom................................................. 191
Top Probe Vertical Offset...........................169                    Viewing Data............... 117, 191, 194, 320, 330
Trademarks ................................................... vii         Viewing Preferences............................. 24, 328
Transformation............................................256              Viewing Results
Transformation formula syntax ................252                            Method to display data too long to fit........ 344
Troubleshooting                                                            Viewing Results ............................ 24, 102, 310
  Communication Errors...............................437                                                    W
  Fluorescence/Luminescence Measurements
      ...............................................................169   Well Analysis Data Reduction . 191, 196, 246,
  Restore optimal performance.....................442                       290
Troubleshooting ..........................................436              Well Analysis Results Table ...... 191, 320, 340
Truncated text..............................................344            Well IDs................................................ 223, 252
Tungsten lamp control ...............................422                   Well Settings................................................ 226
Turn on/off incubator ................................145                  Well Zoom
Turn on/off lamp........................................422                 Modify view ...................................... 194, 330



452 | Index



 Monitor experiment ...................................295           Introduction ................................................. 28
 Report multiple wells simultaneously........340                     Plate View.................................................. 313
 View multiple wells simultaneously..........191                    Wrong pH .................................................... 169
Well Zoom View
 Customizing ...............................................194                                    X
Well Zoom View .........................................194         X Axis/Y Axis ............................................. 330
Wells to Monitor..........................................144
Windows Explorer ........................................47                                        Y
WordPad ......................................................356   Y Axis Intercept........................................... 268
Workspace
