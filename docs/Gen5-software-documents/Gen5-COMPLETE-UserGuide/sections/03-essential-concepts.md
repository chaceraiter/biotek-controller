# Chapter 3: Essential Concepts

     This section reveals the basic concepts upon which Gen5 was built.
     Learning them will enhance your experience using Gen5.


 Experiment vs. Protocol ............................................................ 45
 File Storage............................................................................. 47
 Best Practices.......................................................................... 48



44 | Chapter 3: Essential Concepts




Essential Concepts
         Understanding the basic concepts behind Gen5's structure and behavior will help you
         make the most of it. A few topics are covered here, on the next few pages, more
         information is provided in Gen5's Help.
            Experiment vs. Protocol on page 45
            File Formats:
               Gen5's files are identified by their filename extension:
                .prt = Protocol file
                .xpt = Experiment file (contains the protocol and any data acquired or
                  generated within the experiment)
            File Storage on page 47
            Best Practices on page 48

In Gen5, select Help>Help Topics to find:
            Multiple-Plate Experiments
            Security and FDA Electronic Records Compliance

           Only the Gen5 Secure level of software offers all the capability
             required to meet the FDA's electronic records requirements: SS21 CFR
             Part 11.






Experiment vs. Protocol
    Gen5TM uses two common terms to define distinct elements of its toolkit. The
    distinction is subtle and understanding it will improve your Gen5 experience.

   Protocol      (*.prt)                       Experiment       (*.xpt)

   A protocol is a "recipe" or set of          An experiment has a copy of the
   instructions designed to capture,           protocol and at least one plate. It
   transform and report and/or export          executes the instructions provided by
   data                                        the protocol to produce results

   Protocols are created and saved as          While an experiment is created using an
   standalone files. They function as a        existing protocol, the experiment's copy
   template; an unlimited number of            of the protocol can be modified within
   experiments can be based on one             the experiment

   A protocol consists of reading              Running an experiment is the only way
   requirements, like detection method         to process a protocol. Gen5's Quick
   and wavelength, and reading-related         Read function may at first appear to
   actions, like shaking and incubation        skip the protocol development stage,
   (Procedure), plate layout, data             but it uses the default protocol, and
   reduction, and data viewing, reporting      generally requires reading parameters
   and exporting definitions                   to be defined

   A protocol can be used repeatedly (as-      Multiple plates can be processed in an
   is or modified) within experiments. By      experiment; each one considered a
   itself, a protocol does not produce         unique assay with independently
   results. Protocols do not have plates       reported or exported results. The
   associated with them                        exception is multi-plate protocols,
                                               described later

   .prt is the protocol's filename extension   .xpt is the experiment's filename
                                               extension

   A copy of the protocol is saved within      An experiment is saved as the full
   an experiment, or as a standalone .prt      collection of procedures, formulas,
   file. Since protocols do not have plates,   reporting definitions, and other details,
   they cannot generate data outside of an     i.e., the protocol, and the plate data
   experiment                                  from readings and calculation results

   The Gen5TM Secure level of software          Data acquired and transformed in an
   maintains an audit trail of all activity    experiment is protected by an audit trail
   and changes related to a protocol. All      in both Gen5 Secure and other Gen5
   other Gen5TM software levels do not          software editions. The Reader Control
   support this feature                        edition does not support this feature



46 | Chapter 3: Essential Concepts




       Protocol      (*.prt)                      Experiment      (*.xpt)

       Changes made to a standalone protocol      Within an experiment, you can select
       are not reflected in any previously        Save Protocol As to capture the current
       created experiments based on that          details of the protocol and save them as
       protocol. A new experiment must be         either a new protocol or as an overwrite
       created to apply the revised protocol      of the original protocol



           All newly created protocols and (unless another protocol is selected)
             experiments are based upon the Default Protocol

           Gen5TM also supports more complex multi-plate protocols that are not
             covered in this introductory material. Check out: Designing a Multi-
             Plate Protocol in a subsequent chapter.






About File Storage

File Types
    Gen5TM creates two file types: Protocol = .prt and Experiment = .xpt
          The Gen5 executable file (.exe) and numerous other types of supporting files,
            like an Excel(R) template, are also installed on the computer.
          In addition, ClarityTM Microplate Luminometer users will work with Clarity
            protocol files, which use a .BPF extension. Gen5 references the Clarity files as
            they contain the reading parameters required to control the luminometer.

Databases
       Gen5 installs two databases on your system called LocalDB and SharedDB. While the
       databases are always used for critical, internally-used files, Gen5 offers you the choice
       of using the Windows(R) File System or the Gen5 (SharedDB) database for storing Gen5's
       Protocol (.prt) and Experiment (.xpt) files. This option, combined with the ability to
       create multiple databases, allows you to structure file storage according to your
       organization's requirements.
          Files may be stored on the computer's hard drive, on a network, or on a CD or
            other portable medium. Windows Explorer or a similar application can be used
            to view the file names and locations, and to move, copy, rename, and delete
            files.
          Alternatively, protocol and experiment files may be stored in a secure, shared-
            access database. This database, initially named SharedDB.mdb, can be stored
            on a user's computer or on a shared-access network/computer (LAN). Gen5
            provides a special file maintenance utility for viewing the file names and their
            locations, and for moving, copying, renaming, deleting, importing, and
            exporting files.
          Select the preferred method of storing protocol and experiment files at
             System>Preferences>File Storage

File Location
       During a conventional installation:
              the program files are stored in this default location: C:\Program
                Files\BioTek\Gen5 (software edition)
              the databases are stored in these default locations:
                Windows XP and 2000 systems: C:\Documents and Settings\All
                Users\Application Data\BioTek Instruments\Gen5 (software
                edition)\(version #)\SharedDB or LocalDB
                Windows Vista: Windows XP and 2000 operating systems: C:\Program
                Data\BioTek \Gen5 (software edition)\(version #)\SharedDB or LocalDB
              Gen5 installs Protocol and Experiment folders in the respective File Storage
                locations, e.g. C:\Program Files\BioTek\Gen5 (software edition)\Protocol



48 | Chapter 3: Essential Concepts




Best Practices
         Like most software tools, Gen5TM is flexible, it offers several ways to accomplish a task.
         Here are some recommendations for saving time and using it most efficiently:

Efficiencies
            For an assay or experiment that you will run numerous times, develop a
              Protocol to define the Procedure, Data Reduction, Data Views and Reports
              required. Then you can run an Experiment (File>New Experiment) based on
              the Protocol whenever necessary. You can fine-tune the protocol within an
              experiment, but remember to select File>Save Protocol As to update the
              original protocol with your improvements.
            Just like word processing documents, when you run similar types of
              experiments, you can use File>Save As to give you a head start creating a new
              protocol based an existing protocol that contains the same plate layout, reading
              parameters, or other elements that will be repeated in your new protocol.
            Define and customize Data Views before selecting what to include in reports or
              export files. All the on-screen data (i.e. data views) can be reported or exported.
              If you use on-screen views and paper reports equally, it is most efficient to first
              fine-tune the Data Views, and then include them in reports/exports.
            Always assign Blanks to the plate. Blanks can be deionized (DI) water, buffer,
              reagent without analyte, substrate and so on. When running fluorescence
              cellular assays, a DI-water blank illustrates the background contributed by the
              instrument and labware as separate from the cells and media. Identify the
              location of the Blanks in the Plate Layout and Gen5 will automatically create
              the blank-subtraction data reductions.
            Backup your database regularly, BioTek recommends once per week for most
              organizations. If you're using Gen5's Database for protocol and experiment file
              storage, use the built-in Periodic Optimization feature.
            Take action if you get a warning message about the remaining size of your
              databases, see Maintaining Files for instructions on reducing the database size.
            Consider using Gen5's automatic Save feature to create a new, date-stamped
              folder for storing experiment records. This is an especially good practice for
              large labs with multiple users who run hundreds of plates per day. Gen5 will
              keep all that data organized by date. Define this kind of file management
              setting in the Default Protocol so it will apply to all newly created protocols.
            Turn off the Multi-Read Calculation option to improve Gen5's performance.
              Calculation results will be the same, but your PC's resources will not be
              diverted for performing interim calculations.






Time Savers
        Partial Plate: for assays using strips or partially-filled plates, especially if the
          read steps are long or complicated, you can save time by telling the reader
          exactly which wells or portion of the plate to read
        Default Protocol: all newly created protocols and Quick Reads are based on the
          Default Protocol. If some protocol elements, like plate layout, runtime prompts,
          report headers and footers, etc., are largely the same for most of your projects,
          you'll save significant time by defining these elements before creating the next
          protocol/experiment
        Print Preview: save time and paper by viewing reports on-screen before
          sending them to the printer



50 | Chapter 3: Essential Concepts
