Installation Steps:
==========================================
Install python and pip
1. Install python
For windows:
https://www.python.org/downloads/windows/

For linux:
For ubuntu 14.04
================
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6

For Ubuntu 16.04
================
sudo apt-get update
sudo apt-get install python3.6


pip comes installed with python, using that install virtualenv
2. Install virtualenv
=====================
pip install virtualenv

Also using pip install flask
3. Install flask
=====================
pip install flask

4. Create your personalized environment
=======================================
virtualenv 'your_env'
or
cloned from github (in our case: git@github.com:ColumbiaPythonUsersGroup/Check_Calculator.git)

=======================================================================================================================

Updates
========

# Simple_GUI_Check_Calculator

This is going to be a GUI application that will allow the user to input their inforamtion that would typicaly go into a check.  This is an excersize to learn how to import one application into the next as well as how to build my own back end program that will connect to the front end of a GUI application.

# Updates - 10/13/17
Created GUI Frontend that calls the Backend application for weekly pay frequency with both married and single.  The Backend then calls the updated IRS modules that are imported into the Backend application.  The IRS madules have been split into their respective filing status as well as frequency table.  The federal tax amount is then returned and output through the GUI.

# Updates - 10/27/17
- Changed Python version from 2.* to 3.*

-- This will allow the GUI to be formatted easier by using the .grid() method instead of the .pack() method
- Started working on a web GUI instead of a tkinter GUI using HTML and CSS

-- I am still trying to figure out how I would like the web app to work. 
- Added a Flask backend to Backend.py

# Updates 11/1/17
- Was able to output to the netcheck.html page from the calculation within the Backend.py program

- Added some more fields to the index.html page that will be needed in order to get an accutate Net amount

-- Will work on addind these items to the backend once modules are done

# Updates 11/11/17
- added a file for federal tax brackets
- added a function to calculate federal taxes
- changed the IRS_Married_Weekly and IRS_Single_Weekly to use
simplified tax brackets and tax calculation
- removed old federal tax table file
