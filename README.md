# Project 1 - Computer architecture 2
**Created by:** Dagoberto Rojas Juárez

**University ID:** 2015127575

## Install dependencies

### Create a virtual environment
First, let's create a virtual environment, this way once you remove the project you also remove the dependencies.

For this step, it is necessary to have python 3.9 installed, since the project is developed in and for that specific python version.

*Using different versions might cause the applicaion to crash, to not to work, or produce unexpected behaviors.*

Run the following commands in the root folder of the project

**Windows**

    py -m venv env
    .\env\Scripts\activate

**Linux and OS X**

    python3 -m venv env
    source env/bin/activate

To confirm you are using the virtual environment run:

**Windows**

    where python

**Linux and OS X**

    which python

The previous command should display the locations where python is installed, the first one being the virtual environment just activated.

Once you complete the execution of this project, you can deactivate the virtual environment by typing:

    deactivate

### Install dependencies
To install dependencies, please use the following command on the root folder of the project:

    pip install -r requirements.txt

The previous command is going to install the requirements listed in the file *requirement.txt*
    