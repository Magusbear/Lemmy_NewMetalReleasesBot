# Lemmy_MetalNewReleasesBot
A bot that posts new Metal releases (Albums, Singles) to Lemmy in a weekly release thread.

## Installation
### Running in Virtual Environment
I recommend setting up a virtual environment to install the python requirements

Linux
```
cd /this/git/project
python3 -m venv your_environment
source your_environment/bin/activate
```
Windows
```
cd /this/git/project
py -m venv your_environment
.\your_environment\Scripts\activate
```
Now you can install pip packages normally and they will be installed into the virtual env instead of your global python install. If you want to install additional pip packages at a later time just rerun the cd and virtual env activate commands to reenter the virtual environment.

### Installing the requirements

1. You need Firefox installed on your system for this to work. I'm working on removing this requirement though.
2. cd to the git project
```
cd /this/git/project
```
3. Activate your Virtual Environment (skip this step if you don't want to work with a virtual environment)

Linux
```
source your_environment/bin/activate
```
Windows
```
.\your_environment\Scripts\activate
```
4. Install the requirements
Linux
```
python3 -m pip install -r requirements.txt
```
Windows
```
py -m pip install -r requirements.txt
```
## Usage
Run

Linux
```
cd /this/git/project
source your_environment/bin/activate  <- Skip this if you're not using a virtual environment
python3 metal-archives-scraper.py 
```
Windows
```
cd /this/git/project
py -m venv your_environment
.\your_environment\Scripts\activate  <- Skip this if you're not using a virtual environment
.\metal-archives-scraper.py 
```
