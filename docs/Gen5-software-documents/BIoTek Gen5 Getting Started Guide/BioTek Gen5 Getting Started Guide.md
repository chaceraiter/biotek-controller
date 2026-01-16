# BioTek Gen5 Getting Started Guide

Agilent BioTek Gen5 Data Analysis Software

Getting Started Guide

ERRATA NOTICE: This document contains references to BioTek.
Please note that BioTek is now Agilent. For more information, go to
www.agilent.com/ lifesciences/ biotek.

---

BioTek Gen5
Getting Started Guide
Microplate Data Collection and Analysis Software

Agilent Technologies, Inc.
(C) 2022

---

2 | Welcome to Gen5

Welcome to Gen5
BioTek Gen5 software for BioTek multimode and single mode microplate readers is
an integrated tool for endpoint, kinetic, spectral scanning and well area scanning. It
controls all the functions of the plate reader and has powerful data analysis
capabilities for a broad range of applications. Gen5 microplate reader software is
also used to integrate BioTek plate readers to BioTek BioStack and other automated
syste.
BioTek Gen5 Software for imaging and microscopy offers automated image capture,
processing and analysis for a broad range of samples, from whole organism imaging
to high magnification subcellular imaging. Raw data and images are transformed
into meaningful results with powerful built-in capture, process and analysis tools.
The automated process, known as Augmented Microscopy, enables simple and
straightforward imaging and analysis workflows.

Agilent Technologies, Inc.

---

|3

Contents
BioTek Gen5 Getting Started Guide

1

Welcome to Gen5

2

Contents

3

Revision History

9

Install Gen5

11

Computer System Recommendations

12

Non-Imaging Use

12

Imaging

12

Example: Required Hard Drive Space for Imaging in standard FOV and
WFOV/Confocal

13

Gen5 - Instrument Compatibility Chart

14

Gen5 Software Level Comparison

19

Imaging-Specific Capabilities

20

Install the Software on a Computer

21

Prerequisite

22

Install Gen5 (all versions on a computer)

22

Custom vs. Typical Installation

22

Gen5 OLE Automation Toolkit

23

Printer Settings

23

Recommended Installation Sequence for Imaging

23

Install the USB3/Hamamatsu Camera Driver

24

All Imagers Except Cytation C10 Models with Hamamatsu Camera

24

Cytation C10 with Hamamatsu Camera: C10PHC2 and C10MPHC2 Models

25

Gen5 Getting Started Guide

---

4 | Contents

Establish Communication with the Camera

25

Troubleshooting Software Drivers

25

Defining the Image Library

26

Change the Virtual Memory Settings

26

Disable Sleep Mode

27

Turn Off Automated Updates

27

Storing Gen5 Files on an External Hard Drive

27

Register with Agilent

28

Launch Gen5 and Register the Software

29

Gen5 Licensing

30

Add-On Modules:

31

Initial Setup

33

Connect an Instrument

34

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime

35

Recommended Tasks to Perform

35

Set Up Gen5 Secure, Gen5 Secure Image+, or Gen5 Secure Image Prime

36

Set Up Gen5 IVD or Gen5 IVD Image+

36

Set Up Gen5 Reader Control

37

System Administrator's To-Do List

38

Initial Setup Tasks: All editions of Gen5 Secure

38

Initial Setup Tasks: All editions of Gen5 IVD

38

Periodic/As Needed Tasks

39

Change the System Administrator's Password

39

About Gen5 Databases

40

Organize Your Database Files

43

Agilent Technologies, Inc.

---

|5

File Management Recommendations

43

Move or Copy a Database to a Network

44

About User Accounts

45

Prerequisite

45

How to Create, Modify, or Delete User Accounts

45

About User Groups

46

Prerequisite

46

Create New Groups and Modify Existing Groups

47

Create/Maintain User Accounts

48

Prerequisite

48

User ID

48

Full Name

48

Group

48

Status

48

Startup Mode

49

Startup Action

49

Protocol and Experiment Folders

50

Password

50

Login/Password Controls

50

Prerequisite

50

Login

51

Password

52

Configure Windows Authentication

53

Gen5 Administrator Tasks

53

IT Administrator Tasks

54

Gen5 Getting Started Guide

---

6 | Contents

Configure the Email Notification Feature

54

Defining a Custom Email Template

55

Configure the Email Server

55

Getting Technical Assistance

56

Getting Started

57

Launching Gen5

58

Startup Mode

58

Change Your Startup Preferences

58

Change Your Startup Preferences in Gen5 Secure and Gen5 IVD

60

Task Manager

61

Instant Access

62

Standard Mode Gen5 Workspace

63

Protocol Workspace

66

The Menu Tree(Standard Mode)

67

Buttons and Icons

68

Imaging : Manual Mode

72

Important Prerequisites

72

Focusing and Capture

72

Process and Analyze

73

Edit the Image Processing Step

74

Analyze Captured and Processed Images

75

Troubleshooting

75

Communication Errors

76

If Gen5 fails to save a file

76

When the computer wont communicate with the instrument

76

Agilent Technologies, Inc.

---

|7

Serial Cable Connected and Keypad Readers

77

Restore Optimal Performance

78

Fluorescence/Luminescence Measurements

79

Fluorescence/Luminescence Readings Too Low

80

Fluorescence Background Too High

80

Reader Not Achieving Desired Fluorescence Detection Limit

82

Reader Over-ranging in Fluorescence

83

Bandwidth Verification Failed

83

Error during Auto-Sensitivity Determination

83

Optimizing Imaging Performance

85

System Administrator's Password

86

Essential Concepts

87

Experiment vs. Protocol

88

About File Storage

90

File Types

90

Databases

90

File Location

91

Image File Management

92

Defining the Gen5 Image Library

92

Storing Images

92

Best Practices

93

Efficiencies

93

Time-Savers

94

Basic Tasks

95

Quick Read

96

Gen5 Getting Started Guide

---

8 | Contents

Perform a Quick Read:

96

Create a Standard Curve

96

View Results

98

Important Notes

99

Plate View (Workspace)

100

Print Results

100

Prerequisite

100

Test the Instrument

101

Test History

101

Set Up a Protocol

103

Design a Protocol

104

Define the Imaging or Reading Procedure

104

StepWise Procedure Features

105

Define the Plate Layout

106

Helpful Hints

107

Set Up Data Reduction

108

About Exporting Results

110

Prerequisites

110

About the Export Tools

110

Export Multiple Plates to One File

111

About Reports
Defining Report Elements
Index

111
111
113

Agilent Technologies, Inc.

---

|9

Revision History
Rev

Date

Changes

R

2022

Added support for Lionheart WFOV imagers. BioTek Instruments is now Agilent Technologies: Gen5 has been
rebranded, including a new desktop icon, to support
BioTek's integration with our new company, Agilent.
Online Sample Files provided via the Task Manager are
now accessed from an Agilent website: https://www.agilent.com/en/gen5-lhc-sample-files.

Gen5 Getting Started Guide

---

10 | Revision History

---

Install Gen5
An "install wizard" guides you through the installation of Gen5--just follow the
prompts. Before doing so, make sure your computer and Agilent instruments meet
the system recommendations outlined in this section. You may also want to review
the installation options, software warranty, and related information.
Computer System Recommendations

12

Gen5 - Instrument Compatibility Chart

14

Gen5 Software Level Comparison

19

Install the Software on a Computer

21

Recommended Installation Sequence for Imaging

23

Install the USB3/Hamamatsu Camera Driver

24

Establish Communication with the Camera

25

Defining the Image Library

26

Register with Agilent

28

Gen5 Licensing

30

---

12 | Install Gen5

Computer System Recommendations
To achieve the best Gen5 performance, Agilent offers the following
recommendations.
Non-Imaging Use
l

64-bit version of Windows 10 Professional editions (or equivalent) version V1909,
2004, or 20H2

l

Intel Celeron Dual Core Processor T1600 (1.66 GHz, 667 MHz FSB, 1 MB L2 cache)
or equivalent

l

2 GB RAM or higher

l

100 GB free hard drive space or higher

l

Monitor resolution 1280 x 800 or higher

l

Keyboard/mouse

l

Microsoft Internet Explorer v 9.0 or higher (for online Help); for Take3
XTML export, Internet Explorer v 10 or higher

l

Microsoft Excel 2007 (32-bit only) or Microsoft Excel 2010 or higher (either 32- or
64-bit, install one edition only) for QuickExport and Power Export

l

Serial or USB port for Agilent instrument

Imaging
Agilent provides an imaging controller for instruments that support imaging. The
imaging controller is the recommended host computer. The system
recommendations below are for host computers not supplied by Agilent.
l

64-bit version of Windows 10 Professional editions (or equivalent) version V1909,
2004, or 20H2
Windows N Editions and KN Editions, N for Europe and KN for Korea,
require installation of the Media Feature Pack for N and KN versions
available free from Microsoft Corporation.

l

Intel(R) Core i5 (4th generation) processor or higher

Agilent Technologies, Inc.

---

Computer System Recommendations | 13

l

Intel 8 USB chipset or higher

l

8 GB RAM or higher

l

512 GB hard drive space or higher*

l

Monitor resolution 1680 x 1050 or higher**

l

Software:
l

Gen5 Image+, Gen5 Secure Image+, or Gen5 IVD Image+, or any edition of
Gen5 Image Prime. Spot Counting and/or Auto ROI add-on modules are
required for these advanced-level cellular analysis features.

l

Microsoft Internet Explorer v 9.0 or higher (for online Help)

l

Microsoft Excel for QuickExport and Power Export:
l

Gen5 3.0 or higher: Excel 2007 - 2016 (either 32- or 64-bit, install one edition
only)

l

Keyboard and mouse

l

Connectivity:
l

USB3 port for camera

l

USB 2 or 3 port for instrument

* Each image is approximately 2 MB in size, and 7.8 MB when using a wide field-ofview (WFOV) camera. Image file management is the responsibility of the user. An
RJ-45 Lan connector is recommended for network use. Do not use a WiFi network
connection.
** Gen5 is not designed for use on very high resolution monitors, e.g., 4K or 5K
monitors.
Example: Required Hard Drive Space for Imaging in standard FOV and WFOV/Confocal
Space Required
Imaging Parameters
Std FOV

WFOV1

1 image (standard FOV and WFOV)

2.166 MB

7.8 MB

96-well plate, 1 image per well (96 images x 1 color)

208 MB

749 MB

Gen5 Getting Started Guide

---

14 | Install Gen5

Space Required
Imaging Parameters
Std FOV
96-well plate, RGB, 1 field of view per well (96 wells x

WFOV1

624 MB

2.2 GB

2.1 GB

7.5 GB

6.2 GB

22 GB

78 MB

281 MB

6 H&E slides, whole sample, 15x15 montage (6 samples 8.8 GB

32 GB

3 colors)
96-well plate, DAPI, z-stack, 10 slices per well (96
wells x 1 color x 10 z-planes)
96-well plate, RGB, z-stack, 10 slices per well (96
wells x 3 colors x 10 z-planes)
1 tissue section slide, RGB, 4x3 montage (1 sample x 4
x 3 x 3 colors (RGB))

x 15 x 15 x 3 colors (RGB))
Z-stack-Montage-Kinetic in 24-well plate, Green &

199.6 GB

718.8

DAPI (2 colors) 6 slices - 4x4 tiles - 20 time points

GB

(reads) (24 samples x 6 slices x 16 tiles x 2 colors x 20
reads)
1Confocal image file sizes match WFOV image file sizes.

Gen5 - Instrument Compatibility Chart
Verify that the basecode built into your Agilent instrument is compatible with Gen5.
Note: If your instrument reveals a basecode with a version number lower
than those provided here, please contact TAC for instructions for
downloading and installing updated software.

Agilent Technologies, Inc.

---

Gen5 - Instrument Compatibility Chart | 15

Product

Basecode PN

Compatible

Compatible

Basecode

Gen5

Version

Version1

800 TS

1560200

All versions

3.03 >

Cytation 1

1650200

All versions

3.03 >

Cytation 3

1220200

1.04 and 1.05 2.04

Cytation 3

1220200

1.14

2.05 >

Notes

Adds ability for 40x
and 60x objectives
and Gen5 Image+

Cytation 5

1320200

All versions

2.07 >

W Models

1320200

2.05

3.06 >

Cytation 7

1720200

All versions

3.09 >

Cytation C10

1940200

All versions

3.11 >

ELx800

7330202

3.07

1.00 >

ELx808

7340201

3.15

1.00 >

Eon

1020200

All versions

2.00 >

(1.00)
Epoch

7200200

All versions

1.09 >

(1.07)
Epoch 2

1330200

All versions

2.06 >

(1.06)
FLx800

7080207

1 > this version and higher

Gen5 Getting Started Guide

1.15

1.00 >

---

16 | Install Gen5

Product

Lionheart - LFX

Basecode PN

1760200

Compatible

Compatible

Basecode

Gen5

Version

Version1

All versions

3.01 >

Notes

Basecode, PN
2020200, applies

LLX

1760200

All versions

3.04 >

LFXW

2020200

All versions

3.12

LLXW

2020200

All versions

3.12

LogPhase 600

1800200

All versions

3.09 >

only to the "W"
models: LFXW and
LLXW.

Requires its own
dedicated software
app, in addition to
Gen5.

PowerWave2

7280201

1.21.1

1.00 >

PowerWaveXS

7300200

1.06

1.00-3.03

PowerWaveXS2

7300205

All versions

1.02 >

PowerWaveHT

(1.08)
Synergy 2

7130202

1.06

1.01 >

Use of Synergy 2/4
universal basecode
7160204 (version
1.12 or higher)
requires Gen5 version 1.04 or higher.

Synergy 4

7160204

All versions
(1.08)

1.04-3.03

Synergy 2/4
basecode combined
at version 1.12.

1 > this version and higher
2Several obsolete PowerWave models, with part numbers that began with PRW, are

not compatible with any version of Gen5.

Agilent Technologies, Inc.

---

Gen5 - Instrument Compatibility Chart | 17

Product

Synergy H1

Basecode PN

8040200

Compatible

Compatible

Basecode

Gen5

Version

Version1

All versions

1.11 >

Notes

Basecode 2.00 with
S2-DIP2 toggled for

(1.01.1)

gradient incubation
requires Gen5 2.01
or higher.

Synergy H1

8040200

2.10

2.09 >

Adds dynamic
extended range for
fluorescence reads.
Requires
PMT calibration by
service if upgrading
from version 2.0 or
earlier.

Synergy H1: M2

1910200

1.00

3.09 >

New in version
3.09, Synergy H1
M2 models support
variable bandwidth
monochromators.

Synergy H4

8030200

All versions

1.10 >

(1.00.1)
Synergy HT

7090202

2.24

1.00 >

Synergy HTX

1340200

All versions

2.06 >

(1.02)
Synergy LX

1500200

1 > this version and higher

Gen5 Getting Started Guide

All versions

3.04 >

---

18 | Install Gen5

Product

Synergy Mx

Basecode PN

7190200

Compatible

Compatible

Basecode

Gen5

Version

Version1

All versions

Notes

1.07 >

(1.01.0)
Synergy Neo

1030200

All versions

2.01 >

(1.03)
Synergy Neo2

1350200

All versions

2.09 >

T models

1350200

v.2.02

3.06 >

uQuant

7270201

2.02

1.00-2.06

(MicroQuant)

1 > this version and higher

Agilent Technologies, Inc.

---

Gen5 Software Level Comparison | 19

Gen5 Software Level Comparison
Agilent offers levels of Gen5, from the most basic Reader Control to the fullfeatured, imaging-capable, and FDA-compliant Gen5 Image+ IVD. In addition, AddOn Modules are available for advanced cellular analysis functions: Spot Counting
and Auto ROI modules.
Part Number

GEN5*

GEN5SECURE*

GEN5IVD

GEN5IPLUS*

GEN5SECUREIPLUS*

GEN5IVDIPLUS

Gen5

Gen5

Gen5

Gen5 Secure

Gen5 IVD

Secure

IVD

Image+

Image+

Image+















































































Gen5

Instrument

GEN5IPRIME*

Gen5
Image
Prime

GEN5SECUREIPRIME*

Gen5 Secure
Image Prime

Control
Data reporting and
exporting
Analysis
Single and
multi-mode
data analysis
Image capture and
basic analysis
Image capture and
enhanced
analysis
Image capture and
advanced
analysis
Additional
Features
21 CFR Part









11 compliant features
IVD com-

Gen5 Getting Started Guide







---

20 | Install Gen5
Part Number

GEN5*

GEN5SECURE*

GEN5IVD

GEN5IPLUS*

GEN5SECUREIPLUS*

GEN5IVDIPLUS

Gen5

Gen5

Gen5

Gen5 Secure

Gen5 IVD

Secure

IVD

Image+

Image+

Image+

Gen5

GEN5IPRIME*

GEN5SECUREIPRIME*

Gen5

Gen5 Secure

Image

Image Prime

Prime

pliant features
QC Trend-









ing
Gen5 Validation
Package
included**

* For Research Use Only. Not for Diagnostic Use.
** Gen5 Validation Package is available for purchase separately for all other Gen5
editions.

Imaging-Specific Capabilities
Features
Supports all imaging instrument hardware functionality

Standard Image+

Image
Prime







Image up to 4 color channels per image set







Fast kinetic imaging (up to 10 fps)







Long-term kinetic imaging (up to 7 days)







Z-stack imaging of up to 200 slices for thick samples







Montage imaging for large samples







Combined z-stack and montage imaging







Set multiple beacons per well or vessel in an experiment











Background flattening to improve image signal to noise





Add annotations, including text, shapes, call outs, to any image









Image Acquisition

Find ROIs: use low magnification to discover ROIs, capture ROIs
with high mag
Image Processing

or graph
Record movies of live samples and/or make movies of kinetic

Agilent Technologies, Inc.

---

Install the Software on a Computer | 21

Features

Standard Image+

Image
Prime

image series
Image deconvolution to improve resolution





Digital phase contrast to improve contrast in brightfield images











Cell count and confluence on a live sample







Cell count and confluence on an acquired image















Cellular Analysis
Image Statistics (e.g., image total intensity, intensity above/below a threshold)

Cellular analysis using a single analysis mask (e.g., object size,
shape, area, circularity, intensity)
Analyze subpopulations of cells expressing certain criteria (e.g.,
size, shape, intensity)
Two analysis masks for advanced measurements (e.g., cyto-



plasmic signal, signal translocation)
Advanced cellular analysis optimization tools



Scatterplots/histograms for visualizing and gating cell level



data
Optional Add-On: Spot Counting Module for intracellular objects



(e.g., mitochondria, steatosis)
Optional Add-On: Auto ROI Module for automatically detecting





ROIs based on user-defined parameters.

Note: Add-On Modules are also available, for some Gen5 editions, to provide
additional functionality.

Install the Software on a Computer
Note: Install Microsoft Office before installing Gen5 (if applicable).

Note: Recommended Installation Sequence for Imaging on page 23.

Gen5 Getting Started Guide

---

22 | Install Gen5

Prerequisite
Gen5 requires the user who is installing Gen5 to have Administrator privileges for
the Windows operating system. If a user with restricted access attempts to install
the software, errors may occur. Contact your organizations system administrator if
you are uncertain about your privileges.
Note: Agilent strongly recommends running a Windows Update to ensure the
latest Windows security fixes and critical updates are installed prior to
installing Gen5.
Install Gen5 (all versions on a computer)
1. Start Windows.
l

Be sure you have administrative privileges.

2. Follow the instructions from the insert, Installing Gen5 Software and USB
Drivers, found on the inside of the USB flash drive case.
Note:
l

The Typical installation option is strongly recommended for most users
(see below).

l

Gen5 asks for the serial number shown on your product packaging. Enter
it and click Continue to save time later. If the number is unavailable you
can click Cancel and provide this information later.

l

Be sure to register with Agilent for the fastest response from our support
team, should the need arise.

Custom vs. Typical Installation
The Typical installation option is recommended for most users. It installs:
l

Gen5 application (Gen5.exe and supporting files)

l

Gen5 Diagnostic module

l

Gen5 Take3 module

Agilent Technologies, Inc.

---

Recommended Installation Sequence for Imaging | 23

For Custom installations, click the arrow next to a feature to display the options
menu. Select the desired option. When you opt to not install a feature, its disk icon
is replaced with a red X.
Gen5 OLE Automation Toolkit
Custom installation is required during software installation to install the Gen5 OLE
Automation Toolkit for programming robotic instruments to use Gen5. Instead of
selecting the Install Wizards default option for Typical installation, select Custom.
Change the setting for OLE Automation Toolkit to install this feature.
Gen5 installs an OLE Automation folder when this option is selected. Youll find the
Gen5 Automation Programmers Guide (in PDF format), the BTIStatusCodes.h file,
and a Samples folder containing several program samples in common programming
languages.
Note: To learn about security options when using OLE Automation, see
Login/Password Controls in the Gen5 Help.
Printer Settings
When you install Gen5 on a computer with Windows 10, you may need to disable the
Let Windows manage my default printer setting. Otherwise, your computer
changes the default printer every time you use a different printer. Note that this
option is not always present.
1. From the main screen, click Settings > Devices > Printers & scanners.
2. In the Let Windows manage my default printer box, turn off the option.

Recommended Installation Sequence for Imaging
After following the detailed installation instructions provided in the imaging
instrument's user manual, perform the following steps for the best experience:

Gen5 Getting Started Guide

---

24 | Install Gen5

1. Set up the hardware components as applicable, including:
l

Removing the shipping hardware from the instrument

l

Connecting the gas controller, dispenser, and joystick

2. Install Gen5 on the host computer.
3. Install the USB driver software shipped on the Gen5 software USB flash drive.
4. Connect the instrument to the controller (host computer) with the USB cable.
5. Connect the USB3 camera cable to a USB3 port, and power on the instrument.
Launch Gen5 and follow the prompts to configure your instrument.
6. Install the Camera Driver.

Install the USB3/Hamamatsu Camera Driver
Note: You must install the Gen5 software and connect the instrument to the
controller (host computer) via both USB cable and USB3 camera cable before
performing this procedure.
All Imagers Except Cytation C10 Models with Hamamatsu Camera
Follow these steps to install the USB3 camera driver:
1. Navigate to the Gen5 program files
on your computer, for example,
C:\Program Files\Agilent\Gen5 <version>.
2. Open the USB3 Drivers folder, the
Windows_64 folder, and the
PGRUSBCam folder.
3. Right-click Install PGRDriver.bat,
and select Run as Administrator to
run the driver installer.

Agilent Technologies, Inc.

---

Establish Communication with the Camera | 25

Cytation C10 with Hamamatsu Camera: C10PHC2 and C10MPHC2 Models
1. Navigate to the Gen5 program files on your computer, for example, C:\Program Files\Agilent\Gen5 <version>.
2. Open the HamamatsuDrivers folder.
3. Right-click setup.exe, and select Run as Administrator to run the driver
installer.
Restart the controller (host computer) after installing the camera driver.

Establish Communication with the Camera
1. From the main Gen5 screen, select System > Instrument Configuration,
select your instrument, and then click View/Modify.
2. Click Test Communication.
3. Click Camera Information. If communication is successful, Gen5 displays
information about the camera.
Note: Check the Bus Speed; it should be 5000 Mbits/sec. If a lower bus speed
is reported, review the troubleshooting information next.
Troubleshooting Software Drivers
Some suggestions for troubleshooting either communication with the camera or a
bus speed significantly lower than 5000 Mbits/sec follow:
l

Reboot the host computer.

l

Disconnect and reconnect the USB3 cable from/to the host computer.

l

Rerun the batch (.bat) file as described in step 3 of Install the
USB3/Hamamatsu Camera Driver on the previous page.

l

Make sure the computer meets the Computer System Recommendations on
page 12.

If problems persist, ask your IT group for support or See Getting Technical
Assistance on page 56.

Gen5 Getting Started Guide

---

26 | Install Gen5

Defining the Image Library
System > Preferences > Image Save Options
Use the Image Save Options under System > Preferences to define the Image
Library storage location for saving image files. The Image Save Options settings
apply to all newly created experiments. Likewise, they apply to all
computers/controllers sharing the same Shared DB on a network.
Using an external hard drive for storing image files, i.e., the Image Library, is
strongly recommended as image files are much larger than typical data files. See
Storing Gen5 Files on an External Hard Drive on the facing page.
Note: To override these settings in an individual experiment, go to Protocol
> Protocol Options > Image Save Options, and click Select new image
folder. Navigate to the new image folder, then save the experiment file.

Change the Virtual Memory Settings
Note: Imaging controllers (host computers) supplied by Agilent have already
been configured properly. Skip this step if you are running a Agilent-provided
imaging controller.
For instruments with the imaging module, it is recommended that you prevent
Windows from automatically manage paging file size.
1. From the Windows Start menu, go to Control Panel, and select System.
2. In the left pane, select Advanced system settings.
3. In the System Properties dialog, on the Advanced tab in the Performance area,
click Settings.
4. In the Performance Options dialog, on the Advanced tab in the Virtual memory
area, click Change.

Agilent Technologies, Inc.

---

Defining the Image Library | 27

5. Clear Automatically manage paging file size for all drives, if it is selected.
This is the default setting for Windows 7 and higher.
6. Select Custom Size, enter the following minimum and maximum values, click
Set, and then click OK:
l

Initial size: 20480 MB

l

Maximum size: 40 GB*

7. You will need to restart your computer for the change to take effect.
* The limit of 40 GB will allow you to work with 10,000 to 15,000 standard field-ofview images in memory at the same time. If you plan to open more images for
processing at one time, consider increasing this maximum size.

Disable Sleep Mode
Note: Imaging controllers (host computers) supplied by Agilent have already
been configured properly. Skip this step if you are running a Agilent-provided
imaging controller.
Disabling a computer's sleep mode is recommended for all applications, but it is
especially important when running kinetic or time-elapse assays.
1. Open the Control Panel and select Power Options.
2. Click Change plan settings for the power plan you are using.
3. Set Put the computer to sleep at Never.

Turn Off Automated Updates
Consult your Information Technology (IT) experts and if possible, turn off the
computer's auto-update routines, power-saving options, and virus scans that can
interrupt a Gen5 experiment.

Storing Gen5 Files on an External Hard Drive
Here are some guidelines for using an external hard drive for storing Gen5 files,
especially useful for imaging files and experiments:

Gen5 Getting Started Guide

---

28 | Install Gen5

l

Use a USB3 drive for faster transfer rates.

l

Close the Gen5 experiment or manual mode session before ejecting the device.

l

Always use the eject utility when disconnecting the device from your computer.
Do not disconnect the device by just pulling it out:
For example: right-click

or

in the lower-right corner of your task bar, and

select Eject <drive name> or Safely Remove Hardware and Eject Media.

Register with Agilent
The Pre-Registration screen appears when you launch Gen5 until the software is
registered. A trial-version serial number can be used for the specified number of
days until a licensed version is purchased. Unless the purchased version of Gen5 is a
higher version than the trial version there is no need to reinstall the software;
simply register the software.

Agilent Technologies, Inc.

---

Register with Agilent | 29

Note:
You must have administrative privileges to register with Agilent.
Generally, the user who logged in to Windows when installing Gen5
should be logged in when registering the software.
Windows 10 users: If prompted for administrative privileges, engage
them before registering the software: Locate and right-click the Gen5
desktop icon, and select Run as administrator. At the User Account
Control dialog, click Allow.
Launch Gen5 and Register the Software
1. Open Gen5 by clicking its desktop icon or by using the Windows Start button
and selecting Programs > Gen5 > Gen5.
2. At the Pre-Registration dialog enter the product serial number (if it wasnt
entered during installation or if youve been using a trial version).
3. Click Register to register the software and receive a password. The Registration dialog appears with the serial number and the site key; this is information provided by your computer.
Note: Click Demo to run Gen5 without registering it for the number of days
displayed below the Demo button.
4. Click Obtain Password.
l

Alternatively, if your Internet browser and Gen5 are on different computers, enter www.biotek.com into your browsers address field and select
Request Support. Make note of the serial number and site key for this process.

l

If you do not have access to the Internet, see Getting Technical Assistance on page 56. Make note of the serial number and site key for this process.

Gen5 Getting Started Guide

---

30 | Install Gen5

l

When using the same computer, you can copy and paste (Ctrl+C and
Ctrl+V) the serial number and site key into the registration form.

5. At the Software Registration website page, enter or paste the serial number
and site key information into the form and click Submit.
A registration form will be displayed containing any information Agilent
already has about you and your organization.
6. Review and edit the information as necessary, then click Submit Registration
Form.
7. Your password will be displayed on screen. Copy or make note of it.
8. Return to the Gen5 Registration dialog to paste or enter it into the Password
field.
9. Click Validate Password.
The software should now be registered and you will not see the Pre-Registration
screen again.
Note: Gen5 stores the serial number and site key in the Help > About Gen5
screen so you can log in to Agilents product registration site at any time.

Gen5 Licensing
Select Help>Licensing to display current status or activate an Add-On Module
From the Gen5 Licensing dialog, you can
view the Gen5 License Agreement and
warranty information.

Your edition or level of software is displayed. Learn more: Gen5 Software Level
Comparison.

Agilent Technologies, Inc.

---

Gen5 Licensing | 31

Add-On Modules:
You can see which add-on modules are
available for your version of Gen5 and
whether the modules are activated.

If you have purchased an add-on module, click Enter serial number and enter the
dedicated serial number provided in the Gen5 Add-On module software package
(not to be confused with the regular Gen5 software serial number). Your add-on
module must be successfully activated, Registered (serial number) for its
features to be usable.

Gen5 Getting Started Guide

---

32 | Install Gen5

---

Initial Setup
The first thing all users must do after installing Gen5 is connect an instrument to
the computer and tell Gen5 how to communicate with it. Other initial setup steps
can be performed to improve your experience using Gen5. When running Gen5
Secure, Gen5 Secure Image+, Gen5 IVD, Gen5 IVD Image+, and Gen5 Secure Image
Prime, to meet FDA submission criteria, you must establish and maintain security
conditions. Youll find instructions for performing these tasks in this section.
Connect an Instrument

34

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime

35

Set Up Gen5 Secure, Gen5 Secure Image+, or Gen5 Secure Image Prime

36

Set Up Gen5 IVD or Gen5 IVD Image+

36

Set Up Gen5 Reader Control

37

System Administrator's To-Do List

38

Change the System Administrator's Password

39

About Gen5 Databases

40

Organize Your Database Files

43

Move or Copy a Database to a Network

44

About User Accounts

45

About User Groups

46

Create/Maintain User Accounts

48

Login/Password Controls

50

Configure Windows Authentication

53

Configure the Email Notification Feature

54

Configure the Email Server

55

Getting Technical Assistance

56

---

34 | Initial Setup

Connect an Instrument
System > Instrument Configuration
Note: Before connecting the instrument: to the computer, install the
USB driver provided on the Gen5 software USB flash drive. Connect the
instrument after the driver installation is complete.
When you start Gen5 without an instrument connected to your computer, Gen5
prompts you to add one. After its shipping hardware has been removed and other
installation steps completed, connect the instrument to the computer, power it on,
and perform the following steps:
1. Click Yes.
2. Select an instrument from the list, then click OK.
You can also access the Instrument Configuration dialog by clicking System >
Instrument Configuration.
3. Click Add to define the Instrument Settings:
l

Select either Plug & Play or Com Port as the communication type.

l

Plug & Play: Select an available instrument from the list and click OK.

l

Com Port instruments:
l

Select the Instrument Type from the list.

l

Enter the Com port number in the Com Port field.

l

If necessary, select a baud rate. Retaining the default baud rate is
recommended.
Mismatched baud rate settings can cause serial read errors. When the
baud rate is set to a non-default setting for non-keypad instruments,
Gen5 is unable to communicate with the instruments if they are turned
off and then turned on again while Gen5 is running. For keypad
instruments, ensure that the instrument has the baud rate set to 9600.
If the baud rate is changed, the instrument must be rebooted.

Agilent Technologies, Inc.

---

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime | 35

l

If needed, click Setup to change the factory-tested and defined configuration values. Except for imaging and dispensing, this step is rarely
required.

l

Click OK to save the settings.

4. Click Test Comm. Gen5 attempts to communicate with the instrument.
After you receive a passing message, The reader is communicating, you can save
and Close the Instrument Configuration. If you receive any other message, look for
a remedy: See Troubleshooting on page 75

Set Up Gen5, Gen5 Image+, and Gen5 Image Prime
Gen5 fulfills the instrument control and analytical needs for a wide range of
laboratory settings. The degree to which you follow the recommendations provided
here depends on the needs of your organization.
Recommended Tasks to Perform
1. Designate a System Administrator.
2. Install Gen5 on the Administrators computer.
3. Change the System Administrators password (default is admin).
4. Determine the optimal way to store Gen5s protocol and experiment files. See
About File Storage on page 90.
l

Organize the database or your Windows file structure.

5. Install Gen5 for other users and connect an instrument to each computer. See
Connect an Instrument on the previous page.
6. If applicable, direct each users database configuration to point to the correct
shared database.

Gen5 Getting Started Guide

---

36 | Initial Setup

Set Up Gen5 Secure, Gen5 Secure Image+, or Gen5 Secure Image
Prime
1. Designate a System Administrator.
2. Complete the System Administrator's To-Do List on page 38 (the Initial Setup
tasks).
3. Organize the database. See Organize Your Database Files on page 43.
4. Review/modify Signature Reasons and other security controls (select System >
Security).
5. Install Gen5 on each users computer.
6. Set up each users database configuration to point to the correct shared database. See Move or Copy a Database to a Network on page 44.
7. Connect an instrument to each users computer.
8. Advise users to change their passwords.

Set Up Gen5 IVD or Gen5 IVD Image+
1. Designate a System Administrator.
2. Complete the System Administrator's To-Do List on page 38 (the Initial Setup
tasks).
3. Organize the database. See Organize Your Database Files on page 43.
4. Review/modify Signature Reasons and other security controls (select System >
Security).
5. Install Gen5 on each users computer.
6. Set up each users database configuration to point to the correct shared database. See Move or Copy a Database to a Network on page 44.
7. Connect an instrument to each users computer.
8. Advise users to change their passwords.

Agilent Technologies, Inc.

---

Set Up Gen5 Reader Control | 37

Set Up Gen5 Reader Control
1. Install Gen5 on the computer.
2. Determine the optimal way to store Gen5's protocol and experiment files.
l

Organize the database or your Windows file structure.

3. Connect an instrument to the computer. See Connect an Instrument on
page 34.
4. Set user preferences. See the Gen5 Help for more information.

Gen5 Getting Started Guide

---

38 | Initial Setup

System Administrator's To-Do List
Initial Setup Tasks: All editions of Gen5 Secure
1. Make sure all designated computers and Agilent instruments meet the minimum requirements. See Computer System Recommendations on page 12.
2. Install Gen5 Image+ Secure or Gen5 Secure on one computer.
3. Start Gen5 and log in as the System Administrator.
4. Change the System Administrators password.
5. Copy the database Shared.mdb to a secure network location.
6. Test database configuration of the Shared.mdb on the network.
7. Create/modify user groups, as needed, and assign user permissions to the groups.
8. Create new user accounts and assign the users to a group.*
9. Connect instrument(s) to the PC and establish communication.
Repeat Steps 2, 3, 6, and 8 for the remaining computers.

Initial Setup Tasks: All editions of Gen5 IVD
1. Make sure all designated computers and Agilent instruments meet the minimum requirements. See Computer System Recommendations on page 12.
2. Install Gen5 IVD or Gen5 IVD Image+ on one computer.
3. Start Gen5 and log in as the System Administrator.
4. Change the System Administrators password.
5. Copy the database Shared.mdb to a secure network location.
6. Test database configuration of the Shared.mdb on the network.
7. Copy the database QCDB.mdb to a secure network location.

Agilent Technologies, Inc.

---

Change the System Administrator's Password | 39

8. Test database configuration of the QCDB.mdb on the network.
9. Create/modify user groups, as needed, and assign user permissions to the groups.
10. Create new user accounts and assign the users to a group.*
11. Connect instrument(s) to the PC and establish communication.
Repeat Steps 2, 3, 6, 8, and 10 for the remaining PCs.

* For all editions of Gen5 Secure and Gen5 IVD, you can set up an alternative login
method: Configure Windows Authentication on page 53.
Periodic/As Needed Tasks
l

Customize the security features to accommodate your organizations needs.

l

Organize your database files.

l

Educate users on regulatory requirements and Gen5 best practices.

l

Establish and implement a procedure and schedule for record retention and
archival.

l

Review records, including any training/user-qualification records.

Before modifying a users account, make sure he/she is not logged in to the system.
You can check the System Audit Trail to determine who is currently logged in.

Change the System Administrator's Password
System > Security > Users
System > User Setup > Administrator tab
You should change the System Administrators password immediately following
Gen5 installation to ensure a secure operating environment.
To change the password:
1. Log in as the System Administrator, if you havent already done so.
l

Select System > Login/Logout.

l

Set the User to Administrator.

Gen5 Getting Started Guide

---

40 | Initial Setup

l

Enter the default password: admin.
Note: Passwords are case-sensitive. For example, "Gen5admin" and
"gen5admin" are two distinct passwords.

2. Select System > Security > Users.
3. Double-click the System Administrator user (to edit the record).
4. Define and confirm the new password. The System Audit Trail will open to log
the change and accept your comments.
Note: Record and store the new password in a secure location. If you forget
the password, contact Customer Care for assistance.

About Gen5 Databases
Gen5 installs two databases during regular installation: SharedDB and LocalDB. Only
Gen5 Secure, Gen5 Secure Image+ , Gen5 Secure Image Prime, Gen5 IVD, and Gen5
IVD Image+ are initially set up to use the Gen5 Database for experiment and
protocol file storage. All other levels of Gen5 must select to use the database to
store experiment and protocol files at System > Preferences > File Storage Mode.
l

SharedDB can be set up on a network for sharing information among multiple
users. It contains all protocol and experiment data files and their associated
audit trails, the plate types, and reader-diagnostic history data. In all editions of
Gen5 Secure and Gen5 IVD, SharedDB also contains security settings, user
accounts, and a system audit trail for shared events. This database can be
moved, renamed, and copied. So, if desired, you can create a unique database
for individual projects, teams, or other classification.
The SharedDB must reside in a location that presents the minimum risk
of error. Before moving it to a networked drive, it is recommended
that you analyze the network or disk and server to ensure that the

Agilent Technologies, Inc.

---

About Gen5 Databases | 41

error rate is low. It is not recommended that you use WiFi network connections, external drives, or USB flash drives to hold the SharedDB.

Note: Gen5 Image+ IVD and Gen5 IVD also install the QC Trending
database, QCDB.mdb. It can be set up on a network for sharing among
multiple users, moved, renamed, and copied. It is initially installed in a
QC folder in the default database location described below.
l

LocalDB contains the local setup information, including the Instrument Configuration. For all editions of Gen5 Secure and Gen5 IVD, this database also contains an audit trail for local events. LocalDB is stored on the computers hard
drive, and it cannot be moved or renamed.

l

Default database location: During normal installation, Gen5 installs its databases in Windows Common Application Data Folder:
l

Windows 10: C:\Program Data\Agilent\Gen5 (software level)\(version
#)\SharedDB or LocalDB
Note: You may need to change your operating system settings to view the
Application Data folder.

l

Database Names after Upgrade: The Gen5 Upgrade Utility changes the names of
the databases to help distinguish them:
l

SharedDB: The file name of the database selected for upgrade is not
changed during the process, but the upgraded version is identified by this suffix: "Upgraded_<date_time>.mdb".
Note: The Gen5 Periodic Backup routine appends the filename with
"Auto_Backup_<date_time>".

l

LocalDB: The file name of the LocalDB selected for upgrade is changed
because Gen5 requires the database stored on your hard drive to be named

Gen5 Getting Started Guide

---

42 | Initial Setup

LocalDB. After the upgrade the older version is named with this suffix:
"Before_<date>_<time>.mdb".
l

Max Size: the maximum size of the database files is 2 gigabytes (GB). At startup, Gen5 checks the remaining size of the database. Warning messages are displayed when the database size exceeds 1536 MB. Use Gen5 maintenance and
backup features to archive your database records.

l

Gen5 has built-in error recovery modes. When your connection to the database
is lost for any reason, Gen5 saves any unsaved files as Temporary Files. After a
system failure, the next time you open an affected protocol or experiment file,
Gen5 offers to replace the unsaved files with the Temporary Files. Select Yes to
recover any changes made to the files before the system failure; select No to
open the files as they were last saved, before the unsaved changes were made.
Newly created files are also saved as Temporary Files. Following a system failure, you can rename these temporary files with the proper file name extension
(.xpt or .prt) using Gen5 Maintain Files controls.

l

File locking: When a file is opened in Gen5 it is locked to protect it from
being modified (saved or renamed) by a different user. When a second user
attempts to open the file, he or she receives a message stating: File <filename>
is already in use. Do you want to open it in read-only mode?

l

Gen5 offers automatic backup. You can define settings for regularly and automatically backing up and optimizing databases with Gen5 Auto-Optimize feature.

Agilent Technologies, Inc.

---

Organize Your Database Files | 43

Organize Your Database Files
Note: During regular installation, all editions of Gen5 Secure and Gen5 IVD
use the shared database to store experiment and protocol files. All other
levels of Gen5 must elect to use the database at System > Preferences >
File Storage.
All of your file management requirements can be fulfilled using Gen5 databases
(except image files cannot be stored in the Gen5 databases). You'll be most
satisfied with the final structure if you spend some time planning it up front. In a
multiple-user environment, you can install a Gen5 database on a shared-network
drive (LAN) so multiple users can access the same protocol and experiment files.
Backups: Performing backups on a regular schedule is highly recommended to
preserve your data. And, Gen5 provides a tool to schedule backups to occur
periodically. See below.
File Management Recommendations
l

Put a copy of the SharedDB on a shared-network drive where all your Gen5
users can access it. Be sure to set each user's database configuration to point to
the correct location.

l

Before moving the SharedDB to a network location, make a copy of it to use as a
template for future use:
1. In the default SharedDB folder, highlight the original, right-click, and
select Copy.
2. Deselect the original (click elsewhere in the dialog), right-click, and select
Paste.
3. Highlight the copy, right-click, and select Rename.
4. Give the copy a unique name, like SharedDB_original.mdb.

l

Consider setting up shared databases for different projects or teams within your
organization. You can follow the steps defined above to create multiple databases in the same folder (or directory), or you can move the unique databases to

Gen5 Getting Started Guide

---

44 | Initial Setup

a different network location/folder. Use Database Configuration to point users'
Gen5 sessions to the correct database.
l

Regularly archive and back up the database to preserve your records. Use
Gen5 Optimize and Backup Settings to backup and clean small errors in your
database. Agilent recommends following your organization's existing policy for
securing data, for example, putting the shared database on the network to be
backed up every night.

l

For databases stored locally (not on a network drive), consider using Gen5s
automatic save feature1 to create new, date-stamped folders for storing experiment records. This is an especially good practice for large labs with multiple
users who run hundreds of plates per day. Gen5 organizes all that data by date.
Define this kind of file management setting in the Initial Protocol Settings (System > Preferences) so it will apply to all newly created protocols.

l

Gen5 handles multiple, simultaneous users performing database management
tasks by giving precedence to the user with the greater administrative rights.

Move or Copy a Database to a Network
System > Database Configuration
Note: All editions of Gen5 Secure and Gen5 IVD install and enable the
databases during regular installation. All other levels of Gen5 must elect to
use the database to store protocol and experiment files at System >
Preferences > File Storage.
In a multiple-user environment, you can set up the Gen5 database on a shared
network drive so multiple users can access the same protocol and experiment files.
This is a recommended step for System Administrators. You can also set up multiple
databases, one for each team or project, for example. During a Gen5 session,
access is provided to only one database at a time.

1Click Protocol > Protocol Options > Save Options.

Agilent Technologies, Inc.

---

About User Accounts | 45

1. Select System > Database Configuration.
2. Select the SharedDB tab.
3. Next to the Source field, click Browse.
4. In the Open dialog, highlight and right-click the file SharedDB.mdb, and
select Copy or Cut; use cut to move and copy to copy.
Note: SharedDB is the installed/original name for the shared database.
Because you can change the name, it's possible it has already been
changed.
5. Navigate to the desired location in the Look in field.
6. When the correct location is selected, right-click in the window and select
Paste.
7. Click Open to save and close the window, and return to the Gen5 Database
Configuration dialog.
8. Shut down and restart Gen5 to make the changes take effect.

About User Accounts
System > Security > Users
Prerequisite
This function is available only to the System Administrator.You must log in as the
Administrator (System Menu > LogIn/LogOut) to access all the controls. Nonadministrators are limited to changing their own password and selecting a Startup
Mode, Startup Action and Protocol Folder.
How to Create, Modify, or Delete User Accounts
Only an Administrator can add, modify, or delete users. You can designate multiple
individuals to be system administrators. Any user account can be changed or
deleted, except there must always be at least one System Administrator:

Gen5 Getting Started Guide

---

46 | Initial Setup

l

Click New to set up a new user.

l

Double-click or highlight a user, and click Edit to modify its name, password, or
Group assignment.

l

Highlight a user, and click Delete to remove the user account.

About User Groups
System > Security > Groups
Prerequisite
This function is available only to the System Administrator. You must log in as the
Administrator (System > LogIn/LogOut) to access this control.
All editions of Gen5 Secure and Gen5 IVD use groups to manage the rights or
permissions granted to users. When creating (or maintaining) a group, you define
the level of access and the controls available to certain types of users and then
assign actual users to the groups. Gen5 ships with three groups: Administrator,
Power User, and Standard User.
The System Administrator and Power User groups are given access rights to all
functions. The Administrators rights cannot be changed and include additional
rights to manage user accounts that are not extended to Power Users. When any
edition of Gen5 Secure or Gen5 IVD is installed, the Standard User is limited to the
following permissions. The System Administrator can change these rights as needed:
l

Startup preferences

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

Agilent Technologies, Inc.

---

About User Groups | 47

Create New Groups and Modify Existing Groups
Only a System Administrator can add, modify, or delete groups. Except for the
Administrator group, any group can be changed or deleted, and any group can be
renamed.
l

Click New to set up a new group.

l

Highlight a group and click Edit to modify its name and permissions.

l

Highlight a group and click Delete to remove it as an option. First you must reassign any users to another group. You cannot delete a group with users assigned
to it.

Gen5 Getting Started Guide

---

48 | Initial Setup

Create/Maintain User Accounts
For Gen5 Secure or Gen5 IVD editions only
System > Security > Users
Prerequisite
Most options for user accounts are available only to the System Administrator. Nonadministrators are limited to changing their own password and selecting a Startup
Mode, Startup Action and Protocol Folder.
User ID
Enter a unique ID using 1 to 16 alphanumeric characters. The user will enter or
select this ID when logging into Gen5 and when signing files.
Full Name
Enter the users name. This name will be associated with events logged by this
users actions and with the digital signature applied by this user.
Group
Choose a Group membership to assign access rights and permissions to the user. See
About User Groups on page 46 for information. Users receive the rights assigned to
the Group.
Status
The check box shows whether the users account is currently locked. The System
Administrator can lock or unlock the account. When a users account is locked, the
user cannot log in to Gen5 and cannot sign files. A users account may become
locked due to one of three events:
l Intentional lock by the Administrator using this dialog
l

Automatic lock if the user exceeded the number of successive failed login
attempts

l

Automatic lock if the users password expired

Agilent Technologies, Inc.

---

Create/Maintain User Accounts | 49

Unlocking a user's account following an automatic lock resets its counter or clock.
The reset is specific to the reason for the lockout: When it is caused by password
expiration, the password expiration clock is reset; when it is caused by failed logins,
the user's history of "successive failed login attempts" is reset to 0.
When lockout occurs due to an expired password, unlocking the account allows the
user to log in to Gen5 with the same password, providing a chance to change it.
Alternatively, as system administrator, you can simply change the password yourself
(which will by default unlock the account) and tell the user to log in with the
password you have assigned him or her.
Startup Mode
Gen5 offers slightly different workflow modes:
l Simple: a basic workflow designed for faster set up and execution of experiments; using limited choices and interactive dialogs. Simple Mode always starts
Gen5 displaying the Simple Task Manager with Read Now in focus.
l

Standard: classic Gen5 workflow with access to all potential parameters, settings, and options.

IQOQPQ Procedures: Choose Standard mode when performing Instrument Qualification Procedures supplied by Agilent for the best user experience.
Note: Administrators are set up by default to use Standard Mode.
Startup Action
Select the preferred method for starting Gen5:
l Display Task Manager/Last used page is the default setting. You can also specify a specific Task Manager page, such as Read Now page or Experiment page.
l

Create new experiment opens Gen5 with the Protocol selection dialog open, as
if the user had selected Experiments > Create New.

l

Start at system menu opens Gen5 showing the File, Take3, Window, System,
and Help menus only. Since neither a protocol or experiment is open, the workspace is blank.

Gen5 Getting Started Guide

---

50 | Initial Setup

Protocol and Experiment Folders
Browse to or enter the full path and directory to define the folder in which the
current user will typically store protocol and experiment files. Gen5 defaults to the
most recently accessed folder.
Password
Assign a password for the user to enter the first time he or she logs in to Gen5.
Instruct users to change their password after the first login using the password
you've assigned. Users can change only their own password. System Administrators
can change any user's password.

Login/Password Controls
For Gen5 Secure or Gen5 IVD editions only
System > Security > Login
Prerequisite
Only the System Administrator can access these controls. You must log in as the
Administrator (System > LogIn/LogOut) to change the settings.
The default settings shipped with all editions of Gen5 Secure and Gen5 IVD, as
shown in the screenshot below, comply with the FDAs 21 CFR Part 11 requirements
for controls for identification codes/passwords.

Agilent Technologies, Inc.

---

Login/Password Controls | 51

Login
l

Lock user account after: Specify the number of successive failed login attempts
a user may make before being locked out of Gen5. This feature does not apply to
System Administrator accounts, and only a System Administrator can reinstate a
locked-out account. Valid entry range: 2-10. When this feature is not enabled,
users login attempts are unlimited. Compliance with 21 CFR Part 11 requires setting a limit for failed login attempts.

l

Lock session after: Specify the number of minutes that a Gen5 session can be
idle before it is locked and requires successful user login to reactivate. A session
is considered idle when there is no keyboard or mouse activity and Gen5 is not
controlling a reader activity. Valid entry range: 1-1440 minutes. Compliance
with 21 CFR Part 11 requires setting an idle-time limit.

l

Force user to type ID: Apply this control if your security rules require users to
enter their ID at login and to apply their Signature. When this feature is not
selected, the last users ID is displayed in the login and signature screens, and
users can select an ID from a drop-down list of users.

l

Require login in OLE Automation (BioStack): Select this option to ensure that
Gen5 security permissions are enabled when Gen5 Secure, Gen5 Secure Image+,

Gen5 Getting Started Guide

---

52 | Initial Setup

Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+ is run as an OLE Automation server, for example, for using the BioStack. When Windows Authentication is enabled, the login process may take place automatically. When Windows
Authentication is disabled, Gen5 prompts the user to enter a login ID and password. Logins performed while this option is selected are tracked in the Audit
Log.
Password
l

Minimum password length: Specify the minimum number of alphanumeric characters required for a valid password. Valid entry range: 2-10 characters.

l

Password expiration: Specify the number of days a password can be used before
users are required to change it. When users let their password expire without
changing it, their accounts are locked out and only a System Administrator can
reinstate a locked-out account. Valid entry range: 1-10000 days. If this feature is
not selected, passwords do not expire. Compliance with 21 CFR Part 11 requires
an expiration period.

l

Lock out: When a users password has expired, the system administrator has two
choices:
l

Manually remove the Locked out flag. This resets the password expiration
period allowing the user to log in using his/her current password.

l

Enter a new password for the user (which unlocks the account) and tell the
user to log in with the password you have assigned him/her. Advise the user
to change the password after logging in.

l

Advise user: If password expiration is set, specify the number of days before
passwords expire to alert users to change their password. Valid entry range: 1-30
days, but cannot exceed the number of days to Password Expiration.

l

Password reuse: Specify the number of passwords Gen5 will remember for each
users account to prevent a recently used password from being reused. Valid
entry range: 2-20.

Agilent Technologies, Inc.

---

Configure Windows Authentication | 53

Configure Windows Authentication
For Gen5 Secure or Gen5 IVD editions only
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5
IVD Image+ provide an option to allow users to sign in to Gen5 using Microsoft
Windows Authentication instead of user accounts defined in Gen5. Through Windows
Authentication, users log in to their workstations once and have access to Gen5
without having to log in again. The Windows Authentication feature benefits system
administrators as well by providing a single location for the management of user
settings.
To use Windows Authentication, client workstations must be running Windows 10 or
higher; and LDAP Servers are required. Before Windows Authentication can be
activated in Gen5, both the Gen5 Administrator and the IT administrator must
perform setup tasks.
Gen5 Administrator Tasks
Gen5 Secure, Gen5 Secure Image+, Gen5 Secure Image Prime, Gen5 IVD, and Gen5
IVD Image+ use groups to manage the rights or permissions granted to users. The
Group Names are defined in Gen5 by the Gen5 Administrator.
When creating or maintaining a group, the Gen5 Administrator defines the level of
access and the controls available to certain types of users, and then assigns actual
users to the groups. Gen5 ships with three default groups: Administrator, Power
User, and Standard User.
The System Administrator group is given access rights to all functions. The
Administrators rights cannot be changed. When Gen5 Secure, Gen5 Secure Image+,
Gen5 Secure Image Prime, Gen5 IVD, and Gen5 IVD Image+ is installed, the Standard
User is limited to the following permissions (the System Administrator can change
these controls as needed):
l

Open Protocol

l

Use Gen5 Protocols (requires Gen5 Native)

Gen5 Getting Started Guide

---

54 | Initial Setup

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
The IT administrator must create user groups on the server to mirror the Gen5 User
Groups defined in Gen5. The user groups on the server must be named Gen5_<Gen5
Group Name>, where <Gen5 Group Name> is the name of a group in Gen5, such as
Gen5_System Administrators. The IT administrator can also define permissions that
apply to Windows resources, such as access to folders, printers, and so on.
Each user who has permission to run Gen5 must be defined as a member of a single
Gen5 group in Windows. If a user is defined as a member of more than one Gen5
group, an error message will appear when the user attempts to log in to Gen5. If the
user is not assigned to a Gen5 group, a warning message will appear, indicating that
the user is not a valid Gen5 user. The user can then log in with another, valid Gen5
account.

Configure the Email Notification Feature
For Gen5 Secure or Gen5 IVD editions only
All editions of Gen5 Secure and Gen5 IVD can be set up to send an email notification
to specified recipients when a predefined event, such as a reader error or failed
login, occurs. The email server settings must be configured to support this feature.
The Gen5 Administrator must test these settings to verify that the Email
Notification feature is functioning correctly.
To verify that the email server settings are configured correctly to support this feature, check with your IT administrator.

Agilent Technologies, Inc.

---

Configure the Email Server | 55

Defining a Custom Email Template
By default, Gen5 generates the title and body of the email notification messages,
but you can define a custom template that includes specific variables.
1. On the Email tab of the Security dialog, click Auto in the Template column.
2. In the Email Definition dialog, select Custom as the mode and either Text or
HTML as the format.
3. Modify the Subject and Body text as necessary. Variables associated with the
defined event are listed in the Variables text box. To insert them in the Subject or Body of the email notification, place the cursor where you want the
variable to occur, then double-click the variable in the Variable text box.
4. Click OK.

Configure the Email Server
For Gen5 Secure or Gen5 IVD editions only
System > Preferences > Email Server
System > Security > Emails tab > Email Server
The email server must be configured correctly to support the Gen5 Email
Notification feature. Check with your IT administrator to verify your configuration
settings.
In the Send Emails from area, you can define the email addresses used in the Email
Notification feature.
l

Display name: This field is required. By default, Gen5 displays Gen5_Notice_Do_
Not_Reply@biotek.com as the address from which the notification message is
sent. You can change this address, if desired.

l

Forward errors to: The address specified in this field will receive any mail delivery error messages generated by the server related to the Email Notification feature. If no address is entered, error messages will be sent to the address in the
Display Name field.

Gen5 Getting Started Guide

---

56 | Initial Setup

l

Reply to: The address specified in this field will receive messages sent as a reply
to an Email Notification message. If no email address is entered in this field, the
address in the Display Name field will receive any reply emails.

Getting Technical Assistance
You can contact Technical Support using email, telephone or Agilents Worldwide
Support website.
Please be prepared to provide the following information:
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

An email address
Agilent
Service Toll-Free: (800) 227-9770
Customer Care Email: bio.CustomerCare@agilent.com
Service Email: bio.tac@agilent.com
Obtain a Password Email: bio.password@agilent.com
Worldwide Support Web site: https://www.agilent.com/en/contact-us/page

Agilent Technologies, Inc.

---

Getting Started
Gen5 software provides a logical interface to all automated Agilent plate reads. It is
designed to flow from reading parameters, to plate layout, to data reduction, and
finally to flexible data output options.
Launching Gen5

58

Change Your Startup Preferences

58

Change Your Startup Preferences in Gen5 Secure and Gen5 IVD

60

Task Manager

61

Standard Mode Gen5 Workspace

63

Protocol Workspace

66

The Menu Tree(Standard Mode)

67

Buttons and Icons

68

---

58 | Getting Started

Launching Gen5
During software installation, Gen5 installs a desktop icon and adds itself to
the Windows Start menu. For most users, the first launch of Gen5 presents Startup
Options:
Fill the checkbox to stop this prompt
from opening every time you launch
Gen5. To reset the prompt:
l Gen5: Change Your Startup
Preferences below
l

Gen5 Secure/IVD: Change Your
Startup Preferences in Gen5
Secure and Gen5 IVD on page 60

Startup Mode
Gen5 offers slightly different workflow modes:
l

Simple: a basic workflow designed for faster set up and execution of experiments; using limited choices and interactive dialogs. Simple Mode always starts
Gen5 displaying the Simple Task Manager with Read Now in focus.

l

Standard: classic Gen5 workflow with access to all potential parameters, settings, and options.

IQOQPQ Procedures: Choose Standard mode when performing Instrument Qualification Procedures supplied by Agilent for the best user experience.
Simple Mode is an interactive work flow that limits user options to make
accomplishing tasks easier. Only one file may be open at a time. Standard Mode
represents Gen5 behavior since version 2.09. Standard mode enables a choice of
Startup Action options and the full range of Gen5 features for every Gen5 edition.

Change Your Startup Preferences
For all editions of Gen5 except Secure and IVD.

Agilent Technologies, Inc.

---

Change Your Startup Preferences | 59

System > User Setup
1. Click System > User Setup.
2. Select the preferred Startup Mode: Simple, Standard, or Prompt at startup.
3. If Standard Mode is selected above, choose the preferred Startup Action, for
example:
l

Display Task Manager is the default setting. It opens Gen5 with a screen
that offers several common tasks including creating a new item or opening
a recently used item. (In Simple Mode this option, in Read Now focus, is
fixed.)

l

Create new experiment opens Gen5 with the Protocol selection dialog
open, as if the user had selected Experiments > Create New based on an
existing protocol.

l

Start at system menu opens Gen5 showing the File, Take3, System, and
Help menus only. Since neither a protocol or experiment is open, the workspace is blank.

4. Click Browse to change your Protocol and Experiment folders: browse to the
full path and directory to define the folder where you will typically store protocol and experiment files. Gen5 points to these folders when you save and
open a protocol or experiment.
5. Click OK.
The changes will take effect the next time you log in to Gen5.
Contact your System Administrator if you need assistance.

Gen5 Getting Started Guide

---

60 | Getting Started

Change Your Startup Preferences in Gen5 Secure and Gen5 IVD
For Gen5 Secure and Gen5 IVD only.
System > Security > Users
Users other than the System Administrator are limited to changing their own
password and startup options.
1. Click System > Security > Users.
2. Highlight your user account and click Edit.
3. Select the preferred Startup Mode: Simple, Standard, or Prompt at startup.
4. If Standard mode is selected in the previous step, choose a Startup Action, for
example:
l

Display Task Manager is the default setting. It opens Gen5 with a screen
that offers several common tasks including creating a new item or opening
a recently used item.

l

Create new experiment opens Gen5 with the Protocol selection dialog
open, as if the user had selected Experiments > Create New based on an
existing protocol.

l

Start at system menu opens Gen5 showing the File, Take3, System, and
Help menus only. Since neither a protocol or experiment is open, the workspace is blank.

5. Click Browse to change your Protocol and Experiment folders: Browse to the
full path and directory to define the folder where you will typically store protocol and experiment files. Gen5 points to these folders when you save and
open a protocol or experiment.
6. Change your password, if desired.
7. Click OK.
The changes will take effect the next time you log in to Gen5.
Contact your System Administrator if you need assistance.

Agilent Technologies, Inc.

---

Task Manager | 61

Task Manager
Gen5s Task Manager varies depending on the mode you are in:
Standard Mode

Simple Mode

Click an option (blue link) to open it.
Whenever you start Gen5, the Task Manager opens. You can reopen the Task
Manager by clicking the toolbar button:
clicking

. Likewise, in the Task Manager,

closes the Task Manager, returns to the main screen.

Gen5 Getting Started Guide

---

62 | Getting Started

Instrument Control options are available from the Standard Mode Task Manager:

Gen5 also provides fly-out tabs on the left side or in
the bottom left corner of the workspace in all
modes. Click the Instrument Control tab to access
the controls.

Instant Access
The Task Manager provides quick links to give you instant access to:
l Executing a new read
l

Using the Imager Manual Mode (imaging only)

Agilent Technologies, Inc.

---

Standard Mode Gen5 Workspace | 63

l

Opening or creating an experiment or protocol; the most recently used protocols
and experiments are listed

l

Control several of the instrument's operations (e.g., incubation, shaking, plate
in, stacker control)

l

Accessing configuration and security settings

l

Accessing the Gen5 Help system, FAQs, and sample files

Standard Mode Gen5 Workspace
Gen5 offers several controls and workspaces for developing protocols, running
experiments, and viewing and reporting results:

l

Protocol
Every experiment is based on a protocol. Learn the differences between a
protocol and an experiment in Gen5: Experiment vs. Protocol on page 88.

l

Toolbars and Menus

Gen5 Getting Started Guide

---

64 | Getting Started

See Buttons and Icons on page 68 to learn about Gen5 toolbars, buttons, and
menus.
l

Plate View
In an experiment, Gen5 provides a view or matrix for each plate processed (or to
be processed). Protocols do not have plates, so you must have an experiment
open to have a plate view. Gen5 displays reading and data reduction results in
the matrix.
To open the plate view: double-click the plate icon in the menu tree or select
Plate > View.
Gen5 offers several ways to modify and customize the Plate View for onscreen display and reporting/outputting results. See View Results on page 98 to
learn more.

l

Instrument Control Panel

Agilent Technologies, Inc.

---

Standard Mode Gen5 Workspace | 65

In the Gen5 workspace, click the Instrument Control panel to access commands
and actions for the attached readers and stacker. Select the instrument to
control from the list at the top of the panel.

Gen5 Getting Started Guide

---

66 | Getting Started

Protocol Workspace
When you create a new protocol, Gen5 opens a special workspace limited to the
protocols components.
Standard Mode

Simple Mode

The workspace is made up of
the menu tree with a branch
for each of the protocols
elements. The order of the
protocol elements reflects the
order to follow when defining
most protocols.

Defining the Procedure or reading parameters is the most important step to
Gen5. The Procedure describes the data sets that are used in most subsequent steps
to generate results output. The Plate Layout is the only other protocol element that
is not affected by the Procedure; it is affected by the selected plate size.
For most protocols, its best to define the Plate Layout in your second step.
Gen5 automatically performs a blank-subtraction calculation when Blanks are
defined in the plate layout. (Youll see this Transformation in the Data Reduction
workspace.) Defining the standards and their concentrations in the plate layout is a
prerequisite to generating a standard curve.

Agilent Technologies, Inc.

---

The Menu Tree(Standard Mode) | 67

Data Reduction is one of the most powerful features in Gen5, and it requires
the information provided by the two previous steps to logically offer you its
capabilities. Automatically generated transformations, like path length correction
and the ability to conduct well analysis, for example, depend on the Procedure. To
plot a standard or titer curve and to validate Transformation formulas requires
knowing the Plate Layout.
Report/Export Builders is a tool for selecting and customizing the appearance
of data sets that are then available for printing or exporting.

The Menu Tree(Standard Mode)
l

To keep the menu tree open in a protocol or experiment, click

to dock it in place (click thumbtack

again to collapse the menu tree). When working
with a protocol file, the menu tree, like the toolbar, is limited to related operations.
l

Click

and

next to an item to reveal or hide

its components.
l

The menu tree provides a visual cue of the steps to
follow when creating a protocol.

l

All of the controls available from the menu tree can be accessed using toolbar
buttons or menus.

l

Highlight an item in the menu tree and right-click for a context-sensitive menu
of options, including Read when a plate is selected, for example.

l

Asterisks (*) are displayed next to plate icons (and in the title bar) of an experiment when a change is made or an action is taken but the file has not yet been
saved.

l

You can move the menu tree to another corner of the workspace or let it float
undocked like the Plate workspace: select Floating from the menu, drag the title

Gen5 Getting Started Guide

---

68 | Getting Started

bar, and using the temporarily displayed placement guides, drop it in the
desired location.
l

When you add multiple plates to an experiment, highlight a plate and right-click
for menu options to delete and renumber plates.

Buttons and Icons
Button

Description
Open the Task Manager

Reader Setup
Save the protocol or experiment

Read the plate

Print preview

Print results (formatted via the Report Builder)

Export results

Define the Procedure

Define the Plate Layout

Create Data Reduction steps

Open the Report/Export Builders to design reports

Agilent Technologies, Inc.

---

Buttons and Icons | 69

Button

Description
Paneled protocols

(Imaging only) Go to manual mode

(Imaging only) ROI Manager
Set Reader Optics: Opens the Set Reader Optics dialog in which you
can update the reader with new definitions for filters and mirrors.
Instrument Control: Check the status, open the control panel

Stacker icon: Opens the Stacker control panel, if a Stacker is attached.

Export results to QC (Gen5 Image+ IVD and Gen5 IVD only)

Edit trended protocols (Gen5 Image+ IVD and Gen5 IVD only)

Pin the current plate view to the workspace
Duplicate a coincident display of the plates results

Menu Tree Icons
Plate--not read: Put the plate in the reader and click
Plate read successful
Plate read paused by Stop/Resume step:
When youre ready, put the plate in the reader, click
and select Resume Plate x to continue

Gen5 Getting Started Guide

,

---

70 | Getting Started

Menu Tree Icons
Plate read aborted: To begin again, put the plate in the reader, click

,

and select Re-Read Plate x
Plate read in progress
Plate read error, which is always preceded by an error message. The error
code and message are recorded in the plate data audit trail. It is the
user's responsibility to verify the integrity of the data after an error
occurs.
Protocol
Experiment -- See Experiment vs. Protocol on page 88
Procedure: Define the reading parameters
Plate Layout: Assign location of samples
Data Reduction: Set up calculations
Report/Export Builders
Plate Information: Information obtained at runtime
Sample IDs: User-defined names or IDs assigned to samples
Calculation Warning Log: Data Reduction-related errors issued by unexpected curve or calculation results
Audit trail displays any logged events
Multi-Plate protocol view of data reduction statistics and curves

Agilent Technologies, Inc.

---

Buttons and Icons | 71

Menu Tree Icons
Panel: Multi-protocol experiment performed on one plate
Paneled Protocols: Lists the protocols run (or to be run) in the panel
experiment

Gen5 Getting Started Guide

---

72 | Imaging : Manual Mode

Imaging : Manual Mode
The following sections briefly describe how to use the Gen5 imaging controls in
manual mode. See the Gen5 Help for more complete instructions and descriptions of
these features.
Important Prerequisites
After the imager has been installed and configured (as described in its operators
manual), some basic setup steps are required to prepare the instrument to
successfully capture images:
l

Plate Type: tell Gen5 the precise characteristics of the vessel you are using. Be
sure to define the Bottom Elevation for your plate or vessel. When using high
power objectives (20X and higher): Adjust the Correction Collar.

l

Saving Images: tell Gen5 where and how to save your image captures and analysis results. An external hard drive is recommended for most users because
image files are significantly larger than other data files, making storage an
important issue to address. Seek help from your IT group, if necessary.

Automate your imaging assay by converting a manual mode session into an
experiment. Use manual mode to determine and fine-tune settings like autofocus
and image processing, then save those setting to process multiple plates.

Focusing and Capture
1. From the Task Manager, select Imager Manual Mode and click

.

Options vary based on the type of imager. Generally, you need to choose the
objective and color channel.

Agilent Technologies, Inc.

---

Process and Analyze | 73

2. Click Find Image. Gen5
automatically sets the
exposure and focuses on
the image.

If the displayed image requires additional fine-tuning:
l Click Auto Expose, or expand the Exposure panel to manually adjust the settings.
l

Click Autofocus, or use the focus controls until the image is in focus.
l

Repeat these two
steps until the image
is exposed and
focused to your liking.

3.

Click the camera button to capture the image.
Change the channel, if desired, to capture the same image in another color.
Note: if you move to a different place in the current well or a different well,
or change the objective, Gen5 will create a new image capture.

Process and Analyze

After you capture one or more images, click

Gen5 Getting Started Guide

.

---

74 | Imaging : Manual Mode

Gen5 presents the image processing options
applicable to the type of capture with default
settings based on the objective and color channel.
You can modify the processing settings to improve
the image for analysis.
Use the Line Profile or other tools to determine
optimal settings like threshold and object size.
In the Color Channel panel, use the checkboxes to show or hide individual channels
in the image for review purposes.
Note: Any adjustments made using the B&C (brightness and contrast) and
the Channel Shift tools are for display purposes only; the changes do not
affect the data measurements from the images.

Gen5 adds a prefix to the data set created by image
processing:
Image Preprocessing: "Tsf"
Deconvolution: "Deconvolved"
Digital Phase Contrast: "Dig.Ph.Cont"
Z-Projection: "ZProj"
Image Stitching: "Stitched"
Kinetic Frame Alignment: "Aligned"
Edit the Image Processing Step
In manual mode, you can modify or add imaging process steps: Select the data set in
the Image History box and click Edit step or choose another processing step to
apply to it, such as or , that are relevant for your image.

Agilent Technologies, Inc.

---

Analyze Captured and Processed Images | 75

Note: To display the raw image or a previously processed image, select its
data set in the Image History box.

Analyze Captured and Processed Images

1. Click Analyze tab.

2. In the Analysis Settings box, select the Detection Channel and click Start. The
results are displayed in the right pane.
3. Click Options to modify and/or expand the analysis, e.g., to add a Secondary
mask or subpopulation (if supported).

Troubleshooting
l

First Response: Running a System Test is the best first response to an instrument error. The test may restore the instruments initial settings and computer
communication capability. Note: To stop the alarm, press the carrier eject button; except touch screen readers: tap the screen to acknowledge the error.

l

Reboot the Computer and Instrument: When you cant run a system test, for
example, Gen5 is not responding, or when running a system test doesnt resolve
the issue, turn off your computer and instrument, check all the cabling (i.e.,
make sure your serial or USB cable is in good condition and is properly connected
to the computer and instrument), and then, power on your computer and

Gen5 Getting Started Guide

---

76 | Imaging : Manual Mode

instrument. These steps should refresh the devices and reset communication
parameters.
Visit Agilents website for useful suggestions on getting the most from your
reader.
l

Degrading performance: Consider changing the Multi-Read Calculations setting
if system performance slows significantly.

l

Incompatible protocols: Protocols created with one instrument are not instantly
compatible with other instruments. To correct the error: Procedure was
defined for a different instrument, open the Procedure and click Validate. If
this does not correct the error, open each step in the Procedure and review it
for compatibility with the current instrument.

l

Windows 10 Missing Files: The Gen5 installation routine attempts to avert
potential file sharing issues but when multiple users share a computer, Windows
may use its VirtualStore as the default location for file storage.

Communication Errors
If Gen5 fails to save a file
l

Ensure you are using a wired connection between the computer running Gen5
and the drive on which you are trying to save the files. Using a WiFi connection
when running experiments is strongly discouraged. External hard drives connected via USB to the computer are recommended for storing imaging experiments.

When the computer wont communicate with the instrument
l

Confirm that the instrument passes its system self-test. All Agilent instruments perform a self-test when turned on. Refer to the instruments operators
manual for more details. The instrument will not communicate if it fails an
internal system test. Non-keypad instruments beep continuously when the system test fails. (Press the plate-carrier button to stop the alarm.) Keypad instruments display an error message when the test fails. Refer to the operators

Agilent Technologies, Inc.

---

Troubleshooting | 77

manual to resolve the failure or contact Technical Support.
l

Confirm the Instrument COM Port settings. The instrument COM port must be
configured correctly for successful communication. This is set in the Reader Settings window under Instrument Configuration. COM1 is reserved for serial cable
connections while USB connections are assigned COM2 and higher. The COM port
assignment can be identified through Windows Device Manger under the Ports
(COM & LPT) subheading. Confirm the Gen5 COM setting matches that found in
device manager. Test Communication.

l

Confirm the correct USB drivers are installed. Instruments connected to the
computer via a USB cable or adapter require drivers to be installed. These
drivers can be found with the original Gen5 installation media. Please contact
Technical Support for driver download or installation assistance.

l

Make sure the serial or USB cable is in perfect condition and properly
attached to the port defined in the Instrument Configuration dialog (e.g., COM 1
or Plug & Play). Correct and reboot both computer and reader. Test communication.

l

Confirm that the serial/USB cable was obtained from Agilent. Serial/USB
cables are not universal. Consult the instruments operators manual for proper
cable configuration or contact Customer Care to purchase a factory-tested
cable. After installing a known good cable, reboot both computer and instrument. Test communication.

l

Make sure computer processes are not using excessive memory. CPU intensive tasks, such as virus scans and complex Gen5 data analysis, can interrupt communication between the computer and the instrument. Check your computers
Task Manager for memory intensive processes. Review current settings: System>Preferences>Calculation Options.

Serial Cable Connected and Keypad Readers
l

To prevent damage to the instrument, always turn off the instrument or the
computer before removing or inserting a serial communications cable. USB
cables do not have the same threat.

Gen5 Getting Started Guide

---

78 | Imaging : Manual Mode

l

Confirm the baud rate (or transmission speed) defined in the Gen5 Instrument
Configuration dialog matches the instruments settings. Consult your instruments operators manual for the correct rate. Correct the Gen5 Instrument Settings to match and reboot both computer and instrument. Test communication.

l

Confirm with your computer supplier or a local technician that the serial port
has been enabled. For example, the IBM Thinkpad was originally shipped with
the serial port disabled. Correct and reboot both computer and reader. Test
communication.

l

For advanced computer users, the serial port of the instrument and computer
can be independently tested using an independent serial-communication software package such as Windows Terminal, Hyper Terminal, or ProCom. Agilent
does not support or sell these programs.
l

Select flow control for XON/XOFF and send an ASCII asterisk symbol (*) to
the reader. The instrument should initiate a self-test and return the results
to the computer. If the instrument fails to communicate, and Steps 1 through
5 do not resolve the problem, test the instrument on an alternative computer to confirm which device is at fault. Please contact Technical Support if
the instrument is diagnosed to be faulty.

Restore Optimal Performance
Numerous factors can affect your computers performance. If you notice a
slowdown in Gen5s performance, follow these suggestions:
l

Close all other applications, including Internet browsers, when running Gen5.

l

Do not display Gen5s Curves data in the Plate View while performing a kinetic
analysis. Wait until the read step is finished before viewing the Curves data set.
Displaying the Curves data during a Kinetic read can consume excessive
resources resulting in performance degradation. You can drill down to a Well
Zoom to monitor the progress of one well, then, leaving the Well Zoom open,
change the Matrix Data to a numeric view.

Agilent Technologies, Inc.

---

Fluorescence/Luminescence Measurements | 79

l

Disable the Calculation option Perform data reduction after each read to give
Gen5 sufficient time between obtaining measurements to perform calculations.
Select Protocol > Protocol Options > Calculation Options.

l

Disable the auto-Save option: Save when: Interim read completed. Change the
Save Options to free up resources. Select Protocol > Protocol Options > Save
Options.

To apply these settings universally, to all future experiments, make the changes in
System>Preferences>Initial Protocol Options.

Fluorescence/Luminescence Measurements
Heres a list of potential problems, the possible cause, and a remedy:

Gen5 Getting Started Guide

---

80 | Imaging : Manual Mode

Fluorescence/Luminescence Readings Too Low
l

Possible cause: The fixed Gain in the Read Step dialog is currently set too low
Raise the Gain to an appropriate level. For fluorescence, the Gain is usually set
between 45 and 130. For luminescence it is usually set between 100 and 200.
Learn more in the Gen5 Help.
Try Automatic Gain Adjustment, using the Scale to High Well option and setting
the target value to be between 20,000 and 80,000 for standard range, or
1,000,000-3,500,000 for extended range (if supported by your reader).
Note: Some readers have extended range capabilities with flash
fluorescence. These models are auto-ranging up to 10,000,000.

l

Possible cause: The wrong filters are selected in the Read Step dialog (for filterbased reads only)
Examine the current filter settings and make any corrections. If the filter
settings appear to be correct, check the locations of the actual filters in the
instrument.

l

Possible cause: Top probe setting is not optimized
Gen5 generally positions the top probe at the optimal height for fluorescence
reads, based on the plate type selected; it focuses the beam above the well.
Refer to the Gen5 Help and use the Read Height option in the Read Step dialog
to make adjustments. If supported by your reader, try the Auto-Adjust feature
for the probe height. The reader's user manual may contain additional
suggestions.

Fluorescence Background Too High
l

Possible cause: Using incorrect microplates

Agilent Technologies, Inc.

---

Fluorescence/Luminescence Measurements | 81

Solid black plates for top probe reading lower the background. Black plates with
clear bottoms lower the background if bottom reading is necessary. Corning
3615 or 3614 (for cell culture) are appropriate.
l

Possible cause: The wrong filters are selected in the Read Step dialog (for filterbased reads)
Examine the current filter settings and make any corrections. If the filter
settings appear to be correct, check the locations of the actual filters in the
instrument.

l

Possible cause: Phenol red is used in the media when exciting at 485 nm and
reading at 528-530 nm
Eliminate or replace the phenol red.

l

Possible cause: Cells, media and other contents fluoresce
Use deionized-water blank wells as a diagnostic tool. The blank-well reading will
help you determine the background value contributed by the instrument,
labware, and media.

l

Possible cause: The top and/or bottom probe needs cleaning
Refer to the operators manual for guidance; not all readers have useraccessible internal components.

l

Possible cause: The instrument has fluorescing material spilled inside
Refer to the operators manual for guidance; not all readers have useraccessible internal components.

l

Possible cause: The Gain in the Reading parameters dialog is currently set too
high
Lower the Gain setting. The background should still read higher than zero. 200 is
a recommended minimum and a value of 1000 takes advantage of the systems
five-digit resolution.

Gen5 Getting Started Guide

---

82 | Imaging : Manual Mode

Reader Not Achieving Desired Fluorescence Detection Limit
l

Possible cause: The wrong filters are selected in the Read Step dialog
Examine the current filter settings and make any corrections. If the filter
settings appear to be correct, check the locations of the actual filters in the
instrument.

l

Possible cause: Using incorrect microplates
Refer to the reader's user manual for information on supported plate types.

l

Possible cause: The fixed Gain is currently set too low
Raise the Gain setting until the background wells read at least 200 RFU (1000
RFU is preferred).

l

Possible cause: Readings are taken using the bottom probe
Try switching to the top probe, if applicable/appropriate for your reader and
assay.

l

Possible cause: The solution volume is 50 L or less
Increase the solution volume to 150-200 L, if possible.

l

Possible cause: Wrong pH
Fluorescence is very pH dependent. Use the appropriate pH.

l

Possible cause: Phenol red is used in the media when exciting at 485 nm and
reading at 528-530 nm
Eliminate or replace the phenol red.

l

Possible cause: Top probe setting is not optimized
Gen5 generally positions the top probe at the optimal height for fluorescence
reads, based on the plate type selected; it focuses the beam above the well.
Refer to the Gen5 Help and use the Read Height option in the Read Step dialog
to make adjustments. If supported by your reader, try the Auto-Adjust feature

Agilent Technologies, Inc.

---

Fluorescence/Luminescence Measurements | 83

for the probe height. The reader's user manual may contain additional
suggestions.
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
Lower the Gain setting. If using Automatic Gain Adjustment, try the Scale to
High Well option and set the High Value in the range of 50,000 to 70,000.

Bandwidth Verification Failed
l

Error or warning messages are issued when Gen5 detects overlapping
wavelengths or bandwidth
Select/enter Filter Set wavelengths that do not overlap. Learn more about Gen5
bandwidth verification in the Gen5 Help.

Error during Auto-Sensitivity Determination
l

Reader cannot fulfill request to determine optimal Gain
Gen5 displays an error message when the reader cannot determine the optimal
Gain based on the defined reading parameters.

Gen5 Getting Started Guide

---

84 | Imaging : Manual Mode

Luminescence integration time should be <= 1 sec and > 1 ms, especially when
scaling to low wells.
Manually enter a Gain value or use an alternative method to determine the
optimal sensitivity, if the error persists. Learn more in Gen5 Help.

Agilent Technologies, Inc.

---

Fluorescence/Luminescence Measurements | 85

Optimizing Imaging Performance
Performing imaging reads requires much more computer resources than a nonimaging read. If you are experiencing problems with imaging reads, such as an
automatic abortion of the read with a memory error message, consider the
following recommendations:
Ensure that your computer is fast enough to avoid accumulating too many images in
memory. Computer System Recommendations on page 12. An extended delay in
the display of image data reduction results or very high CPU activity during the read
may indicate that the performance of the computer or network is not high enough
to execute such a procedure.
Image files are significantly larger than typical data files. Consider using an
external hard drive to store images: Image File Management on page 92.
Change the virtual memory settings.
1. From the Windows Start menu, go to Control Panel and select System.
2. In the left pane, select Advanced system settings.
3. In the System Properties dialog, on the Advanced tab in the Performance area,
click Settings.
4. In the Performance Options dialog, on the Advanced tab, in the Virtual
Memory area, click Change.
5. Clear Automatically manage paging file size for all drives, if it is selected.
6. Select Custom Size, enter the following minimum and maximum values, and
then click OK:
l

Minimum: 10 GB

l

Maximum: 20 GB

7. You may need to restarted your computer for the change to take effect.
Run a complete chkdsk on the hard drive and defragment the hard drive.
l

Accessible at:
<Drive> > Properties > Tools > Error checking (include the recovery of bad

Gen5 Getting Started Guide

---

86 | Optimizing Imaging Performance

sectors)
<Drive> > Properties > Tools > Defragmentation.
Close and restart Gen5 before running a protocol with which you have had
trouble in the past.
Rebooting your computer can also be helpful.
If you keep experiencing problems during imaging experiments, consider the
following options:
l Reduce the number of images collected during the read.
l

Use lower montage dimensions by using lower magnifications.

l

Limit the read to channels that are absolutely necessary.

l

Use fewer kinetic points and a larger interval.

System Administrator's Password
Contact Customer Care if you have lost or forgotten the System Administrator's
password. Gen5 ships with the System Administrator's password set to admin.

Agilent Technologies, Inc.

---

Essential Concepts
This section will give you a good basis of information for understanding the
structure and terminology of Gen5. You can find more details and answers to
specific questions by using the online Help system. Select Help > Help Topics from
the menu.
Experiment vs. Protocol

88

About File Storage

90

Image File Management

92

Best Practices

93

---

88 | Essential Concepts

Experiment vs. Protocol
Gen5 uses two common terms to define distinct elements of its toolkit. The
distinction is subtle and will have more or less importance depending on how you
use Gen5. In any case, youll work most efficiently by understanding each role and
making them work for you.
Protocol (*.prt)

Experiment (*.xpt)

A protocol is a set of instructions

An experiment has a copy of the pro-

designed to capture, transform, and

tocol and at least one plate. It executes

report and/or export data.

the instructions provided by the protocol to produce results.

Protocols are created and saved as

Although an experiment is created using

stand-alone files. They function as a

an existing protocol, that protocol can

template; an unlimited number of

be modified within the experiment and

experiments can be based on one pro-

saved as a new protocol.

tocol.
A protocol consists of reading require-

Running an experiment is the only way

ments, like detection method and

to process a protocol.

wavelength, and reading-related
actions, like shaking and incubation,

The Read Now button is available

plate layout, data reduction, and data

after a read step has been defined in a

viewing, reporting, and exporting para-

protocol, but this action creates an

meters.

experiment based on the protocol.

A protocol can be used repeatedly (as is Multiple plates can be processed in an
or modified) within experiments. By

experiment, each one considered a

itself, a protocol does not produce res-

unique assay with independently repor-

ults. Protocols do not have plates asso-

ted or exported results. The exception

ciated with them.

is multi-plate protocols, described

Agilent Technologies, Inc.

---

Experiment vs. Protocol | 89

Protocol (*.prt)

Experiment (*.xpt)
later.

.prt is the protocols file name exten-

.xpt is the experiments file name

sion.

extension.

A copy of the protocol is saved within

An experiment is saved as the full col-

an experiment or as a stand-alone .prt

lection of procedures, formulas, report-

file. Since protocols do not have plates, ing definitions, and other details. The
they cannot generate data outside of an non-imaging plate data are recalculated
experiment.

when the file is opened in Gen5.

Gen5 Secure and Gen5 IVD maintain an

Data acquired and transformed in an

audit trail of all activity and changes

experiment is protected by an audit

related to a protocol. All other Gen5

trail in Gen5 Secure, Gen5 IVD, and

software levels do not support this fea-

Gen5. The Reader Control edition does

ture.

not support this feature.

Changes made to a stand-alone protocol Within an experiment, you can select
are not reflected in any previously cre-

Save Protocol As to capture the current

ated experiments based on that pro-

details of the protocol and save them as

tocol. A new experiment must be

either a new protocol or as an overwrite

created to apply the revised protocol.

of the original protocol.

Gen5 also supports more complex multi-plate protocols that are not covered in this
introductory material. See Design a Multi-Plate Protocol in the Gen5 Help system.

Gen5 Getting Started Guide

---

90 | Essential Concepts

About File Storage
File Types
Gen5 creates multiple file types:
l Protocol = .prt
l

Experiment = .xpt

l

Panel = .pnl

l

Imaging = .tif

l

Imager manual mode session = .imm

System file types include:
l Plate type (vessel) = .ptf
l

*.xml = several components, like objectives and filter cubes, are managed with
their own unique XML file.

The Gen5 executable file (.exe) and numerous other types of supporting files, like a
Microsoft Excel template, are also installed on the computer.
Databases
Gen5 installs two databases on your system called LocalDB and SharedDB. While the
databases are always used for critical, internally used files, Gen5 offers you the
choice of using the Windows File System or the Gen5 (SharedDB) database for
storing Gen5 protocol (.prt) and experiment (.xpt) files (excluding image files,
which cannot be stored in the SharedDB). This option, combined with the ability to
create multiple databases, allows you to structure file storage according to your
organizations requirements.
l

Files may be stored on the computers hard drive, on a network, or on a portable medium. Windows Explorer or a similar application can be used to view the
file names and locations, and to move, copy, rename, and delete files.

l

Alternatively, protocol and experiment files may be stored in a secure, sharedaccess database. This database, initially named SharedDB.mdb, can be stored on
a users computer or on a shared-access network/computer (LAN). Gen5
provides a special file maintenance utility for viewing the file names and their

Agilent Technologies, Inc.

---

About File Storage | 91

locations, and for moving, copying, renaming, deleting, importing, and exporting files.
l

Select the preferred method of storing protocol and experiment files at System
> Preferences > File Storage.
Note: When upgrading to a higher version of Gen5, you will be prompted to
also upgrade your databases (or not). Gen5 does a good job during a
database upgrade to both preserve your legacy data and to apply changes to
files to make them compatible with new and improved features.

Gen5 IVD and Gen5 IVD Image+ also install the QC Trending database, QCDB.mdb. It
can be set up on a network for sharing among multiple users, moved, renamed, and
copied. It is initially installed in a QC folder in the default database location
described below. See the Gen5 Help system for more information.
File Location
During a typical installation:
l the program files are stored in this default location: C:\Program Files\Agilent\Gen5 (software edition)
l

the databases are stored in this default location: C:\Program Data\Agilent\Gen5
(software edition)\(version #)\SharedDB or LocalDB

l

Gen5 installs Protocol and Experiment folders in the respective File Storage locations, for example: C:\Users\Public\Documents\Protocol

l

Gen5 prompts you to define the location for the Image Library, when applicable. Then, Gen5 maintains a connection between an imaging experiment or
manual mode session and the images acquired in the session.

The databases are critical to Gen5 functionality. Make sure they are not deleted
from your system.
Image Save Options are defined globally in the System>Preferences and locally
in Protocol>Protocol Options.

Gen5 Getting Started Guide

---

92 | Essential Concepts

Image File Management
Each saved image is saved as a TIF file. The TIF files will contain metadata,
pertaining to the instrument, experiment, plate, well, and image, though this data
will likely not be accessible by other TIF file readers. With Quick Export for Imaging
(described in the Gen5 Help) you can save and report the metadata.
Defining the Gen5 Image Library
The first time you connect to an instrument with imaging capability, Gen5 prompts
you to define an Image Library location where images will automatically be saved
when you run an experiment. The Image Library location can be changed at any
time in the Image Save Options dialog.
Storing Images

Warning! Each image is at least 2 MB in standard field-of-view (FOV). When
using a wide field-of-view (WFOV) camera, e.g., Cytation 5 W-models, or a confocal
imager, e.g., Cytation C10, images are almost four times the size of standard FOV
images. Imaging microplates can quickly generate very large amounts of
data: reading only one image per well of a 96-well microplate in standard FOV
results in 200 MB of images. Image montages, z-stacks and processed image files,
such as stitched images, can be much larger. Review your data storage
requirements with your IT department.
Within the image files folder, Gen5 creates an experiment folder for each imaging
experiment executed. Within the experiment folder are subfolders for captured
images of each plate run in the experiment. It is important to not rename the
folders that contain the images. Doing so may break the link between the
experiment or IMM session from its images. See also Relinking an Experiment
(described in the Gen5 Help).
You may find that you need more hard disk space than is allocated by default. For
example, running a multi-plate experiment, imaging all 96 wells in a 4x4 montage in

Agilent Technologies, Inc.

---

Best Practices | 93

three colors will require an increase to virtual memory. Without this change, the
message, "This procedure may require that you increase the size of the virtual
memory in Windows," may appear. In this case, please consult with your IT group to
increase: Change the Virtual Memory Settings on page 26.

Reduce file size by applying binning during image
capture.

Best Practices
Like most software tools, Gen5 is flexible and offers several ways to accomplish a
task. Here are some recommendations for saving time and using it most efficiently.
Efficiencies
l

For an assay or experiment that you will run numerous times, develop a protocol
to define the Procedure, Data Reduction, Data Views, and Reports required.
Then you can run an experiment (from the Task Manager, Experiments > Create
using an existing protocol) based on the protocol whenever necessary. You can
fine-tune the protocol within an experiment, but remember to select File >
Save Protocol As to update the original protocol with your improvements.

l

Use File > Save As to give you a head start creating a new protocol based on an
existing one that contains the same or similar plate layout, reading parameters,
or other elements that will be repeated in your new protocol.

l

Define and customize Data Views before selecting what to include in reports or
export files. All the on-screen data (i.e., data views) can be reported or exported. If you use on-screen views and paper reports equally, it is most efficient to
first fine-tune the Data Views, and then include them in reports/exports.

l

When appropriate, assign Blanks to the plate. Blanks can be deionized (DI)
water, buffer, reagent without analyte, substrate, and so on. When running
fluorescence cellular assays, a DI-water blank illustrates the background contributed by the instrument and labware as separate from the cells and media.

Gen5 Getting Started Guide

---

94 | Essential Concepts

Identify the location of the Blanks in the Plate Layout, and Gen5 will automatically create the blank-subtraction data reductions.
l

Back up your database regularly: once per week is recommended for most organizations. If youre using a Gen5 Database for protocol and experiment file storage, use the built-in Periodic Optimization feature.

l

Take action if you get a warning message about the remaining size of your databases; see Maintaining Files in Gen5 Help for instructions on archiving and deleting records.

l

Turn off the Multi-Read Calculation option to improve Gen5 performance. Calculation results will be the same, but your computers resources will not be
diverted for performing interim calculations. Find this option at Protocol > Protocol Options > Calculation Options.

Time-Savers
l

Partial Plate: For assays using strips or partially filled plates, especially if the
read steps are long or complicated, you can save time by telling the reader
exactly which adjacent wells or portion of the plate to read.

l

Use the Gen5 automatic Save feature to create a new, date-stamped folder for
storing experiment records. This is an especially good practice for large labs
with multiple users who run hundreds of plates per day. Gen5 will keep all the
data organized by date. Define this kind of file management setting in the Initial
Protocol Settings so it will apply to all newly created protocols. Select System >
Preferences > Initial Protocol Settings > Save Options.

l

Print Preview: Save time and paper by viewing reports on screen before sending
them to the printer.

Agilent Technologies, Inc.

---

Basic Tasks
This section provides instructions for some basic tasks.
Quick Read

96

Create a Standard Curve

96

View Results

98

Plate View (Workspace)

100

Print Results

100

Test the Instrument

101

---

96 | Basic Tasks

Quick Read
You can perform a quick read using the microplate reader connected
to the computer to read a plate and report the results. Its called
quick because it is accomplished without taking the time to set up a
full protocol.
Perform a Quick Read:
1. Click Read Now from the Task Manager, and either select an existing protocol
or create a new one for this read.
2. After you select a protocol, or define a reading procedure for a new protocol,
the reader reads the plate.
When the reading is done you can report the results. If you have a full-level edition
of Gen5 (any version other than Gen5 RC), you can perform data analysis.

Create a Standard Curve
Gen5 lets you create one or more standard curves for determining the concentration
of test samples:
1.

Select Read Now > New.

2. In the Procedure dialog, define the Read step (and any other required steps),
then click OK.
Gen5 performs the read and exports your results.

Agilent Technologies, Inc.

---

Create a Standard Curve | 97

Select Plate Layout:

3.

Select

l

Standard Curves as one of the
well types.
l

Define the concentrations of
the Standards.

l

Assign the location of the
standards, samples, and blanks
(if any) on the plate.

4.

Select Data Reduction > Standard Curve.
Note: Gen5 may have generated a corrected data set: if you
assigned blanks to the plate or selected Path length Correction or
Polarization in the Read step, you may want to select these data sets
for Data In for the Y-Axis Data to plot the curve.

5. On the Data In tab, select the Y-Axis Data.
6. On the Curve Fit tab, choose a curve fit method.

7. After you save the data reduction step, the plate matrix will display a Graphs
tab to display the standard curve.
8. Define the reporting or export requirements and save the protocol using File >
Save Protocol As.
Other options and requirements when defining multiple curves:

Gen5 Getting Started Guide

---

98 | Basic Tasks

Curve Name: Replace the default Curve with a more meaningful or unique name.
On the Data Out tab: Replace the default Conc for the Data Set Name with a
more meaningful or unique name.
On the Data Out tab: Define interpolations to plot on the curve.

View Results
You can instantly view the results of an experiment in the Gen5 main workspace:
Plate View (Workspace) on page 100.
l

After reading the
plate (or otherwise
acquiring data), in the
plate view (Matrix)
use the Data list to a
data set to display.
You can also select
Create new Matrix to
define a new view.

l

Click Edit Matrix next to a data set to customize the views appearance. This
feature is also available in the Data Views.

l

Click

to instantly open the current view in Microsoft Excel.

l

Asterisks (**) are used to signal a change: In the Gen5 title bar an asterisk indicates the current file has been changed but not yet saved. When a data set is
enclosed by asterisks, it has become invalid. Generally this is because a Read
step or Data Reduction step has been altered. Edit custom-made data views to
select valid data sets.

l

384- and 1536-well plates require resizing to effectively see the data. Gen5
adds a button to the Plate View to zoom in on the top-left quadrant of the plate
and zoom out to view the entire plate. After zooming in, use the scroll bars to
bring the other quadrants into focus.

Agilent Technologies, Inc.

---

View Results | 99

l

Multi-index readings offer another viewing option. Kinetic and scanning reads
generate views based on the number of intervals, wavelengths, or positions
defined. Use the buttons or enter the desired read index and click Show to display it. Gen5 displays the time, wavelength, or position of the selected read
number.

l

Kinetic and Scanning protocols can generate Well Analysis data sets labeled
Curves. In the Matrix tab, open the Curves data set and click on a well for a Well
Zoom. (384- and 1536-well plates show a magnifying glass in the well in lieu of a
curve.)
Starting at the Curves data set, you can display multiple well zooms

simultaneously by holding Ctrl while selecting wells.
l

Select the Statistics tab to view a table of data reduction results.

l

Select the Graphs tab (when available) to view any standard curves.

l

Select the Results List tab (when available) to view the values or results of the
cutoff or validation formulas.

l

Review the description of the Gen5 naming convention for the raw data/results.

l

In the upper-right corner, click

to pin a plate view in the workspace. Pinning

a plate view allows you to have multiple plates' plate views open simultaneously. If a plate view is not pinned, when you open another plate, it opens
in the same plate view.
l

In the upper-right corner, click

to open another instance of the Plate View.

Use this feature to view the raw data results of a reading in one window and simultaneously display a curve plotted from the results in another window, for
example.
Important Notes
l

Gen5 may not display some data points by default; to see them you must create
your own Data Views. If you expected to see certain results that are not currently displayed, try creating your own views.

Gen5 Getting Started Guide

---

100 | Basic Tasks

l

All data views are also available for reporting and/or exporting.

l

Modify a data view to change the way results are reported, including the number
of decimal places and significant digits.

l

Gen5 always uses your computers regional settings to display and input data.

Plate View (Workspace)
Plate > View

Use the Plate View to view the results of an experiment and, if needed, to mask or
alter the results.
l

Well Zoom - drilling into individual wells - is available in imaging and multi-read
assays.

l

Gen5 uses icons in the menu tree to indicate plate read status (successful, aborted, in progress, errror).

Print Results
Click the Print button to print the results of an experiment.
Prerequisite
First, you must select the specific content for the report using the Gen5
Report/Export Builder (Protocol > Report/Export Builders).
Reporting in an experiment is done on a per-plate basis:

Agilent Technologies, Inc.

---

Test the Instrument | 101

l

Highlight a plate in the menu tree and select Print/Print Preview.

l

In a multi-plate experiment: You can select multiple plates by holding the Ctrl
key while highlighting them, or to select contiguous plates, highlight the first
plate, hold the Shift key, and select the last plate. Then, click Print.
Gen5 offers enormous flexibility in report output. After defining the report

elements, use the Print Preview option to view the report on screen before printing
it to paper. Unneeded columns and other individual report elements can be
removed or modified to improve the appearance and usefulness of the report.
Note: In Gen5 Help you can find step-by-step instructions for creating and
customizing reports.

Test the Instrument
System > Diagnostics > Run System Test
Most Agilent instruments perform a self-test every time theyre turned on, but when
you want to view and/or print the results of a system test:
1. From the Gen5 main window, select System > Diagnostics > Run System Test.
When there is more than one instrument attached to the computer, select the
desired one and click OK.
2. When the test is completed, fill in the text fields--User, Company, Comments--to be included in the report of the test results, then click OK.
3. Print the report to retain a hard copy for your records.
4. Click Save As to convert the results to a text file. This is especially useful
when troubleshooting an instrument. You can email the text file to Agilent.
Test History
Gen5 keeps the results of System Tests when they are performed using the menu
controls.

Gen5 Getting Started Guide

---

102 | Basic Tasks

Note: To review or print the results, select System > Diagnostics > Test
History.

Agilent Technologies, Inc.

---

Set Up a Protocol
This section walks through the basic steps to creating a protocol. You'll find more
details in the Gen5 Help. If you haven't already done so, read the differences
between experiments and protocols in Gen5 in the Essential Concepts section.
Design a Protocol

104

Define the Imaging or Reading Procedure

104

Define the Plate Layout

106

Set Up Data Reduction

108

About Exporting Results

110

About Reports

111

---

104 | Set Up a Protocol

Design a Protocol
In the Task Manager, click Read Now > New to get started.

1.

Define the Procedure, then click OK. Gen5 performs the read and displays the resulting data.

2.

Define the plate layout (for all except Gen5 Reader Control).

3.

Define the data reduction requirements (for all except Gen5 Reader Control).

4.

Define the reporting and exporting requirements.

5. Save the protocol (File > Save Protocol As).
Note: Follow this sequence of tasks when developing a protocol to take
advantage of the automatically created Gen5 data reduction events. For
example, when you add Blanks to the Plate Layout, Gen5 automatically
creates a Blank-Subtraction data set.
You can find instructions for developing specific types of protocols in the Gen5
Help.

Define the Imaging or Reading Procedure
Protocol > Procedure
Note: Procedure grayed out? When one or more plates have been read in an
experiment, the procedure cannot be changed for the current experiment. If
this isn't the case, your System Administrator may have restricted your
ability to modify the protocol elements.

Agilent Technologies, Inc.

---

Define the Imaging or Reading Procedure | 105

Note: Grayed-out buttons mean the action cannot be performed by the
current reader or because previously defined steps--for example, a kinetic
loop--limit the function or your level of software limits the feature.
For all procedures, define the Plate Type and then:
1. Click a link to add that step to the procedure. Most links open a screen for
defining the parameters of that step, for example, Read lets you define
wavelengths.
When defining a kinetic or synchronized well/plate mode analysis, add the
Kinetic or Synchronized Mode steps first. Kinetic and Synchronized Mode steps
form a loop or block. Put the Read and other valid steps to be performed
inside the loop, between the Start and End. Monitor Well is similar: First add
the Monitor Well step and then add a Read step inside the Monitor Well loop.
2. Define the details of the step and click OK.
3. Click Validate to check the selection and sequence of the steps.
Your instrument must be communicating with Gen5 for it to fully validate the
procedure: Make sure it is turned on, not busy, and properly connected to the
computer.
StepWise Procedure Features
l

You can drag and drop steps in the procedure to change their sequence order.

l

You can also copy (Ctrl+C) and paste (Ctrl+V) a procedure step or a block of
steps from one location to another in a the same procedure.

l

Highlight a step in the procedure, and then click an action button to add a step
before it.

l

Double-click a step to open it for editing.

l

Select a step in the sequence and right-click for additional options.

l

Click Validate at any time to verify the reader's ability to perform the current
sequence of steps.

l

Highlight a step and press Delete to remove it from the procedure.

Gen5 Getting Started Guide

---

106 | Set Up a Protocol

l

Kinetic analysis, Synchronized Mode processing, and Monitor Well functions are
set up in a loop or block. First define the function, for example, add the Kinetic
step, and put the read and other steps inside the loop

Drag and drop is limited in Synchronized Modes. For example, you cannot drag and
drop a step into or out of a Well Mode block.

Define the Plate Layout
Protocol > Plate Layout
Note: The Plate Layout Wizard appears when the plate layout has not yet
been defined (and custom Well IDs have not been created and the wizard is
not disabled in System Preferences).
1. In the Plate Layout Wizard, select the well types you want to define for the
plate, then click Next. The Wizard prompts you to define each type of well
you have selected. When all well types are defined, the Plate Layout dialog
opens.
2. Select a well ID in the left pane, then click in a well, or drag over contiguous
wells, to assign the selected well type to the plate layout.
Note: Some readers support random well selection.
l

The well assignment starts with the well ID you select in the left pane. For
example, if you select Well SPL1:4 in the left pane, when you click in a cell in
the plate layout, that cell will be assigned SPL1:4.

l

Use the Auto Select and Replicates options to speed up your work: set the
options and click and drag to fill multiple wells at once. Click a column or row
header to fill it.

l

Use the Serial Assignment tools (

,

, and

) to quickly assign replicates to

the plate layout in a horizontal or vertical line or in square groupings. Select one

Agilent Technologies, Inc.

---

Define the Plate Layout | 107

of the directions (toggle through to access horizontal, vertical, or square) then
click or drag in the plate layout.
l

You can export a plate layout for use in multiple experiments, or import an existing plate layout.
Note: The type of plate, such as 96-well, is defined in the procedure and
displayed in a representative matrix or grid format in the Layout and
Transformation screens.

Helpful Hints
l

Set up your preferred default Well IDs at System > Preferences > Plate Layout
Well IDs. For example, you can define PC (for Positive Control) instead of CTL1
for Assay Controls. Well IDs defined in the System Preferences are available
when defining the plate layout for all newly created protocols/experiments.

l

Click Undo at the bottom of the screen to undo the last action. Up to 10 previous actions can be undone.

l

To clear the grid and start over, right-click and select Empty Layout. To clear
selected cells, set the Type of Well Settings to Empty and select the cells you
want to clear.

l

You can print the plate layout. 384-well plates print out in two sections,
columns 1-12 and 13-24. 1536-well plates print in eight sections to fit all 48
columns and rows from A to Z and AA to AF.

l

For Samples (unknown test specimen) Gen5 lets you assign and track data
points, such as age or gender, in addition to the Sample ID. You can create additional identification fields.

l

To copy the contents of the grid to the Windows virtual clipboard to paste into a
text/external file, right-click and select Copy Layout. Open the receiving file,
for example, Microsoft Word or Excel, then right-click and select Paste. Generally, plates larger than 96 wells do not fit completely in a standard-size Word
or text file; a spreadsheet is required.

Gen5 Getting Started Guide

---

108 | Set Up a Protocol

l

Each instance of a Sample and Sample Control Well ID and each Assay Control
group can have a unique concentration/dilution value. Gen5 assigns a dilution
index to the Well ID to keep track each instance.

l

Well selection must be compatible with the Replicate, Auto Select, and Filling
option settings.

l

You can resize the plate view in the standard Microsoft Windows way: click and
drag the outer borders of the view, or click the maximize button in the top-right
corner.

l

You can resize the rows and columns: hover your mouse over a grid line between
two numbered columns or alpha-labeled rows until the cursor changes to a separator, then click and drag.

l

When running an experiment with a cuvette, the plate layout is mapped on a 96well plate.

Set Up Data Reduction
Protocol > Data Reduction
For the best experience using Gen5s data reduction
the read or imaging parameters

and the plate layout

options, first define
, e.g., assign blanks

or standards, if applicable.
Gen5 uses a logical approach to presenting data reduction steps. Based on the
defined read step and plate layout, Gen5 either creates the most commonly applied
data reduction steps, like blank subtraction, or presents applicable data reduction
options for definition. For example, you cannot create a standard curve until
standards have been assigned in the plate layout.
To analyze complex imaging captures, a montage, z-stack, and kinetic timeline,
requires image processing before data reduction steps can be applied:

Agilent Technologies, Inc.

---

Set Up Data Reduction | 109

Image capture

Processing required

Montage

Stitching

Z-stack

Z Projection

Kinetic timeline

Image Statistics or Cellular Analysis

Gen5 presents only the data reduction options that can be performed with the
currently available data sets. See also Dynamic Data Reduction Explained.
Example
When the raw data is a montage-Z-stack image capture, Gen5 presents only
image preprocessing, deconvolution, and stitching, because the montage must
be stitched before a Z Projection can be created. Likewise, the Z Projection
must be created before Image Statistics or Cellular Analysis can be performed.
Thus, these data reduction options are not presented until that step has been
defined.
Likewise with kinetic analysis, montages must be stitched, z-stacks made into
z projections, and either a statistics or analysis step defined before kinetic
analysis is offered.

Imaging Process and Analysis Optimization Control button at
bottom of dialog.
Top Things to Know about Data Reduction Workspace

Make sure none of the Data Reduction step icons display the red invalid
symbol. The invalid symbol may indicate that a previously selected data in set has
changed, e.g., it has been renamed. Open the step and reselect the data in to fix
the problem.

Gen5 Getting Started Guide

---

110 | Set Up a Protocol

Important note about Cellular Analysis improvements:

With each release of

Gen5, we make improvements to the software. When data reduction processes are
improved, results can be altered. Gen5 uses the Calculation Warning Log to alert
users that their data may have changed. For example, users may see this message:
Failed to calculate cell count due to improved edge object exclusion when using
plugs when they open an experiment created in a previous version of Gen5.

About Exporting Results
Gen5 provides the following exporting tools:
l

Quick Export to instantly export the current view to a Microsoft Excel worksheet

l

Export to Excel: to export selected data to Excel using the Power Export feature

l

Export to File:to export selected data, excluding curves, to a text file (for use in
another software application) using the File Export feature

l

Right-Click Menu Options: Copy to Clipboard and Save As; to copy or save the
current selection for use in another software application

l

to instantly export an image to an Excel spreadsheet.

l

to export an image's metadata to an Excel spreadsheet.

Prerequisites
For the QuickExport and Power Export features, you must have Excel 2007 or higher
installed on your computer. Use File Export or right-click options if you do not have
Excel.
About the Export Tools
l

The Power Export and File Export methods require selecting the content you
want included in the output file before executing the export for a designated
plate.

l

You can save your export selections with the protocol to reuse them every time
you run an experiment based on that protocol.

Agilent Technologies, Inc.

---

About Reports | 111

l

Exporting data is like generating a report; it is done individually for each plate*.
Although you can select the export content in a protocol, you must run (or
execute) the export in an experiment (after selecting a plate or multiple
plates1).
[* except in multi-plate assays]

l

In an experiment, to run the export, you can select a plate in the menu tree and
right-click for a menu that offers the Export option.

Export Multiple Plates to One File
When you run multiple plates in an experiment you can export all the data to one
file:
1. In the menu tree, select/highlight multiple plates (by holding down the Ctrl
key).
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
1. When setting up the protocol, after customizing the Data Views, select
Report/Export Builders from the Protocol menu tree.
2. From the Report/Export Builders dialog, click New Report.

1Hold the CTRL key while selecting multiple plates.

Gen5 Getting Started Guide

---

112 | Set Up a Protocol

3. Define your settings in the Properties, Content, and Options screens, then
click OK. If you are running Gen5 Secure, Gen5 Secure Image+, Gen5 Secure
Image Prime, Gen5 IVD, or Gen5 IVD Image+, Gen5 prompts you to add a comment to the Audit Trail event.

Agilent Technologies, Inc.

---

diagnostics

Index

test the reader 101
A

duplicating a plate view 99
E

Add-On Modules 31
Auto ROI Add-On
licensing 31

email notification feature
configure 54

B

email server, configure 55
errors

buttons 68
C

communication 76
fluorescence 79

camera driver 24
luminescence 79
communication errors 76
experiments
computer requirements 12
vs. protocol 88
Contact Agilent 56
export
contact Technical Support 56
File Export 110
curves
Power Export 110
create standard 96
QuickExport 110
D
data reduction
set up 108

exporting
results 110
External Hard Drive 27

databases

F

copying to a network 44
File Export
moving to a network 44
about 110
organize 43

---

114 | file storage

file storage

Gen5 Reader Control 37

about 90

Gen5 Secure

imaging 92

set up 36

fluorescence

Get Technical Assistance 56

errors 79

H
G

Hamamatsu camera 24

Gen5
available levels 19
best practices 93
install 21
register with BioTek 28
set up 35
starting app 58
supported readers 12
workspace 63
Gen5 databases 40
Gen5 Image+
about 19

I
icons 68
imaging
file management 92
how to install 23
manual mode 72
optimizing performance 85
save options, default 26
install Gen5 21
instrument control
connecting an
instrument 34

setting up 35
Gen5 Image+ IVD 36
about 19
Gen5 Image+ Secure 36
about 19

L
Launching Gen5 58
login 50
luminescence
errors 79

Gen5 IVD 36

Agilent Technologies, Inc.

---

system administrator | 115

M

vs. experiments 88

manual mode

workspace 66

imaging 72

Q

menu tree

Quick Export

using 67

about 110
P

password
changing system administrator's 39

R
reports
building 111
restore optimal

controls 50

performance 78

pinning a view 99

right-click menu options 110

plate layout
define 106
plate view
duplicating 99
pinning 99
workspace 100
Power Export
about 110
printing results 100
procedure
defining 104
protocols
designing 104

Gen5 Getting Started Guide

S
Sleep Mode 27
Spot Counting Add-On
llicensing 31
standard curve
create 96
startup preferences
changing 58
changing in Gen5 IVD 60
changing in Gen5 Secure 60
Storing Gen5 Files 27
system administrator
as-needed tasks 39

---

116 | system requirements

changing password 39
password 86
setting up Gen5 IVD 38
setting up Gen5 Secure 38

Virtual Memory 26
W
Windows authentication
configure 53

system requirements
computer requirements 12
reader requirements 12
T
Task Manager 61
Technical Assistance 56
troubleshooting
general 75
U
user accounts
about 45
create 45, 48
maintain 48
modify 45
user groups
about 46
create 47
modify 47
V
viewing results 98

Agilent Technologies, Inc.

---
