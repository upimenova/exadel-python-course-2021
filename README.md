# exadel-python-course-2021
Exadel Python Course 2021 for employees.

[TASKS](https://docs.google.com/document/d/1EgIJw4_dZehaOURjYDdtZI09jMlQe2AGmfneZUgxfDM/edit?usp=sharing).

## How to get started
1. Install Python
    1. the latest [Python](https://www.python.org/downloads/) version.
    2. Make sure that Python is available through the command line, check its location (`where python`  - Windows, `which python` - Linux). You may need to update your `PATH` variable.
    3. Try to run python REPL via command line:
        ```bash
        > python
        ``` 
2. Install IDE of your choice:
    * [PyCharm Community](http://www.jetbrains.com/pycharm/download) - the Python IDE from JetBrains
    * [VSCode Python extension](https://code.visualstudio.com/docs/languages/python)
    * [Python plugin for IDEA](https://www.jetbrains.com/help/idea/plugin-overview.html)
3. Install [git](https://git-scm.com/downloads) (if not installed yet)
4. Clone the repository & run `hello_world.py` 
    ```bash
    git clone https://github.com/minotru/exadel-python-course-2021.git
    cd exadel-python-course-2021
    python tasks/task00/hello_world.py
    ```
## Repository structure
Place your solution inside `tasks` folder, create a separate folder for every task. Treat every task folder as a separate project.

Example:
```
tasks/
    task00/
        hello_world.py
    task99/
        super_app.py
        requirements.txt
```

## Solution & review workflow
* Create a separate branch for each task like:
    ```bash
    git checkout -b task01
    ```
* Create a separate folder for your task:
    ```
    tasks/task01
    ```
* Solve it :)
* Commit your solution to the task branch
* Once ready with your solution:
    * Open a Pull Request (PR) to `main` from task branch
    * Add your mentors as PR reviewers
    * Resolve PR comments
    * Once PR is approved, merge it to `main` branch