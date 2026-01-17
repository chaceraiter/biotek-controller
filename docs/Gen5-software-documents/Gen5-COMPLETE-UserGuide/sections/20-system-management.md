# Chapter 20: System Management

     This chapter supplements the Getting Started Guide shipped with
     the Gen5 product CD, which you should consult first for installation
     and intial set up instructions.


 System Requirements .............................................................. 426
 Gen5's System Administrator .................................................... 427
 Changing your password (Gen5 Secure) ..................................... 428
 Changing your Startup Preferences ............................................ 429
 Customizing the Toolbar ........................................................... 430
 Plate Type Database................................................................. 431



426 | System Management




System Requirements
       Before installing Gen5TM make sure your hardware meets the minimum requirements.

Computer Requirements
       For Gen5 to run successfully, the computer must meet the following requirements:
             Windows XP or Windows 2000 (Professional Editions)
             Pentium III-Class PC (or compatible) processor (500 MHz or higher)
             512 MB RAM or higher
             2 GB Hard Drive space or higher
             Designed for XGA Resolution at 1024 x 768 or higher
             CD-ROM Readable Drive
             Keyboard & Mouse
             Microsoft Internet Explorer v 5.0 or higher (for online Help)
             Serial or USB port for BioTek instrument

Reader Requirements
       Verify that the Base Code and Assay Code built into your BioTek reader is compatible
       with Gen5. BioTek has validated the following list of base codes. Any instrument with
       the base codes listed below or higher is compatible with Gen5.

         If your instrument has a base code with a version lower than these
           please contact TAC to download and install updated software


            Instrument          Base Code

            Powerwave           1.21.1

            PowerwaveXS         1.06

            Synergy 4           1.03
            Synergy 2           1.03

            Synergy HT          2.24

            FLx800              1.15

            ELx800              3.07

            ELx808              3.15

            uQuant              2.02







Gen5's System Administrator
   For all levels of Gen5 except Gen5 Secure
     It is necessary to login as the System Administrator to change User Permissions and
     Database Configuration, and to access any features which are denied as Users
     Permissions

 How to change the System Administrator's password:

       This function is only available to the System Administrator. You
         must login, System> Administrator LogIn, as the Administrator to
         access these controls

      1.   Select System> User Setup, and select the Administrator tab
      2.   Enter the current password in the Current Password field. Gen5 ships with the
           password set to "admin."
      3.   Enter the new password in both the New and Confirm password fields
      4.   Click OK. 0.

 How to maintain Users Permissions:
     Except in Gen5 Secure, access to Gen5's functions, like reading a plate, modifying a
     protocol, and masking values, is defined equally for all users except the System
     Administrator, who has all "permissions."



428 | System Management




Changing Your Password

         For Gen5TM Secure Only

    System> Security> Users
       Users other than the System Administrator are limited to changing their own login
       password.

How to change your password:
        1.   Select System> Security> Users
        2.   Identify and open your user account: highlight and click Edit (or double click)
        3.   Enter your current password in the Current Password field
        4.   Enter your new password in both the New and Confirm password fields
        5.   Click OK. 0.
       The password will take effect the next time you log into Gen5.

         Contact your System Administrator if you've forgotten your password.
           He/she can change your password without knowing the current one.






Changing Your Startup Preferences

        For all levels of Gen5 except Gen5 Secure

   System> User Setup

How to change your startup preferences:
       1.   Select System> User Setup

       2.      Use the drop-down to select the preferred method for Startup Action:
             Display Welcome dialog is the default setting, it opens Gen5 with a screen
               that offers several common tasks including creating a new item or opening
               a recently used item
             Create new experiment opens Gen5 with the Protocol selection dialog
               open, as if the user had selected File>New Experiment
             Start at system menu opens Gen5 showing the File, System and Help
               menus only. Since neither a protocol nor experiment is open, the workspace
               is blank.

       3.     Use the 3-dot button to change your Protocol and Experiment Folders:
            browse to the full path and directory to define the folder where you will
            typically store protocol and experiment files. Gen5 will point to these folders
            when you save and open a protocol or experiment.
       4.   Click OK. 0.
      The changes will take effect the next time you log into Gen5.

        Contact your System Administrator if you need assistance.



430 | System Management




Customize the Toolbar




    Double click the toolbar, anywhere without a button, to open the Customize Toolbar
    tool or select System> Preferences> Customize Toolbar
          Gen5 has two toolbars, Protocol and Experiment. Set the current state to
            correspond to the toolbar you want to customize: select either File>New
            Protocol or File>New Experiment, accordingly

          You can remove unused buttons. Add favorite buttons. Insert separators
            between buttons to make them easier to distinguish.
          The Customize Toolbar dialog opens with the Current Toolbar Buttons
            displayed in the box on the right and any unused buttons and the separator in
            the box on the left. The Separator is always available and there is no limitation
            on its use.

To remove buttons from the toolbar:
        1.   Highlight the button you want to remove from the toolbar in the Current
             toolbar buttons box on the right
        2.   Click Remove
             The button is moved into the Available toolbar buttons box and removed from
             the toolbar when you click Close. 0.

To add buttons to the toolbar:
        1.   Highlight the button you want to add to the toolbar in the Available toolbar
             buttons box on the left
        2.   In the Current toolbar buttons box, highlight the button or Separator before
             which you want to place the button
        3.   Click Add
             The button is moved into the Current toolbar buttons box and added to the
             toolbar when you click Close.0.

                 Use the Reset button to restore the toolbar to its default configuration.


          To rearrange the buttons on the toolbar, first remove them and then add them in
       the desired location


         The toolbar configuration corresponds to the user logged into
           Windows(R) at the time it is customized.






Plate Types Database
   System> Plate Types

About the Plate Types Database
             All of the default and custom plate types currently stored in the database are
             listed. When a reading is initiated, Gen5 sends the appropriate plate-type details
             to the reader. The reader uses this information to precisely position the plate
             when taking measurements. Most readers support only the Default Plate Types:
             click the button to view this list. Consult your reader's operator's manual for a list
             of supported plate sizes.
             Gen5TM comes with details for more than forty industry-standard microplates. If
             your reader supports custom plates, you can add your own microplates by
             selecting Add, or Import them from a previous version of Gen5 or KC4.

Plate Types Database Tools:

                             Click the Default Plate Types button to view the list and
             dimension details of the plate types supported by all BioTek readers
         Double click a plate type in the Default or Custom lists to review its
           dimensions, such as width, length, height, and the number of rows and
           columns. Or highlight the plate and click View

        Important: Only BioTek's Synergy and PowerWaveXS readers support
          Custom Plate Types.

         Add: to add a new plate type to the database. Take and record careful
           measurements of its size before creating the new record.
         View/Modify: to change or update the details of a plate.

        Warning! Modifying the dimensions of the installed plate types is not
          recommended; consider adding a new plate type instead. Please
          contact BioTek with any questions regarding the current dimensions.

         Export and Import: to transfer custom plate types from KC4 or to and from
           another Gen5 system. Learn more... Since the Plate Type Database is stored in
           Gen5's SharedDB:
              you do not need to use the Export-Import tools to archive or backup the
                database
              when the SharedDB resides on a network, all users connected to the
                SharedDB reference the same Plate Types Database, so you do not need to
                transfer custom plate types between system users
         Click Delete to remove a selected plate type from the database.



432 | System Management



Plate Type Measurements




    When creating or updating plate dimensions, taking precise measurements is essential.
    Use calipers with precision to 0.01 millimeters (mm) to gather the following
    measurements. A standard ruler is not precise enough. Note: when entering values based
    in 10 micron increments, values always end in 0 (zero).

         Important! Dimension values are used by the software to calculate
           reading positions. Any inaccuracies in these dimensions could
           significantly affect your results.

Dimensions
          Number of Columns is the number of vertical columns of wells when viewing
            the plate in its normal orientation. There are 12 in a 96-well plate.
          Number of Rows is the number of horizontal rows of wells when viewing the
            plate in its normal orientation. There are 8 in a 96-well plate.
          Length is the longest dimension of the plasticware (the x axis).
          Width is the shorter dimension of the plasticware (the y axis).





         Height is the distance from the bottom mounting surface of the plate to the top
           face of the plate.
         Well Diameter is the diameter of any well.
         Top Left X is the distance from the left side of the plate to the center of well A1.
         Top Left Y is the distance from the top of the plate to the center of well A1.
         Bottom Right X is the distance from the left side of the plate to the center of the
           last well on the plate. In a 96-well plate, this is H12.
         Bottom Right Y is the distance from the top of the plate to the center of the last
           well on the plate. In a 96-well plate, this is H12.



Import and Export Plate Types
   System> Plate Types
      Gen5 provides the Export and Import feature to transfer custom plate types from KC4
      or to and from another Gen5 system. It may be necessary, for example, to import a
      custom plate type associated with a Gen5 protocol you've received from BioTek or
      another Gen5 system user.
      The Import routine examines the plates in the import file and compares them to the
      current plate type files. New plate types are added to the database. Existing plate types
      with new dimensions will replace the existing dimensions after user confirmation.
      Existing plates with identical dimensions are ignored. Gen5 Secure logs the event in
      the System Audit Trail.

  How to Import Plate Types
      When you have one or more custom plate types exported from KC4 or Gen5 (and
      therefore in the proper file format):
       1.   Click Import. Gen5 opens the standard Windows(R) browse dialog.
       2.   Locate the plate type file and click Open.
            Gen5, by default, looks for files with the .ptf extension, but, it will accept a file
            with any extension, as long as the data is correctly formatted. Change the Files
            of type: using the drop-down list to see all file types. 0.

  How to Export Plate Types
      When you want to export one or more custom plate types:
       1.   Highlight the files in the Custom Plate Types box. Hold the Ctrl key to select
            multiple files.
       2.   Click Export. Gen5 opens the standard Windows(R) Save As dialog.
       3.   Browse to the storage location for the files, enter a File name and click Save.
            Gen5, by default, assigns the .ptf extension to the file, but you can change it, if
            desired, by typing a different filename extension. 0.



434 | System Management
