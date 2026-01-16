# Gen5 Reading DesigningProtocols etc

Microplate Data Collection & Analysis Software

Gen5

TM

Getting Started Guide

---

---

Gen5(TM)
Getting Started Guide
Microplate Data Collection and Analysis Software

(C) 2017
BioTek(R) Instruments, Inc.
PN 5321045 Rev L

---

2|

Notices
BioTek(R) Instruments, Inc.
Highland Park, P.O. Box 998
Winooski, Vermont 05404-0998
USA

All Rights Reserved
(C) 2017, BioTek Instruments, Incorporated. No part of this documentation may be reproduced,
transcribed, or transmitted in any form, or by any means electronic or mechanical, including
photocopying and recording, or any purpose other than the purchaser's use without written
permission of BioTek Instruments, Inc.
Restrictions and Liabilities
Information in this documentation is subject to change, and does not represent a commitment by
BioTek Instruments, Inc. Changes made to the information in this document will be incorporated in
new editions of the documentation.
No responsibility is assumed by BioTek for the use or reliability of software or equipment that is not
supplied by BioTek or its affiliated dealers.
Trademarks
BioTek(R) is a registered trademark and 800 TS(TM), BioCell(TM), BioStack(TM), Cytation(TM), ELx800(TM), ELx808(TM),
Eon(TM), Epoch(TM), FLx800(TM), Gen5(TM), Lionheart(TM) FX, PowerWave(TM), Precision(TM), Precision Power(TM),
StepWise(TM), Synergy(TM), and Take3(TM) are trademarks of BioTek Instruments, Inc.
Microsoft(R), Internet Explorer(R), Windows(R), and Excel(R) are either registered trademarks or trademarks
of Microsoft Corporation in the United States and/or other countries.
All other trademarks are the property of their respective holders.

BioTek Instruments, Inc.

---

Contents | 3

Contents
Notices
Contents
Revision History
Install Gen5
Gen5 License Agreement and Warranty
Computer System Recommendations
Gen5/Instrument Compatibility Chart
Gen5 Software Level Comparison
Install the Software on a PC
Recommended Installation Sequence for Imaging
Install the USB 3 Camera Driver
Establish Communication with the Camera
Change the Virtual Memory Settings
Defining the Image Library
Disable Sleep Mode
Turn Off Automated Updates
Storing Gen5 Files on an External Hard Drive
Register with BioTek
Initial Setup
Connect an Instrument
Set Up Gen5, Gen5 Image+, and Gen5 Image Prime
Set Up Gen5 Secure, Gen5 Secure Image+, or Gen5 Secure Image Prime
Set Up Gen5 IVD or Gen5 IVD Image+
Set Up Gen5 Reader Control
System Administrator's To-Do List
Change the System Administrator's Password
About Gen5 Databases
About User Accounts
About User Groups
Login/Password Controls
Configure Windows Authentication
Configure the Email Notification Feature
Getting Started
Task Manager
The Gen5 Workspace
Protocol Workspace
The Menu Tree
Buttons and Icons
Troubleshooting

Gen5 Getting Started Guide

2
3
5
7
8
10
11
14
15
17
17
18
19
20
20
20
20
20
23
24
25
25
26
26
27
28
29
32
32
35
36
38
39
40
41
43
44
45
47

---

4|

Getting Technical Assistance
Essential Concepts
Experiment vs. Protocol
About File Storage
Best Practices
Basic Tasks
Quick Read
Create a Standard Curve
View Results
Print Results
Test the Instrument
Set Up a Protocol
Design a Protocol
Define the Reading Procedure
Define the Plate Layout
Set Up Data Reduction
About Exporting Results
About Reports
Index

52
53
54
55
57
59
60
60
61
62
63
65
66
66
67
69
70
71
73

BioTek Instruments, Inc.

---

Revision History | 5

Revision History
Rev

Date

Changes

I

2/2015

Minor text edits, updated references to Windows 8 to
Windows 8.1; added .tif files to list of file types Gen5
creates

J

7/2015

Updated the System Recommendations, added chart
describing hard drive space requirements for various
imaging scenarios, added Gen5/Instrument Compatibility
Chart, removed imaging-specific setup instructions.

K

7/2016

Removed references to Windows XP and Excel 2003; added
support for Windows 10; added support for Lionheart FX,
added Gen5 Image Prime and Gen5 Secure Image Prime

L

2017

Added support for the Cytation 1 and 800 TS.

Gen5 Getting Started Guide

---

6|

---

Install Gen5
An "install wizard" guides you through the installation of Gen5--just follow the
prompts. Before doing so, make sure your computer and BioTek instruments meet
the system requirements outlined in this section. You may also want to review the
installation options, software warranty, and related information.

Gen5 License Agreement and Warranty

8

Computer System Recommendations

10

Gen5/Instrument Compatibility Chart

11

Gen5 Software Level Comparison

14

Install the Software on a PC

15

Recommended Installation Sequence for Imaging

17

Install the USB 3 Camera Driver

17

Establish Communication with the Camera

18

Change the Virtual Memory Settings

19

Defining the Image Library

20

Disable Sleep Mode

20

Turn Off Automated Updates

20

Storing Gen5 Files on an External Hard Drive

20

Register with BioTek

20

---

8 | Install Gen5

Gen5 License Agreement and Warranty
License Agreement
BioTek Instruments, Inc. (also referred to as BioTek) has developed Gen5 Microplate Software for
Windows. The price paid for this software includes the license granting the purchaser a nonexclusive use of the Gen5 product per the guidelines given below.
Gen5: The purchase of Gen5 RC, Gen5 Image Plus, Gen5 Secure Image Plus, Gen5 Image Prime and
Gen5 Secure Image Prime entitles the installation of the licensed copy on up to two (2) computers
for simultaneous use. The purchase of Gen5 entitles the installation of the licensed copy on up to
five (5) computers for simultaneous use. The purchase of Gen5 Secure entitles the installation of the
licensed copy on up to twenty five (25) computers for simultaneous use. The purchase of Gen5 IVD
entitles the installation of the licensed copy on up to twenty-five (25) computers for simultaneous
use. The installation of Gen5 on one computer for the purpose of controlling one or two BioTek
microplate readers at a time is expressly permitted. Simultaneous use of the software on other
computers solely for the purpose of analyzing, reporting and otherwise working with data already
collected is expressly permitted.
This license agreement does not grant the user title to the software or any copyrights of proprietary
rights in the software. The user may not sublicense, rent, lease, modify, translate, decompile or
disassemble the software for any purpose. The license is not a sale of the original software or any
copy.
For Gen5 Image Prime or Gen5 Secure Image Prime: The product is provided under an intellectual
property license from Life Technologies Corporation. The transfer of this product is conditioned on
the buyer using the purchased product solely for research and development purposes and for the
purposes of research or development services (including under contract or as fee for service test) to
generate results that are used solely for the internal research and development activities and other
internal purposes of a client, including quality control and quality assurance. The buyer must not
sell or otherwise transfer this product or its components for (a) diagnostic, therapeutic or
prophylactic purposes; and (b) resale, whether or not resold for use in research. For information on
purchasing a license to this product for purposes other than as described above, contact Life
Technologies Corporation, 5791 Van Allen Way, Carlsbad, CA 92008 or outlicensing@lifetech.com.

Limited Warranty
BioTek warrants that for a period of ninety (90) days from the date of shipment, the software
product manufactured and sold by BioTek will conform, as to all substantial operational features, to
BioTeks then current published specifications (meaning those specifications in effect as of the date
of purchase), and will be free of defects which, in BioTeks sole judgment, substantially affect system
performance. This warranty is limited to the original purchaser and cannot be assigned or
transferred. All claims under this Limited Warranty must be made in writing to BioTek, Attention:
Service Department or to BioTeks authorized representative or dealer. The purchaser must notify
BioTek within ninety (90) days after the date of shipment of the software to the purchaser of any
claim under this limited warranty. This 90-day period shall not be extended by the delivery or receipt
of any subsequent modifications to the software. Modifications to the software within a version
(Updates) are expressly excluded from the terms of this warranty. If the software is found to be
defective by BioTek, BioTeks sole obligation under this warranty is to use efforts consistent with

BioTek Instruments, Inc.

---

Gen5 License Agreement and Warranty | 9

BioTeks regular business practices to attempt to remedy such a defect. In no event shall BioTeks
liability under this Warranty exceed the original purchase price of the software.
This warranty shall be null and void if the purchaser makes any modifications to the software.
Correction of difficulties of defects traceable to Purchasers errors or system changes shall be billed
to the purchaser at BioTeks standard time and material charges.

Gen5 Getting Started Guide

---

10 | Install Gen5

Computer System Recommendations
To achieve the best Gen5 performance, BioTek offers the following recommendations.

Non-Imaging Use
l

l

Windows 7 Professional Editions (with SP1), or Windows 10 Professional Editions
Intel Celeron Dual Core Processor T1600 (1.66 GHz, 667 MHz FSB, 1 MB L2 cache) or
equivalent

l

2 GB RAM or higher

l

100 GB free hard drive space or higher

l

Monitor resolution 1024 x 768 or higher

l

Keyboard/mouse

l

l

l

Microsoft Internet Explorer v5.0 or higher (for online Help); for Take3 XTML export,
Internet Explorer v10 or higher
Microsoft Excel 2007 or later for QuickExport and Power Export (excluding Excel 2010 and
Excel 2013 64-bit)
Serial or USB port for BioTek instrument

Imaging
The drivers and firmware should be updated only by BioTek personnel.
l

64-bit version of Windows 7, or Windows 10, Professional editions

l

Intel Core i5 processor or higher

l

Intel 8 USB chipset or higher

l

8 GB RAM or greater

l

128 GB hard drive space or greater*

l

Monitor resolution 1600 x 900 or higher**

l

Software:
l

l

Gen5 v2.09 or higher: Gen5 Image+, Gen5 Secure Image+, or Gen5
IVD Image+, or any edition of Gen5 Image Prime. Spot Counting add-on
module is required for this advanced level of imaging cellular analysis.

Keyboard and mouse

BioTek Instruments, Inc.

---

Gen5/Instrument Compatibility Chart | 11
l

Connectivity:
l

USB 3 port for camera

l

USB 2 or 3 port for instrument

* Each image is approximately 2 MB in size. Image file management is the responsibility of the user. An
RJ-45 Lan connector is recommended for network use. Do not use a WiFi network connection.
** Gen5 is not designed for use on very high resolution monitors, e.g., 4K or 5K monitors.
Instruments with FireWire cameras or host computers that do not meet the recommended
configurations: Contact BioTek TAC for alternative instructions.
Gen5 will run on a computer system that meets the minimum requirements for most
applications. For very fast kinetic reactions in multiple wells, especially in higher density plates
where large amounts of data are captured, and for imaging, BioTek recommends a 2 GHz
processor speed and at least 8 GB RAM for best performance.

Example: Required Hard Drive Space for Imaging
Imaging Parameters

Space Required

1 image

2 MB

96-well plate, 1 image per well

192 MB (96 images x 1 color x 2 MB)

96-well plate, RGB, 1 field of view per
well

576 MB (96 wells x 3 colors x 2 MB)

96-well plate, DAPI, z-stack, 10 slices per
well

1.9 GB (96 wells x 1 color x 10 z-planes x 2
MB)

96-well plate, RGB, z-stack, 10 slices per
well

5.8 GB (96 wells x 3 colors x 10 z-planes x
2 MB)

1 tissue section slide, RGB, 4x3 montage

72 MB (1 sample x 4 x 3 x 3 colors (RGB) x 2
MB)

1 H&E slide, whole sample, 15x15
montage

1.4 GB (1 sample x 15 x 15 x 3 colors (RGB) x 2
MB)

Gen5/Instrument Compatibility Chart
Verify that the basecode built into your BioTek instrument is compatible with Gen5.
If your instrument reveals a basecode with a version number lower than those provided here,
please contact TAC for instructions for downloading and installing updated software.

Gen5 Getting Started Guide

---

12 | Install Gen5

Product

Compatible Compatible
Basecode PN Basecode Gen5
Notes
Version
Version

800 TS

1560200

All versions

3.03

Lionheart FX

1450200

All versions

3.0-current

Cytation 1

1650200

All versions

3.03

Cytation 3

1220200

1.04 and
1.05

2.04

Cytation 3

1220200

1.14

2.05-
current

Cytation 5

1320200

All versions
(1.05)

2.07-
current

ELx800

7330202

3.07

1.00-
current

ELx808

7340201

3.15

1.00-
current

Eon

1020200

All versions
(1.00)

2.00-
current

Epoch

7200200

All versions
(1.07)

1.09-
current

Epoch 2

1330200

All versions
(1.06)

2.06-
current

FLx800

7080207

1.15

1.00-
current

PowerWave

7280201

1.21.1

1.00-
current

PowerWaveXS

7300200

1.06

1.00-
current

PowerWaveXS2 7300205

All versions
(1.08)

1.02-
current

Synergy 2

7130202

1.06

1.01-
current

Use of Synergy 2/4 universal basecode
7160204 (version 1.12 or higher) requires
Gen5 version 1.04 or higher.

Synergy 4

7160204

All versions
(1.08)

1.04-
current

Synergy 2/4 basecode combined at version
1.12.

Synergy H1

8040200

All versions
(1.01.1)

1.11-
current

Basecode 2.00 with S2-DIP2 toggled for
gradient incubation requires Gen5 2.01 or
higher.

Adds ability for 40x and 60x objectives and
Gen5 Image+

ELx800 TS

PowerWaveHT

BioTek Instruments, Inc.

---

Gen5/Instrument Compatibility Chart | 13

Product

Compatible Compatible
Basecode PN Basecode Gen5
Notes
Version
Version

Synergy H1

8040200

2.10

2.09-
current

Synergy H4

8030200

All versions
(1.00.1)

1.10-
current

Synergy HT

7090202

2.24

1.00-
current

Synergy HTX

1340200

All versions
(1.02)

2.06-
current

Synergy Mx

7190200

All versions
(1.01.0)

1.07-
current

Synergy Neo

1030200

All versions
(1.03)

2.01-
current

Synergy Neo2

1350200

All versions

2.09-
current

Gen5 Getting Started Guide

Added feature of dynamic extended range for
fluorescence reads. Requires PMT calibration
by service if upgrading from version 2.0 or
earlier.

---

14 | Install Gen5

Gen5 Software Level Comparison
BioTek offers ten levels of Gen5, from the most basic Reader Control utility to the full-featured,
imaging-capable, and FDA-compliant Gen5 Image+ IVD.
Check out www.biotek.com for a detailed breakdown of the distinctions between software
levels.

BioTek Instruments, Inc.

---

Install the Software on a PC | 15

Imaging-Specific Capabilities

Install the Software on a PC
On new computers, install Microsoft Office before installing Gen5.

Gen5 Getting Started Guide

---

16 | Install Gen5

See See Recommended Installation Sequence for Imaging on page 17 for imaging-specific
installation instructions.

Prerequisite
Gen5 requires the user who is installing the application to have Administrator privileges for the
Windows operating system. If a user with restricted access attempts to install the application, errors
may occur. Contact your organizations system administrator if you are uncertain about your
privileges.
BioTek strongly recommends running a Windows Update to ensure the latest Windows security
fixes and critical updates are installed prior to installing Gen5.

Install Gen5 (all versions on a PC)
1. Start Windows.
l

Be sure you have administrative privileges.

2. Follow the instructions from the insert, Installing Gen5 from a USB Stick, found on the
inside of the USB stick case.
The Typical installation option is strongly recommended for most users (see below).
Gen5 asks for the serial number shown on your product packaging. Enter it and click Continue
to save time later. If the number is unavailable you can click Cancel and provide this information
later.
Be sure to register with BioTek for the fastest response from our support team, should the need
arise.

Custom vs. Typical Installation
The Typical installation option is recommended for most users. It installs:
l

Gen5 application (Gen5.exe and supporting files)

l

Gen5 Diagnostic module

l

Gen5 Take3 module

For Custom installations, click the arrow next to a feature to display the options menu. Select the
desired option. When you opt to not install a feature, its disk icon is replaced with a red X.

Printer Settings (Windows 10)
When you install Gen5 on a computer with Windows 10, you may need to disable the Let Windows
manage my default printer setting. Otherwise, the default printer for your computer changes every

BioTek Instruments, Inc.

---

Recommended Installation Sequence for Imaging | 17

time you a different printer. Note that this option is not always present.
1. From the main screen, click Settings > Devices > Printers & scanners.
2. In the Let Windows manage my default printer box, turn off the option.

Gen5 OLE Automation Toolkit
Custom installation is required during software installation to install the Gen5 OLE Automation
Toolkit for programming robotic instruments to use Gen5. Instead of selecting the Install Wizards
default option for Typical installation, select Custom. Change the setting for OLE Automation Toolkit
to install this feature.
Gen5 installs an OLE Automation folder when this option is selected. Youll find the Gen5
Automation Programmers Guide (in PDF format), the BTIStatusCodes.h file, and a Samples folder
containing several program samples in common programming languages.
To learn about security options when using OLE Automation, see Login/Password Controls in
the Gen5 Help.

Recommended Installation Sequence for Imaging
Following the detailed installation instructions provided in the imaging instrument's operator's
manual, perform the following steps for the best experience:
1. Set up the hardware components as applicable, including:
l

Removing the shipping hardware from the instrument

l

Connecting the gas controller, dispenser, and joystick

2. Install Gen5 on the host computer.
3. Install the USB driver software shipped on the Gen5 software USB flash drive.
The instructions for installing the USB driver are included in the Gen5 USB flash drive.
4. Connect the instrument to the host computer with the USB cable.
5. Connect the USB 3 camera cable to a USB 3 port, and power on the instrument.
6. Install the USB 3 camera driver.

Install the USB 3 Camera Driver
You must install the Gen5 software and connect the instrument to the host computer via both
USB cable and USB 3 camera cable before performing this procedure.

Gen5 Getting Started Guide

---

18 | Install Gen5

1. Navigate to the Gen5
program files on your
computer, for example,
C:\Program Files\BioTek\Gen5
<version>.
2. Open the USB 3 Drivers
folder, the Windows_64
folder, and the PGRUSBCCam
folder.
3. Right-click Install
PGRDriver.bat, and select Run
as Administrator to run the
driver installer.

Establish Communication with the Camera
1. From the main Gen5 screen, select System > Instrument Configuration, select your
instrument, and then click View/Modify.
2. Click Test Communication.
3. Click Camera Information. If communication is successful, Gen5 displays information
about the camera.
Check the Bus Speed; it should be 5000 Mbits/sec. If a lower bus speed is reported, review the
troubleshooting information next.

Troubleshooting Software Drivers
Some suggestions for troubleshooting either communication with the camera or a bus speed
significantly lower than 5000 Mbits/sec follow:
l

Reboot the host computer.

l

Disconnect and reconnect the USB 3 cable from/to the host computer.

l

Rerun the batch (.bat) file as described in step 3 of Install the USB 3 Camera Driver.

l

Make sure the computer meets the recommended requirements.

If problems persist, ask your IT group for support or contact TAC@BioTek.com.

Disable "CPUHalt" Batch File
Gen5 provides a batch file from the camera manufacturer, Point Grey Research, Inc., that repairs
image acquisition problems. The fix disables the processor's idle state or halt routine to prevent it
from interrupting Gen5's processing.
This file is supported on the Windows 7 operating system only.

BioTek Instruments, Inc.

---

Change the Virtual Memory Settings | 19

Depending on your version of Gen5, follow the path to the batch files:
Gen5 3.0 (or higher)

C:\Program Files\BioTek\Gen5 3.00\Camera
Utilities\HaltStateFix

Gen5 2.9 (or lower)

C:\Program Files(86)\BioTek\Gen5 2.x\Camera
Utilities\HaltStateFix

Four files are provided: two run the PGRIdleStateFix.exe to either enable or disable the function.
l

PGRIdleStateFix.exe

l

Disable CPUHalt.bat: Stops the computer's idle state routine

l

Enable CPUHalt.bat: Restores the computer's idle state routine

l

Query CPUHalt State.bat: Displays the current state
1. Right-click Disable CPUHalt.bat and select Run as administrator to run the batch file.
2. Run Enable CPUHalt.bat to reverse the setting.

When running a laptop, keep it plugged into an electrical supply to prevent battery depletion
from interrupting Gen5.

Change the Virtual Memory Settings
For instruments with the imaging module, it is recommended that you not allow Windows to
automatically manage paging file size.
1. From the Windows Start menu, go to Control Panel, and select System.
2. In the left pane, select Advanced system settings.
3. In the System Properties dialog, on the Advanced tab in the Performance area, click
Settings.
4. In the Performance Options dialog, on the Advanced tab in the Virtual memory area, click
Change.
5. Clear Automatically manage paging file size for all drives, if it is selected. This is the
default setting for both Windows 7 and later.
6. Select Custom Size, enter the following minimum and maximum values, click Set, and then
click OK:
l

Initial size: 20480 MB

l

Maximum size: 40 GB*

7. You will need to restart your computer for the change to take effect.

Gen5 Getting Started Guide

---

20 | Install Gen5

* The limit of 40 GB will allow you to work with 10,000 to 15,000 images in memory at the same time.
If you plan to open more images in the Image Processing Tool, for example, consider increasing that
maximum size.

Defining the Image Library
System > Preferences > Image Save Options
Use the Image Save Options under System > Preferences to define default naming conventions and the
Image Library location for automatically saving image files. Settings defined in the Image Save Options
dialog apply to all newly created images. These settings apply to all PCs sharing the same shared DB on
a network.
To override these settings in an individual experiment, go to Protocol > Protocol Options
> Image Save Options, and click Select new image folder. Navigate to the new image folder,
then save the experiment file.

Disable Sleep Mode
Disabling a computer's sleep mode is recommended for all applications, but it is especially important
when running kinetic or time-elapse assays.
1. Open the Control Panel and select Power Options.
2. Click Change plan settings for the power plan you are using.
3. Set Put the computer to sleep at Never.

Turn Off Automated Updates
If possible, turn off the computer's auto-update routines, power-saving options, and virus scans
that can interrupt a Gen5 experiment.

Storing Gen5 Files on an External Hard Drive
Guidelines for using an external hard drive for storing Gen5 files, including imaging files, follow:
l

Use a USB 3.0 drive for faster transfer rates.

l

Close the Gen5 experiment or manual mode session before ejecting the device.

l

Always use the eject utility when disconnecting the device from your computer. Do not
disconnect the device by just pulling it out. Right-click
screen, and select Eject <drive name>.

in the lower-right corner of your

Register with BioTek
The Pre-Registration screen appears when you launch Gen5 until the software is registered. A trialversion serial number can be used for the specified number of days until a licensed version is

BioTek Instruments, Inc.

---

Register with BioTek | 21

purchased. Unless the purchased version of Gen5 is a higher version than the trial version there is
no need to reinstall the software; simply register the software.
As required for installing the software, you must have administrative privileges to register with
BioTek. Generally, the user who logged in to Windows when installing Gen5 should be logged in
when registering the software.
Windows 7, Windows 8.1, and Windows 10 users: If prompted for administrative privileges,
engage them before registering the software: Locate and right-click the Gen5 desktop icon, and
select Run as administrator. At the User Account Control dialog, click Allow.

Launch Gen5 and Register the Software
1. Open Gen5 by clicking its desktop icon or by using the Windows Start button and selecting
Programs > Gen5 > Gen5.
2. At the Pre-Registration dialog enter the product serial number (if it wasnt entered during
installation or if youve been using a trial version).
3. Click Register to register the software and receive a password. The Registration dialog
appears with the serial number and the site key; this is information provided by your
computer.
Click Demo to run Gen5 without registering it for the number of days displayed below the Demo
button.
4. Click Go to Internet Site.
l

l

l

Alternatively, if your Internet browser and Gen5 are on different computers, enter
the BioTek URL into your browsers address field. Make note of the serial number
and site key to proceed.
If you do not have access to the Internet, contact BioTek. See Getting Technical
Assistance on page 52.
When using the same computer, you can copy and paste (Ctrl+C and Ctrl+V) the
serial number and site key into the registration form.

5. At BioTeks Software Registration website page, enter or paste the serial number and site
key information into the form and click Submit.
A registration form will be displayed containing any information BioTek already has about
you and your organization.
6. Review and edit the information as necessary, then click Submit Registration Form.
7. Your password will be displayed on screen. Copy or make note of it.
8. Return to the Gen5 Registration dialog to paste or enter it into the Password field.
9. Click Validate Password.
The software should now be registered and you will not see the Pre-Registration screen again.

Gen5 Getting Started Guide

---

22 | Install Gen5

Gen5 stores the serial number and site key in the Help > About Gen5 screen so you can log in to
BioTeks product registration site at any time.

BioTek Instruments, Inc.

---

Initial Setup
The first thing all users must do after installing Gen5 on a PC is connect an
instrument to the computer and tell Gen5 how to communicate with it. Other initial
setup steps can be performed to improve your experience using Gen5. , Gen5
Secure, Gen5 Secure Image+, Gen5 IVD, Gen5 IVD Image+, and Gen5 Secure Image
Prime, to meet FDA submission criteria, require establishing security conditions.
Youll find instructions for performing all these tasks in this section.

Connect an Instrument

24

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime

25

Set Up Gen5 Secure, Gen5 Secure Image+, or Gen5 Secure Image Prime

25

Set Up Gen5 IVD or Gen5 IVD Image+

26

Set Up Gen5 Reader Control

26

System Administrator's To-Do List

27

Change the System Administrator's Password

28

About Gen5 Databases

29

About User Accounts

32

About User Groups

32

Login/Password Controls

35

Configure Windows Authentication

36

Configure the Email Notification Feature

38

---

24 | Initial Setup

Connect an Instrument
System > Instrument Configuration
Before connecting the instrument: If you plan to connect the instrument to the computer via
the USB port, you must first install a necessary USB driver. The driver and installation
instructions are included on the Gen5 software USB flash drive. Connect the instrument after the
driver installation is complete.
When you start Gen5 without an instrument connected to your computer, Gen5 prompts you to
add one. Connect the instrument to the computer and then perform the following steps:
1. Click Yes.
2. Select an instrument from the list, then click OK.
You can also access the Instrument Configuration dialog later by clicking System >
Instrument Configuration.
3. Click Add to define the Instrument Settings:
l

Select either Plug & Play or Com Port as the communication type.

Plug & Play
l

Select an available instrument from the list.

l

Click OK to save the settings.

For Com Port instruments:
l

Select the Instrument Type from the list.

l

Enter the number of the Com port in the Com Port field.

l

If necessary, select a baud rate. Retaining the default baud rate is recommended.
Mismatched baud rate settings can cause serial read errors. When the baud rate
is set to a non-default setting for non-keypad instruments, Gen5 is unable to
communicate with the instruments if they are turned off and then turned on again
while Gen5 is running. For keypad instruments, ensure that the instrument has the
baud rate set to 9600. If the baud rate is changed, the instrument must be
rebooted.

l

If needed, click Setup to change the factory-tested and defined configuration values.

BioTek Instruments, Inc.

---

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime | 25

This step is rarely required.
l

Click OK to save the settings.

4. Click Test Comm. Gen5 attempts to communicate with the instrument.
5. After you receive a passing message, The reader is communicating, click OK and then
Close at Instrument Configuration. If you receive any other message, look for a remedy in
the Troubleshooting section of this guide.
Gen5 captures the information it needs from the instrument itself, including probe size, wavelength,
bandwidth capability, filter set and mirror configuration, and any other applicable information.
Two models of PowerWave XS are listed in Gen5: PowerWave XS and PowerWave XS2. If you are
connecting a PowerWave XS reader that has a USB port and an MQX200R2 product number
(take note of the 2), you must select the PowerWave XS2. Our changes to the PowerWave XS
hardware to incorporate a USB/RS-232 COM port require unique reader identification in Gen5.
There is no difference in the optical performance characteristics of the reader.

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime
Gen5 fulfills the instrument control and analytical needs for a wide range of laboratory settings. The
degree to which you follow the recommendations provided here depends on the needs of your
organization.

Recommended Tasks to Perform
1. Designate a System Administrator.
2. Install Gen5 on the Administrators computer.
3. Change the System Administrators password.
4. Determine the optimal way to store Gen5s protocol and experiment files. See About File
Storage on page 55.
l

Organize the database or your Windows file structure.

5. Install Gen5 for other users and connect an instrument to each computer. See Connect an
Instrument on page 24.
6. If applicable, direct each users database configuration to point to the correct shared
database.

Set Up Gen5 Secure, Gen5 Secure Image+, or Gen5 Secure Image Prime
1. Designate a System Administrator.
2. Complete the System Administrators To-Do List (the Initial Setup tasks).
3. Organize the database. See Organize Your Database Files on page 30.

Gen5 Getting Started Guide

---

26 | Initial Setup

4. Review/modify Signature Reasons and other security controls (select System > Security).
5. Install Gen5 on each users computer.
6. Set up each users database configuration to point to the correct shared database. See
Move or Copy a Database to a Network on page 31.
7. Connect an instrument to each users computer.
8. Advise users to change their passwords.

Set Up Gen5 IVD or Gen5 IVD Image+
1. Designate a System Administrator.
2. Complete the System Administrators To-Do List (the Initial Setup tasks).
3. Organize the database. See Organize Your Database Files on page 30.
4. Review/modify Signature Reasons and other security controls (select System > Security).
5. Install Gen5 on each users computer.
6. Set up each users database configuration to point to the correct shared database. See
Move or Copy a Database to a Network on page 31.
7. Connect an instrument to each users computer.
8. Advise users to change their passwords.

Set Up Gen5 Reader Control
1. Install Gen5 on the computer.
2. Determine the optimal way to store Gen5's protocol and experiment files.
l

Organize the database or your Windows file structure.

3. Connect an instrument to the computer. See Connect an Instrument on page 24.
4. Set user preferences. See the Gen5 Help for more information.

BioTek Instruments, Inc.

---

System Administrator's To-Do List | 27

System Administrator's To-Do List
Initial Setup Tasks: Gen5 Secure, Gen5 Secure Image+, and Gen5 Secure Image Prime
1. Make sure all designated computers (PCs) and BioTek instruments meet the minimum
requirements. See Computer System Recommendations on page 10.
2. Install Gen5 Image+ Secure or Gen5 Secure on one computer (PC).
3. Start Gen5 and log in as the System Administrator.
4. Change the System Administrators password.
5. Copy the database Shared.mdb to a secure network location.
6. Test database configuration of the Shared.mdb on the network.
7. Create/modify user groups, as needed, and assign user permissions to the groups.
8. Create new user accounts and assign the users to a group.*
9. Connect instrument(s) to the PC and establish communication.
Repeat Steps 2, 3, 6, and 8 for the remaining PCs.

Initial Setup Tasks: Gen5 IVD and Gen5 IVD Image+
1. Make sure all designated computers (PCs) and BioTek instruments meet the minimum
requirements. See Computer System Recommendations on page 10.
2. Install Gen5 IVD or Gen5 IVD Image+ on one computer (PC).
3. Start Gen5 and log in as the System Administrator.
4. Change the System Administrators password.
5. Copy the database Shared.mdb to a secure network location.
6. Test database configuration of the Shared.mdb on the network.
7. Copy the database QCDB.mdb to a secure network location.
8. Test database configuration of the QCDB.mdb on the network.
9. Create/modify user groups, as needed, and assign user permissions to the groups.
10. Create new user accounts and assign the users to a group.*
11. Connect instrument(s) to the PC and establish communication.
Repeat Steps 2, 3, 6, 8, and 10 for the remaining PCs.

* For Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+,
you can use Windows Authentication as an alternative. See Configure Windows Authentication on
page 36.

Gen5 Getting Started Guide

---

28 | Initial Setup

Periodic/As Needed Tasks
l

Customize the security features to accommodate your organizations needs.

l

Organize your database files.

l

Educate users on regulatory requirements and Gen5 best practices.

l

Establish and implement a procedure and schedule for record retention and archival.

l

Review records, including any training/user-qualification records.

Before modifying a users account, make sure he/she is not logged in to the system. You can
check the System Audit Trail to determine who is currently logged in.

Change the System Administrator's Password
System > Security > Users
System > User Setup > Administrator tab
You should change the System Administrators password immediately following Gen5 installation to
ensure a secure operating environment.
To change the password:
1. Log in as the System Administrator, if you havent already done so.
l

Select System > Login/Logout.

l

Set the User to Administrator.

l

Enter the default password: admin.
Passwords are case-sensitive. For example, "Gen5admin" and "gen5admin" are two
distinct passwords.

2. Select System > Security > Users.
3. Double-click the System Administrator user (to edit the record).
4. Define and confirm the new password. The System Audit Trail will open to log the change
and accept your comments.
Record and store the new password in a secure location. If you forget the password, contact
BioTek TAC for assistance.

BioTek Instruments, Inc.

---

About Gen5 Databases | 29

About Gen5 Databases
Gen5 installs two databases during regular installation: SharedDB and LocalDB. Only Gen5 Secure,
Gen5 Secure Image+ , Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+ are initially set up
to use the Gen5 Database for experiment and protocol file storage. All other levels of Gen5 must
select to use the database to store experiment and protocol files at System > Preferences > File
Storage Mode.
l

SharedDB can be set up on a network for sharing information among multiple users. It
contains all protocol and experiment data files and their associated audit trails, the plate
types, and reader-diagnostic history data. In Gen5 Secure Image +, Gen5 Secure Image
Prime, Gen5 IVD Image+, Gen5 Secure, and Gen5 IVD, SharedDB also contains security
settings, user accounts, and a system audit trail for shared events. This database can be
moved, renamed, and copied. So, if desired, you can create a unique database for
individual projects, teams, or other classification.
The SharedDB must reside in a location that presents the minimum risk of error. Before moving it
to a networked drive, it is recommended that you analyze the network or disk and server to
ensure that the error rate is low. It is not recommended that you use WiFi network connections,
external drives, or USB flash drives to hold the SharedDB.

Gen5 Image+ IVD and Gen5 IVD also install the QC Trending database, QCDB.mdb. It can
be set up on a network for sharing among multiple users, moved, renamed, and copied.
It is initially installed in a QC folder in the default database location described below.
l

l

LocalDB contains the local setup information, including the Instrument Configuration. For
Gen5 Secure Image +, Gen5 Secure Image Prime, Gen5 IVD Image+, Gen5 Secure, and Gen5
IVD, this database also contains an audit trail for local events. LocalDB is stored on the
computers hard drive, and it cannot be moved or renamed.
Default database location: During normal installation, Gen5 installs its databases in
Windows Common Application Data Folder:
l

Windows 7, Windows 8.1, and Windows 10: C:\Program Data\BioTek\Gen5
(software level)\(version #)\SharedDB or LocalDB

You may need to change your operating system settings to view the Application Data
folder.
l

Database Names after Upgrade: The Gen5 Upgrade Utility changes the names of the
databases to help distinguish them:
l

SharedDB: The file name of the database selected for upgrade is not changed during
the process, but the upgraded version is identified by this suffix: "Upgraded_<date_
time>.mdb".
The Gen5 Periodic Backup routine appends the filename with "Auto_Backup_
<date_time>".

Gen5 Getting Started Guide

---

30 | Initial Setup
l

l

l

l

l

LocalDB: The file name of the LocalDB selected for upgrade is changed because
Gen5 requires the database stored on your hard drive to be named LocalDB. After
the upgrade the older version is named with this suffix: "Before_<date>_
<time>.mdb".

Max Size: the maximum size of the database files is 2 gigabytes (GB). At startup, Gen5
checks the remaining size of the database. Warning messages are displayed when the
database size exceeds 1536 MB. Use Gen5 maintenance and backup features to archive
your database records.
Gen5 has built-in error recovery modes. When your connection to the database is lost for
any reason, Gen5 saves any unsaved files as Temporary Files. After a system failure, the
next time you open an affected protocol or experiment file, Gen5 offers to replace the
unsaved files with the Temporary Files. Select Yes to recover any changes made to the files
before the system failure; select No to open the files as they were last saved, before the
unsaved changes were made. Newly created files are also saved as Temporary Files.
Following a system failure, you can rename these temporary files with the proper file name
extension (.xpt or .prt) using Gen5 Maintain Files controls.
File locking: When a file is opened in Gen5 it is locked to protect it from being modified
(saved or renamed) by a different user. When a second user attempts to open the file, he
or she receives a message stating: File <filename> is already in use. Do you want to open it
in read-only mode?
Gen5 offers automatic backup. You can define settings for regularly and automatically
backing up and optimizing databases with Gen5 Auto-Optimize feature.

Organize Your Database Files
During regular installation,Gen5 Secure Image+, Gen5 IVD Image+, Gen5 Secure, and Gen5 IVD
use the shared database to store experiment and protocol files. All other levels of Gen5 must
elect to use the database at System > Preferences > File Storage.
All of your file management requirements can be fulfilled using Gen5 databases. You'll be most
satisfied with the final structure if you spend some time planning it up front. In a multiple-user
environment, you can set up a Gen5 database on a shared-network drive (LAN) so multiple users
can access the same protocol and experiment files.
Backups: Performing backups on a regular schedule is highly recommended to preserve your data.
And, Gen5 provides a tool to schedule backups to occur periodically. See below.

File Management Recommendations
l

l

Put a copy of the SharedDB on a shared-network drive where all your Gen5 users can
access it. Be sure to set each user's database configuration to point to the correct location.
Before moving the SharedDB to a network location, make a copy of it to use as a template
for future use:
1. In the default SharedDB folder, highlight the original, right-click, and select Copy.
2. Deselect the original (click elsewhere in the dialog), right-click, and select Paste.

BioTek Instruments, Inc.

---

About Gen5 Databases | 31

3. Highlight the copy, right-click, and select Rename.
4. Give the copy a unique name, like SharedDB_original.mdb.
l

l

l

l

Consider setting up shared databases for different projects or teams within your
organization. You can follow the steps defined above to create multiple databases in the
same folder (or directory), or you can move the unique databases to a different network
location/folder. Use Database Configuration to point users' Gen5 sessions to the correct
database.
Regularly archive and back up the database to preserve your records. Use Gen5 Optimize
and Backup Settings to backup and clean small errors in your database. BioTek
recommends following Follow your organization's existing policy for securing data, for
example, putting the shared database on the network to be backed up every night.
Consider using the Gen5 automatic Save feature to create a new, date-stamped folder for
storing experiment records. This is an especially good practice for large labs with multiple
users who run hundreds of plates per day. Gen5 organizes all that data by date. Define this
kind of file management setting in the Initial Protocol Settings (System > Preferences) so it
will apply to all newly created protocols.
Gen5 handles multiple, simultaneous users performing database management tasks by
giving precedence to the user with the greater administrative rights.

Move or Copy a Database to a Network
System > Database Configuration
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+
install and enable the databases during regular installation. All other levels of Gen5 must elect to
use the database to store protocol and experiment files at System > Preferences > File Storage.
In a multiple-user environment, you can set up the Gen5 database on a shared network drive so
multiple users can access the same protocol and experiment files. This is a recommended step for
System Administrators. You can also set up multiple databases, one for each team or project, for
example. During a Gen5 session, access is provided to only one database at a time.
How To
1. Select System > Database Management > Database Configuration.
2. Select the SharedDB tab.
3. Next to the Source field, click Browse.
4. In the Open dialog, highlight and right-click the file SharedDB.mdb, and select Copy or Cut;
use cut to move and copy to copy (see File Management Recommendations below).
SharedDB is the installed/original name for the shared database. Because you can change
the name, it's possible it has already been changed.
5. Navigate to the desired location in the Look in field.

Gen5 Getting Started Guide

---

32 | Initial Setup

6. When the correct location is selected, right-click in the window and select Paste.
7. Click Open to save and close the window, and return to the Gen5 Database Configuration
dialog.
8. Shut down and restart Gen5 to make the changes take effect.

About User Accounts
System > Security > Users
Prerequisite
This function is available only to the System Administrator. You must log in as the Administrator
(System Menu > LogIn/LogOut) to access all the controls. Non-administrators are limited to
changing their own password and selecting a Startup Action and Protocol Folder.
How to Create, Modify, or Delete User Accounts
Only an Administrator can add, modify, or delete users. You can designate multiple individuals to be
system administrators. Any user account can be changed or deleted, except there must always be at
least one System Administrator:
l

l

l

Click New to set up a new user.
Double-click or highlight a user, and click Edit to modify its name, password, or Group
assignment.
Highlight a user, and click Delete to remove the user account.

About User Groups
System > Security > Groups
Prerequisite
This function is available only to the System Administrator. You must log in as the Administrator
(System > LogIn/LogOut) to access this control.
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+ use
groups to manage the rights or permissions granted to users. When creating (or maintaining) a
group, you define the level of access and the controls available to certain types of users and then
assign actual users to the groups. Gen5 ships with three groups: Administrator, Power User, and
Standard User.
The System Administrator and Power User groups are given access rights to all functions. The
Administrators rights cannot be changed and include additional rights to manage user accounts
that are not extended to Power Users. When Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image
Prime, Gen5 IVD, and Gen5 IVD Image+ is installed, the Standard User is limited to the following
permissions. The System Administrator can change these rights as needed:

BioTek Instruments, Inc.

---

About User Groups | 33
l

Open a protocol

l

Add a new plate

l

Create/Edit Sample IDs

l

Edit plate information

l

Edit Plate Layout

l

Edit Report/Export Builders

l

Define test plates

l

Create folder in database

Create New Groups and Modify Existing Groups
Only a System Administrator can add, modify, or delete groups. Except for the Administrator group,
any group can be changed or deleted, and any group can be renamed.
l

Click New to set up a new group.

l

Highlight a group and click Edit to modify its name and permissions.

l

Highlight a group and click Delete to remove it as an option. First you must reassign any
users to another group. You cannot delete a group with users assigned to it.

Create/Maintain User Accounts
For Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5
IVD Image+ only.
System > Security > Users

Prerequisite
Most options for user accounts are available only to the System Administrator. Non-administrators
are limited to changing their own password and selecting a Startup Action and Protocol Folder.

User ID
Enter a unique ID using 1 to 16 alphanumeric characters. The user will enter or select this ID when
logging into Gen5 and when signing files.

Full Name
Enter the users name. This name will be associated with events logged by this users actions and
with the digital signature applied by this user.

Gen5 Getting Started Guide

---

34 | Initial Setup

Group
Choose a Group membership to assign access rights and permissions to the user. See About User
Groups in the Gen5 Help for information. Users receive the rights assigned to the Group.

Status
The check box shows whether the users account is currently locked. The System Administrator can
lock or unlock the account. When a users account is locked, the user cannot log in to Gen5 and
cannot sign files. A users account may become locked due to one of three events:
l

Intentional lock by the Administrator using this dialog

l

Automatic lock if the user exceeded the number of successive failed login attempts

l

Automatic lock if the users password expired

Unlocking a user's account following an automatic lock resets its counter or clock. The reset is
specific to the reason for the lockout: When it is caused by password expiration, the password
expiration clock is reset; when it is caused by failed logins, the user's history of "successive failed
login attempts" is reset to 0.
When lockout occurs due to an expired password, unlocking the account allows the user to log in to
Gen5 with the same password, providing a chance to change it. Alternatively, as system
administrator, you can simply change the password yourself (which will by default unlock the
account) and tell the user to log in with the password you have assigned him or her.

Startup Action
Select the preferred method for starting Gen5:
l

l

l

Display Task Manager/Last used page is the default setting. You can also specify a specific
Task Manager page, such as Read Now page or Experiment page.
Create new experiment opens Gen5 with the Protocol selection dialog open, as if the user
had selected Experiments > Create New.
Start at system menu opens Gen5 showing the File, Take3, Window, System, and Help
menus only. Since neither a protocol or experiment is open, the workspace is blank.

Protocol and Experiment Folders
Browse to or enter the full path and directory to define the folder in which the current user will
typically store protocol and experiment files. Gen5 defaults to the most recently accessed folder.

Password
Assign a password for the user to enter the first time he or she logs in to Gen5. Instruct users to
change their password after the first login using the password you've assigned. Users can change
only their own password. System Administrators can change any user's password.

BioTek Instruments, Inc.

---

Login/Password Controls | 35

Login/Password Controls
System > Security > Login
Prerequisite
Only the System Administrator can access these controls. You must log in as the Administrator
(System > LogIn/LogOut) to change the settings.
The default settings shipped with Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime,
Gen5 IVD, and Gen5 IVD Image+, as shown in the screenshot below, comply with the FDAs 21
CFR Part 11 requirements for controls for identification codes/passwords.

Login
l

l

Lock user account after: Specify the number of successive failed login attempts a user may
make before being locked out of Gen5. This feature does not apply to System
Administrator accounts, and only a System Administrator can reinstate a locked-out
account. Valid entry range: 2-10. When this feature is not selected, users login attempts
are unlimited. Compliance with 21 CFR Part 11 requires setting a limit for failed login
attempts.
Lock session after: Specify the number of minutes that a Gen5 session can be idle before it
is locked and requires successful user login to reactivate. A session is considered idle when
there is no keyboard or mouse activity and Gen5 is not controlling a reader activity. Valid
entry range: 1-1440 minutes. Compliance with 21 CFR Part 11 requires setting an idle-time
limit.

Gen5 Getting Started Guide

---

36 | Initial Setup
l

l

Force user to type ID: Apply this control if your security rules require users to enter their
ID at login and to apply their Signature. When this feature is not selected, the last users ID
is displayed in the login and signature screens, and users can select an ID from a dropdown list of users.
Require login in OLE Automation (BioStack): Select this option to ensure that Gen5
security permissions are enabled when Gen5 Secure, Gen5 Secure Image+, Gen5 Secure
Image Prime, Gen5 IVD, and Gen5 IVD Image+ is run as an OLE Automation server, for
example, for using the BioStack. If Windows Authentication is enabled, the login process
may take place automatically. If the user does not have Windows Authentication enabled,
Gen5 prompts the user to enter a login ID and password. Logins performed while this
option is selected are tracked in the Audit Log.

Password
l

l

l

Minimum password length: Specify the minimum number of alphanumeric characters
required for a valid password. Valid entry range: 2-10 characters.
Password expiration: Specify the number of days a password can be used before users are
required to change it. When users let their password expire without changing it, their
accounts are locked out and only a System Administrator can reinstate a locked-out
account. Valid entry range: 1-10000 days. If this feature is not selected, passwords do not
expire. Compliance with 21 CFR Part 11 requires an expiration period.
Lock out: When a users password has expired, the system administrator has two choices:
l

l

l

l

Manually remove the Locked out flag. This resets the password expiration period
allowing the user to log in using his/her current password.
Enter a new password for the user (which unlocks the account) and tell the user to
log in with the password you have assigned him/her. Advise the user to change the
password after logging in.

Advise user: If password expiration is set, specify the number of days before passwords
expire to alert users to change their password. Valid entry range: 1-30 days, but cannot
exceed the number of days to Password Expiration.
Password reuse: Specify the number of passwords Gen5 will remember for each users
account to prevent a recently used password from being reused. Valid entry range: 2-20.

Configure Windows Authentication
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+
provide an option to allow users to sign in to Gen5 using Microsoft Windows Authentication instead
of user accounts defined in Gen5. Through Windows Authentication, users log in to their
workstations once and have access to Gen5 without having to log in again. The Windows
Authentication feature benefits system administrators as well by providing a single location for the
management of user settings.
To use the Windows Authentication feature, workstations must be running Windows 7, Windows
8.1, or Windows 10; earlier versions of the operating system will not work properly. Servers must be
running Windows 2003 or Windows 2008.

BioTek Instruments, Inc.

---

Configure Windows Authentication | 37

BioTek has validated this on Microsoft Windows Server 2003 (SP2 and SP3) and Microsoft
Windows Server 2008 (SP1). BioTek does not provide support for the use of the Windows
Authentication feature on a server that has not been validated.
Before Windows Authentication can be activated in Gen5, both the Gen5 Administrator and the IT
administrator must perform some setup tasks.

Gen5 Administrator Tasks
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+ use
groups to manage the rights or permissions granted to users. The Group Names are defined in Gen5
by the Gen5 Administrator.
When creating or maintaining a group, the Gen5 Administrator defines the level of access and the
controls available to certain types of users, and then assigns actual users to the groups. Gen5 ships
with three default groups: Administrator, Power User, and Standard User.
The System Administrator group is given access rights to all functions. The Administrators rights
cannot be changed. When Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD,
and Gen5 IVD Image+ is installed, the Standard User is limited to the following permissions (the
System Administrator can change these controls as needed):
l

Open Protocol

l

Use Gen5 Protocols (requires Gen5 Native)

l

Add a New Plate

l

Create/Edit Sample IDs

l

Edit Plate Information

l

Edit Report/Export Builders

l

Create folder in database

l

Edit Paneled protocols

l

View protected/read-only protocol items

IT Administrator Tasks
The IT administrator must create user groups on the server to mirror the Gen5 User Groups defined
in Gen5. The user groups on the server must be named Gen5_<Gen5 Group Name>, where <Gen5
Group Name> is the name of a group in Gen5, such as Gen5_System Administrators. The IT
administrator can also define permissions that apply to Windows resources, such as access to
folders, printers, and so on.
Each user who has permission to run Gen5 must be defined as a member of a single Gen5 group in
Windows. If a user is defined as a member of more than one Gen5 group, an error message will
appear when the user attempts to log in to Gen5. If the user is not assigned to a Gen5 group, a

Gen5 Getting Started Guide

---

38 | Initial Setup

warning message will appear, indicating that the user is not a valid Gen5 user. The user can then log
in with another, valid Gen5 account.

Configure the Email Notification Feature
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+ can
be set up to send an email notification to specified recipients when a predefined event, such as a
reader error or failed login, occurs. The email server settings must be configured to support this
feature. The Gen5 Administrator must test these settings to verify that the Email Notification feature
is functioning correctly.
To verify that the email server settings are configured correctly to support this feature, check
with your IT administrator.

Defining a Custom Email Template
By default, Gen5 generates the title and body of the email notification messages, but you can define
a custom template that includes specific variables.
1. On the Email tab of the Security dialog, click Auto in the Template column.
2. In the Email Definition dialog, select Custom as the mode and either Text or HTML as the
format.
3. Modify the Subject and Body text as necessary. Variables associated with the defined event
are listed in the Variables text box. To insert them in the Subject or Body of the email
notification, place the cursor where you want the variable to occur, then double-click the
variable in the Variable text box.
4. Click OK.

Configure the Email Server
System > Preferences > Email Server
System > Security > Emails tab > Email Server
The email server must be configured correctly to support the Gen5 Email Notification feature. Check
with your IT administrator to verify your configuration settings.
In the Send Emails from area, you can define the email addresses used in the Email Notification
feature.
l

l

l

Display name: This field is required. By default, Gen5 displays Gen5_Notice_Do_Not_
Reply@biotek.com as the address from which the notification message is sent. The user
can change this address, if desired.
Forward errors to: The address specified in this field will receive any mail delivery error
messages generated by the server related to the Email Notification feature. If no address is
entered, error messages will be sent to the address in the Display Name field.
Reply to: The address specified in this field will receive messages sent as a reply to an Email
Notification message. If no email address is entered in this field, the address in the Display
Name field will receive any reply emails.

BioTek Instruments, Inc.

---

Getting Started
Gen5 software provides a logical interface to all automated BioTek plate reads. It is
designed to flow from reading parameters, to plate layout, to data reduction, and
finally to flexible data output options.

Task Manager

40

The Gen5 Workspace

41

Protocol Workspace

43

The Menu Tree

44

Buttons and Icons

45

Troubleshooting

47

Getting Technical Assistance

52

---

40 | Getting Started

Task Manager
Whenever you start Gen5, the Task Manager opens. You can also return to the Task Manager by
selecting File > New Task or
main screen.

. If you are in the Task Manager, selecting

returns you to the

.

BioTek Instruments, Inc.

---

The Gen5 Workspace | 41

Instant Access
The Task Manager provides quick links to give you instant access to:
l

Executing a new read

l

Using the Imager Manual Mode (imaging only)

l

l

Opening or creating an experiment or protocol; the most recently used protocols and
experiments are listed
Control several of the instrument's operations (e.g., incubation, shaking, plate in, stacker
control)

l

Accessing configuration and security settings

l

Opening the System menu

l

Accessing the Gen5 Help system, FAQs, and sample files

The Gen5 Workspace
Gen5 offers several controls and workspaces for developing protocols, running experiments, and
viewing and reporting results:

Gen5 Getting Started Guide

---

42 | Getting Started

Gen5 workspace with File menu displayed

1. Protocol
Every experiment is based on a protocol. The differences between a protocol and an experiment in
Gen5 are described in the Essential Concepts chapter.

2. Menu Tree
The menu tree, docked at the left side of the workspace, provides an alternative to using the
toolbars and menus.

3. Toolbars and Menus
See Buttons and Icons on page 45 to learn about Gen5 toolbars, buttons, and menus.

4. Plate View
Gen5 provides a view or workspace for each plate processed (or to be processed) in an experiment.
You must have an experiment, rather than a protocol, open to have a Plate View.
To open the Plate View: In an experiment, if it is not already open in the main view of Gen5, doubleclick the plate icon in the menu tree or select Plate > View.
Gen5 offers several ways to modify and customize the Plate View for on-screen display and
reporting/outputting results. See View Results on page 61 to learn more.

BioTek Instruments, Inc.

---

Protocol Workspace | 43

5. Instrument Control Panel
While in the Gen5 workspace, you can click the Instrument Control panel to access commands and
actions for the attached readers and stacker. Select the instrument you want to control from the list
at the top of the panel.

Gen5 workspace with Instrument Control panel
for reader displayed

Gen5 workspace with Instrument Control panel for
stacker displayed

Protocol Workspace
When you create a new protocol, Gen5 opens a special workspace limited to the protocols
components.

The workspace is made up of the menu tree with a branch for each of the protocols elements. The
order of the protocol elements reflects the order to follow when defining most protocols:

Gen5 Getting Started Guide

---

44 | Getting Started

Defining the Procedure or reading parameters is the most important step to Gen5. The
Procedure describes the data sets that are used in most subsequent steps to generate results
output. The Plate Layout is the only other protocol element that is not affected by the Procedure; it
is affected by the selected plate size.
For most protocols, its best to define the Plate Layout in your second step. Gen5
automatically performs a blank-subtraction calculation when Blanks are defined in the plate layout.
(Youll see this Transformation in the Data Reduction workspace.) Defining the standards and their
concentrations in the plate layout is a prerequisite to generating a standard curve.
Data Reduction is one of the most powerful features in Gen5, and it requires the information
provided by the two previous steps to logically offer you its capabilities. Automatically generated
transformations, like path length correction and the ability to conduct well analysis, for example,
depend on the Procedure. To plot a standard or titer curve and to validate Transformation formulas
requires knowing the Plate Layout.
Report/Export Builders is a tool for selecting and customizing the appearance of data sets
that are then available for printing or exporting.

The Menu Tree
l

l

l

l

l

l

l

l

To keep the menu tree open in a protocol or experiment, you must click
to dock it in
place. When youre working with a protocol file, the menu tree, like the toolbar, is limited
to related operations.
The menu tree provides a visual cue of the steps to follow when creating a protocol.
All of the controls available from the menu tree can alternatively be accessed using toolbar
buttons or menus.
Click

and

next to an item to reveal or hide its components.

Highlight an item in the menu tree and right-click for a context-sensitive menu of options,
including Read when a plate is selected, for example.
Asterisks (*) are displayed next to plate icons (and in the title bar) of an experiment when a
change is made or an action is taken but the file has not yet been saved.
You can move the menu tree to another corner of the workspace or let it float undocked
like the Plate workspace: click the undock button, drag the title bar, and drop it in the
desired location.
When you add multiple plates to an experiment, highlight a plate and right-click for menu
options to delete and renumber plates.

BioTek Instruments, Inc.

---

Buttons and Icons | 45

Buttons and Icons
Button

Description
Open the Task Manager
Save the protocol or experiment
Read the plate
Print preview
Print results
Export results

Procedure

Plate layout
Data reduction
Report/Export Builders
Paneled protocols
(Imaging only) Go to manual mode

Set Reader Optics: Opens the Set Reader Optics dialog in which you can update the reader with
new definitions for filters and mirrors.
Instrument Control: Check the status, open the control panel
Stacker icon: Opens the Stacker control panel, if a Stacker is attached.
Export results to QC (Gen5 Image+ IVD and Gen5 IVD only)
Edit trended protocols (Gen5 Image+ IVD and Gen5 IVD only)

Gen5 Getting Started Guide

---

46 | Getting Started
Button

Description
Pin the current plate view to the workspace
Duplicate a coincident display of the plates results

Menu Tree Icons
Plate--not read: Put the plate in the reader and click
Plate read successful
Plate read paused by Stop/Resume step:
When youre ready, put the plate in the reader, click

,

and select Resume Plate x to continue
Plate read aborted: To begin again, put the plate in the reader, click

, and select Re-Read Plate x

Plate read in progress
Plate read error, which is always preceded by an error message. The error code and message are
recorded in the plate data audit trail. It is the user's responsibility to verify the integrity of the data after
an error occurs.
Protocol
Procedure: Define the reading parameters
Plate Layout: Assign location of samples
Data Reduction: Set up calculations
Report/Export Builders
Plate Information: Information obtained at runtime
Sample IDs: User-defined names or IDs assigned to samples
Calculation Warning Log: Data Reduction-related errors issued by unexpected curve or calculation
results
Audit trail displays any logged events
Multi-Plate protocol view of data reduction statistics and curves
Panel: Multi-protocol experiment performed on one plate
Paneled Protocols: Lists the protocols run (or to be run) in the panel experiment

BioTek Instruments, Inc.

---

Troubleshooting | 47

Troubleshooting
l

l

First Response: Running a System Test is the best first response to an instrument error.
The test may restore the instruments initial settings and computer communication
capability. Note: To stop the alarm, press the carrier eject button.
Reboot the Computer and Instrument: When you cant run a system test, for example,
Gen5 is not responding, or when running a system test doesnt resolve the issue, turn off
your computer and instrument, check all the cabling (i.e., make sure your serial or USB
cable is in good condition and is properly connected to the PC and instrument), and then,
power on your computer and instrument. These steps should refresh the devices and
reset communication parameters.
Visit BioTeks website for useful suggestions on getting the most from your reader:
www.biotek.com/resources

l

l

Incompatible protocols: Protocols created with one instrument are not instantly
compatible with other instruments. To correct the error Procedure was defined for a
different instrument, open the Procedure and click Validate. If this does not correct the
error, open each step in the Procedure and review it for compatibility with the current
instrument.
Windows 7, Windows 8.1, Windows 10 Missing Files: The Gen5 installation routine
attempts to avert potential file sharing issues on Windows 7, Windows 8.1, and Windows
10, but when multiple users share a computer, Windows may use its VirtualStore as the
default location for file storage.

Communication Errors
FYI
l

l

To prevent damage to the instrument, always turn off the instrument or the computer
before removing or inserting a communications (serial or USB) cable.
Gen5 and the instrument-communication parameters supersede the Windows settings.
Windows communication port configuration settings should not need adjustment to
enable proper communications.

If Gen5 fails to save a file
l

Ensure you are using a tethered (i.e., wired) connection between the computer running
Gen5 and the drive on which you are trying to save the files. It is strongly recommended
that you not use a WiFi connection when running experiments

When the computer (PC) wont communicate with the instrument
l

Confirm that the instrument passes its system self-test. All BioTek instruments perform a
self-test when turned on. Refer to the instruments operators manual for more details.
The instrument will not communicate if it fails an internal system test. Non-keypad
instruments beep continuously when the system test fails. (Press the plate-carrier button
to stop the alarm.) Keypad instruments display an error message when the test fails. Refer
to the operators manual to resolve the failure or contact BioTek TAC.

Gen5 Getting Started Guide

---

48 | Getting Started
l

l

l

l

l

l

Make sure the serial or USB cable is in perfect condition and properly attached to the
port defined in the Instrument Configuration dialog (e.g., COM 1 or Plug & Play). Correct
and reboot both PC and reader. Test communication.
Confirm the baud rate (or transmission speed) defined in the Gen5 Instrument
Configuration dialog matches the instruments settings. Consult your instruments
operators manual for the correct rate. Correct the Gen5 Instrument Settings to match and
reboot both PC and instrument. Test communication.
Disable the Calculation Option: The Perform data reduction after each read option gives
Gen5 sufficient time between obtaining measurements to perform calculations.
Confirm that the serial/USB cable is the correct onewas obtained from BioTek.
Serial/USB cables are not universal. Consult the instruments operators manual for proper
cable configuration or contact BioTek customer service to purchase a factory-tested cable.
After installing a known good cable, reboot both PC and instrument. Test communication.
Confirm with your computer supplier or a local PC technician that the serial port has
been enabled. For example, the IBM Thinkpad was originally shipped with the serial port
disabled. Correct and reboot both PC and reader. Test communication.
For advanced PC users, the serial port of the instrument and PC can be independently
tested using an independent serial-communication software package such as Windows
Terminal, Hyper Terminal, or ProCom. BioTek does not support or sell these programs.
l

Select flow control for XON/XOFF and send an ASCII asterisk symbol (*) to the
reader. The instrument should initiate a self-test and return the results to the PC. If
the instrument fails to communicate, and Steps 1 through 5 do not resolve the
problem, test the instrument on an alternative PC to confirm which device is at
fault. Please contact BioTek if the instrument is diagnosed to be faulty.

Restore Optimal Performance
Numerous factors can affect your computers performance. If you notice a slowdown in Gen5s
performance, follow these suggestions:
l

l

l

l

Close all other applications, including Internet browsers, when running Gen5.
Do not display Gen5s Curves data in the Plate View while performing a kinetic analysis.
Wait until the read step is finished before viewing the Curves data set. Displaying the
Curves data set during a Kinetic read can consume excessive resources resulting in
performance degradation. You can drill down to a Well Zoom to monitor the progress of
one well, then, leaving the Well Zoom open, change the Matrix Data to a numeric view.
Disable the Calculation option Perform data reduction after each read to give Gen5
sufficient time between obtaining measurements to perform calculations. Select Protocol
> Protocol Options > Calculation Options.
Disable the auto-Save option: Save when: Interim read completed. Change the Save
Options to free up resources. Select Protocol > Protocol Options > Save Options.

Fluorescence/Luminescence Measurements
Heres a list of potential problems, the possible cause, and a remedy:

BioTek Instruments, Inc.

---

Troubleshooting | 49

Fluorescence/Luminescence Readings Too Low
l

Possible cause: The fixed Gain in the Read Step dialog is currently set too low
Raise the Gain to an appropriate level. For fluorescence, the Gain is usually set between 45
and 130. For luminescence it is usually set between 100 and 200. Learn more in the Gen5
Help.
Try Automatic Gain Adjustment, using the Scale to High Well option and setting the target
value to be between 20,000 and 80,000 for standard range, or 1,000,000-3,500,000 for
extended range (if supported by your reader).
Some readers have extended range capabilities with flash fluorescence. These models are
auto-ranging up to 10,000,000.

l

Possible cause: The wrong filters are selected in the Read Step dialog (for filter-based
reads only)
Examine the current filter settings and make any corrections. If the filter settings appear to
be correct, check the locations of the actual filters in the instrument.

l

Possible cause: Top probe setting is not optimized
Gen5 generally positions the top probe at the optimal height for fluorescence reads, based
on the plate type selected; it focuses the beam above the well. Refer to the Gen5 Help and
use the Read Height option in the Read Step dialog to make adjustments. If supported by
your reader, try the Auto-Adjust feature for the probe height. The reader's operator's
manual may contain additional suggestions.

Fluorescence Background Too High
l

Possible cause: Using incorrect microplates
Solid black plates for top probe reading lower the background. Black plates with clear
bottoms lower the background if bottom reading is necessary. Corning 3615 or 3614 (for cell
culture) are appropriate.

l

Possible cause: The wrong filters are selected in the Read Step dialog (for filter-based
reads)
Examine the current filter settings and make any corrections. If the filter settings appear to
be correct, check the locations of the actual filters in the instrument.

l

Possible cause: Phenol red is used in the media when exciting at 485 nm and reading
at 528-530 nm
Eliminate or replace the phenol red.

l

Possible cause: Cells, media and other contents fluoresce

Gen5 Getting Started Guide

---

50 | Getting Started

Use deionized-water blank wells as a diagnostic tool. The blank-well reading will help you
determine the background value contributed by the instrument, labware, and media.
l

Possible cause: The top and/or bottom probe needs cleaning
Refer to the operators manual for guidance; not all readers have user-accessible internal
components.

l

Possible cause: The instrument has fluorescing material spilled inside
Refer to the operators manual for guidance; not all readers have user-accessible internal
components.

l

Possible cause: The Gain in the Reading parameters dialog is currently set too high
Lower the Gain setting. The background should still read higher than zero. 200 is a
recommended minimum and a value of 1000 takes advantage of the systems five-digit
resolution.

Reader Not Achieving Desired Fluorescence Detection Limit
l

Possible cause: The wrong filters are selected in the Read Step dialog
Examine the current filter settings and make any corrections. If the filter settings appear to
be correct, check the locations of the actual filters in the instrument.

l

Possible cause: Using incorrect microplates
Refer to the reader's operator's manual for information on supported plate types.

l

Possible cause: The fixed Gain is currently set too low
Raise the Gain setting until the background wells read at least 200 RFU (1000 RFU is
preferred).

l

Possible cause: Readings are taken using the bottom probe
Try switching to the top probe, if applicable/appropriate for your reader and assay.

l

Possible cause: The solution volume is 50 L or less
Increase the solution volume to 150-200 L, if possible.

l

Possible cause: Wrong pH
Fluorescence is very pH dependent. Use the appropriate pH.

l

Possible cause: Phenol red is used in the media when exciting at 485 nm and reading
at 528-530 nm
Eliminate or replace the phenol red.

l

Possible cause: Top probe setting is not optimized

BioTek Instruments, Inc.

---

Troubleshooting | 51

Gen5 generally positions the top probe at the optimal height for fluorescence reads, based
on the plate type selected; it focuses the beam above the well. Refer to the Gen5 Help and
use the Read Height option in the Read Step dialog to make adjustments. If supported by
your reader, try the Auto-Adjust feature for the probe height. The reader's operator's
manual may contain additional suggestions.
l

Possible cause: Transfection efficiency in gene expression is too low
Use more cells, or improve the transfection efficiency.

l

Possible cause: DNA is old or of poor quality
Use high quality, new DNA.

l

Possible cause: Not using nuclease-free buffer in DNA quantitation
Use nuclease-free buffer.

l

Possible cause: Poor dilution methods
Use appropriate dilution method in tubes.

Reader Over-ranging in Fluorescence
l

Possible cause: The Gain in the Read Step dialog is currently set too high
Lower the Gain setting. If using Automatic Gain Adjustment, try the Scale to High Well option
and set the High Value in the range of 50,000 to 70,000.

Bandwidth Verification Failed
l

Error or warning messages are issued when Gen5 detects overlapping wavelengths or
bandwidth
Select/enter Filter Set wavelengths that do not overlap. Learn more about Gen5 bandwidth
verification in the Gen5 Help.

Error during Auto-Sensitivity Determination
l

Reader cannot fulfill request to determine optimal Gain
Gen5 displays an error message when the reader cannot determine the optimal Gain based
on the defined reading parameters.
Luminescence integration time should be <= 1 sec and > 1 ms, especially when scaling to low
wells.
Manually enter a Gain value or use an alternative method to determine the optimal
sensitivity, if the error persists. Learn more in Gen5 Help.

Gen5 Getting Started Guide

---

52 | Getting Started

System Administrator's Password
Contact BioTek Customer Care if you have lost or forgotten the System Administrator's password.
Gen5 ships with the System Administrator's password set to admin.

Getting Technical Assistance
You can telephone the Technical Assistance Center (TAC) at BioTek World Headquarters US between
8:30 AM and 5:30 PM Eastern Standard Time (EST), Monday through Friday, excluding holidays.
Whichever method of contact you choose, please be prepared to provide the following information:
l

The software version and revision numbers displayed at Help > About Gen5

l

The license type or software level

l

The specific steps that produce your problem

l

Any error codes displayed

l

A daytime phone number

l

Your name and company information

l

An email address and/or fax number, if available

BioTek US--World Headquarters
Phone: (802)655-4740
Toll-Free: (888)451-5171
Service Toll-Free: (800)242-4685
Email: CustomerCare@biotek.com
Service Email: TAC@biotek.com
www.biotek.com/contact

BioTek Instruments, Inc.

---

Essential Concepts
This section will give you a good basis of information for understanding the
structure and terminology of Gen5. You can find more details and answers to
specific questions by using the online Help system. Select Help > Help Topics from
the menu.

Experiment vs. Protocol

54

About File Storage

55

Best Practices

57

---

54 | Essential Concepts

Experiment vs. Protocol
Gen5 uses two common terms to define distinct elements of its toolkit. The distinction is subtle and
will have more or less importance depending on how you use Gen5. In any case, youll work most
efficiently by understanding each role and making them work for you.
Protocol (*.prt)

Experiment (*.xpt)

A protocol is a set of instructions designed to
capture, transform, and report and/or export data.

An experiment has a copy of the protocol
and at least one plate. It executes the
instructions provided by the protocol to
produce results.

Protocols are created and saved as stand-alone
files. They function as a template; an unlimited
number of experiments can be based on one
protocol.

Although an experiment is created using
an existing protocol, that protocol can be
modified within the experiment.

A protocol consists of reading requirements, like
detection method and wavelength, and readingrelated actions, like shaking and incubation
(procedure), plate layout, data reduction, and data
viewing, reporting, and exporting parameters.

Running an experiment is the only way to
process a protocol.

A protocol can be used repeatedly (as is or
modified) within experiments. By itself, a protocol
does not produce results. Protocols do not have
plates associated with them.

Multiple plates can be processed in an
experiment, each one considered a
unique assay with independently
reported or exported results. The
exception is multi-plate protocols,
described later.

.prt is the protocols file name extension.

.xpt is the experiments file name
extension.

A copy of the protocol is saved within an
experiment or as a stand-alone .prt file. Since
protocols do not have plates, they cannot generate
data outside of an experiment.

An experiment is saved as the full
collection of procedures, formulas,
reporting definitions, and other details.
The non-imaging plate data are
recalculated when the file is opened in
Gen5.

Gen5 Secure and Gen5 IVD maintain an audit trail
of all activity and changes related to a protocol. All
other Gen5 software levels do not support this
feature.

Data acquired and transformed in an
experiment is protected by an audit trail
in Gen5 Secure, Gen5 IVD, and Gen5. The
Reader Control edition does not support
this feature.

Changes made to a stand-alone protocol are not
reflected in any previously created experiments
based on that protocol. A new experiment must be
created to apply the revised protocol.

Within an experiment, you can select
Save Protocol As to capture the current
details of the protocol and save them as
either a new protocol or as an overwrite
of the original protocol.

BioTek Instruments, Inc.

---

About File Storage | 55

Gen5 also supports more complex multi-plate protocols that are not covered in this
introductory material. See Design a Multi-Plate Protocol in the Gen5 Help system.

About File Storage
File Types
Gen5 creates multiple file types:
l

Protocol = .prt

l

Experiment = .xpt

l

Panel = .pnl

l

Imaging = .tif

l

Imager manual mode session = .imm

System file types include:
l

l

Plate type (vessel) = .ptf
*.xml = several components, like objectives and filter cubes, are managed with their own
unique XML file.

The Gen5 executable file (.exe) and numerous other types of supporting files, like a Microsoft
Excel template, are also installed on the computer.

Databases
Gen5 installs two databases on your system called LocalDB and SharedDB. While the databases are
always used for critical, internally used files, Gen5 offers you the choice of using the Windows File
System or the Gen5 (SharedDB) database for storing Gen5 protocol (.prt) and experiment (.xpt) files.
This option, combined with the ability to create multiple databases, allows you to structure file
storage according to your organizations requirements.
l

l

l

Files may be stored on the computers hard drive, on a network, or on a portable medium.
Windows Explorer or a similar application can be used to view the file names and locations,
and to move, copy, rename, and delete files.
Alternatively, protocol and experiment files may be stored in a secure, shared-access
database. This database, initially named SharedDB.mdb, can be stored on a users
computer or on a shared-access network/computer (LAN). Gen5 provides a special file
maintenance utility for viewing the file names and their locations, and for moving, copying,
renaming, deleting, importing, and exporting files.
Select the preferred method of storing protocol and experiment files at System >
Preferences > File Storage.

Gen5 Getting Started Guide

---

56 | Essential Concepts

When upgrading to a higher version of Gen5, you will be prompted to also upgrade your
databases (or not). Gen5 does a good job during a database upgrade to both preserve your
legacy data and to apply changes to files to make them compatible with new and improved
features.
Gen5 IVD and Gen5 IVD Image+ also install the QC Trending database, QCDB.mdb. It can be set
up on a network for sharing among multiple users, moved, renamed, and copied. It is initially
installed in a QC folder in the default database location described below. See the Gen5 Help
system for more information.

File Location
During a typical installation:
l

l

l

l

the program files are stored in this default location: C:\Program Files\BioTek\Gen5
(software edition)
the databases are stored in this default location: C:\Program Data\BioTek\Gen5 (software
edition)\(version #)\SharedDB or LocalDB
Gen5 installs Protocol and Experiment folders in the respective File Storage locations, for
example: C:\Users\Public\Documents\Protocol
Gen5 prompts you to define the location for the Image Library, when applicable. Then,
Gen5 maintains a connection between an imaging experiment or .imm session and the
images acquired in the session.

The databases are critical to Gen5 functionality. Make sure they are not deleted from your
system.
Image Save Options are defined in the System Preferences dialog, under Initial Protocol Settings.

Image File Management
Each saved image is saved as a TIF file. The TIF files will contain metadata, pertaining to the
instrument, experiment, plate, well, and image, though this data will likely not be accessible by
other TIF file readers.
Defining the Gen5 Image Library
The first time you connect to an instrument with imaging capability, Gen5 prompts you to define an
Image Library location where images will automatically be saved when you run an experiment. You
can change the path later in the Image Save Options dialog.

BioTek Instruments, Inc.

---

Best Practices | 57

Storing Images
Warning! Each image is about 2 MB. Imaging microplates can quickly lead to generating very
large amounts of data: reading only one image per well of a 96-well microplate results in 200 MB
of images. Review your data storage requirements with your IT department. In addition,
processed image files, such as stitched images, can be much larger.
Within the image files folder, Gen5 creates an experiment folder for each imaging experiment run.
Within the experiment folder are subfolders for each plate run in the experiment. The individual
image files are stored in the plate folders.
You may find that you need more hard disk space than is allocated by default. For example, running
a multiplate experiment, imaging all 96 wells in a 4x4 montage in three colors will require an increase
to virtual memory. Without this change, the message, "This procedure may require that you
increase the size of the virtual memory in Windows," may appear. In this case, please consult with
your IT group to increase virtual memory. The Gen5 Help provides instructions to change the virtual
memory settings.
Reduce file size by applying binning during image capture.

Best Practices
Like most software tools, Gen5 is flexible and offers several ways to accomplish a task. Here are
some recommendations for saving time and using it most efficiently.

Efficiencies
l

l

l

l

l

For an assay or experiment that you will run numerous times, develop a protocol to define
the Procedure, Data Reduction, Data Views, and Reports required. Then you can run an
experiment (from the Task Manager, Experiments > Create using an existing protocol)
based on the protocol whenever necessary. You can fine-tune the protocol within an
experiment, but remember to select File > Save Protocol As to update the original
protocol with your improvements.
Use File > Save As to give you a head start creating a new protocol based on an existing
one that contains the same or similar plate layout, reading parameters, or other elements
that will be repeated in your new protocol.
Define and customize Data Views before selecting what to include in reports or export files.
All the on-screen data (i.e., data views) can be reported or exported. If you use on-screen
views and paper reports equally, it is most efficient to first fine-tune the Data Views, and
then include them in reports/exports.
When appropriate, assign Blanks to the plate. Blanks can be deionized (DI) water, buffer,
reagent without analyte, substrate, and so on. When running fluorescence cellular assays,
a DI-water blank illustrates the background contributed by the instrument and labware as
separate from the cells and media. Identify the location of the Blanks in the Plate Layout,
and Gen5 will automatically create the blank-subtraction data reductions.
Back up your database regularly: once per week is recommended for most organizations. If
youre using a Gen5 Database for protocol and experiment file storage, use the built-in
Periodic Optimization feature.

Gen5 Getting Started Guide

---

58 | Essential Concepts
l

l

Take action if you get a warning message about the remaining size of your databases; see
Maintaining Files in Gen5 Help for instructions on archiving and deleting records.
Turn off the Multi-Read Calculation option to improve Gen5 performance. Calculation
results will be the same, but your PCs resources will not be diverted for performing interim
calculations. Find this option at Protocol > Protocol Options > Calculation Options.

Time-Savers
l

l

l

Partial Plate: For assays using strips or partially filled plates, especially if the read steps are
long or complicated, you can save time by telling the reader exactly which adjacent wells or
portion of the plate to read.
Use the Gen5 automatic Save feature to create a new, date-stamped folder for storing
experiment records. This is an especially good practice for large labs with multiple users
who run hundreds of plates per day. Gen5 will keep all the data organized by date. Define
this kind of file management setting in the Initial Protocol Settings so it will apply to all
newly created protocols. Select System > Preferences > Initial Protocol Settings > Save
Options.
Print Preview: Save time and paper by viewing reports on screen before sending them to
the printer.

BioTek Instruments, Inc.

---

Basic Tasks
This section provides instructions for some basic tasks.

Quick Read

60

Create a Standard Curve

60

View Results

61

Print Results

62

Test the Instrument

63

---

60 | Basic Tasks

Quick Read
You can perform a Quick Read using the microplate reader connected to the PC to read a plate and
report the results. Its called quick because it is accomplished without taking the time to set up a full
protocol.

Perform a Quick Read:
1. Click Read Now from the Task Manager, and either select an existing protocol or create a
new one for this read.
2. After you select a protocol, or define a reading procedure for a new protocol, the reader
reads the plate.
When the reading is done you can report the results. If you have a full-level edition of Gen5 (any
version other than Gen5 RC), you can perform data analysis.

Create a Standard Curve
Gen5 lets you create one or more standard curves for determining the concentration of test
samples:
1. From the Task Manager, select Read Now > New.
2. In the Procedure dialog, define the Read step (and any other required steps), then click OK.
Gen5 performs the read and exports your results.
3. Select Plate Layout:
l

Select Standard Curves as one of the well types.

l

Define the concentrations of the Standards.

l

Assign the location of the standards, samples, and blanks (if any) on the plate.

4. Select Data Reduction > Standard Curve.
Gen5 may have generated a corrected data set: if you assigned blanks to the plate or
selected Path length Correction or Polarization in the Read step, youll want to select
these data sets for Data In for the Y-Axis Data to plot the curve.
5. On the Data In tab, select the Y-Axis Data.
6. On the Curve Fit tab, choose a curve fit method.
7. Other options and requirements when defining multiple curves:

BioTek Instruments, Inc.

---

View Results | 61
l

l

l

Curve Name: Replace the default Curve with a more meaningful or unique name.
On the Data Out tab: Replace the default Conc for the Data Set Name with a more
meaningful or unique name.
On the Data Out tab: Define interpolations to plot on the curve.

8. Define the reporting or export requirements and save the protocol using File > Save
Protocol As.

View Results
You can instantly view the results of an experiment in the Gen5 main workspace using the Plate
View:
l

l

l

l

l

l

l

l

l

In the upper-right corner, click
to pin a plate view in the workspace. Pinning a plate
view allows you to have multiple plates' plate views open simultaneously. If a plate view is
not pinned, when you open another plate, it opens in the same plate view.
In the upper-right corner, click
to open another instance of the Plate View. Use this
feature to view the raw data results of a reading in one window and simultaneously display
a curve plotted from the results in another window, for example.
After reading the plate (or otherwise acquiring data), in the Plate View use the Data list to
display the raw data and any data reduction results. You can also select Create new Matrix
to define a new view.
Click Edit Matrix next to a data set to customize the views appearance. This feature is also
available in the Data Views dialog.
Click

to instantly open the current view in Microsoft Excel.

Asterisks (**) are used to signal a change: In the Gen5 title bar an asterisk indicates the
current file has been changed but not yet saved. When a data set is enclosed by asterisks,
it has been become invalid. Generally this is because a Read step or Data Reduction step
has been altered. Edit custom-made data views to select valid data sets.
384- and 1536-well plates require resizing to effectively see the data. Gen5 adds a
button to the Plate View to zoom in on the top-left quadrant of the plate and zoom out to
view the entire plate. After zooming in, use the scroll bars to bring the other quadrants
into focus.
Multi-index readings offer another viewing option. Kinetic and scanning reads generate
views based on the number of intervals, wavelengths, or positions defined. Use the
buttons or enter the desired read index and click Show to display it. Gen5 displays the
time, wavelength, or position of the selected read number.
Kinetic and Scanning protocols can generate Well Analysis data sets labeled Curves. In the
Matrix tab, open the Curves data set and click on a well for a Well Zoom. (384- and 1536well plates show a magnifying glass in the well in lieu of a curve.)

Starting at the Curves data set, you can display multiple well zooms simultaneously by holding
Ctrl while selecting wells.

Gen5 Getting Started Guide

---

62 | Basic Tasks
l

Select the Statistics tab to view a table of data reduction results.

l

Select the Graphs tab (when available) to view any standard curves.

l

l

Select the Results List tab (when available) to view the values or results of the cutoff or
validation formulas.
Review the description of the Gen5 naming convention for the raw data/results.

Important Notes
l

l

l

l

Gen5 may not display some data points by default; to see them you must create your own
Data Views. If you expected to see certain results that are not currently displayed, try
creating your own views.
All data views are also available for reporting and/or exporting.
Modify a data view to change the way results are reported, including the number of
decimal places and significant digits.
Gen5 always uses your computers regional settings to display and input data.

Print Results
Click the Print button to print the results of an experiment.

Prerequisite
First, you must select the specific content for the report using the Gen5 Report/Export Builder
(Protocol > Report/Export Builders).
Reporting in an experiment is done on a per-plate basis:
l

l

Highlight a plate in the menu tree and select Print/Print Preview.
In a multi-plate experiment: You can select multiple plates by holding the Ctrl key while
highlighting them, or to select contiguous plates, highlight the first plate, hold the Shift
key, and select the last plate. Then, click Print.

Gen5 offers enormous flexibility in report output. After defining the report elements, use the
Print Preview option to view the report on screen before printing it to paper. Unneeded columns
and other individual report elements can be removed or modified to improve the appearance and
usefulness of the report.
In Gen5 Help you can find step-by-step instructions for creating and customizing reports.

BioTek Instruments, Inc.

---

Test the Instrument | 63

Test the Instrument
System > Diagnostics > Run System Test
Most BioTek instruments perform a self-test every time theyre turned on, but when you want to
view and/or print the results of a system test:
1. From the Gen5 main window, select System > Diagnostics > Run System Test.
When there is more than one instrument attached to the PC, select the desired one and click
OK.
2. When the test is completed, fill in the text fields--User, Company, Comments--to be
included in the report of the test results, then click OK.
3. Print the report to retain a hard copy for your records.
4. Click Save As to convert the results to a text file. This is especially useful when
troubleshooting an instrument. You can email the text file to BioTek TAC.

Test History
Gen5 keeps the results of System Tests when they are performed using the menu controls.
To review or print the results, select System > Diagnostics > Test History.

Gen5 Getting Started Guide

---

64 | Basic Tasks

---

Set Up a Protocol
This section walks through the basic steps to creating a protocol. You'll find more
details in the Gen5 Help. If you haven't already done so, read the differences
between experiments and protocols in Gen5 in the Essential Concepts section.

Design a Protocol

66

Define the Reading Procedure

66

Define the Plate Layout

67

Set Up Data Reduction

69

About Exporting Results

70

About Reports

71

---

66 | Set Up a Protocol

Design a Protocol
In the Task Manager, click Read Now > New to get started.
1. Define the procedure, then click OK. Gen5 performs the read and displays the resulting
data.
2. Define the plate layout (for all except Gen5 Reader Control).
3. Define the data reduction requirements (for all except Gen5 Reader Control).
4. Define the reporting and exporting requirements.
5. Save the protocol (File > Save Protocol As).
Follow this sequence of tasks when developing a protocol to take advantage of the
automatically created Gen5 data reduction events. For example, when you add Blanks to the
Plate Layout, Gen5 automatically creates a Blank-Subtraction data set.
You can find instructions for developing specific types of protocols in the Gen5 Help.

Define the Reading Procedure
Protocol > Procedure
Procedure grayed out? When more than one plate has been read in an experiment, the
procedure cannot be changed for the current experiment. If this isn't the case, your System
Administrator may have restricted your ability to modify the protocol elements.
Grayed-out buttons mean the action cannot be performed by the current reader or because
previously defined steps--for example, a kinetic loop--limit the function or your level of
software limits the feature.

How to:
For all procedures, define the Plate Type and then:
1. Click a link to add that step to the procedure. Most links open a screen for defining the
parameters of that step, for example, Read lets you define wavelengths.
When defining a kinetic or synchronized well/plate mode analysis, add the Kinetic and
Synchronized Mode steps first. Kinetic and Synchronized Mode steps form a loop or block.
Put the Read and other valid steps to be performed inside the loop, between the Start and
End. Monitor Well is similar: First add the Monitor Well step and then add a Read step inside
the Monitor Well loop.
2. Define the details of the step and click OK.

BioTek Instruments, Inc.

---

Define the Plate Layout | 67

3. Click Validate to check the selection and sequence of the steps.
Your instrument must be communicating with Gen5 for it to fully validate the procedure:
Make sure it is turned on, not busy, and properly connected to the PC.

StepWise Procedure Features
l

l

You can drag and drop steps in the procedure to change their sequence order.
You can also copy (Ctrl+C) and paste (Ctrl+V) a procedure step or a block of steps from one
location to another in a the same procedure.

l

Highlight a step in the procedure, and then click an action button to add a step before it.

l

Double-click a step to open it for editing.

l

Select a step in the sequence and right-click for additional options.

l

l

l

Click Validate at any time to verify the reader's ability to perform the current sequence of
steps.
Highlight a step and press Delete to remove it from the procedure.
Kinetic analysis, Synchronized Mode processing, and Monitor Well functions are set up in
a loop or block. First define the function, for example, add the Kinetic step, and put the
read and other steps inside the loop

Drag and drop is limited in Synchronized Modes. For example, you cannot drag and drop a step
into or out of a Well Mode block.

Define the Plate Layout
Protocol > Plate Layout
The Plate Layout Wizard appears only when no plate layout has been defined (including
Preferred Well IDs) and the wizard is not disabled in Do Not Show Preferences.
1. In the Plate Layout Wizard, select the well types you want to define for the plate, then click
Next. The Wizard prompts you to define each type of well you have selected. When all well
types are defined, the Plate Layout dialog opens.
2. Select a well ID in the left pane, then click in a well, or drag over contiguous wells, to assign
the selected well type to the plate layout.
Some readers support random well selection.
l

The well assignment starts with the well ID you select in the left pane. For example, if you
select Well SPL1:4 in the left pane, when you click in a cell in the plate layout, that cell will

Gen5 Getting Started Guide

---

68 | Set Up a Protocol

be assigned SPL1:4.
l

l

l

Use the Auto Select and Replicates options to speed up your work: set the options and
click and drag to fill multiple wells at once. Click a column or row header to fill it.
Use the Serial Assignment tools (
,
, and
) to quickly assign replicates to the plate
layout in a horizontal or vertical line or in square groupings. Select one of the directions
(toggle through to access horizontal, vertical, or square) then click or drag in the plate
layout.
You can export a plate layout for use in multiple experiments, or import an existing plate
layout.

The type of plate, such as 96-well, is defined in the procedure and displayed in a representative
matrix or grid format in the Layout and Transformation screens.

Helpful Hints
l

l

l

l

l

l

l

l

l

l

Set up your preferred default Well IDs at System > Preferences > Plate Layout Well IDs.
For example, you can define PC (for Positive Control) instead of CTL1 for Assay Controls.
Well IDs defined in the System Preferences are available when defining the plate layout for
all newly created protocols/experiments.
Click Undo at the bottom of the screen to undo the last action. Up to 10 previous actions
can be undone.
To clear the grid and start over, right-click and select Empty Layout. To clear selected cells,
set the Type of Well Settings to Empty and select the cells you want to clear.
You can print the plate layout. 384-well plates print out in two sections, columns 1-12 and
13-24. 1536-well plates print in eight sections to fit all 48 columns and rows from A to Z and
AA to AF.
For Samples (unknown test specimen) Gen5 lets you assign and track data points, such as
age or gender, in addition to the Sample ID. You can create additional identification fields.
To copy the contents of the grid to the Windows virtual clipboard to paste into a
text/external file, right-click and select Copy Layout. Open the receiving file, for example,
Microsoft Word or Excel, then right-click and select Paste. Generally, plates larger than 96
wells do not fit completely in a standard-size Word or text file; a spreadsheet is required.
Each instance of a Sample and Sample Control Well ID and each Assay Control group can
have a unique concentration/dilution value. Gen5 assigns a dilution index to the Well ID to
keep track each instance.
Well selection must be compatible with the Replicate, Auto Select, and Filling option
settings.
You can resize the plate view in the standard Microsoft Windows way: click and drag the
outer borders of the view, or click the maximize button in the top-right corner.
You can resize the rows and columns: hover your mouse over a grid line between two
numbered columns or alpha-labeled rows until the cursor changes to a separator, then

BioTek Instruments, Inc.

---

Set Up Data Reduction | 69

click and drag.
l

When running an experiment with a cuvette, the plate layout is mapped on a 96-well plate.

Set Up Data Reduction
Protocol > Data Reduction
There are several options available for interpreting the results of your experiment. Gen5
automatically creates the most commonly applied data reduction steps.

Top Six Things to Know about Data Reduction
1. Reductions are StepWise, that is, they can be built one upon another based on their
sequence in the Data Reduction dialog. For example, a data set created in a previous step
can be used in a later transformation, curve, cutoff, and so on, if applicable.
A slight exception to this StepWise rule is Replicate Rejection, which must be the first step
applied to a data set before it can be used as Data In. Because replicate rejection can
mask data, altering the data values, it must be performed before the data set is used in a
calculation.
2. Gen5 creates some data reduction steps automatically:
l

l

l

l

When blanks (BLK) are assigned to the plate, Gen5 automatically creates a Blank
Subtraction data set. Gen5 subtracts the mean of the blanks from all other wells on
the plate.
A Well Analysis step is created when a multi-read index Read step is defined: Kinetic,
Spectrum, Area, or Linear Scan. If applicable, blank-subtraction results are used to
perform the well analysis.
A path length-corrected data set is created when this option is selected in an
Absorbance read step.
The Fluorescence Polarization (FP) transformation is performed automatically when
this reading mode is selected in the Read step. If applicable, blank-subtraction results
are used to perform the FP reduction. In kinetic experiments, well analysis is based
on the FP transformation results.

3. Once the Data Reduction dialog is opened and saved, that is, OK is selected to close it,
Gen5-created reductions are no longer added, deleted, or changed. Keep this in mind when
modifying a protocol or experiment.
4. Plate-specific Data Reduction Variables can be collected from users when they read the
plate so Gen5 can use them in data reduction calculations. First, define the variable in the
Runtime Prompts (Protocol menu), then write a formula using the variable. At runtime,
when the measurements and variables are obtained, Gen5 performs the calculation using
the input value. You can also create a static experiment-level, rather than plate-level, Data
Reduction Variable for use in calculations when defining Data Reduction steps.
5. Raw data sets used in Data Reduction steps are named according to the Gen5 Data Set
Naming Convention, which is based on the number of Read steps defined in the procedure.
When the number of read steps is changed, any previously defined Data Reduction steps

Gen5 Getting Started Guide

---

70 | Set Up a Protocol

are voided, because the data set name is also changed. When you add or remove a Read
step, you must update the effected Data Reduction steps.
6. In the Data Reduction dialog, you can:
l

Double-click a step to open it for modification or deeper review (or right-click and
select Edit).

l

Copy and paste a Data Reduction step with a right-click or Ctrl+C and Ctrl+V.

l

Select a step and right-click to delete it.

l

Drag and drop to change sequence (in limited circumstances, when Data In and
data out, i.e., New Data Set are not affected).

Make sure none of the Data Reduction step icons display the red invalid symbol. The invalid
symbol may indicate that a previously selected data in set has changed, e.g., it has been renamed.

About Exporting Results
Gen5 provides the following exporting tools:
l

QuickExport: to instantly export the current view to a Microsoft Excel worksheet

l

Export to Excel: to export selected data to Excel using the Power Export feature

l

l

Export to File: to export selected data, excluding curves, to a text file (for use in another
software application) using the File Export feature
Right-Click Menu Options: Copy to Clipboard and Save As; to copy or save the current
selection for use in another software application

l

Quick Export Image: to instantly export an image to an Excel spreadsheet.

l

Quick Export Metadata: to export an image's metadata to an Excel spreadsheet.

Prerequisites
For the QuickExport and Power Export features, you must have Excel 2007 or higher installed on
your PC. Use File Export or right-click options if you do not have Excel.

About the Export Tools
l

l

l

The Power Export and File Export methods require selecting the content you want included
in the output file before executing the export for a designated plate.
You can save your export selections with the protocol to reuse them every time you run an
experiment based on that protocol.
Exporting data is like generating a report; it is done individually for each plate*. Although
you can select the export content in a protocol, you must run (or execute) the export in an
experiment (after selecting a plate or multiple plates).
[* except in multi-plate assays]

BioTek Instruments, Inc.

---

About Reports | 71
l

In an experiment, to run the export, you can select a plate in the menu tree and right-click
for a menu that offers the Export option.

Export Multiple Plates to One File
When you run multiple plates in an experiment you can export all the data to one file:
1. In the menu tree, select/highlight multiple plates (by holding down the Ctrl key).
2. Right-click and select Export.
Make sure the File Export Settings are defined to automatically append the data.

About Reports
Protocol > Report/Export Builders > New Report
You can use the Report/Export Builders to define exactly:
l

What to include in the report

l

How to format an item in the report

l

Where to place the item in the report

Defining Report Elements
1. When setting up the protocol, after customizing the Data Views, select Report/Export
Builders from the Protocol menu tree.
2. From the Report/Export Builders dialog, click New Report.
3. Define your settings in the Properties, Content, and Options screens, then click OK. If you
are running Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, or
Gen5 IVD Image+, Gen5 prompts you to add a comment to the Audit Trail event.

Gen5 Getting Started Guide

---

72 | Set Up a Protocol

---

fluorescence
errors 48

Index

G
B
buttons 45

C
communication errors 47
computer requirements 10
curves
create standard 60

D
data reduction
set up 69
databases
copying to a network 31
moving to a network 31
organize 30
diagnostics
test the reader 63
duplicating a plate view 61

E
email notification feature
configure 38
email server, configure 38
errors
communication 47
fluorescence 48
luminescence 48
experiments
vs. protocol 54
export
File Export 70
Power Export 70
QuickExport 70
exporting
results 70

F
File Export
about 70
file storage
about 55

Gen5
available levels 14
best practices 57
install 15
licence agreement 8
register with BioTek 20
set up 25
supported readers 10
warranty 8
workspace 41
Gen5 databases 29
Gen5 Image+
about 14
setting up 25
Gen5 Image+ IVD 26
about 14
Gen5 Image+ Secure 25
about 14
Gen5 IVD 26
Gen5 Reader Control 26
Gen5 Secure
set up 25

I
icons 45
imaging
save options, default 20
install Gen5 15
instrument control
connecting an instrument 24

L
login 35
luminescence
errors 48

M
menu tree
using 44

P
password
changing system administrator's 28

---

74 | pinning a view

controls 35
pinning a view 61
plate layout
define 67
plate view
duplicating 61
pinning 61
Power Export
about 70
printing results 62
procedure
defining 66
protocols
designing 66
vs. experiments 54
workspace 43

Q

U
user accounts
about 32
create 32-33
maintain 33
modify 32
user groups
about 32
create 33
modify 33

V
viewing results 61

W
Windows authentication
configure 36

Quick Export
about 70

R
reports
building 71
restore optimal performance 48
right-click menu options 70

S
standard curve
create 60
system administrator
as-needed tasks 28
changing password 28
password 52
setting up Gen5 IVD 27
setting up Gen5 Secure 27
system requirements
computer requirements 10
reader requirements 10

T
Task Manager 40
trademarks 2
troubleshooting
general 47

BioTek Instruments, Inc.

---
