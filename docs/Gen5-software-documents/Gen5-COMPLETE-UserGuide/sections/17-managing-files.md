# Chapter 17: Managing Files

     This chapter offers instructions and suggestions for managing your
     Gen5 experiment and protocol files, with a focus on Gen5's
     database. Methods for recovering from Database Errors are
     provided.


 Managing Files......................................................................... 370
 File Storage............................................................................. 371
 Database Management ............................................................. 372
 Database Errors....................................................................... 379



370 | Chapter 17: Managing Files




Managing Files
     Gen5 offers two methods for storing its protocol (.prt) and experiment (.xpt) files. You can
     use a secure database called SharedDB (and its companion LocalDB) provided by Gen5 or
     you can use the Windows(R) File System. Both options let you set up Gen5 files to be shared
     by multiple users. Conversely, you can prohibit file sharing by only installing Gen5 locally,
     on an individual's PC.
     The SharedDB ships with Gen5, and for all software levels, it contains security information
     and the Plate Types Database. Except for Gen5 Secure, the File Storage option must be
     changed to use the database for storing .prt and .xpt files.
     Gen5 Secure is intended to be used with the SharedDB, it is a major component of making
     it "secure." In Gen5 Secure the SharedDB contains user accounts and a System audit trail,
     in addition to the security information and the Plate Type database, and it is set up by
     default to store .xpt and .prt files and their associated audit trails.

How to manage files
     Gen5 provides Database Management tools when its Shared database (SharedDB) is used
     for file storage. The SharedDB can be moved to a shared, network directory, where all
     required users can access it. When the Windows file system is used for file storage, you
     manage files using Windows Explorer. In addition to storing the files online, files can be
     stored on CD or diskette.







File Storage
   System> Preferences> File Storage Mode
      Use this control to select a method for storing protocol and experiment files.

         Attention Gen5 Secure users: To ensure 21 CFR Part 11 compliance
           retain the setting to use the Gen5 Database

About File Storage
      Gen5 provides two methods for storing protocol and experiment files. You can use the
      secure, shared-access database provided with Gen5, which is required for compliance
      with the FDA's 21 CFR Part 11 regulation on electronic records submission.
      Alternatively, you can use the file system provided with the Windows(R) operating
      system on a local computer or network (LAN). If your organization is unconcerned
      with FDA regulations, the choice is a matter of preference. However, one advantage to
      using the Gen5 Database is its ability to recover from a system crash. New and
      modified files are saved as Temporary Files in the database and can be used to recover
      information that wasn't saved before a system failure.

         ClarityTM Luminometer protocol files, with a .bpf extension, cannot be
           stored in Gen5's shared database. They are typically stored in the
           C:\Program Files\BioTek\Clarity\protocols folder.

How to
         Select an option for storing Experiment and Protocol files:
          Gen5 Database: all actions related to managing and maintaining files, like
            File>Open, File>Save, Browse..., and so on, will occur in Gen5's SharedDB.
          Windows File System: Gen5 will not control the management of files. Actions
            related to managing and manipulating files will be determined by the
            Windows operating system, e.g. you can use Windows(R) Explorer. Generally
            during file management activities like File>Open, Windows begins at the last
            directory and folder used.

         AutoSave Feature: Gen5 offers this feature to give you additional
           control over the storage of saved files.



372 | Chapter 17: Managing Files




Database Management

 Organize Your Database Files

           During regular installation, Gen5 Secure installs and enables the
             shared database to store experiment and protocol files. All other
             levels of Gen5 must elect to use the database at System>
             Preferences> File Storage

        All of your file management requirements can be fulfilled using Gen5's secure
        databases. You'll be most satisfied with the final structure if you spend some time
        planning it up-front. In a multiple-user environment, you can set up Gen5's database
        on a shared-network drive (LAN) so multiple users can access the same protocol and
        experiment files, including the Default Protocol.
        Multiple Databases: You can create multiple copies of the clean, installed SharedDB,
        renaming them with meaningful titles for use by various projects or teams or
        researchers. Within each database you can set up a consistent file structure, e.g. specific
        folders for specific types of Protocols and Experiments, or a different folder for each
        user. The possibilities are endless.
        Backups: Performing backups on a regular schedule is highly recommended to
        preserve your data. And, Gen5 provides a tool to schedule backups to occur
        periodically. See below.

 File Management Recommendations
            Put a copy of the SharedDB on a shared-network drive where all your Gen5
              users can access it. Be sure to set each user's Database Configuration to point to
              the correct location.
            Before moving the SharedDB to a network location, make a copy of it to use as
              a template for future use:
         1.   In the default SharedDB folder, highlight the original, right-click and select Copy
         2.   De-select the original (click elsewhere in the dialog), right-click and select Paste
         3.   Highlight the copy, right-click and select Rename
         4.   Give the copy a unique name, like SharedDB_original.mdb0.




            Consider setting up shared databases for different projects or teams within
              your organization. You can follow the steps defined above to create multiple
              databases in the same folder (or directory), or you can move the unique
              databases to a different network location/folder. Use Database Configuration
              to point user's Gen5 sessions to the correct database.






       Regularly archive and backup the database to preserve your records. There are
         numerous ways to do this, so BioTek recommends following your
         organization's existing policy for securing data. For example, if you put the
         shared database on the network and your network is backed up every night,
         this may be sufficient. You can use Gen5's Optimize and Backup Settings to
         facilitate your data-protection policy.
       Consider using Gen5's automatic Save feature to create a new, date-stamped
         folder for storing experiment records. This is an especially good practice for
         large labs with multiple users who run hundreds of plates per day. Gen5 will
         keep all that data organized by date. Define this kind of file management
         setting in the Default Protocol so it will apply to all newly-created protocols
         (System>Preferences>Default Protocol>Protocol Options>Save).
       Gen5 handles multiple, simultaneous users performing database management
         tasks by giving precedence to the user with the greater administrative rights.


About Gen5 Databases
    All levels of Gen5 install two databases during regular installation: SharedDB and
    LocalDB. Only Gen5 Secure is initially set up to use the Gen5 Database for experiment
    and protocol file storage. All other levels of Gen5 must elect to use the database to
    store experiment and protocol files at System> Preferences> File Storage
       SharedDB can be set up on a network for sharing information amongst
         multiple users. It contains all protocol and experiment data files and their
         associated audit trails, the plate types, and reader-diagnostic history data. In
         Gen5 Secure, SharedDB also contains security settings, user accounts, and a
         system audit trail for shared events. This database can be moved, renamed, and
         copied. So, if desired, you can create a unique database for individual projects,
         teams, or other classification.
       LocalDB contains the local setup information, including the Reader
         Configuration. For Gen5 Secure, this database also contains an audit trail for
         local events. LocalDB is stored on the computer's hard drive, and it cannot be
         moved or renamed.
       Default database location: During normal installation, Gen5 installs its
         databases:
              Windows XP and 2000 systems: C:\Documents and Settings\All
                Users\Application Data\BioTek Instruments\Gen5 (software
                edition)\(version #)\SharedDB or LocalDB
              Windows Vista: Windows XP and 2000 operating systems: C:\Program
                Data\BioTek \Gen5 (software edition)\(version #)\SharedDB or LocalDB

      You may need to change your operating system settings to view the
        Application Data folder. In Windows(R) Explorer, select Tools>Folder
        Options>View and make sure it is set to "Show hidden files and
        folders."



374 | Chapter 17: Managing Files



            Max Size: the maximum size of the database files is 2 gigabytes (Gb). At
              startup, Gen5 checks the remaining size of the database. Warning messages are
              displayed when the database size exceeds 1536Mb. Use Gen5's maintenance
              and backup features to archive your database records.
            Gen5 has built-in error recovery modes, when your connection to the database
              is lost for any reason, Gen5 saves any unsaved files as Temporary Files. After a
              system failure, the next time you open an affected protocol or experiment file,
              Gen5 offers to replace the unsaved files with the Temporary Files. Say Yes to
              recover any changes made to the files before the system failure, say No to open
              the files as they were last saved, before the unsaved changes were made.
              Newly-created files are saved as Temporary Files, also. Following a system
              failure, you can rename these temporary files with the proper filename
              extension (.xpt or .prt) using Gen5's Maintain Files controls.
            File locking: When a file is opened in Gen5 it is "locked" to protect it from
              being modified (saved or renamed) by a different user. When a second user
              attempts to open the file, they will receive a message stating: "File <filename>
              is already in use. Do you want to open it in read-only mode?"
            Gen5 offers automatic backup: you can define settings for regularly and
              automatically backing up and optimizing databases with Gen5's Auto-
              Optimize feature.


 Database Configuration
     System> Database Configuration

  Prerequisite
        Some features of this dialog require System Administrator privileges. Contact your
        System Administrator if you are unable to perform actions as expected.


        When Gen5 is installed, there are two primary databases, a shared and a local
        database. They are named SharedDB.mdb and LocalDB.mdb respectively. The
        LocalDB cannot be moved or renamed. The SharedDB can be moved and renamed. All
        operations affecting them take place using their respective tabs, except the upgrade
        utility.

  Troubleshooting
        When launched, Gen5 attempts to connect to the Gen5 databases. Review this
        information if errors occur: Database Errors (page 379)

                         Gen5 presents the Reset Connection button only when it detects an
        error that can be repaired by its functionality. Click it, several times if needed, until it is
        grayed-out. Review the Database Errors information if the button doesn't fix the error.






Source

           Gen5 displays the current location of the database.
           LocalDB: You cannot move or rename the LocalDB database, thus the 3-dot
             button is disabled. If necessary to see the full pathname of its location, you can
             click inside the text field and scroll to the right.
           SharedDB: Click the 3-dot button to view the current location of the database.
             You can move, rename or copy the SharedDB database. Learn how in the
             Getting Started Guide shipped with the product CD.

Test

                        Use the Test button to check the connection to the Gen5 database.
           Potential error messages are referenced in the Troubleshooting section above.

Stats

                        Use the Stats button to assess the number of files and amount of
        space used in the Gen5 database.
           Generally, the most important information is Size: reported as used/available.
             If the used value is nearing the available value, it's time to move some files. Use
             the DB maintenance tools to archive files not currently being used.
           Occasionally using the Optimize option (described below) helps keep the DB in
             good shape.

Optimize

                     Click the Optimize button to engage Gen5's corruption-repair and size-
        compacting functions. Learn more in Gen5's Help.
           Periodically Optimize and Backup: to direct Gen5 to automatically backup and
        optimize the database on a regular basis. Select the option and define its settings. Use
        the 3-dot button to modify the settings. (See page 377)

Upgrade

                        There are two uses for the Database Upgrade Utility:
               install an updated version of the software
               install a higher level of software, e.g. upgrade Gen5 to Gen5 Secure



376 | Chapter 17: Managing Files



Maintaining Files
     System> Maintain Files
         Use this dialog as you would Windows(R) Explorer to manage your Protocol (.prt) and
         Experiment (.xpt) files. Gen5 Secure tracks activities, like creating, moving, and
         deleting files, in its System Audit Trail.




                                    Important: the DB (database) this dialog opens is
         controlled by Database Configuration. It is the SharedDB defined as Source.

Tools:

                       Toggle the view between Details and Icons of the files and folders. In
                Details view, click on a column header to set the sort order. For example, click
                Type to organize the files by file type, or click Modified (once or twice) to sort
                them in the desired ascending or descending date order.

                  Create a new folder to save certain files separately

                  Refresh or update the view to show files or folders added by another user

                  Move up one folder/directory level with this button




                                  Right-click menu: highlight one or more items (folders or
                files) and right click for a pop-up menu. Notice the Hidden option: system
                administrators can hide/reveal selected files to prevent other system users
                from accessing them. Warning for Windows XP users...
            Ctrl+C to copy, Ctrl+V to paste, and the Delete key are also supported

                  Highlight a file or folder and Delete it with this button. You must delete
                sub-folders (i.e. folders within a folder) before you can delete their parent or
                higher-level folder


                                               Column Headers can be used to sort the files:
                click on a header to sort the files in ascending/descending order by that
                category. For example, click Modified to sort the files by "last modified" date.
                Click the same column header to reverse the order.






Tasks:
         Find step-by-step instructions for performing these tasks in Gen5's Help:
            Organize your files
            Copy to CD, diskette or other portable media
            Export a file
            Import a file
            Reduce the database size


Optimize and Backup Database
   System> Database Configuration


Optimize Now

                      Click the Optimize button to run Gen5's database compacting and
         backup program.


            Before "optimizing" the database, close all protocol or experiment files.


  When to do it:
            After restoring database connections following an error
            After exporting and deleting records to reduce the database size (Maintaining
              Files)
            After system audit trail events are exported or deleted

           Gen5 creates a backup copy of the database (in its present location
             unless a different storage location was selected in the Optimize
             Periodically settings) before beginning optimization. It is named:
             <original filename>_yymmdd_hhmmss.mdb (year, month, day_hour,
             minute, second). .mdb is the filename extension. Backup files can be
             used to repair Gen5 when the current database file is corrupt, for
             example.



378 | Chapter 17: Managing Files



Periodic Optimization


                                           Use this option to schedule Gen5 to conduct
        Optimization on a regular basis. BioTek suggests once per week.

        Use these controls to define the rules for regular, automatic database optimization.

           Important: Only use this automatic method for backing up files when
             you're saving them to a network or external drive. Do not use it to
             save a backup to the same (local) hard drive used to store the original
             database. Manually backup your database if you are limited to one
             hard drive/PC, unconnected to a network.

How it works:
        Whenever Gen5 is launched it checks the contents of the backup location to determine
        if optimization is due. When it is, Gen5:
         1.   Renames and moves a copy of the current database to the Backup location. The
              naming convention is:
              Auto_Backup_<original filename>_yymmdd_hhmmss.mdb.
         2.   Executes the repair and compact operations on the current database
         3.   As needed, it deletes the oldest archived (or previously backed-up) database
              file to correspond to the current settings
         4.   Gen5 displays a status gauge on screen to tell users the operation is underway
              0.

How to define the settings:
         1.   Set the number of days to run the optimization in the Optimize every _ days
              field

         2.      Backup: you can retain Gen5's default location for storing a backup copy of
              the database, or click the 3-dot button and select an alternative location.
         3.   Define the number of previously backed-up or archived database files to keep
              in the backup location in the Keep _ last archived databases field0.







Database Errors
          Certain conditions can cause database-related errors:
             The database file is not available. Potential causes: the shared database is on a
               network and the cable is unplugged, or the file is locked by another user
             The database file is corrupt. Potential cause: an incomplete write operation
               occurred because Gen5 was closed unexpectedly due to a power outage or
               hardware problem
             Verification of the database capacity failed. Potential cause: the maximum
               size of the database (2 gigabytes) has been exceeded
             File importation failure. Potential causes: the filename extension is wrong, a
               protocol file was misnamed with an .xpt filename extension instead of .prt

Fixing the errors
           1.    First, make sure non-Gen5-system issues are resolved, for example:
                  network cables are plugged in and the network is up and running;
                  another Gen5 user is not currently performing database maintenance
                    routines;
                  the Database Configuration for both the SharedDB and LocalDB databases
                    point to the expected locations;
           2.    Then, follow these instructions for fixing the errors:
                  Fixing a Database Connection Error (page 379)
                  Fixing a Corrupted File Error (page 380)
                  Fixing a Database Capacity Error (page 381)
                  Fixing a File Importation Error (page 381)
           3.    If the above solutions do not work, try Restoring an archived database (page
                 382). 0.


Fixing a Database Connection Error
                Connection to SharedDB failed.
            This type of error is most commonly caused by a network timeout or
            disconnection, or corruption to the SharedDB file residing on a network.

To fix:
           1.    Make sure you are properly connected to your network, if applicable, i.e.
                 cables/wires installed and the network server is live.



380 | Chapter 17: Managing Files



         2.     Click Reset Connection at the Database Configuration screen.
                Gen5 immediately opens the Database Configuration screen after displaying
                the error message. Otherwise, select System> Database Configuration

           Important: Click the Reset button several times, if needed, until it is
             grayed out.

           Quit: If Gen5 cannot restore the network connection, usually because
             of external factors, e.g. the network is down, when you click Quit at a
             secondary error message, Gen5 will save any currently opened and
             modified files to the Windows Temp directory. When the database is
             restored you can import the files from the Temp folder to the
             database.

         3.     When the database connection has been repaired, click Optimize.

If Reset button fails:
        If your network is performing as expected, and you've checked the cabling from your
        PC to the network, and the Reset button fails to re-establish a connection with the
        shared database:
         1.     Reboot your PC
        If the same message is displayed:
         2.     Restore a previous version of the database or contact your System
                Administrator to inspect and repair your system connection.


Fixing a Corrupted File Error
              Database file is corrupt
           There are two potential ways to fix a corruption error:
            Reboot your PC to try to clear the error by restarting the system.
            Install an archived version of the LocalDB.mdb: use Windows(R) Explorer to
              locate and restore a backup of the database.

           Windows(R) Explorer provides an option to hide certain folders from
             view, if you cannot find the Application Data folder (C:\Documents
             and Settings\All Users\Application Data) it is probably hidden. In
             Explorer, select Tools>Folder Options>View and enable Show hidden
             files and folders

                If these options fail to repair Gen5's behavior, contact BioTek TAC.






Fixing a Database Capacity Error
      When the cumulative size of the files in your database nears or exceeds its capacity (2
      gigabytes) Gen5 displays an error message or warning. You must reduce the size of the
      database. There are numerous ways to accomplish this, the least invasive method, to
      remove files, is described here.

Prerequisite
      This function is only available to the System Administrator. You must login,
      System>Administrator Login, as the Administrator to access these controls.

        Optimize the database before proceeding to see if Gen5 can compact
          the database sufficiently to comply with its size limits. Select
          System>Database Configuration>Optimize. When the process is
          finished click the Stats... button to check the current size.

To reduce the size of your database:
       1.     Select System> Maintain Files
       2.     Highlight multiple database records: hold down the Ctrl key while selecting
              records
       3.     Right click and select Export to Disk from the pop-up menu
       4.     Select a folder (using the standard Windows dialog) where you want to save or
              archive the Gen5 records

       5.        Back in the Maintain Files dialog, highlight the same records, and click the
              Delete button (or right click and select Delete)
       6.     Finally, Optimize the database to ensure it's running in top form.


Fixing a File Importation Error
            File importation failure

            The requested file may be a Protocol file

            The requested file may be an Experiment file
      Gen5 tests the file's format when you perform certain operations like importing a file
      and File>Open. One of these error messages may be displayed when an
      incompatibility is found.

Change the filename extension to fix these errors
       1.     Locate the offending file: depending on the current File Storage mode:
               using the Gen5 Database, select System> Maintain Files
               using the Windows File System, use Windows(R) Explorer



382 | Chapter 17: Managing Files



         2.   Highlight the file, right click and select Rename:
               change the filename extension for a misnamed Protocol file from .xpt to .prt
               change the filename extension for a misnamed Experiment file from .prt to
                 .xpt
         3.   Retry the desired action, e.g. open the file, import the file


Restore an archived database
     When Gen5's error recovery processes cannot resolve database errors, a final-resort
     solution is to replace the current database file with an archived or backup copy of it.
     Ideally, you or your System Administrator has regularly (or at least recently) backed up or
     archived the database. Gen5's Optimize tools can perform backups regularly, for instance.


         Check the Auto-Optimize Settings, if they were defined, to determine the location of
     the last-saved backup file.


How to
         1.   Using Windows(R) Explorer, locate the last-saved archived or backed-up
              database file.
         2.   Copy and Paste it to the desired location. Rename the database file, too. (All of
              these commands are available from the right-click menu.)
         3.   In Gen5, select System> Database Configuration
         4.   Select the SharedDB tab

         5.      Next to the Source field, click the 3-dot button and browse to the location
              selected in Step 2.
         6.   Click OK. 0.
