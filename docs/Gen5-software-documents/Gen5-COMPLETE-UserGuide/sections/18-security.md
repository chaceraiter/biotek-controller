# Chapter 18: Security

     Primarily for Gen5 Secure users, this chapter describes Gen5's tools
     for managing security issues, including audit trails, electronic
     signatures and user accounts.


 Changing your password........................................................... 385
 Login/Password Controls ........................................................... 386
 FDA's 21 CFR Part 11 ............................................................... 388
 Signing Protocols ..................................................................... 389
 Audit Trail ............................................................................... 391
 User Accounts ......................................................................... 398



384 | Chapter 18: Security




Security
           To meet the FDA's electronic records requirements, Gen5 Secure offers several
           tools to enable a secure software environment. In addition to the content provided
           here, you can find detailed information about these features in the Gen5 Help:
            Audit Trail on page 391
            Electronic Signatures on page 389
            System Administrator's "To Do List" on page 8
            Manage User Accounts:
               Setting Up New Users on page 398
               Changing a User's Passwords on page 385
               Changing a User's Privileges on page 401
            About 21 CFR Part 11 on page 388







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
       5.   Click OK.0.
      The password will take effect the next time you log into Gen5.

        Contact your System Administrator if you've forgotten your password.
          He/she can change your password without knowing the current one.



386 | Chapter 18: Security




Login/Password Controls

           For Gen5TM Secure Only

     System> Security> Login

Prerequisite
        Only the System Administrator can access these controls. You must login:
        System>Login/Logout, as the Administrator to change the settings.

           Important: The default settings shipped with Gen5 Secure, and
             shown in the screenshot below, comply with the FDA's 21 CFR Part 11
             requirements (page 388) on controls for identification passwords.




Login
            Lock user account after: Specify the number of successive failed login
              attempts a user may make before being locked out of Gen5. This feature does
              not apply to System Administrator accounts and only a System Administrator
              can reinstate a locked out account. Valid entry range: 2-10. When this feature is
              unchecked, users login attempts are unlimited. Compliance with 21 CFR Part
              11 requires setting a limit for failed login attempts.
            Lock session after: Specify the number of minutes that a Gen5 session can be
              idle before it is locked and requires successful user login to reactivate. A






           session is considered idle when there is no keyboard or mouse activity and
           Gen5 is not controlling a reader activity. Valid entry range: 1-1440 minutes.
           Compliance with 21 CFR Part 11 requires setting an idle-time limit.
       Force user to type ID: apply this control if your security rules require users
         to enter their ID at login and to apply their Signature. When this feature is
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

      Lock out: when a user's password has expired, the system
        administrator has two choices:
        = manually remove the Locked out flag: this resets the password
        expiration period allowing the user to login using his/her current
        password.
        = enter a new password for the user (which unlocks the account) and
        tell the user to login with the password you have assigned him/her.
        Advise the user to change the password after logging in.

       Advise user: If password expiration is set, specify the number of days before
         their password expires to alert users to change their password. Valid entry
         range: 1-30 days, but cannot exceed the number of days to Password
         Expiration.
       Password reuse: Specify the number of passwords Gen5 will remember for
         each user's account to prevent a recently used password from being reused.
          Valid entry range: 2-20.



388 | Chapter 18: Security




FDA's 21 CFR Part 11
     This is a description of the FDA's electronic-records submission requirements
     and how they are satisfied by Gen5TM Secure.
     A significant component of this secure software environment is the ability to create
     individual user accounts to ensure that only authorized users can gain access to the system
     and to any restricted functions. A site-designated System Administrator creates and
     maintains the user accounts.

  Gen5 Secure complies with FDA's Electronic Signatures rule, 21 CFR Part 11:
            System Administrator - The System Administrator creates and maintains user
              accounts and user groups to specify which Gen5 functions shall be protected
              from use by limited-access users, e.g. masking data. The System Administrator
              sets special password and login characteristics including minimum password
              length, password aging, and idle session time-out. The System Administrator is
              also responsible for managing the database of Gen5 files and audit trails.
            Support for Multiple Users - Each user is identified by a unique combination
              of User ID and encrypted password. Users must log in to Gen5 Secure with
              these identifiers to gain access.
            Time-stamped Audit Trails - Activities such as user login/logout, protocol
              and experiment creation and modification, and plate reading are permanently
              logged in a secure database.
            Embedded Signatures - Authorized users can electronically sign protocol and
              experiment files. Electronic signatures are permanent and remain a part of the
              overall data record for the life of that file.
            Secure Record Storage - Gen5 proprietary files (.prt and .xpt) are stored in a
              secure shared-access database. Activities performed on files within this
              database (such as rename, move, copy, overwrite, and delete) are performed
              within the Gen5 environment, and every change is tracked in an audit trail. In
              addition, the System Administrator can configure the system so that these
              activities may only be performed by Power Users or high-level users.
            Protected Functions - The System Administrator can protect a variety of
              functions from use by limited-access users, e.g. Standard Users. These functions
              include the deletion, renaming, modification, and overwriting of various record
              types.







Signing Protocols

         For Gen5TM Secure Only

    System> Security> Signature Reasons
       Gen5 Secure provides users the ability to sign (i.e. sign off on) a protocol or
       experiment file. Your System Administrator can define the Signature Reasons to give
       meaning to each signature recorded. Gen5 ships with three reasons: Authorship,
       Review, and Approval. These terms can be kept, modified, or added to.
       When users create, review, or perform any other activity on a Protocol or Experiment
       for which a signature or sign-off is required, they use the Sign option, select a Reason,
       and enter their password to confirm the action.
       Representatives can sign off on files for another user. Gen5 provides an option for two
       users to digitally sign records as representatives of a third user.




What do you want to do:
          Create/Modify Signature Reasons (below)
          Sign a Protocol or Experiment (page 390)
          Include Signatures in the Experiment Report:
                  To include Signatures in a report or export file:
                     1   Open the preferred reporting tool: Report Builder, File Export
                         Builder or Power Export Builder
                     2   In the Available Data Views or Excel report objects, find Table, and
                         add Signatures to the report content.
                  Gen5 reports the Signatory, Reason, and Date


Signature Reasons

         For Gen5TM Secure Only

    System> Security> Signature Reasons

  Prerequisite:
       This function is only available to the System Administrator. You must login:
       System>Login/Logout as the Administrator to access this control



390 | Chapter 18: Security



  How to create/modify Signature Reasons:
        Simply, click in the text fields of the Signature Reasons table to add new or replace
        existing reasons for signing protocols and experiments.




    Sign
     Protocol> Sign
     Plate> Sign
        To sign off on a Protocol, select Sign from the Protocol menu or click the Sign button
            To sign off on an Experiment, highlight a plate in the menu tree, select Sign
              from the Plate menu (or right click and select Sign, or click the Sign button)

Sign Off on a file:
          1.   Use the appropriate option (described above) to open the signature screen

          2.     Reason: Use the drop-down list to select the reason for signing the file.
               Your System Administrator creates and maintains the Reasons selection list .
          3.   User: Gen5 sets this to match the user who is currently logged in. Use the
               drop-down list to change it, if necessary.
          4.   Password: Enter your password.

          5.   Click            0.
               If the file hasn't already been saved, Gen5 opens the Save dialog.

Sign as a Representative:
        Two users are required to sign as a Representative of another user. Follow steps 1 and
        2 above, then:
          1.      Select the checkbox for Representative of and use the drop-down list to
               identify the user being represented.
               Gen5 adds 2 tabs to the dialog, one for each representative.
          2.   Each representative must select their user ID and enter their password.

          3.   Click            0.
               If the file hasn't already been saved, Gen5 opens the Save dialog.







Audit Trail

  About Audit Trails
       Depending on the level of Gen5 you're running, one or more Audit Trails keep track of
       certain activities and build a "change history" log of events. The protocol and data
       audit trails cannot be edited or deleted. They are part of the permanent record of the
       protocol or experiment file.
       When the Audit Trail Notification feature is deployed in Gen5 Secure, users are
       prompted to enter comments into the record each time a logging event takes place. You
       can view and report the audit trail and calculation warning logs, as needed.

Audit Trail Types:
          Data Audit Trail - All levels of Gen5 - logs values-masking and -editing
            events, plate addition and deletions, and other related events. Data audit trails
            occur at the Experiment level to log the experiment-related events, like which
            protocol it was based on, and at the Plate level for plate-related events, like the
            read's status/progress
          Protocol Audit Trail - Gen5 Secure Only - logs all events related to the
            creation and modification of protocol files, like changes to plate layout and data
            reduction steps
          System Audit Trail - Gen5 Secure Only - logs system-level events, like user
            login/logout and reader-setting modifications, maintenance and updates to
            database folders and files, and so on. System events can be archived and
            deleted from the database.
         All the audit trails include an Event description, a time and date stamp, Gen5
         Secure logs the ID of the user logged in at the time of the event, and any user-
         entered comments


Audit Trail Notification Options

         For Gen5TM Secure Only

    System> Security> Audit Trail

  Prerequisite
       Only the System Administrator can access these controls. You must login:
       System>Login/Logout, as the Administrator to change the settings.

  About Audit Trail Notification
       These controls turn on or off notification to users when an audit-trail-logging event
       occurs. When Notification occurs, users are provided an opportunity to add a
       Comment to the record. If the system-generated text does not provide as much detail



392 | Chapter 18: Security



        about the event as you'd like, you can use the Comments feature to encourage users to
        enter more useful information. For example, when the plate layout of a protocol is
        changed, Gen5 simply logs the event as "Plate Layout changed", while the user can add
        details to the record like, "Added blanks: H11, H12."
        Notification and comment control for each type of audit trail can be selected
        individually using the checkboxes and drop-down lists.

  How to
          1.      Turn on Notification: for each type of audit trail using the checkbox to turn
               on or off (remove the checkmark) notification of an event. Notification
               identifies the event with a brief description and provides a text area for users'
               Comments

          2.      Prompt user for a comment: if Notification for an audit trail is turned on,
               select a comment-required setting:0.
                Accept an empty comment: user is not required to enter text in the
                  Comment area
                Invite user to type a comment: if user does not enter a comment during
                  notification of an event, the Message inviting the user to enter a comment:
                  defined in the text box below, will be presented to them. You can replace
                  the default text with your own wording
                Comment required: if user does not enter a comment during notification of
                  an event, the Message requiring the user to enter a comment: defined in
                  the second text box below, will be presented to them. You can replace the
                  default text with your own wording. Users will not be permitted to
                  quit/exit the audit trail notification without entering some text in the
                  Comment area



 Exporting Audit Trail Events

           For Gen5TM Secure Only

     System> Audit Trail> Export button
        Use this feature to export System Audit Trail events for archiving and to generate a
        report of the events. Exported records can be deleted from the system during the
        export process to maintain the size of the database, and to remove unnecessary
        records.

           Important: Gen5 does not retain control over the exported text files.
             It is your organization's responsibility to ensue the security of the
             exported audit trail records.






To export audit trail events:
      1.   Select System> Audit Trail
      2.   Click the Shared or Local tab to select the source database of the records you
           want to export
      3.   Click Export
      4.   Enter a date range of the events you want included in the export file
      5.   Check or ignore the Delete events after exportation option
      6.   Set the Save in field to the location you want to send the text file to. Use the
           standard Windows(R) browse tools to select the location
      7.   Click Save to export the events0.

After export, compact the database:
     If the Delete events after exportation option was used, the System Administrator
     should:
      1.   Make sure there are no users are currently logged into to the shared database
      2.   Select System> Database Configuration
      3.   In the Shared or Local database, as appropriate, click Optimize0.


        After exporting the file, you can open it with Notepad(R) or a word processor, to
     review or print it.



394 | Chapter 18: Security



Data Audit Trail
        Each plate and each experiment has a Data Audit Trail, a change history or log of
        automatically-recorded events. An event is an action like:
               Plate read started
               Plate successfully read
               Plate read failed with message "Reader error: 0IE0"
               Modify Value - Well A2 - 390 - Old: 2.180 - New: 2.080

           When values are masked or edited, Gen5 logs the event as Mask or
             Modify Value <Well>-<Data set name><read index for
             kinetic/scan><position for scan>; old and new values are provided
             when the value is changed.

   What events are logged:
        The level of software determines the types of events logged by the data audit trail:
            Gen5: All Gen5 levels log data changing/masking and plate addition and
              deletion events, and plate-read status and warnings
            Gen5 Secure also logs digital signature events
            All audit trails contain a description of the Event, a time and date stamp. Gen5
              Secure also contains the ID of the user logged in at the time and any user-
              entered comments (if Audit Trail Notification is turned on)

   Viewing Audit Trails:
                                                       In the menu tree, each Plate
                                                       has a Data Audit Trail, and
                                                       so does the Experiment
                                                       You can also open them from
                                                       a menu:
                                                       Plate>Audit Trail
                                                       File>Audit Trail (for the
                                                       Experiment)




   Reporting/Printing Audit Trails:
        You can include the Data Audit Trail in reports and export files, and copy and paste
        items to an external file:






          In the Report Builder and Export Builder, look for Audit Trail under Table in
            the Available Data Views tree, to add an item to the Report or Export Content
          Copy and Paste: In the audit trail screen, highlight event details and use Ctrl+C
            to copy. Open Notepad or a word processor, and paste it with Ctrl+V

  Security:
       Data audit trails cannot be edited or deleted. They remain a permanent part of the
       Experiment file for the life of that file.


Protocol Audit Trail

         For Gen5TM Secure Only

       Each protocol has an audit trail that automatically logs all events related to its creation
       and modification. For example:
               Copy of protocol X (the full path and filename)
               Plate Layout modified
               Data Reduction modified

  What events are logged:
               Procedure
               Data Reduction steps
               Plate Layout
               Report and Export definitions
               Miscellaneous protocol options
               A description of the Event, a time and date stamp, the ID of the user logged
                 in at the time (if applicable) and any user-entered comments (if Audit Trail
                 Notification is turned on)

  Viewing the Audit Trail:
               In the menu tree, expand the Protocol branch to locate its Audit Trail
               In a multi-plate calibrator or single-assay protocol, the Protocol Audit Trail
                 is split into a main log and separate Method Audit Trails for each
                 Calibration Plate and Other Plates.

  Reporting/Printing the Audit Trail:
               In the Report Builder and Export Builder, look for Audit Trail under Table
                 in the Available Data Views tree, to add an item to the Report or Export
                 Content



396 | Chapter 18: Security



                In the audit trail screen, highlight event details and use Ctrl+C to copy.
                  Open Notepad(R) or a word processor, and paste it with Ctrl+V

   Security:
        Protocol audit trails cannot be edited or deleted. They remain a permanent part of the
        Protocol and/or Experiment file for the life of that file.




System Audit Trail

           For Gen5TM Secure Only

     System> Audit Trail
        System-level events, like user login/logout and reader-setting modifications, are
        automatically recorded in the System Audit Trail. For example:
                Logout (computer and user ID)
                File "database + filename" created
                File "database + filename" pasted from clipboard

  What events are logged:
                User login and logout
                System security updates (user accounts, login and password parameters,
                  protected functions, audit trail notifications, and file location and format)
                Plate Type Database modifications
                System Test and Test Plate runs, and adding and modifying Test Plates
                Reader settings changes (reader type, probe selection, communication
                  parameters, and filters/wavelengths)
                System setup changes (protocol defaults, format settings, start-up options,
                  and database settings)
                User-customizable application settings (such as toolbar and position/size of
                  main window)
                A description of the Event, a time and date stamp, the ID of the user logged
                  in at the time and any user-entered comments (if Audit Trail Notification is
                  turned on)

   Viewing the System Audit Trail:
        Select System>Audit Trail to open the viewer.






Reporting the System Audit Trail:
    You must export Audit Trail Events to print them from a text or word processing file.

Exporting Audit Trail Events:
    Gen5 provides a quick and easy method for exporting the System Audit Trail. Use this
    feature to establish a regular schedule for "archiving" past events and to generate a
    report of the events, if needed. The export action itself is logged in the audit trail.
    Exported records can be optionally deleted from the system.

      Important: Gen5 does not retain control over the exported text files.
        It is your organization's responsibility to ensure the security of the
        exported audit trail records.



398 | Chapter 18: Security



User Accounts

About User Accounts

           For Gen5TM Secure Only

     System> Security> Users

  Prerequisite
        This function is only available to the System Administrator. You must login: System>
        Login/Logout as the Administrator to access all the controls. Non-administrators are
        limited to changing their own password and selecting a Startup Action and Protocol
        Folder.

  How to Create, Modify or Delete User Accounts
        Only an Administrator can add, modify, or delete users. Except for the Administrator,
        any user account can be changed or deleted:

                           Click New to set up a new user

                        (Double-click or) Highlight a user and click Edit to modify its
                name, password, or Group assignment
            Highlight a user and click Delete to remove the user account


Setting User's Permissions
     Gen5 Secure: System> Security> Users> Edit
     All other Gen5 levels: System> User Setup

  Prerequisite
        This function is only available to the System Administrator. You must login, System>
        Administrator Login, as the Administrator to access these controls
        Depending on the level of software, User's are given permission to perform tasks based
        on their Group assignment in Gen5 Secure or the User Permissions given to all users
        in all other levels of Gen5.

   Gen5 Secure
        User Permissions are defined by the User Group. When you select or change a user's
        Group assignment you're simultaneously assigning their permissions:
          1.    Select Security> Users
          2.    Highlight the user and click Edit (or double click the user record)
          3.    Use the drop-down list to change the Group assignment0.






         See Modifying User Permissions (on page 401) to change the
          permissions assigned to a group

  Gen5, Gen5 ELISA, Gen5 Reader Control
      For all levels of Gen5, except for Gen5 Secure, there are only two types of users: System
      Administrator and User (non-administrator). The System Administrator can set or
      change the User Permissions for non-administrators. Gen5 provides all user rights and
      privileges to administrators.

  To change User Permissions:
       1.   Login as the System Administrator
       2.   Select Security> User Permissions
       3.   Add or remove a tick mark for each permission to give or deny access to it to
            all non-administrator users0.




About User Groups

        For Gen5TM Secure Only

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



400 | Chapter 18: Security



                           Click New to set up a new group

                         Highlight a group and click Edit to modify its name and
                permissions

                          Highlight a group and click Delete to remove it as an option. First
                you must reassign any users to another group. You cannot delete a group with
                users assigned to it.


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

           See important information about expired passwords on page 387.






Startup Action
     Use the drop-down to select the preferred method for starting Gen5:
            Startup Window is the default setting, it offers several options including
              creating a new item or opening a recently used item
            Create new experiment opens Gen5 with the Protocol selection dialog
              open, as if the user had selected File>New Experiment
            Start at main menu opens Gen5 showing the File, System and Help menus
              only. Since neither a protocol or experiment is open, the workspace is blank.

Protocol and Experiment Folders
     Browse to or enter the full path and directory to define the folder in which the current
     user will typically store protocol and experiment files. If a folder is not specified, Gen5
     will default to the most recently-accessed folder.

Password
     Assign a password for the user to enter the first time he/she logs in to Gen5. Instruct
     users to change their password after the first login using the Password you've
     assigned. Users can only change their own password. System Administrators can
     change any user's password.


Modifying User Permissions in Gen5 Secure

       For Gen5TM Secure Only

  System> Security> Groups> Edit
     User's are given permission to perform tasks based on their Group assignment in Gen5
     Secure.

Prerequisite
     This function is only available to the System Administrator. You must login,
     System>Login/Logout, as the Administrator to access these controls

How to Change User Permissions:

      1.               Select System> Security> Groups, highlight the group and click
           Edit to change the permissions or access rights of group members. Or click
           New to create a new user group.

      2.   Add or remove a check mark for each function to grant access or deny it.0.



402 | Chapter 18: Security



              Denying user permissions usually results in making the applicable dialog Read
              Only.

Permissions

  Protocol/Experiment Controls
        This table describes the capability each Permission gives users. The Audit Trail icon
        shows when Gen5 Secure logs the activity in the Protocol or Data Audit Trails. Links
        are provided to learn more about the function.

    Function                                                                          Audit
                                                                                      Trail

    Create a new Protocol: Access to menu options File>New Protocol,
    File>Save As, and Startup Page options to create a new protocol file

    Open a Protocol: Access to File>Open, Recent Files List and Startup Page
    options to open an existing protocol

    Perform a Quick Read/Use default protocol: Access to creating an
    experiment from the default protocol

    Add a New Plate: Access to menu options and toolbar buttons for Adding
    one or multiple plates to an experiment

    Delete a plate: Access to Plate menu option to Delete, i.e. remove the plate
    information and all data associated with the plate (if any) from an experiment

    Create/Edit Sample IDs: Access to Plate menu and menu tree options to
    enter or modify Sample IDs for each plate or in a Batch for multiple plates

    Edit Plate Information: Access to Plate menu and menu tree options to
    modify the Plate Information. Note: Information is intended to be captured at
    run-time, for each plate in an experiment

    Mask/Unmask values: Access to Mask button in data views to select
    individual wells and mark them to be ignored in data reduction and curve
    plotting

    Edit values: Access to Change button in data views to select individual wells
    and change/enter alternative data for use in curve plotting and data reduction

    Re-read plate: Access to Read button after plate has been read to overwrite
    the current measurement results with newly acquired measurements

    Simulate Read: Access to Simulate option of the Plate Read dialog to let
    Gen5 simulate a reading instead of actually reading the plate. (Useful for
    Gen5 training/tutorials.)

    Read from File (import): Access to Read From File option of the Plate Read
    dialog to acquire/import reading data from a text file






Enter Manually (raw data): Access to Enter Manually option of the Plate
Read dialog to manually enter (type in) reading data instead of actually
reading a plate

Edit Protocol: This switch gives or denies access to the next nine related
functions. You can override it by individually selecting the permissions and
assigning access

Edit Procedure: Access to the Procedure dialog to alter the reading
requirements and related events, like Delay, Shake. Gen5 always prohibits
users from changing an experiment's Procedure after the first plate is read

Edit Plate Layout: Access to the Plate Layout dialog to change the plate
layout, Well IDs, Concentrations/Dilutions

Edit Data Reduction: Access to the Data Reduction dialog to change data
reduction steps, add new steps or alter existing ones

Edit Report Builder: Access to the Report Builder to create or modify the
report definitions

Edit Runtime Prompts: Access to create or modify the "prompts"
(information requests) presented to users at read time. Users' responses
become Plate Information

Edit Data Views: Access to alter the format/font of data views items; create
custom data views

Edit File Export Builder: Access to select and modify the content for export
to a text file; define the filename and format settings for export files

Edit Power Export Builder: Access to select and modify the content for
export to Excel(R)

Edit Protocol Options: Access to define miscellaneous, protocol-related
parameters


System Controls
    This table describes the capability each Permission gives users. The Audit Trail icon
    shows when Gen5 Secure logs the activity in the System Audit Trail

Function                                                                           Audit
                                                                                   Trail

Manage and Maintain Systems: This switch gives or denies access to the
next five items. You can override it by individually assigning access to the
permissions

Edit Default Protocol: Access to define or modify the Default Protocol
Settings

Edit file storage mode: Access to menu option System>Preferences>File
Storage to alter the option: database or Windows(R) file system



404 | Chapter 18: Security



    Edit Read from File options: Access to menu option
    System>Preferences>Read from File Settings to alter the designation of the
    text delimiter for importing data via text files

    Manage and maintain Database: Access to change the location of the local
    and shared databases, and their backups. Run maintenance tasks and tests,
    and repair errors. Only when File Storage "uses the SharedDB"

    Delete System Audit Trail Events after export: Access to delete records
    after exporting them to a text file. All users can export records, only users
    with this permission are able to delete them

    Manage and Maintain Devices: This switch gives or denies access to the
    next four related permissions. You can override it by individually assigning
    access to them

    Edit Reader Settings: Access to Reader Configuration to set up and alter
    the settings. Denying access restricts the user's ability to change a reader's
    filter/wavelength settings in Gen5

    Edit Plate Types: Access to create, modify or delete records in the Plate
    Type Database

    Define Universal Plates: Access to Diagnostics options to set up and modify
    the Universal Test Plate records used to conduct testing

    Delete Diagnostic Test History: Ability to delete test records. All users can
    view the test history, only users with this permission can delete the records

    Manage and Maintain File Storage: This switch gives or denies access to
    the next seven related permissions. You can override it by individually
    assigning access to them. They are only applicable when File Storage "uses
    the SharedDB"

    Create folder in Database: Ability to create a new folder while maintaining
    database files and when saving protocol and experiment files. Users denied
    this function are limited to saving files in existing database folders

    Delete/Overwrite folder in Database: Ability to delete or overwrite (Save
    As) folders and files from/in the database

    Export file from Database: When maintaining database files, ability to use
    the right-click menu to Export to Disk

    Rename folder/file in Database: Ability to rename database files and
    folders in the database

    Move folder/file in Database: Ability to relocate folders and files within the
    database

    Import file to Database: Ability to import, paste from clipboard, or drag
    and drop files from another location
