# Lemmy_MetalNewReleasesBot
A bot that posts new Metal releases (Albums, Singles) to Lemmy in a weekly release thread.

## Installation
I recommend setting up a virtual environment to install the python requirements

Linux
```
cd /this/git/project
python3 -m venv your_environment
source env/bin/activate
```
Windows
```
cd /this/git/project
py -m venv your_environment
.\env\Scripts\activate
```
Now you can install pip packages normally and they will be installed into the virtual env instead of your global python install. If you want to install additional pip packages at a later time just rerun the cd and virtual env activate commands to reenter the virtual environment.

Installing the requirements
```
cd /this/git/project
```
Linux
```
python3 -m pip install -r requirements.txt
```
Windows
```
py -m pip install -r requirements.txt
```
