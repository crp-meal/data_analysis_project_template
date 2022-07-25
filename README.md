# data_analysis_project_template

This is a generic project template. Its purpose is to serve as a scaffold for quickly setting up a familiar project structure.

data_analysis_project_template/
├── cookiecutter.json
├── README.md
└── {{cookiecutter.project_name}}/ (Root directory)
    └── packages/
        └── {{cookiecutter.package_name}}/              # Generated folder, named during project initialization
            ├── config.yml                              # Specifies project parameters, file names and variables.
            ├── logs/                                   
            │   └── log.txt                             # Captures information of data processing activities in project.
            ├── requirements.txt                        # Lists all dependencies required for project to perform.
            ├── tox.ini                                 # Configuration file for managing settings for virtual environment and testing.
            └── {{cookiecutter.package_name}}/          # Generated folder, named during project initialization.
                ├── config/
                │   ├── config.py                       # Settings defining variables for project structure and reading settings from config.yml.
                │   └── logging.py                      # Defining logging functionality, called by modules throughout package.
                ├── input/
                │   └── data/
                │       └── raw_data.csv                # Locally stored data file.
                ├── main.py                             # Main executing module; collects modules and runs project functionality in specified order.
                ├── output/
                │   └── graphical_output/               # Storage point for output of graphical output, such as statistical charts.
                ├── pipelines/
                │   └── pipelines.py                    # Specifies execution sequence of data processing steps (preprocessors and analyzers)
                ├── processing/
                │   ├── analyzers.py                    # Defines format (template) for individual data analytical units. Executes as part of pipeline.
                │   ├── data_management.py              # Defines data load and export functionality.
                │   └── preprocessors.py                # Defines format (template) for individual data transformation units. Executes as part of pipeline.
                ├── VERSION                             # Specifies version of project; major/minor/patch
                └── visualization/
                    └── graphing.py                     # Helper functionality for drawing graphs.