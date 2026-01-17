# Front Matter

# Gen5 User Guide (Agilent BioTek)




Gen5TM & Gen5 Secure
User's Guide
Microplate Data Collection & Analysis Software




BioTek(R) Instruments, Inc.
July 2007
(c) 2006-2007
PN 5321001
Revision D







Contents

      Notices ................................................................................ vii
      About this Guide ................................................................... viii

Chapter 1: Initial Setup............................................................. 1
      Set up Gen5......................................................................... 2
      Set up Gen5 Secure .............................................................. 8
      Set up Gen5 Reader Control................................................... 20
      Connecting a Reader ............................................................. 21
      Setting up the Clarity Luminometer......................................... 23
      Setting up Preferences .......................................................... 24

Chapter 2: Getting Started ........................................................ 27
      Getting Started..................................................................... 28
      Gen5's Workspace ................................................................ 30
      About the Plate Workspace .................................................... 32
      Introducing the Protocol Workspace ........................................ 33
      Gen5's Wizard ...................................................................... 35
      Buttons and Icons Guide........................................................ 36
      About the Menu Tree............................................................. 38
      Tips for KC4 Users ................................................................ 39
      Getting Technical Assistance .................................................. 41

Chapter 3: Essential Concepts ................................................... 43
      Essential Concepts ................................................................ 44
      Experiment vs. Protocol ......................................................... 45
      About File Storage ................................................................ 47
      Best Practices....................................................................... 48

Chapter 4: Assay Examples ....................................................... 51
      Sample Protocols and Experiments ......................................... 52
      How do I set up my assay? .................................................... 54
      Quantitative ELISA Example ................................................... 55
      Subtracting Blank Plate Reads ................................................ 58







ii|



      Pathlength Correction Example ............................................... 60
      Dual Wavelength Absorbance Endpoint .................................... 62
      Basic Spectrum Analysis ........................................................ 64
      Protein Quantification: Endpoint Absorbance ............................ 66
      Basic Fluorescence Assay Example .......................................... 69
      Kinetic Fluorescence Assay Example........................................ 71
      Fluorescence Assay with Injection........................................... 74
      Fluorescence Area Scan Example ............................................ 77
      Fluorescence Polarization Example .......................................... 79
      Basic Luminescence Glow Assay Example ................................ 81
      Luminescence Flash Assay with Injection ................................. 82
      Max Binding Determination/Competitive Assay ......................... 83
      Toxicity/Cytotoxicity Assay .................................................... 86
      Endotoxin Test ..................................................................... 89
      ss-Galactosidase .................................................................... 92
      Dispensing Reagent .............................................................. 94
      Fast Kinetics with Injection for Absorbance .............................. 97

Chapter 5: Basic Tasks .............................................................. 99
      Quick Read .......................................................................... 100
      How to Create a Standard Curve............................................. 101
      Viewing Results .................................................................... 102
      Printing Results .................................................................... 104
      Quick Export ........................................................................ 105
      Quick Output Options ............................................................ 106
      Reader System Test .............................................................. 108
      Setting up an Experiment ...................................................... 109
      Read a Plate......................................................................... 110
      Acquiring Data ..................................................................... 110

Chapter 6: Designing a Protocol................................................ 111
      Design a Protocol.................................................................. 112
      Defining the Reading Procedure .............................................. 113
      Modify a Protocol .................................................................. 114
      Defining the Plate Layout ....................................................... 115








      Setting up Data Reduction ..................................................... 116
      Customizing Data Views, Reports, and Exports ......................... 117
      Reporting Results ................................................................. 118
      Using the Default Protocol...................................................... 119
      Default Protocol Setup........................................................... 120

Chapter 7: Defining the Procedure ............................................ 121
      Defining the Reading Parameters ............................................ 122
      Validate the Procedure .......................................................... 125
      Read Step............................................................................ 127
      Procedure Steps: Reading-Related Activities ............................ 138

Chapter 8 : Fluorescence and Luminescence ............................. 149
      Fluorescence Analysis............................................................ 150
      Luminescence Analysis .......................................................... 153
      Time-Resolved Fluorescence Analysis ...................................... 154
      Fluorescence Polarization ....................................................... 155
      Filter Set Options.................................................................. 156
      PMT Sensitivity ..................................................................... 158
      Measurement Options ........................................................... 162
      Synchronized Modes ............................................................. 164
      Troubleshooting Fluorescence/Luminescence............................ 169
      Filters and Mirrors................................................................. 173
      Multi-Detection/Multi-Mode Protocols ...................................... 182
      Features and Restrictions of Kinetic Multi-Detection Protocols..... 183

Chapter 9: Kinetic Analysis ....................................................... 185
      How to set up a Kinetic Analysis ............................................. 186
      Kinetic Minimum Interval ....................................................... 188
      Discontinuous Kinetic Procedure ............................................. 189
      Well Zoom ........................................................................... 191
      Well Analysis Calculation Types .............................................. 196

Chapter 10: Scanning Analysis Options ..................................... 199
      Area Scan ............................................................................ 200
      Linear Scan.......................................................................... 202






iv|



      Spectrum Scan ..................................................................... 203

Chapter 11: Multi-Plate Protocols ............................................. 205
      Designing a Multi-Plate Protocol.............................................. 206
      About Multi-Plate Protocols .................................................... 207
      Running a Multi-Plate Protocol ................................................ 209
      Calibrator-Plate Protocols....................................................... 212
      Multi-Plate Assay Protocols .................................................... 215
      Processing a Batch of Samples ............................................... 218

Chapter 12: Preparing Plates .................................................... 219
      Defining the Plate Layout ....................................................... 221
      Assigning Well IDs ................................................................ 223
      Custom Plate Layout ............................................................. 229
      Plate Information.................................................................. 230
      Runtime Prompts .................................................................. 231
      Assigning Sample IDs............................................................ 235

Chapter 13: Data Reduction Options ......................................... 245
      Setting up Data Reduction ..................................................... 246
      Define Transformations ......................................................... 249
      Plotting a Curve.................................................................... 261
      Curve Fit ............................................................................. 264
      Multiple Curves..................................................................... 282
      Troubleshooting Curve Fits..................................................... 288
      Kinetic Analysis Options......................................................... 289
      Define Cutoffs ...................................................................... 296
      Validation ............................................................................ 301
      Fluorescence Polarization ....................................................... 307

Chapter 14: Viewing Results ..................................................... 309
      Viewing Results .................................................................... 310
      Data Views .......................................................................... 315
      Data Set Naming Convention ................................................. 316
      Symbols and Special Notations ............................................... 317
      Data Points Reference ........................................................... 319









      Gen5's Tables....................................................................... 320
      Modify/Customize Views/Data ................................................ 323

Chapter 15: Reporting Results .................................................. 333
      Building Reports ................................................................... 334
      How to create and customize a report ..................................... 336
      Customizing Reports ............................................................. 338
      Reporting Well Analysis Results .............................................. 340
      Edit Report Items ................................................................. 344
      Fields and Field Groups.......................................................... 346

Chapter 16: Exporting Results .................................................. 351
      Exporting Results.................................................................. 352
      Quick Export ........................................................................ 354
      Right-Click Menu Options ....................................................... 356
      Export to File (File Export Builder) .......................................... 358
      Power Export........................................................................ 362

Chapter 17: Managing Files ....................................................... 369
      Managing Files ..................................................................... 370
      File Storage ......................................................................... 371
      Database Management .......................................................... 372
      Database Errors.................................................................... 379

Chapter 18: Security ................................................................. 383
      Security............................................................................... 384
      Changing Your Password........................................................ 385
      Login/Password Controls........................................................ 386
      FDA's 21 CFR Part 11 ............................................................ 388
      Signing Protocols .................................................................. 389
      Audit Trail............................................................................ 391
      User Accounts ...................................................................... 398

Chapter 19: Reader Control....................................................... 405
      When you have Two Readers ................................................. 406
      Reader Configuration ............................................................ 408
      Controlling the Clarity ........................................................... 409





vi|



      Reader Settings .................................................................... 413
      Reader Control Panel............................................................. 417
      Testing the Reader................................................................ 423

Chapter 20: System Management.............................................. 425
      System Requirements ........................................................... 426
      Gen5's System Administrator ................................................. 427
      Changing Your Password........................................................ 428
      Changing Your Startup Preferences ......................................... 429
      Customize the Toolbar........................................................... 430
      Plate Types Database ............................................................ 431

Chapter 21: Troubleshooting..................................................... 435
      Troubleshooting.................................................................... 436
      Communication Errors: Reader to Computer ............................ 437
      Error Messages..................................................................... 438
      Calculation Warnings............................................................. 439
      Restoring Optimal Performance .............................................. 442
      System Administrator's Password ........................................... 442

Index ........................................................................................ 443











Notices

          Highland Park, P.O. Box 998
          Winooski, Vermont 05404-0998 USA


      All Rights Reserved
              (c) 2007, BioTek(R) Instruments, Incorporated. No part of this publication may be
              reproduced, transcribed, or transmitted in any form, or by any means electronic
              or mechanical, including photocopying and recording, for any purpose other
              than the purchaser's use without written permission of BioTek Instruments,
              Inc.



      Trademarks
              BioTek(R) is a registered trademark, and Gen5TM, SynergyTM 4, SynTMrgy"! 2,
              SynergyTM HT, and other instrument logos are trademarks of BioTek
              Instruments, Inc. Microsoft(R), Windows(R), and the Windows logo are registered
              trademarks of Microsoft Corporation in the United States and other countries.
              All other trademarks are the property of their respective holders.



      Restrictions and Liabilities
              Information in this document is subject to change and does not represent a
              commitment by BioTek Instruments, Inc. Changes made to the information in
              this document will be incorporated in new editions of the publication. No
              responsibility is assumed by BioTek for the use or reliability of software or
              equipment that is not supplied by BioTek or its affiliated dealers.







viii|




About this Guide
         This user guide is intended for licensed users of Gen5TM and Gen5TM Secure, BioTek's
         microplate data collection and analysis software.


Document Conventions

             Special or important information uses this format to call your attention
               to it.



             Tips or suggestions, for example, to improve performance, are shown in this
           manner, following a light bulb graphic.



        Navigation instructions for the current topic are presented in this format




Document History

             Revision     Date             Changes
                 A        May 2006         Initial Release
                 B        Sept 2006        New features related to the SynergyTM 2 reader and
                                           Filter Wheel Library
                 C        March 2007       Added description of new features and
                                           enhancements released in Gen5 version 1.02
                 D        June 2007        New features related to the SynergyTM 4 reader and
                                           enhancements released in Gen5 version 1.04
