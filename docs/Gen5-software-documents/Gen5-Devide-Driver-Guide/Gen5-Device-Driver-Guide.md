# Gen5 Device Driver Guide

BioTek Gen5 Reader

Device Driver Guide

Original Instructions

---

Notices
Manual Part Number

Warranty

D0003471 Revision D

The material contained in this document is
provided as is, and is subject to being
changed, without notice, in future editions.
Further, to the maximum extent permitted
by applicable law, Agilent disclaims all warranties, either express or implied, with
regard to this manual and any information
contained herein, including but not limited
to the implied warranties of merchantability
and fitness for a particular purpose. Agilent
shall not be liable for errors or for incidental
or consequential damages in connection
with the furnishing, use, or performance of
this document or of any information contained herein. Should Agilent and the user
have a separate written agreement with
warranty terms covering the material in this
document that conflict with these terms,
the warranty terms in the separate agreement shall control.

November 2021

Copyright
(C) Agilent Technologies, Inc. 2021
No part of this manual may be reproduced
in any form or by any means (including
electronic storage and retrieval or
translation into a foreign language) without
prior agreement and written consent from
Agilent Technologies, Inc. as governed by
United States and international copyright
laws.

Contact Information
Agilent Technologies Inc.
Automation Solutions
5301 Stevens Creek Blvd.
Santa Clara, CA 95051
USA
Web:
https://www.agilent.com
Contact page:
https://www.agilent.com/en/contactus/page
Documentation feedback:
documentation.automation@agilent.com

Acknowledgements
Microsoft(R) and Windows(R) are either
registered trademarks or trademarks of the
Microsoft Corporation in the United States
and other countries.

Technology Licenses
The hardware and/or software described in
this document are furnished under a license
and may be used or copied only in
accordance with the terms of such license.

Restricted Rights Legend
If software is for use in the performance of
a U.S. Government prime contract or
subcontract, Software is delivered and
licensed as Commercial computer
software as defined in DFAR 252.227-7014
(June 1995), or as a commercial item as
defined in FAR 2.101(a) or as Restricted
computer software as defined in FAR
52.227-19 (June 1987) or any equivalent
agency regulation or contract clause. Use,
duplication or disclosure of Software is
subject to Agilent Technologies standard
commercial license terms, and non-DOD
Departments and Agencies of the U.S.
Government will receive no greater than
Restricted Rights as defined in FAR 52.22719(c)(1-2) (June 1987). U.S. Government
users will receive no greater than Limited
Rights as defined in FAR 52.227-14
(June1987) or DFAR 252.227-7015 (b)(2)
(November 1995), as applicable in any
technical data.

Safety Notices

WARN I N G
A WARNING notice denotes a hazard. It calls attention to an operating
procedure, practice, or the like that, if
not correctly performed or adhered
to, could result in personal injury or
death. Do not proceed beyond a
WARNING notice until the indicated
conditions are fully understood and
met.

CAUT ION
A CAUTION notice denotes a hazard.
It calls attention to an operating procedure, practice, or the like that, if not
correctly performed or adhered to,
could result in damage to the product
or loss of important data. Do not proceed beyond a CAUTION notice until
the indicated conditions are fully
understood and met.

---

Contents
Preface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . v
About this guide. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . vi
Accessing user guides . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii
1. Setting up a BioTek Reader device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Setup workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Adding a BioTek Reader device and setting properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Creating and initializing a profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
Testing a BioTek Reader device . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Create Gen5 Experiment (BioTek Gen5 Reader) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
Run Experiment (BioTek Gen5 Reader) task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
Set Temperature (BioTek Gen5 Reader) task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
Wait for Temperature (BioTek Gen5 Reader) task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

BioTek Gen5 Reader Device Driver Guide

iii

---

Contents

This page is intentionally blank.

iv

BioTek Gen5 Reader Device Driver Guide

---

Preface
This preface contains the following topics:
-

About this guide on page vi

-

Accessing user guides on page viii

v

---

About this guide

About this guide
Who should read this guide
This user guide is for people with the following job roles:
Job role

Responsibilities

Installer

Unpacks, installs, and tests the device before it is used.

Integrator

Configures hardware and writes software.

Lab manager,
administrator, or
technician

-

Manages the automation system that contains the device

-

Develops the applications that are run on the system

-

Develops training materials and standard operating
procedures for operators

Operator

Performs the daily production work on the device and solves
routine problems.

What this guide covers
This guide describes how to set up BioTek microplate readers in the VWorks software.
The VWorks software supports the following models of BioTek readers:
-

Cytation 1, 5, or 7 Imaging Multi-Mode Reader

-

Cytation 5 Hybrid Multi-Mode Reader

-

Epoch2 Microplate Spectrophotometer

-

Synergy H1 Multi-Mode Reader

-

Synergy Neo2 Hybrid Multi-Mode Reader

What is new in this edition
This edition contains updates to the device and profile descriptions and procedures to
reflect changes introduced in VWorks software 14.1.

Software version
This guide is applicable for the following versions of VWorks software and BioTek Gen5
Reader Diagnostics:

C AU T I O N

vi

-

13.1.8 - 13.1.x

-

14.1.0 and later

VWorks Plus 14.1 requires BioTek Gen5 Reader protocols and experiment files to be
stored on local drive in visible Windows directories. Agilent recommends that you
copy Gen5 protocols and experiment files to a more secure location after data
acquisition and processing is complete.

BioTek Gen5 Reader Device Driver Guide

---

About this guide
The VWorks software runs on the Microsoft Windows 10 64-bit operating system.
The VWorks BioTek Reader Device Driver is verified to be compatible with BioTek Gen5
software version 3.10.

Related guides
Use this guide in conjunction with the relevant BioTek user documentation and the
following guides for your version of the VWorks software:
-

VWorks Automation Control Setup Guide. Explains how to define labware and
labware classes, liquid classes, and pipetting techniques, and how to track and
manage labware in storage.

-

VWorks Automation Control User Guide. Explains how to create protocols, and set
task parameters for each device in the system.

Related topics
For information about...

See...

Accessing the Agilent automation product
user guides

Accessing user guides on page viii

BioTek user documentation

https://btresource.force.com/CRC/s/

Setting up a BioTek Reader device

Setup workflow on page 2

BioTek Gen5 Reader Device Driver Guide

vii

---

Accessing user guides

Accessing user guides
About this topic
This topic describes the different formats of user information and explains how to
access it for the Agilent Automation Solutions products.

Where to find user information
The user information is available in the following locations:
-

Knowledge base. The help system for the Automation Solutions products is
available from:
-

Help menu within the VWorks software: Select Help > Knowledge Base or press
F1.

-

From the Windows desktop: Select Start (
Technologies > VWorks Knowledge Base.

) > All Apps > Agilent

For guidelines on using the VWorks context-sensitive help and knowledge base
features, see Using the knowledge base, below.
-

PDF files. The PDF files of the user guides are installed with the VWorks software
(C:\Program Files (x86)\Agilent Technologies\VWorks\UserGuides) and are
available in the VWorks Knowledge Base.

-

Website. You can search the online VWorks Knowledge Base or download the latest
version of any PDF file from the Agilent website at www.agilent.com/chem/askb.

Accessing safety information
Safety information for the Agilent Automation Solutions devices appears in the
Automation Solutions Products General Safety Guide and in the corresponding device
safety guide or user guide.
You can also search the knowledge base or the PDF files for safety information.

Using the knowledge base
Knowledge base topics are displayed using web browser software such as Microsoft
Edge.
Note: If you want to use Microsoft Internet Explorer to display the topics, you might
have to allow local files to run active content (scripts and ActiveX controls). For
instructions, see the Microsoft user documentation.

viii

BioTek Gen5 Reader Device Driver Guide

---

Accessing user guides

Opening the help topic for an area in the VWorks window

To access the context-sensitive help feature:

1

In the main window of the VWorks software, click the help button

. The pointer

changes to
. Notice that the different icons or areas are highlighted as you
move the pointer over them.

2

Click an icon or area of interest. The relevant topic or document opens.

BioTek Gen5 Reader Device Driver Guide

ix

---

Accessing user guides

Features in the Knowledge Base window

Step

x

For this task...

1

Contents pane. Lists all the books and the table of contents of the books.

2

Search. Allows you to search the Knowledge Base (all products or selected products) using
keywords.

3

Topic area. Displays the selected online help topic.

4

Navigation buttons. Enable you to navigate through the next or previous topics listed in the Contents
tab.

5

Toolbar buttons: Enable you to:
-

Expand or collapse all the sections in a topic that has drop-down headings.

-

Print the topic.

-

Send feedback by email for a given topic.

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
This chapter describes how to set up a BioTek Reader device in the VWorks
software. You must have VWorks administrator or technician privileges to set up
devices in the VWorks software.
The topics in this chapter are:
-

Setup workflow on page 2

-

Adding a BioTek Reader device and setting properties on page 3

-

Creating and initializing a profile on page 8

-

Testing a BioTek Reader device on page 12

-

Create Gen5 Experiment (BioTek Gen5 Reader) on page 16

-

Run Experiment (BioTek Gen5 Reader) task on page 19

-

Set Temperature (BioTek Gen5 Reader) task on page 22

-

Wait for Temperature (BioTek Gen5 Reader) task on page 24

1

---

Setting up a BioTek Reader device
Setup workflow

Setup workflow
The following table presents the workflow for setting up the BioTek Gen5 Reader
devices.
Step

For this task...

See...

1

Ensure that the BioTek Gen5
software is installed on the
computer that you are using to
control the BioTek reader
instrument.

BioTek documentation for the device

2

Configure the instrument.

BioTek documentation for the device

3

Add the device to the VWorks
device file and set the device
properties.

Adding a BioTek Reader device and
setting properties on page 3

4

Create a device profile and set
the profile properties.

Creating and initializing a profile on
page 8

5

Verify the device control.

Testing a BioTek Reader device on
page 12

6

Create a VWorks protocol.

VWorks Automation Control User Guide
See Accessing user guides on
page viii.

7

Set the task parameters for the
device in a VWorks protocol.

-

Create Gen5 Experiment (BioTek
Gen5 Reader) on page 16

-

Set Temperature (BioTek Gen5
Reader) task on page 22

-

Wait for Temperature (BioTek
Gen5 Reader) task on page 24

-

Run Experiment (BioTek Gen5
Reader) task on page 19

Related topics

2

For more information about

See

BioTek user documentation

https://btresource.force.com/CRC/s/

Using JavaScript to set task
parameters

VWorks Automation Control User Guide
See Accessing user guides on page viii.

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Adding a BioTek Reader device and setting properties

Adding a BioTek Reader device and setting properties
About this topic
This topic describes how to add the BioTek Reader device (
VWorks software and set the device properties.

) in the

The device properties provides the VWorks software with information about an
instruments current configuration. The device property settings are stored in the
device file. The VWorks software uses the information in a device file to communicate
with and operate the device.
You must have VWorks administrator privileges to create and edit device files.
For detailed information about device files and associations with profiles, teachpoints,
and labware definitions, see the VWorks Automation Control User Guide.

Devices and device files defined
A device is an item in your lab automation system that has an entry in a VWorks
software device file. A device can be a robot, an instrument, or a location in a lab
automation system that can hold a piece of labware.
The device file (*.dev) stores information for all the devices in an integrated system,
including:
-

Type of device

-

Device configuration information (for example, approach height, allowed or
prohibited labware, and so on)

-

Profile to use

Creating a device file
If you are setting up a new device or workstation configuration, you need to create a
VWorks device file.
To add a new device to an existing device file, see Adding a BioTek Reader device to a
device file on page 4.

To create a device file:
1 Log in to the VWorks software as an administrator.

2

In the VWorks window, click File > New > Device. A Device File tab appears in the
VWorks window.

BioTek Gen5 Reader Device Driver Guide

3

---

Setting up a BioTek Reader device
Adding a BioTek Reader device and setting properties

3
4

Click File > Save.
In the Save As or Save File As dialog box, select the storage location, type the file
name, and then click Save.

Adding a BioTek Reader device to a device file
Before you start:
-

Ensure that any devices are physically networked to the computer.

-

Turn on the devices.

To add devices to a device file:
1 In the VWorks window, verify that the correct device file is open.

2

In the Available Devices area, double-click the BioTek 5 Reader icon. Alternatively,
you can drag the icon to the Device File tab.
Note: To show or hide the list of available devices, choose View > Available
Devices.

4

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Adding a BioTek Reader device and setting properties

3
4

In the Device File tab, select the BioTek Gen5 Reader-n icon.
Under BioTek Gen5 Reader Properties, type a Name for the device. By default, the
software assigns BioTek Gen5 Reader-n, and increments the number for each
device that you add.
To identify the specific device, you might want to include the device serial number
in the device name.

5

In the Profile list, select a profile for the device.
If the Profile list is empty:

a

Create a profile. For instructions, see Creating and initializing a profile on
page 8.

b

Return to this step to select the new profile.

A profile is required to establish communication with the device.

BioTek Gen5 Reader Device Driver Guide

5

---

Setting up a BioTek Reader device
Adding a BioTek Reader device and setting properties

6

On the Device File tab, expand the BioTek Gen5 Reader device icon, and then click
Location. The corresponding location properties appear.

7

Set the following properties.
Property

Description

Allowed/prohibited
labware

Optional. Click
if you want to specify labware
restrictions for this location. The Allowed/prohibited
labware dialog box appears. For details on the labware
classes, see the VWorks Automation Control Setup
Guide.
Note: If the
field.

BCR on south/west/
north/east side

button is not visible, click the empty

The location of the barcode reader and the desired
barcode reader device.
Use this field only if a barcode reader is installed on the
device.

Teachpoint for robot
<robot name>

Specify whether the robot can access this location.

Use for deadlock
avoidance

Option to permit the location to be used for deadlock
avoidance.
Select Yes (default) to permit labware to be moved to
this location to avoid a deadlock in the system.
Select No if you do not want to move random labware
to this location to avoid a deadlock.

6

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Adding a BioTek Reader device and setting properties

8

Property

Description

Door

This property is not applicable for the BioTek Reader
device.

Click File > Save to save the changes.
If you are creating a new device file, the Save As or Save File As dialog box appears
so that you can specify a name and location for your device file. Ensure the file type
is *.dev.
Alternatively, you can select File > Save All to save the device file and the current
protocol file at the same time.

Related topics
For more information about

See

Setting up a device

Setup workflow on page 2

Creating a VWorks device profile for a
BioTek Reader

Creating and initializing a profile on page 8

Using Diagnostics to test the BioTek
Reader device

Testing a BioTek Reader device on page 12

Create a VWorks protocol.

VWorks Automation Control User Guide

Configuring the BioTek Reader tasks
in a VWorks protocol

-

Create Gen5 Experiment (BioTek Gen5
Reader) on page 16

-

Run Experiment (BioTek Gen5 Reader)
task on page 19

-

Set Temperature (BioTek Gen5 Reader)
task on page 22

-

Wait for Temperature (BioTek Gen5
Reader) task on page 24

BioTek Gen5 Reader Device Driver Guide

7

---

Setting up a BioTek Reader device
Creating and initializing a profile

Creating and initializing a profile
Before you start
The profile is referenced by a VWorks device file. The device file must be open before
you can create or modify a profile.
VWorks Plus. The software logs audit trails for device profiles, which are records of
interest.

Creating a profile
Note: VWorks software v14.1 and later versions store the profile in an XML file in Shared
Services storage. VWorks software v13.1.x stores the profile in the Windows Registry.

To create a profile:
1 In the VWorks software window, ensure the correct device file is open.

2

8

In the Devices area of the opened device file tab, highlight the BioTek Gen5 Reader
icon, and then click Device diagnostics.

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Creating and initializing a profile
The BioTek Gen5 Reader Diagnostics dialog box opens. This dialog box is the
same in VWorks 14.1 and 13.1.x, except that the 13.1.x versions do not include the
log areas at the bottom of the window.
Figure BioTek Gen5Reader Diagnostics dialog box in VWorks 14.1

VWorks 14.1 only. A log of profile activity appears in the box at the bottom of the
window. The VWorks software records these events and stores the information in
the Main log.

3

In the Profiles tab, under Profile Management, click Create a new profile. The Create
Profile dialog box opens.

4
5

Type a name, and click OK. The name appears in the Profile Management area.
In the Profile Settings area, set the following parameters:

BioTek Gen5 Reader Device Driver Guide

9

---

Setting up a BioTek Reader device
Creating and initializing a profile
Profile parameter

Description

Reader type

The type of BioTek Reader associated with this profile.
The options are

Timeout (sec)

-

Cytation 1

-

Cytation 5

-

Cytation 7

-

Epoch 2

-

Synergy H1

-

Synergy Neo2

Maximum time (seconds) that the BioTek Reader can
take to run the specified experiment.
Note: VWorks displays an error message if the actual
duration of the run exceeds the specified timeout.
Default: 300 sec

Barcode

The location of the barcode on the plate when
performing a read operation.
The options are None, South, West, East, or North.
Note: VWorks passes the barcode to the BioTek
software for use when referencing the data from the
run.

Retract stage when not
in use

The option to retract the stage when not in use.

Reader configured with
180 degrees plate
rotation

The option to specify that the reader is configured with
180 plate rotation.

Experiment file folder

The path of the folder that contains the BioTek
experiment files.

Select the check box if you want the plate stage to
retract when not in use. Otherwise, clear the check box.

Select this check box only if the reader is configured
for this rotation. Otherwise, clear this check box.

Click
to open the Browse for Folder dialog box.
Select the folder, and then click OK.

6

Click Update this profile to save the changes.
VWorks 14.1 only. In the Diagnostics dialog box, the Modified Variables area clears,
and the update is logged in the box at the bottom of the window.

Initializing the profile in diagnostics
IMPORTANT

10

Before initializing a Gen5 device in the VWorks software, ensure that the Gen5 software
is not running in the background. If the Gen5 software is open in the background, it has
control over the BioTek instrument and the VWorks software will not be able to
establish communication with the BioTek instrument.

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Creating and initializing a profile

To initialize the profile:
1 In the Profiles tab of BioTek Gen5 Reader Diagnostics, ensure that you have the
correct profile name selected.

2

Click Initialize this profile to establish communication with the device.
Note: If initialization fails, open Windows Task Manager and verify that no
instances of the Gen5 software are running in the background.

Related topics
For more information about

See

Setting up a device

Setup workflow on page 2

Using Diagnostics to test the BioTek
Reader device

Testing a BioTek Reader device on page 12

Create a VWorks protocol.

VWorks Automation Control User Guide

Configuring the BioTek Reader task in
a VWorks protocol

-

Create Gen5 Experiment (BioTek Gen5
Reader) on page 16

-

Run Experiment (BioTek Gen5 Reader)
task on page 19

-

Set Temperature (BioTek Gen5 Reader)
task on page 22

-

Wait for Temperature (BioTek Gen5
Reader) task on page 24

BioTek user documentation

BioTek Gen5 Reader Device Driver Guide

https://btresource.force.com/CRC/s/

11

---

Setting up a BioTek Reader device
Testing a BioTek Reader device

Testing a BioTek Reader device
About this topic
This topic describes how to use BioTek Gen5 Diagnostics to test a BioTek Reader
device.

Before you start
Ensure the following:
-

The BioTek instrument is turned on.

-

The BioTek Gen5 software is not running in the background.

-

You have a suitable Gen5 Experiment file to reference for the device that you are
testing.

-

You have labware that is suitable for the Gen5 Experiment file to be run.

Note: For more information on your BioTek instrument and software, refer to the BioTek
user documentation for the specific instrument.

Using Diagnostics to test a BioTek Reader device
To test a BioTek Reader device:
1 Open BioTek Gen5 Reader Diagnostics.
To do this, in the Devices area of the opened device file tab, highlight the device
icon, and then click Device diagnostics.

2

In the BioTek Gen5 Reader Diagnostics window, select the correct Profile name, and
then click Initialize this profile.

Note: The button label changes from Initialize this profile to Close this profile.

12

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Testing a BioTek Reader device

3

Click the Controls tab, and ensure that the Status readout displays IDLE.

4

In the Reader Operations area:

a

Select the Experiment file.
The experiment files are located in the folder specified in the Profiles tab.

b

Optional. Enter the Barcode for the plate that you want to read.

BioTek Gen5 Reader Device Driver Guide

13

---

Setting up a BioTek Reader device
Testing a BioTek Reader device

5

If applicable. Set the following parameters in the Temperature area, and click
Set Temperature.
Parameter

Description

SetPoint

The target temperature (C) of the readers incubator.

Gradient

The temperature offset for the top of the read chamber
to mitigate condensation.
Range: 0-2 C

Current temperature

The current temperature (C) of the readers incubator.

Note: The temperature setpoint is only required if the Gen5 Experiment
procedure includes the Set Temperature command before the Read command.
If the reader is not preheated before executing a Gen5 Experiment that includes
a Set Temperature command, the reader will remain idle until it reaches
temperature and potentially time-out.

6

Place an appropriate labware on the BioTek Reader carrier.
If necessary, click Carrier Out to access the carrier. The Status readout displays
EXTENDING CARRIER.

14

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Testing a BioTek Reader device

7

Click Run to move the carrier into the instrument and run the specified experiment.
The Status readout displays READ IN PROGRESS.

Aborting a read in progress
To abort a read in progress in diagnostics:
In the Controls tab, click Abort.

Editing the selected experiment file
You can edit the selected experiment file if a read is not currently in progress.

IMPORTANT

If data has already been collected for an experiment, making changes to the Read
procedure, such as adding a Set Temperature will prompt the Gen5 software to erase
the existing read.

To edit the experiment file selected in the Controls tab:
In the Controls tab, click Edit. The selected file opens in the BioTek Reader software. For
details, see the BioTek software user documentation.

BioTek Gen5 Reader Device Driver Guide

15

---

Setting up a BioTek Reader device
Create Gen5 Experiment (BioTek Gen5 Reader)

Related topics
For more information about

See

Setting up a device

Setup workflow on page 2

Create a VWorks protocol.

VWorks Automation Control User Guide

Configuring the BioTek Reader task in
a VWorks protocol

-

Create Gen5 Experiment (BioTek Gen5
Reader) on page 16

-

Run Experiment (BioTek Gen5 Reader)
task on page 19

-

Set Temperature (BioTek Gen5 Reader)
task on page 22

-

Wait for Temperature (BioTek Gen5
Reader) task on page 24

BioTek user documentation

https://btresource.force.com/CRC/s/

Create Gen5 Experiment (BioTek Gen5 Reader)
Task description
This topic describes how to set the parameters for the Create Gen5 Experiment (BioTek
Gen5 Reader) task (

) task in a VWorks protocol.

For instructions on how to create a VWorks protocol, see the VWorks Automation
Control User Guide.

Create Gen5 Experiment task defined
You use the Create Gen5 Experiment (BioTek Gen5 Reader) task to set up an
experiment to run on the BioTek Reader.
Task is available for...

Task is available in...

BioTek Gen5 Reader (various models)

Startup Protocol
Main Protocol

16

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Create Gen5 Experiment (BioTek Gen5 Reader)

Setting the task parameters
To set the task parameters:
1 Add a Create Gen5 Experiment (BioTek Gen5 Reader) task to a protocol.

2

Select the task icon in the protocol, and then set the following task parameters.

Parameter

Description

Protocol file

The Gen5 protocol upon which the experiment is based.
Click the blank field, and then click
. In the Open dialog
box, locate the Gen5 protocol file (.prt), and then click OK.

Experiment output
folder

The folder in which the experiments file will be created.
Click the blank field, and then click
. In the Browse for
Folder dialog box, locate the folder and then click OK.

Experiment file

The file name of the experiment file.
If you do not provide a name, the software uses the file
name of the specified protocol appended with the datetime
stamp: <protocolfile>_<timestamp>.xpt

3

Click File > Save.

BioTek Gen5 Reader Device Driver Guide

17

---

Setting up a BioTek Reader device
Create Gen5 Experiment (BioTek Gen5 Reader)

About the device selection
The VWorks software automatically assigns the Device Selection to the BioTek Gen5
Reader device.

Related topics

18

For more information about

See

Setting up a device

Setup workflow on page 2

Creating a VWorks device profile for a
BioTek Reader

Creating and initializing a profile on page 8

Create a VWorks protocol.

VWorks Automation Control User Guide

BioTek user documentation

https://btresource.force.com/CRC/s/

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Run Experiment (BioTek Gen5 Reader) task

Run Experiment (BioTek Gen5 Reader) task
About this topic
This topic describes how to set the parameters for the Run Experiment (BioTek Gen5
Reader) task (

).

For instructions on how to create a VWorks protocol, see the VWorks Automation
Control User Guide.

Run Experiment (BioTek Gen5 Reader) task defined
The Run Experiment (BioTek Gen5 Reader) task runs the specified experiment on the
BioTek Reader.
Task is available for...

Task is available in...

BioTek Gen5 Reader (various models)

Main Protocol

Setting the task parameters

To set the task parameters:
1 Add a Run Experiment (BioTek Gen5 Reader) task to a protocol.

2

Select the task icon in the protocol, and then set the following task parameters.

BioTek Gen5 Reader Device Driver Guide

19

---

Setting up a BioTek Reader device
Run Experiment (BioTek Gen5 Reader) task
Parameter

Description

Use experiment
from Create
Gen5
Experiment task

The option to use the experiment file created by the Create
Gen5 Experiment (BioTek Gen5 Reader) task in this protocol.

Experiment file

The option to specify a previously created Gen5 Experiment
file (*.xpt) that you want the VWorks protocol to run.

If you select this check box, the Experiment file parameter is
unavailable.

Select the file from the list. Ensure that the file is suitable for
the model of BioTek reader and consumables. Refer to the
BioTek Gen5 user documentation for details.
Note: Alternatively, you can use a JavaScript variable to
specify the file. For details, see the VWorks Automation
Control User Guide.
Note: The folder for storing the experiment files is specified in
the device profile. Only the files in this folder are available for
selection.
For details on creating an experiment file, refer to the BioTek
reader user documentation for the specific instrument model.
Sample ID file

The option to import the sample IDs from a file into the Gen5
experiment plate before reading the plate.
Click the Sample ID file field, and then click
dialog box, locate the file and click Open.

. In the Open

Refer to the BioTek reader user documentation for use cases
that require a sample ID file and the format requirements of
sample ID files.
Plate Layout file

The option to import the plate layout from a file into the Gen5
experiment plate before reading the plate.
Click the Plate Layout file field, and then click
dialog box, locate the XML file and click Open.

. In the Open

Refer to the BioTek Gen5 software user documentation for
instructions on how to create a plate layout file.
Use existing
plate

The option to use an existing plate or create a new plate
specified in the experiment file:
-

If the Use existing plate check box is cleared (default), a
new plate is added to the specified experiment file and
the run operation is performed on this new plate.

-

If the check box is selected, a valid Plate ID must be
specified. In this case, the read operation is performed on
the specified plate.
If the Plate ID does not match a plate in the experiment
file, an error occurs and the read is aborted.

Plate ID

Enabled if Use existing plate is selected.
The ID of the plate in the specified experiment file to which
the software will attach the data for this plate run.

3
20

Click File > Save.
BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Run Experiment (BioTek Gen5 Reader) task

About the device selection
The VWorks software automatically assigns the Device Selection to the BioTek Gen5
Reader device.

Related topics
For more information about

See

Setting up a device

Setup workflow on page 2

Creating a VWorks device profile for a
BioTek Reader

Creating and initializing a profile on page 8

Create a VWorks protocol.

VWorks Automation Control User Guide

BioTek user documentation

https://btresource.force.com/CRC/s/

BioTek Gen5 Reader Device Driver Guide

21

---

Setting up a BioTek Reader device
Set Temperature (BioTek Gen5 Reader) task

Set Temperature (BioTek Gen5 Reader) task
Task description
The Set Temperature (BioTek Gen5 Reader) task (
) preheats
the BioTek Gen5 Reader for incubated reads where the Gen5 Experiment contains a Set
Temperature command in the acquisition procedure.
Task is available for...

Task is available in...

BioTek Gen5 Reader (various models)

Main Protocol

For instructions on how to create a VWorks protocol, see the VWorks Automation
Control User Guide.
Note: The Set Temperature (BioTek Gen5 Reader) task does not replace the Set
Temperature command within the Gen5 Experiment procedure.

Setting Set Temperature task parameters
To set the task parameters:
1 Add a Set Temperature (BioTek Gen5 Reader) task to a protocol.

2

22

Select the task icon in the protocol, and then set the following task parameters.

Parameter

Description

Temperature
(18 - 65 C)

The target temperature (C) of the readers incubator.

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Set Temperature (BioTek Gen5 Reader) task
Parameter

Description

Gradient (0 - 2)

The temperature offset for the top of the read chamber to
mitigate condensation.
Range: 0-2 C

Wait

The option to pause the protocol for a specified wait time to
allow the readers incubator to reach the target temperature.
If you want the protocol to continue before the set
temperature is reached, you can set a wait timeout and
tolerance later in the protocol using the Wait for Temperature
(BioTek Gen5 Reader) task.

3

Tolerance (1 - 5)

The acceptable tolerance ( minutes) for the timeout
duration.

Timeout (1 - 60
minutes)

The amount of time to pause the protocol while waiting for
the readers incubator to reach the target temperature.

Click File > Save.

About the device selection
The VWorks software automatically assigns the Device Selection to the BioTek Gen5
Reader device.

Related topics
For more information about

See

Setting up a device

Setup workflow on page 2

Creating a VWorks device profile for a
BioTek Reader

Creating and initializing a profile on page 8

Create a VWorks protocol.

VWorks Automation Control User Guide

BioTek user documentation

https://btresource.force.com/CRC/s/

BioTek Gen5 Reader Device Driver Guide

23

---

Setting up a BioTek Reader device
Wait for Temperature (BioTek Gen5 Reader) task

Wait for Temperature (BioTek Gen5 Reader) task
Task description
You use the Wait for Temperature (BioTek Gen5 Reader) task
(
) coupled with the Set Temperature (BioTek Gen5
Reader) task in a VWorks protocol. The Wait for Temperature (BioTek Gen5 Reader)
task pauses the VWorks protocol until the specified BioTek Readers incubator reaches
target temperature.
Task is available for...

Task is available in...

BioTek Gen5 Reader (various models)

Main Protocol

For instructions on how to create a VWorks protocol, see the VWorks Automation
Control User Guide.

Wait for Temperature task requirements
A Set Temperature (BioTek Gen5 Reader) task must proceed the Wait for Temperature
task (BioTek Gen5 Reader) in the VWorks protocol.

Setting the task parameters
To set the task parameters:
1 Add a Wait for Temperature (BioTek Gen5 Reader) task to a protocol.

2

24

Select the task icon in the protocol, and then set the following task parameters.

BioTek Gen5 Reader Device Driver Guide

---

Setting up a BioTek Reader device
Wait for Temperature (BioTek Gen5 Reader) task

3

Parameter

Description

Timeout (1 - 60
minutes)

The amount of time to pause the protocol while waiting for
the Readers incubator to reach the target temperature.

Tolerance (1 - 5)

The acceptable tolerance ( minutes) for the timeout
duration.

Click File > Save.

About the device selection
The VWorks software automatically assigns the Device Selection to the BioTek Gen5
Reader device.

Related topics
For more information about

See

Setting up a device

Setup workflow on page 2

Creating a VWorks device profile for a
BioTek Reader

Creating and initializing a profile on page 8

Create a VWorks protocol.

VWorks Automation Control User Guide

BioTek user documentation

https://btresource.force.com/CRC/s/

BioTek Gen5 Reader Device Driver Guide

25

---

In This Guide
This guide describes how to configure the
VWorks software to control a BioTek Gen5
Reader.

www.agilent.com
(C) Agilent Technologies, Inc. 2021
November 2021

*D0003471*
D0003471 Revision D

---
