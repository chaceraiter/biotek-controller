# Chapter 19: Reader Control

     This chapter supplements the Getting Started Guide instructions for
     attaching a reader to Gen5 with more in-depth information about
     how to control, configure and test your reader.


 Reader Configuration................................................................ 408
 Controlling the Clarity............................................................... 409
 About Com Ports...................................................................... 410
 Reader Settings ....................................................................... 413
    Absorbance Wavelengths...................................................... 415
    Fluorsecence/Luminescence Filters ........................................ 416
    Dispenser Settings .............................................................. 418
 Reader Control Panel ................................................................ 417
    Preheating.......................................................................... 417
 Testing the Reader................................................................... 422



406 | Chapter 19: Reader Control




When you have Two Readers
        Gen5 lets you set up and control two readers simultaneously. Here's how Gen5
        determines which reader to deploy when you have two readers attached to your PC.

          Note: Fluorescence and Luminescence protocols are not instantly
            interchangeable between Synergy 2/4 and other BioTek readers. (The
            Synergy 2 and Synergy 4 have newer basecode.) When you try to read
            a plate using a protocol defined on a different reader, Gen5 will alert
            you of the need to edit the Read step. To use a protocol created with a
            different reader, open all the Read steps while communicating with the
            current reader. This action will update the protocol to match the
            current reader's capabilities.

Compatibility
          Gen5 tests the readers for compatibility with the Procedure when you:
               Edit/Open an Existing Procedure
               Read a plate
         1.   All available, i.e. not busy, readers are tested for compatibility. A reader
              performing a read is considered busy.
              Compatibility is determined by these criteria:
               If the protocol was created for the Clarity, then the reader must be a Clarity.
                  If the protocol was not created for the Clarity, then the reader cannot be a
                 Clarity
               If it is not a Clarity protocol, Gen5 tests the reader's capability to perform
                 the required detection method:
               Absorbance: minimum and maximum wavelengths supported
               Fluorescence
               Luminescence
               Spectrum Scans
               Linear Scans
               Area Scans
               Gen5 tests the reader's capability to perform:
               Incubation: minimum and maximum temperature supported
               Shake
               Dispense: number of dispensers available
               Gen5 tests the reader's capability to perform:
               Well Mode: maximum number of reads, shakes, and dispenses
               Synchronized Plate Mode: maximum number of synchronized plate reads,
                 shakes, and dispenses






      Pathlength Correction
2.   If exactly one reader meets the criteria, it is automatically selected to edit the
     Procedure or read the plate
3.   If more than one reader meets the criteria, Gen5 determines if one of them was
     last used to edit the Procedure or read the plate. If so, then it is selected. If not,
     the user is prompted to select which reader to use.
     Gen5 checks the Protocol for a reader type and serial number to determine
     which reader was last used. If it does not find an exact match, but only one of
     the readers is the same type, that reader is selected.
4.   If none of the readers matches the criteria:0.
      Gen5 will display an error message and offer to Continue or Cancel. Users
        who select Continue can modify the Procedure to make it compatible with
        their reader



408 | Chapter 19: Reader Control




Reader Configuration
     System> Reader Configuration
        Use these controls to tell Gen5 about the attached reader(s) and to retrieve software
        version information for tech support or other purposes. The status of an instrument is
        displayed as Ready or Busy: Ready to perform a read or Busy doing so.

          Special note for Clarity users: Configuration parameters and port
            settings can only be defined through the Clarity PC software. See
            Setting up the Clarity Luminometer in the Getting Started Guide

Add a Reader
        Click the Add button to connect up to two readers to the system. You'll select the
        Reader Type and the Communication Port its plugged into on your PC (see page 410),
        and if necessary, define Setup properties.

                     and              lead to Reader Settings on page 413

Modify a Reader
        Highlight a reader and click Modify (or double click a reader) to change the reader's
        Com Port or Setup properties

Delete a Reader
        Highlight a reader and click Delete to eliminate it from potential use by Gen5.

ActiveX Version
        Click the Active X button to retrieve the latest software version number:



        You may need to provide this information when seeking assistance from BioTek's TAC
        (Technical Assistance Center)







Controlling the Clarity
    System> Reader Control> Clarity

Microplate Holder Control
        The Clarity's microplate holder can be opened and closed only through software
        control. Under Move Plate:
                Click Out to extend/open the microplate holder
                Click In to retract the microplate holder into the reading and heating
                  chamber

          Important: Do not forcibly push in or pull out the microplate holder!
            If for any reason you cannot control the holder using the software, use
            the Allan key supplied with the instrument to extend or retract the
            holder. Refer to the ClarityTM Operator's Manual for more information.

Prime
        The reagent lines and injectors should be primed with the dispensing fluid before
        running the protocol. Click Priming to open the Priming Parameters dialog.

          Refer to the Clarity Operator's Manual for complete priming
            instructions.

To prime the injectors:
          1.   Fill the reagent bottle(s) with the fluid to be dispensed.
          2.   Select System>Reader Control>Clarity and click Priming for the Priming
               Parameters dialog. All installed injectors are displayed. Injectors marked by an
               asterisk (*) have yet to be initialized. Initialization takes place automatically
               when the injector is used.
          3.      Click on the injector's check box. The drop-down list box Direction, Volume
               [ul] and Strokes are enabled.
          4.   Set the Direction To Mpl. Specify the Volume [ul] and the number of Strokes or
               cycles. The total liquid volume is displayed as the Total Volume.
          5.   Click Prime to prime the injector(s). 0.

Heating
        The Clarity's optional incubator is controlled via software. Click the Incubation...
        button to access the Sample Incubation dialog.

          Refer to the Clarity Operator's Manual for complete heating
            instructions.



410 | Chapter 19: Reader Control



About Com Ports
        Com Ports are communication ports that allow your computer (PC) to connect to and
        control other devices. BioTek ships the required serial and/or USB cables with the
        reader. You must tell Gen5 which com port is used to connect to a reader. (More on
        page 413)

  Serial cable (see samples on page 411)
        Generally, Windows(R)-compatible PCs have two serial com ports, which it assigns as
        Com1 and Com2. If you're uncertain which com port the serial cable is plugged into,
        try Com1 and Test Communication. If you receive an error, try Com2.
        Advanced users can attach additional com ports to a PC, and can use Window's
        Control Panel to identify or modify the com port number.

  USB cable (see samples on page 412)
        For compatible instruments, BioTek ships USB-Driver software along with the USB
        cable. Follow the instructions provided for USB installation, e.g. installing the USB
        Driver software, and review the ComPort Guide to learn how to identify or modify the
        com port number.

  Troubleshooting
        Review the information provided in the Troubleshooting chapter for resolving
        communication errors.






Serial Communication Cables and Ports 9-pin and 25-pint



412 | Chapter 19: Reader Control



USB Communication Cables and Ports







Reader Settings
  System> Reader Configuration> Add/View

        Prerequisite: You must be authorized to make changes to the
         Reader Configuration. If the options are grayed out, contact your
         System Administrator for access rights.

       Special note for Clarity users: Configuration parameters and port
         settings can only be defined through the Clarity PC software.

     Use these controls to tell Gen5 the type of reader, communications port and baud rate
     to use:

      1.       Click the down arrow to select the Reader Type
      2.    Enter number of the Com Port in the text field
      3.    BioTek recommends retaining the default Baud Rate or transmission speed. If
            you have a compelling reason you can select another rate from the list

       Baud rate settings can cause "serial read" errors: when the baud
         rate is set to a non-default setting for Synergy and PowerWaveXS
         readers, Gen5 will be unable to communicate with them if they are
         turned off and then turned on again while Gen5 is running.

      4.    Generally, the Setup option is not needed. Gen5 communicates with the reader
            to obtain the probe sizes and configuration of the filter/wavelengths tables. 0.

 Reader Types
     Gen5 only needs to know the basic model of reader, then Gen5 can communicate with
     the reader to learn its specific capabilities, e.g. Incubation, Dispensing. BioTek
     recommends installing the latest version of basecode for your reader, which is
     generally free-of-charge and easy to obtain and install. Contact BioTek.

 Com Port
     Enter the serial communications port number. When using a USB connection to the
     PC, the Windows(R) operating system sets up a "virtual" Com Port. Follow the
     instructions below:
     All BioTek Readers except the Clarity
      1.    Plug in the USB cable
      2.    For first time set up, Windows recognizes New Hardware, and prompts you to
            install the required driver. Follow the installation directions provided with the
            driver. When the wizard is finished installing the driver, a new "COM port"
            will be available.



414 | Chapter 19: Reader Control



          3.   Go to Control Panel>Administrative Tools>Computer Management>Device
               Manager>Ports(COM & LPT) to see the new virtual Com port assigned to the
               USB.
          4.   Enter this port for the reader. 0.

        Clarity Luminometers
          1.   Connect the Clarity to the PC with the USB cable.
          2.   Launch the Clarity software, and go to Options>Com Port Settings. Select
               USB.
               Once you get this set up initially, you won't have to do it again unless you
               switch to a serial port connection.
          3.   Close the Clarity software and launch Gen5. 0.
               Gen5 will automatically use whatever connection was specified in the Clarity
               software. All connection information is controlled by the Clarity software only.

  Baud Rate
        Make sure the Baud Rate matches the reader's settings. Consult your reader's
        operator's manual for the correct rate. Readers without keypads, Synergy and
        PowerWaveXS, will issue a "serial read" error when it is powered down and then up
        again while Gen5 is running if the baud rate is set to other than the default setting.

  Test Communication
        Use this button when adding or modifying a reader to test the Com Port setting. Gen5
        attempts to communicate with the reader and reports its results in an on-screen
        message.

  Setup
        Generally, the Setup option is not needed. Gen5 communicates with the reader to
        obtain the information it contains. Occasionally, you may want to view or modify:
           Absorbance Wavelengths (next page)
           Fluorescence/Luminescence Filters (on page 416)






Absorbance Wavelengths
  System> Reader Configuration> Add/Modify button> Setup button
     Use the Absorbance Wavelength tab to ensure that Gen5's wavelengths table is aligned
     with the reader's internal table. Depending on the reader, you can specify up to six
     wavelengths to be made available as default selections in the Read Step dialog
     (Protocol>Procedure>Read).
        Get Wavelengths: retrieve wavelength values from the instrument
        Send Wavelengths: download and calibrate wavelength values. Enter the
          desired values in the Wavelength fields and then click Send Wavelengths.
          The values will be downloaded to the instrument, overwriting its existing
          wavelength table.

       Note: To exchange wavelength information between Gen5 and the
         reader, the two must be communicating, i.e. the reader must be
         turned on and correctly configured in Gen5.

     Reader-Specific Information

       Reader Series               Wavelength             Wavelength selection
                                   range

       ELx-Series                  340-900                Filters: Update the reader
                                   depends on specific    when changing filters
                                   model

       uQuant and PowerWave        200-999                Monochromator: selectable
       series                      depends on specific    by 1nm increments
                                   model

       Synergy HT and              200-999                Monochromator: selectable
       Synergy 2/4                                        by 1nm increments


       Note: You must conform to the specific BioTek reader procedures
         when altering the reader's configuration. For filter-based readers, it is
         your responsibility to ensure that the filters are positioned correctly
         and recorded here accurately.

     ELx-Series Filter-Based Readers
     BioTek updates the on-board software with the current configuration of filters before
     shipping the reader to you. Unless you change the filters without updating the on-
     board software, Gen5 will capture the filter-wheel configuration when it initiates
     communication with the reader.
     If you do change the filter-wheel configuration, you can use Gen5 to update the reader:
      1.   Precisely record the wavelength and position of the filters before reinstalling
           the filter wheel



416 | Chapter 19: Reader Control



         2.   In Gen5, select System>Reader Configuration and click the View/Modify
              button
         3.   Click the Setup button, and select the Absorbance tab
         4.   Fill in the Wavelength table to match the filter-wheel configuration
         5.   Click Send Wavelengths. 0.


Fluorescence/Luminescence Filters
     System> Reader Configuration> View/Modify button> Setup button
        Normally, these controls are only needed when you are changing a filter wheel

          The Filter Wheel Library can also update the reader's
            Fluorescence/Luminescence Filters table. See the Filters and Mirrors
            section beginning on page 173.

  To change the current settings and download them to the instrument:
         1.   Select the filter Type using the drop-down list for each Filter position in the
              Excitation and Emission filter wheels.
         2.   When applicable for the filter Type, enter Wavelength and Bandwidth values
              in the fields.

          The Wavelength value and its accompanying Bandwidth, in
            nanometers, are etched into the filters. For example, the
            Wavelength/Bandwidth combination of 485/20 will transmit light from
            475 to 495 nm (10 nm on either side of the center). See the reader's
            operator's manual for details.

         3.   When all values have been entered, click Send Values. The values will be
              downloaded to the instrument, overwriting its existing wavelength table. 0.

  To retrieve filter wheel settings from the instrument:
           Click Get Values. This reports the values in the reader's on-board memory.
             Since the reader does not have the ability to mechanically determine the filter
             configuration, these values may NOT truly represent the current filter wheels.
        Find additional information about changing Filter Wheels and recommended
        configurations in the Filters and Mirrors section beginning on page 173.







Reader Control Panel
   System> Reader Control


         or, click on the reader button in Gen5's toolbar to open the control panel.
   If supported by the current reader, you can use this feature to view information about the
   attached reader, control the reader door or plate carrier, and control incubation.
   The reader must be connected, turned on, and properly communicating with Gen5TM for
   the controls to be enabled. This means the reader must be "ready" not busy reading a plate
   or running a system test, for example.
         Information
         Door/Carrier
         Pre-Heating (below)
         Dispenser (page 418)
         Tungsten Lamp (page 422)

        Detailed information about the Filter Wheel and Mirror tabs is provided
          earlier in this guide.


Pre-Heating Parameters
   System> Reader Control> Pre-Heating

 In the control panel for readers with incubation capability:
         The Set Temperature Procedure defined for the Protocol offers the ability to
           activate Pre-Heating. This screen reflects the parameters defined in the protocol
         To use the reader as incubator in between experiments: enter the temperature
           in the Requested field and then check On to begin pre-heating. Most BioTek
           readers allow a temperature range of 20-50^0C.
         The temperature will rise or fall to the Requested temperature, as appropriate.
           Off disables the incubation unit; the temperature will return to ambient.
         The Actual field reports the current temperature (Celsius) of the incubation
           unit.
             The Total Time field reports the total time elapsed since the On box was
               checked. Associated with the Total Time field, you can use the Beep after
               checkbox to direct Gen5TM to "beep" continuously after the specified
               duration. The clock starts when the incubation unit is turned On.
             The Time Since Reached field reports the total time elapsed since the
               incubation temperature reached the Requested temperature. Associated



418 | Chapter 19: Reader Control



                  with the Time Since Reached field, use the Beep after checkbox and field to
                  tell Gen5 to "beep" continuously after a specified duration. The clock starts
                  when the incubation temperature reaches the Requested temperature.
           Temperature Reached is displayed when the incubation temperature reaches
             the Requested temperature.

          Note: As the temperature of the incubation unit approaches the
            Requested temperature, it may take a few minutes to settle within an
            acceptable tolerance (+/- 0.5^0 C). During this settling period, the
            Temperature Reached indication may appear for a few seconds,
            disappear, then reappear moments later. The Time Since Reached field
            will automatically reset to 00:00:00 each time the indication appears.
            If the Beep after checkbox associated with Time since reached field is
            enabled and set to, for example, 10 minutes, Gen5 will "beep" 10
            minutes after the incubation temperature has consistently settled
            within +/- 0.5^0 C of the Requested temperature.


Dispenser Settings
     System> Reader Configuration> Add/Modify button> Setup button

          Read Only: for everyone except BioTek qualified technicians, these
            controls provide information, they do not let you alter it.



          Use the Reader Control Panel to position the dispensers for performing
        maintenance.


  Calibration Volumes
        Gen5 shows the minor differences between the expected (Target) dispensing volumes
        and the actual (Measured) volumes, as determined at the BioTek factory.
           Click Get Values. Actual measured values will be uploaded from the reader's
             current internal tables.

  Injector Position
        Gen5 shows the current position of the injector, if applicable to the reader.
           Next to Top Probe
           Above Bottom Probe

        Also see: Special filter position requirements for the Synergy HTTR w/Injectors on
        page Error! Bookmark not defined..






Dispenser Control and Maintenance
   System> Reader Control> Dispenser




      In the control panel for readers with dispensing or injection capability:

          Dispenser: up to two dispensers may be attached to the reader, use the drop-down
      list to select the one you want to control or review information about.

 Dispenser Information
   The fields on the left side of the screen display the current state of the selected dispenser:
              Connected: the reader detects a live connection (Yes) via serial cables with
                the dispenser module. "No" indicates a faulty connection. Check the
                cabling.
              Initialized: Prior to performing a dispense step the dispenser module must
                be initialized. Click the Initialize button if this status reports "No."
              Primed: Prior to performing a dispense step the dispenser must be primed.
                Place the priming plate on the carrier and click the Prime button if this
                status reports "No."
              Injector position: Gen5 reports the position of the injector in relation to the
                reader's probe

 Dispenser Routines
                         Ensure normal and correct communication between the
                         dispenser module and reader

                         Prime the tubing with fluid



420 | Chapter 19: Reader Control



                          Remove and recover fluid from the tubing

                          Move the dispenser's syringe pump into maintenance
                          position for installation or replacement

          When defining a Dispense Step in the Procedure you can also define
            Tip Priming


Priming the Dispenser
        This routine is only applicable for Readers with Injectors. Refer to your reader's
        Operator's Manual for specific and more detailed maintenance guidelines.
        Priming the tubing with reagent (dispensing fluid) is an important first step when
        running an experiment. Likewise, flushing the tubing of reagent after each use is an
        important maintenance step. The priming routine is used for both steps.

          When dispensing volumes less than or equal to 20 ul/well, we
            recommend specifying a tip prime volume that is equal to the dispense
            volume. For dispense volumes greater than 20 ul/well, we recommend
            a tip prime volume of 20 ul.

  To prime the dispenser:
         1.   Fill the supply bottle(s) with the dispensing fluid when running an experiment
              or with deionized or distilled water when performing maintenance. Insert the
              supply (inlet) tubes into the bottles.
         2.   Place the priming plate on the carrier.
         3.   Select System> Reader Control> Dispenser
         4.   Set Dispenser to 1
         5.   Set the Volume to at least:
               1000 ul for pre-experiment priming
               5000 ul for maintenance
         6.   Set the dispense Rate (BioTek recommends 275 for priming)
         7.   Click Prime to start the process.
              When the process is complete, carefully remove the priming plate from the
              carrier and empty it.
         8.   Repeat the process for Dispenser 2, if applicable.0.


            Maintaining the Tubing: Leave DI water in the system overnight or until the
        instrument will be used again. Purge the fluid from the system and then prime with
        the dispense reagent before running an assay.






Purging the Dispenser
       This routine is only applicable for Readers with Injectors. Refer to your reader's
       Operator's Manual for specific and more detailed maintenance guidelines.
       Purging the dispenser is an important part of the recommended daily maintenance
       routine. Gen5's purging capability can also be used to recover and preserve expensive
       reagents.

  To purge the dispenser of fluid:
        1.   Remove the inlet tubes from the supply bottles.
        2.   Select System> Reader Control> Dispenser
        3.   Select the Dispenser number: 1 or 2
        4.   Set the Volume (2000ul guarantees all fluid in the system's tubing is removed).
        5.   Click Purge to start the process.
        6.   When the purge is complete, repeat the process for the other Dispenser, if
             applicable. 0.

         After purging the system, you may wish to run a quick Dispense-
           Only experiment to visually verify the dispense accuracy.


Dispenser Prime/Purge Rate
       The allowable volume ranges for each dispense rate are:

             Rate (ul/sec) Volume Range (ul)

             225                5-5000

             250                15-5000

             275                25-5000

             300                30-5000

       BioTek recommends using the default rate of 275 for priming.



422 | Chapter 19: Reader Control




Tungsten Lamp Control
     System> Reader Control > Tungsten Lamp



        Use this control to turn off the Tungsten Lamp when it is not needed. Follow the menu
        path shown above to access the controls. Note: when the tungsten lamp is not required
        in a Procedure, Gen5 turns off the lamp.
        Conversely, you can use the Turn Lamp On button. The lamp takes approximately
        180 seconds to warm up before measurements can be taken. When the lamp is not
        warmed up before a reading is requested Gen5 displays a message that counts down
        this warm up period before prompting you to put the plate on the carrier.







Testing the Reader
    Gen5TM provides the following options for testing the reader:
           Run a System Test
           If you've purchased BioTek's Gen5 Reader Diagnostics Utility:
                  Run the Absorbance Test Plate


 Reader System Test
    System> Diagnostics> Run System Test

          The System Test for the ClarityTM Microplate Luminometer must be
            performed using the Clarity PC software. Refer to the Clarity
            Operator's Manual for instructions.

Run the Test
      Most BioTek readers perform a self test every time they're turned on, but when you
      want to view and/or print the results of a system (aka optics) test:
         1.   Select System> Diagnostics>Run System Test
         2.   When there is more than one reader attached to the PC, select the desired
              reader and click OK
         3.   When the test is completed: 0.
                   1.   Fill in the text fields, User, Company, Comments, to be included in
                        the report of the test results. Then, click OK.
                   2.   Print the report to retain a hard copy for your records
                   3.   Save As to convert the results to a text file. This is especially useful
                        when troubleshooting a reader. You can email the text file to BioTek
                        TAC. 0

Test History
        Gen5 keeps the results of System Tests when they are performed using the menu
        controls. To review or print them, select System> Diagnostics> History...



424 | Chapter 19: Reader Control



 System Test Results
     System> Diagnostics> History
          Immediately after running a system test on the reader, Gen5 displays the results, and
          then stores them in History (in the shared database).

  Print
     Click Print to generate a paper version of the results.

  Save As
     Click Save As to convert the results to a text file. This is especially useful when
     troubleshooting a reader. You can email the text file to BioTek TAC.
             Gen5 opens the standard Windows(R) file save dialog, and sets the file type to .txt
               Text files are the default format for Notepad(R) and is recognized by most word
               processing programs.
             Optionally, click in the File Name field to modify the default name:
               SystemTest. Add the date, instrument name, or other information to ensure the
               file has a distinguishable name.
             Use the drop-down list and other tools to navigate to the Save In location


 Reader Test History
     System> Diagnostics> History
     Gen5TM keeps this database of test results from System (formerly-called Optics) Tests and
     Diagnostic Tests, if applicable. It is stored in Gen5's shared database.
             Double-click the desired test to open it on screen and to print it or save it as a
               text file

  Use the options in the Test History dialog to:

                   Click the Refresh button to capture any tests that were conducted since
                 the dialog has been opened

                  Use the drop-down lists in the Selection area to filter the list of tests shown
                 by reader (Device) and user (Operator), if applicable
             Column Headers can be used to sort the tests: click on a header to sort the files
               in ascending/descending order by that category. For example, click Status to
               sort the files by Pass/Fail. Click the same column header to reverse the order
             Highlight a test and click:
                  View: to open it for viewing, printing, saving as a text file
                  Delete: to delete it, erase it from the database.
