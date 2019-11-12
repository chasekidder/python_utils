#!/usr/bin/python3

from pathlib import Path
import os
import PySimpleGUI as sg
import itertools


result = []
dupes = []
temp = []

#Get Path To Search
path = sg.popup_get_folder('Duplicate Finder - Count number of duplicate files', 'Enter path to folder you wish to find duplicates in') 

if path is None:
    os._exit(0)

#Populate list of files
result = list(Path(path).rglob("*.*"))

result = [file for file in result if os.path.basename(file.__str__()) != "Thumbs.db"]

result = [x.__str__() for x in result]

#Check For Duplicates
for file in result:
    if os.path.basename(file) in temp:
        dupes.append(os.path.basename(file))
    else:
        temp.append(os.path.basename(file))

# Grab full path and basename for sorting/display
dupes = [(file, os.path.basename(file)) for file in result if os.path.basename(file) in dupes]

# Sort By Base Name
dupes = sorted(dupes, key=lambda x: x[1])

#Remove Base Name Dimension
dupes = [file[0] for file in dupes]

#Check if no duplicates were found
if len(dupes) == 0:
    dupes = ["No Duplicates Found!"]

#Create Results Window Layout
layout = [[sg.Listbox(dupes, size=(60, 20))]]

#Create Results Window
window = sg.Window("Duplicate Checker Results", layout)
window.Read()
