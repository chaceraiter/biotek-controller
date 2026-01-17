# Chapter 1: Initial Setup

     This section provides instructions and suggestions for setting up
     Gen5 to perform most efficiently and effectively in your lab.


 Setting up Gen5 ...................................................................... 2
 Setting up Gen5 Secure ............................................................ 8
 Setting up Gen5 Reader Control................................................. 20
 Connecting a Reader ................................................................ 21
 Setting up Preferences.............................................................. 24







Set up Gen5

            For Gen5TM Only

         Gen5TM fulfills the reader control and analytical needs for a wide range of laboratory
         settings. The degree to which you follow the recommendations provided here depends
         on the needs of your organization.

   Recommended tasks to perform:
              1.    Designate a System Administrator
              2.    Install Gen5 on the Administrator's computer

            Installation instructions are included in the Getting Started Guide
              shipped with the CD.

              3.    Change the System Administrator's Password (see below)
              4.    Determine the optimal way to store Gen5's protocol and experiment files:
                    File Storage (page 4)
                     Organize the Database (page 10) or your Windows(R) file structure
              5.    Install Gen5 for other users and Connect a Reader (page 21) to each
                    computer
              6.    If applicable, direct each user's Database Configuration (page 12) to point to
                    the correct shared database
              7.    Set User Preferences (page 24)
              8.    Learn how to use Gen5:0.
                     Check out the tutorials (animated demos) in the Help system: Select
                        Help>Tutorials
                     Alternatively, begin by performing the Learning Exercises in the Getting
                       Started Guide.










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
             2.   Enter the current password in the Current Password field. Gen5 ships with
                  the password set to "admin."
             3.   Enter the new password in both the New and Confirm password fields
             4.   Click OK.0

  How to maintain Users Permissions
    Except in Gen5 Secure, access to Gen5's functions, like reading a plate, modifying a
    protocol, and masking values, is defined equally for all users except the System
    Administrator, who has all "permissions." Learn more on page 5.

  Learn about Gen5's Databases
        You can opt to save Gen5's protocol and experiment files in Gen5 SharedDB:
           About Gen5 Databases (refer to the Managing Files chapter)
           Organize Your Database Files (page 10)










File Storage
     System> Preferences> File Storage Mode
         Use this control to select a method for storing protocol and experiment files.

            Attention Gen5 Secure users: To ensure 21 CFR Part 11 compliance
              use the Gen5 Database for file storage

   About File Storage
         Gen5 provides two methods for storing protocol and experiment files. You can use the
         secure, shared-access database provided with Gen5, which is required for compliance
         with the FDA's 21 CFR Part 11 regulation on electronic records submission.
         Alternatively, you can use the file system provided with the Windows(R) operating
         system on a local PC or network (LAN). If your organization is unconcerned with FDA
         regulations, the choice is a matter of preference. However, one advantage to using the
         Gen5 Database is its ability to recover from a system crash. New and modified files are
         saved as Temporary Files in the database and can be used to recover information that
         wasn't saved before a system failure.

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










User Setup

          For all levels of Gen5 except Gen5 Secure

    System> User Setup

Gen5 User Permissions
        Only the Gen5 Secure product level offers the multiple-user login and password
        controls required to comply with the FDA's electronic-records submission directive.
        This page describes the more limited security options provided in other Gen5
        products.

  About Gen5 User Accounts
    There are only two types of Users in Gen5: Administrator and User, i.e. System
    Administrator and non-administrator. Neither account be deleted

       You Can:                         You Cannot:
       Change the                       Login as a User; only the System
       Administrator's password         Administrator requires login
       Change the Permissions           Change the Permissions for
       for User                         Administrator: all rights and privileges
                                        are already given
       Maintain/store Gen5 files        Keep track of which user is responsible
       in a secure database             for Gen5 activities
       Select a Startup option          Turn on/off Audit Trail notification.
       and Protocol and                 Events for which users are invited to add
       Experiment Folders for           comments to the change log/audit trail
       users                            are fixed by Gen5











Permissions

   Prerequisite:
         To change the User Permissions, you must login, System>Administrator LogIn, as
         the System Administrator

            Function

            Add a New Plate: Access to menu options and toolbar buttons for Adding
            one or multiple plates to an experiment

            Delete a plate: Access to Plate menu option to Delete, i.e. remove the
            plate information and all data associated with the plate (if any) from an
            experiment

            Mask/Unmask values: Access to Mask button in the Plate View to mask
            the values for selected wells. Masked wells are ignored in data reduction and
            curve plotting

            Edit values: Access to Edit button in the Plate View to change the values of
            selected wells

            Re-read plate: Access to Read button after plate has been read to
            overwrite the current measurement results with newly acquired
            measurements

            Simulate Read: Access to Simulate option of the Plate Read dialog to let
            Gen5 simulate a reading instead of actually reading the plate. (Useful for
            Gen5 training/tutorials.)

            Read from File (import): Access to Read From File option of the Plate
            Reading dialog to acquire/import reading data from a text file

            Enter Manually (raw data): Access to Enter Manually option of the Plate
            Reading dialog to manually enter (type in) reading data instead of actually
            reading a plate


   System Controls
         This table describes the capability each Permission gives users.

            Function

            Manage and Maintain Systems: This switch gives or denies access to the
            next five items. You can override it by individually assigning access to the
            permissions

            Edit Default Protocol: Access to define or modify the Default Protocol
            Settings

            Edit file storage mode: Access to menu option System>Preferences>File
            Storage to alter the option: database or Windows(R) file system











          Function

          Edit Read from File options:

          Manage and Maintain Devices: This switch gives or denies access to the
          next four related permissions. You can override it by individually assigning
          access to them

          Define Test Plates: Access to Diagnostics options to set up and modify the
          Universal Test Plate records used to conduct testing

          Delete Diagnostic Test History: Ability to delete test records. All users
          can view the test history, only users with this permission can delete the
          records

          Manage and Maintain File Storage: This switch gives or denies access to
          the next seven related permissions. You can override it by individually
          assigning access to them. They are only applicable when File Storage "uses
          the SharedDB"

          Create folder in Database: Ability to create a new folder while maintaining
          database files and when saving protocol and experiment files. Users denied
          this function are limited to saving files in existing database folders

          Delete/Overwrite folder in Database: Ability to delete or overwrite
          (Save As) folders and files from/in the database

          Export file from Database: When maintaining database files, ability to use
          the right-click menu to Export to Disk

          Rename folder/file in Database: Ability to rename database files and
          folders in the database

          Move folder/file in Database: Ability to relocate folders and files within
          the database

          Import file to Database: Ability to import, paste from clipboard, or drag
          and drop files from another location

          View hidden files and folders in Database: Ability to hide files, to see
          hidden files, and to reveal hidden files











Set up Gen5 Secure

            For Gen5TM Secure Only

         Follow these procedures to set up Gen5 Secure:
              1.    Designate a System Administrator
              2.    Complete the System Administrator's To Do List (see below)
              3.    Organize the Database (page 10)
              4.    Review/modify Signature Reasons and other security controls (see Gen5's
                    Help)
              5.    Define certain Preferences by using Gen5's Default Protocol. Each shared
                    database has one Default Protocol which defines the initial settings for all
                    newly-created protocols. (page 24)
              6.    Set up each user's Database Configuration to point to the correct shared
                    database, if applicable. (page 13)
              7.    Connect a reader to each user's computer (page 21)
              8.    Advise users to change their passwords (see Gen5's Help)
              9.    Encourage users to watch the Help>Tutorials and run through the Learning
                    Exercises provided in the Getting Started Guide.0


System Administrator's To Do List
            Also see information about the FDA's Requirements on the next page.

   Initial Setup Tasks
              1.    Make sure all designated computers (PCs) and BioTek readers meet the
                    System Requirements
              2.    Install Gen5 Secure on one computer (PC)

            Installation instructions are included in the Getting Started Guide
              shipped with the CD.

              3.    Start Gen5 and log in as the System Administrator
              4.    Change the System Administrator's password (page 14)
              5.    Copy the database: Shared.mdb to a secure network location (page 13)
              6.    Test Database Configuration of the Shared.mdb on the network (page 13)
              7.    Create/modify User Groups, as needed, and assign User Permissions to the
                    Groups (page 15)
              8.    Create new user accounts and assign the users to a Group








             9.   Connect reader(s) to the PC and establish communication (page 21)
            10. Repeat steps 2, 3, 6, and 8 for the remaining PCs0

  Periodic/As Needed Tasks
               Customize the security features to accommodate your organization's needs
               Organize your database files
               Educate users on regulatory requirements and Gen5 best practices
               Establish and implement a procedure and schedule for record retention and
                 archival
               Review records, including any training/user-qualification records

          Before modifying a user's account, make sure he/she is not logged into
            the system. You can check the System Audit Trail to determine who is
            currently logged in.


FDA's System Administrator Requirements
        The FDA's Electronic Signatures Rule (21 CFR Part 11) contains requirements that sites
        must meet in order to be in compliance. The System Administrator should be
        cognizant of the following:
           Administrator: The site shall select an "Administrator" who will be the person
             responsible for all high-level administration of the program. This person will
             control access to the program by adding new users, structuring the individual
             users authority levels, and reporting to management, as appropriate, on any
             unauthorized use of the program.
           Personnel Qualifications: Personnel who develop, maintain, or use electronic
             records/electronic signatures shall have the education, training and experience
             necessary to perform their assigned tasks.
           Written Policies: There shall be written policies which hold individuals
             accountable and responsible for action initiated under their electronic
             signatures, in order to deter record and signature falsification. There shall be
             written revision and change control procedures to ensure that the program is
             administered in compliance with the FDA's requirements.
           Record Archiving and Deletion: The site is responsible to ensure that
             archiving or other file management techniques are suitable such that electronic
             records generated by the system shall be accurate and readily retrievable.
              Records may be removed by deleting the entire shared database or individual
             files within the database. This action may be conducted by the Administrator
             or by any Power User.
           User Identity: Any person who will be authorized to use an electronic
             signature will have their identity confirmed by the Administrator prior to
             granting them program access. Only the genuine owner of the electronic








               signature is allowed to access the program through their ID/password
               combination. System users should be informed that accessing the program
               using someone else's login is a violation of the FDA rule.
            Password Expiration/Recall: All passwords must be checked, recalled, or
              revised at an interval appropriate with the security needs of the organization.
              Personnel who no longer work at the establishment shall have their program
              access capabilities deactivated in a timely manner.
            Certification to FDA: The site must certify to FDA that the electronic
              signatures utilized on records are intended to be as legally binding as
              handwritten signatures, prior to or at the time of record submission to FDA.
              The FDA rule should be consulted for details and method to be used.
            Notification of Attempted Security Breaches: The software utilizes an error
              log system to notify the Administrator of log-in failure incidents that exceed
              the limits they have established. The administrator is responsible to
              "immediately and urgently" notify the appropriate personnel at the site if the
              activity appears to be an attempt to breach security.
            Signature Representations: The administrator should be made aware that
              while electronic signatures representations cannot be excised or added they can
              be copied by screen copy techniques and pasted into other documents. These
              modified documents cannot be re-saved in the secure program but may be
              printed out as is.


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
                  1.   In the default SharedDB folder, highlight the original, right-click and
                       select Copy
                  2.   De-select the original (click elsewhere in the dialog), right-click and
                       select Paste
                  3.   Highlight the copy, right-click and select Rename
                  4.   Give the copy a unique name, like SharedDB_original.mdb.0




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
             setting in the Default Protocol so it will apply to all newly-created protocols.
           Gen5 handles multiple, simultaneous users performing database management
             tasks by giving precedence to the user with the greater administrative rights.











File Storage
     System> Preferences> File Storage Mode
         Use this control to select a method for storing protocol and experiment files.

           Attention Gen5 Secure users: To ensure 21 CFR Part 11 compliance
             use the Gen5 Database for file storage

   About File Storage
         Gen5 provides two methods for storing protocol and experiment files. You can use the
         secure, shared-access database provided with Gen5, which is required for compliance
         with the FDA's 21 CFR Part 11 regulation on electronic records submission.
         Alternatively, you can use the file system provided with the Windows(R) operating
         system on a local PC or network (LAN). If your organization is unconcerned with FDA
         regulations, the choice is a matter of preference. However, one advantage to using the
         Gen5 Database is its ability to recover from a system crash. New and modified files are
         saved as Temporary Files in the database and can be used to recover information that
         wasn't saved before a system failure.

           ClarityTM Luminometer protocol files, with a .bpf extension, cannot be
             stored in Gen5's shared database. They are typically stored in the
             C:\Program Files\BioTek\Clarity\protocols folder.

   How to
            Select an option for storing Experiment and Protocol files:
            Gen5 Database: all actions related to managing and maintaining files, like
              File>Open, File>Save, Browse..., and so on, will occur in Gen5's SharedDB.
              Learn About Gen5's Databases
            Windows File System: Gen5 will not control the management of files. Actions
              related to managing and manipulating files will be determined by the
              Windows operating system, e.g. you can use Windows(R) Explorer. Generally
              during file management activities like File>Open, Windows begins at the last
              directory and folder used.

           AutoSave Feature: Gen5 offers this feature to give you additional
             control over the storage of saved files.











Database Configuration
    System> Database Configuration

  Prerequisite
         Some features of this dialog require System Administrator privileges.


         When Gen5 is installed, there are two primary databases, a shared and a local
         database. They are named SharedDB.mdb and LocalDB.mdb respectively. The
         LocalDB cannot be moved or renamed. The SharedDB can be moved and renamed. All
         operations affecting them take place using their respective tabs, except the upgrade
         utility. Learn more: About Gen5's Databases

  Source

            Gen5 displays the current location of the database.
            LocalDB: You cannot move or rename the LocalDB database, thus the 3-dot
              button is disabled. If necessary to see the full pathname of its location, you can
              click inside the text field and scroll to the right.
            SharedDB: Click the 3-dot button to view the current location of the database.
              You can move, rename or copy the SharedDB database.

  Test

                         Use the Test button to check the connection to the Gen5 database.
            Potential error messages are referenced in the Troubleshooting section above.




Move/Copy Database to Network
    System> Database Configuration

           Gen5 Secure installs and enables the databases during regular
             installation. All other levels of Gen5 must elect to use the database to
             store protocol and experiment files at System>Preferences>File
             Storage

         In a multiple-user environment, you can set up Gen5's database on a shared network
         drive so multiple users can access the same protocol and experiment files. This is a
         recommended step for Gen5 Secure System Administrators. You can also set up
         multiple databases, one for each user, for example. During a Gen5 session, access is
         provided to only one database at a time.










   How to:
              1.   Select System> Database Management> Database Configuration

              2.               Select the SharedDB tab

              3.       Next to the Source field, click the 3-dot button

              4.                  In the Open dialog, highlight and right-click the file
                   SharedDB.mdb, and select Copy or Cut: use cut to move and copy to copy
                   (see File Management Recommendations below)
                   Note: SharedDB is the installed/original name for the shared database.
                   Since you can change the name, it's possible it has already been changed.
              5.   Use the browse tools to navigate to the desired location in the Look in field
              6.   When the correct location is selected, right-click in the window and select
                   Paste
              7.   Click the Open button to save and close the window and return to the Gen5
                   Database Configuration dialog
              8.   Shut down and restart Gen5 to make the changes take effect.0

           Important: if you're moving the Shared DB to a network drive you
             may want to consider Disabling Write Caching. Consult your IT
             department or Microsoft's knowledge base.


Changing the System Administrator's Password

           For Gen5TM Secure Only

     System> Security> Users
         BioTek recommends changing the System Administrator's password immediately
         following Gen5 installation to ensure a secure operating environment.
         To change the password:
              1.   Login as the System Administrator, if you haven't already done so:
              2.   Select System> Login/Logout
              3.   Set the User to Administrator
              4.   Enter the default password: admin
              5.   Select System> Security> Users
              6.   Double click the System Administrator user (to Edit the record)
              7.   Define and confirm the new password.0

           Important: Do not forget the Administrator's password. If you do,
             you'll have to reinstall Gen5.









About User Accounts

          For Gen5TM Secure Only

    System> Security> Users

  Prerequisite
        This function is only available to the System Administrator.

  How to Create, Modify or Delete User Accounts
        Only an Administrator can add, modify, or delete users. Except for the Administrator,
        any user account can be changed or deleted:

                        Click New to set up a new user

                       (Double-click or) Highlight a user and click Edit to modify its
               name, password, or Group assignment
           Highlight a user and click Delete to remove the user account


Creating/Maintaining User Accounts

          For Gen5TM Secure Only

    System> Security> Users

  Prerequisite
        Most options for user accounts are only available to the System Administrator. Non-
        administrators are limited to changing their own password and selecting a Startup
        Action and Protocol Folder.

  User ID
        Enter a unique ID using 1 to 16 alphanumeric characters. The user will enter or select
        this ID when logging into Gen5 and when signing files.

  Full Name
        Enter the user's name. This name will be associated with events logged by this user's
        actions and with the digital signature applied by this user.

  Group
        Choose a Group membership to assign access rights and permissions to the user. Users
        receive the rights assigned to the Group.










   Status
         The checkbox shows whether or not the user's account is currently locked. The System
         Administrator can lock or unlock the account. When a user's account is locked, the
         user cannot log into Gen5 and cannot sign files. A user's account may become locked
         due to one of three events:
                Intentional lock by the Administrator through this dialog
                Automatic lock if the user exceeded the number of successive failed login
                  attempts
                Automatic lock if the user's password expired

            Important: Unlocking a user's account following an automatic lock
              resets its counter or clock. The reset is specific to the reason for the
              lockout: when it is caused by password expiration, the password
              expiration clock is reset and when it is caused by failed logins, the
              user's history of "successive failed login attempts" is reset to 0.

         When lock out occurs due to an expired password, unlocking the account allows the
         user to login to Gen5 with the same password, giving them a chance to change it.
         Alternatively, as system administrator, you can simply change the password yourself
         (which will by default unlock the account) and tell the user to login with the password
         you have assigned him/her.

   Startup Action
         Use the drop-down to select the preferred method for starting Gen5:
                Startup Window is the default setting, it offers several options including
                  creating a new item or opening a recently used item
                Create new experiment opens Gen5 with the Protocol selection dialog
                  open, as if the user had selected File>New Experiment
                Start at main menu opens Gen5 showing the File, System and Help menus
                  only. Since neither a protocol nor experiment is open, the workspace is
                  blank.

   Protocol and Experiment Folders
         Browse to or enter the full path and directory to define the folder in which the current
         user will typically store protocol and experiment files. If a folder is not specified, Gen5
         will default to the most recently accessed folder.

   Password
         Assign a password for the user to enter the first time he/she logs in to Gen5. Instruct
         users to change their password after the first login using the Password you've
         assigned. Users can only change their own password. System Administrators can
         change any user's password.










Login/Password Controls

          For Gen5TM Secure Only

     System> Security> Login

Prerequisite
        Only the System Administrator can access these controls. You must login:
        System>Login/Logout, as the Administrator to change the settings.

          Important: The default settings shipped with Gen5 Secure, and
            shown in the screenshot below, comply with the FDA's 21 CFR Part 11
            requirements for controls for identification codes/passwords.

Login
           Lock user account after: Specify the number of successive failed login attempts
             a user may make before being locked out of Gen5. This feature does not apply
             to System Administrator accounts and only a System Administrator can
             reinstate a locked out account. Valid entry range: 2-10. When this feature is
             unchecked, users login attempts are unlimited. Compliance with 21 CFR Part
             11 requires setting a limit for failed login attempts.
           Lock session after: Specify the number of minutes that a Gen5 session can be
             idle before it is locked and requires successful user login to reactivate. A
             session is considered idle when there is no keyboard or mouse activity and
             Gen5 is not controlling a reader activity. Valid entry range: 1-1440 minutes.
             Compliance with 21 CFR Part 11 requires setting an idle-time limit.
           Force user to type ID: apply this control if your security rules require users to
             enter their ID at login and to apply their Signature. When this feature is
             unchecked, the last user's ID is displayed in the login and signature screens and
             users can select an ID from a drop-down list of users. This is not a requirement
             for compliance with 21 CFR Part 11.

Password
           Minimum password length: Specify the minimum number of alphanumeric
             characters required for a valid password. Valid entry range: 2-10 characters.
           Password expiration: Specify the number of days a password can be used
             before users are required to change it. When users let their password expire
             without changing it, their accounts are locked out and only a System
             Administrator can reinstate a locked out account. Valid entry range: 1-10000
             days. If this feature is unchecked passwords do not expire. Compliance with 21
             CFR Part 11 requires an expiration period.











           Lock out: when a user's password has expired, the system administrator has two
           choices:
                    manually remove the Locked out flag: this resets the password
                      expiration period allowing the user to login using his/her current
                      password.
                    enter a new password for the user (which unlocks the account) and tell
                      the user to login with the password you have assigned him/her. Advise
                      the user to change the password after logging in.
            Advise user: If password expiration is set, specify the number of days before
              their password expires to alert users to change their password. Valid entry
              range: 1-30 days, but cannot exceed the number of days to Password
              Expiration.
            Password reuse: Specify the number of passwords Gen5 will remember for
              each user's account to prevent a recently used password from being reused.
              Valid entry range: 2-20.


About User Groups

           For Gen5TM Secure Only

     System> Security> Groups

   Prerequisite
         This function is only available to the System Administrator.
         Gen5 Secure uses Groups to manage the rights or permissions granted to users. When
         creating (or maintaining) a group, you define the level of access and the controls
         available to certain types of users, and then assign actual users to the groups. Gen5
         ships with three groups: Administrator, Power User, and Standard User.
         The System Administrator and Power User groups are given access rights to all
         functions. The Administrator's rights cannot be changed, and include additional rights
         to manage user accounts that are not extended to Power Users. When Gen5 Secure is
         installed, the Standard User is limited to the following permissions. The System
         Administrator can change these controls as needed:
                Quick Read/Use Default Protocol
                Add a New Plate
                Create/Edit Sample IDs
                Edit Plate Information
                Edit Report Builder
                Create folder in database








  How to create new and modify existing groups:
        Only a System Administrator can add, modify, or delete groups. Except for the
        Administrator group, any group can be changed or deleted, and any group can be
        renamed.

                           Click New to set up a new group

                           Highlight a group and click Edit to modify its name and
               permissions

                         Highlight a group and click Delete to remove it as an option. First
               you must reassign any users to another group. You cannot delete a group with
               users assigned to it.











Set up Gen5 Reader Control

           For Gen5TM Reader Control Only

         Recommended tasks to perform:
              1.   Install Gen5 on the computer

           Installation instructions are included in the Getting Started Guide
             shipped with the CD.

              2.   Determine the optimal way to store Gen5's protocol and experiment files:
                   File Storage (page 4)
              3.   Connect a Reader to the computer (page 21)
              4.   Set User Preferences (page 24)
              5.   Learn how to use Gen5: 0
                    Watch the online demos, select Help>Tutorials
                    Alternatively, begin by performing the Learning Exercises in the Getting
                      Started Guide.











Connecting a Reader
    System> Reader Configuration
        After following the Operator's Manual instructions for attaching the reader to the
        computer, you must tell Gen5 what type of reader it is and which communications port
        (Com Port) it is plugged into. Gen5 and Gen5 Secure allow up to two readers to be
        assigned at a time.

          Special note for Clarity users: Configuration parameters and port
            settings can only be defined through the Clarity PC software: Follow
            instructions on page 23.

             1.   Turn on the reader
             2.   From the menu, select System> Reader Configuration

             3.                Click the Add button to define the Reader Settings

             4.      Use the drop-down list to select the Reader Type
             5.   Except for the Clarity (see page 23), in the Com Port text field, enter the
                  number of the communications port.
             6.   Retain the default Baud Rate.
             7.   Click Test Comm. Gen5 will attempt to communicate with the reader.
             8.   After you receive a passing message, "The reader is communicating," click
                  OK and then click Close at Reader Configuration. If you receive any other
                  message look for a remedy in the Troubleshooting section of this guide.0
        That's it! Gen5 captures the information it needs from the reader itself, including probe
        size, wavelength and bandwidth capability, and any other applicable information.

  Instrument-Specific Information
           SynergyTM HT: For this multi-detection reader, Gen5 must obtain the
             fluorescence/luminescence filter sets. BioTek sets the reader's on-board
             software with the ordered configuration before shipping the reader. Gen5 will
             capture the stored information when it initiates communication with the
             reader.
           SynergyTM 2: For this multiple-module, multiple-detection reader, Gen5 must
             obtain both the fluorescence/luminescence filter sets and the mirror-holder
             configuration. BioTek sets the reader's on-board software with the ordered
             configuration before shipping the reader. Gen5 will capture the stored
             information when it initiates communication with the reader.
           SynergyTM 4: For this multiple-module, multiple-detection reader, Gen5 must
             obtain both the fluorescence/luminescence filter sets and the mirror-holder
             configuration. BioTek sets the reader's on-board software with the ordered









               configuration before shipping the reader. Gen5 will capture the stored
               information when it initiates communication with the reader.
            ClarityTM: A Clarity luminometer can be added or deleted in the instrument
              configuration dialog. But, unlike other readers, the COM port that is used to
              attach to the Clarity cannot be set or modified in Gen5's Reader Configuration
              dialog. You must use the Clarity software to define the connection settings. Use
              the Clarity Control Panel.
            FLx800TM: Gen5 must obtain the fluorescence/luminescence filter wheel
              configuration. BioTek sets the reader's on-board software with the ordered
              configuration before shipping the reader. Gen5 will capture the stored
              information when it initiates communication with the reader.
            PowerWaveTM: This 8-channel monochromator does not need special set up.
              When Gen5 communicates with the reader the Absorbance Wavelength table
              currently stored in the reader's memory is displayed. When defining a Read
              Step select from the stored wavelengths or enter a different one.
            PowerWaveTM XS: This single-channel monochromator does not need special
              set up. When Gen5 communicates with the reader the Absorbance Wavelength
              table currently stored in the reader's memory is displayed. When defining a
              Read Step select from the stored wavelengths or enter a different one.

           Two models of PowerWave XS are listed in the Gen5: PowerWave XS
             and PowerWave XS2. If you are connecting a PowerWave XS reader
             that has a USB port and an MQX200R2 product number (take note of
             the 2), you must select the PowerWave XS2. Our changes to the
             PowerWave XS hardware to incorporate a USB/RS-232 com port
             requires unique reader identification in Gen5. There is no difference in
             the optical performance characteristics of the reader.

            ELx800TM and ELx808TM: BioTek configures the on-board software of these
              filter-wheel-based readers with the installed filters. Gen5 will capture the filter
              configuration when it initiates communication with the reader.
            uQuantTM: This single-channel monochromator does not need special set up.
              When Gen5 communicates with the reader the Absorbance Wavelength table
              currently stored in the reader's memory is displayed. When defining a Read
              Step select from the stored wavelengths or enter a different one.

           Learn about the Absorbance Wavelengths tables in the Reader Control
             and Configuration chapter.










Setting up the Clarity Luminometer
        Clarity users must follow a slightly different sequence of steps to establish
        communication between the Clarity and Gen5. First, follow the installation instructions
        provided with the Clarity, including installing the Clarity PC software. After
        installation, when you're running assays, Gen5 uses the Clarity PC software in place of
        its StepWiseTM Procedure. But, you define the other elements of the Protocol and run
        the Experiment with Gen5.

          Important: Install the Clarity PC software before proceeding.

             1.   Connect the luminometer to the computer (if not already connected) and
                  turn it on.
             2.   Start the Clarity software and set up the communications port (Options>
                  Com Port Settings).
             3.   Then, select Options> Instrument Info to test communication. Details
                  about the current instrument should be displayed on-screen. If not, repeat
                  Step 2, making sure the correct port is selected.
             4.   Important: Close the Clarity software.
             5.   Start Gen5 and log in (if required).
             6.   Select System> Reader Configuration and set the Reader Type to
                  Clarity
             7.   Select System> Reader Control> Clarity to make sure Gen5 is
                  communicating with the Clarity. If the control panel does not open, repeat
                  Step 6 and retry. Contact BioTek TAC if problems persist.0
                  If the control panel does not open:
                   on Windows(R) XP and 2000 systems, repeat Step 6 and retry.
                   on Windows(R) Vista systems:
                     1   Locate and right-click the Clarity desktop icon, and select Run as
                         administrator. If prompted, enter the password,
                     2   At the User Account Control dialog, click Allow,
                     3   The Clarity software will launch and communicate with the reader.
                         Close the Clarity software.
                     4   Return to Gen5 and test communication with the Clarity by
                         performing Step 7 above.
                   Contact BioTek TAC if problems persist.











Setting up Preferences
         Gen5TM offers tools for defining certain preferences. Take advantage of them to save
         time and enforce consistency of use. They can be overridden, as needed, during normal
         use of the software.

Set up the Default Protocol
         The Default Protocol can be used to define numerous settings that you're likely to
         apply to all experiments. Consider using the Default Protocol to:
            Customize Well IDs in the Plate Layout
            Set up Protocol Options to automatically save files and to automatically execute
              your preferred method of results output immediately after reading a plate.
              Define File Naming Conventions and File Locations for your export files under
              Export Options

Set Startup Preferences
         Set user's Startup Preference and Protocol and Experiment Folders:
                Gen5 Secure: Creating/Maintaining User Accounts (page 15)
                All other Gen5 levels select System>User Setup

   Define Startup Preferences
              1.       Use the drop-down to select the preferred method for Startup Action:
                    Display Welcome dialog is the default setting, it opens Gen5 with a
                      screen that offers links to several common tasks including creating a
                      new item or opening a recently used item. Note: the only way to access
                      the Welcom page is to launch Gen5.
                    Create new experiment opens Gen5 with the Protocol selection dialog
                      open, as if the user had selected File>New Experiment
                    Start at main menu opens Gen5 showing the File, System and Help
                      menus only. Since neither a protocol nor experiment is open, the
                      workspace is blank.

              2.      Use the 3-dot button to change your Protocol and Experiment Folders:
                   browse to the full path and directory to define the folder where you will
                   typically store protocol and experiment files. Gen5 will point to these
                   folders when you save and open a protocol or experiment.
              3.   Click OK.0
         The changes will take effect the next time you log into Gen5.










Customize the Toolbar
        Gen5 has two toolbars, one for each mode: Protocol or Experiment. You can change
        their configuration to facilitate your work. Find instructions in the System
        Management chapter.

Select a List Separator for Import Files
        If you regularly import data files, rather than obtaining measurements from the reader,
        take a moment to identify for Gen5 your normal list separator. Select
        System>Preferences> Read from File Settings
