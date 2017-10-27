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
