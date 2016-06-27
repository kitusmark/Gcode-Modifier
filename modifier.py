#!/usr/bin/python -tt
# -*- coding: utf-8 -*-



"""A tiny Python program to modify some parameters on Gcodes
generated by Slic3r or similar.
The main objective is to modify 3D printer Gcode to be able to print with larger
printers controlled by MACH3 and with a VFD driving a pump
"""

import sys
import os
import re
import glob
import shutil

#-------------------VARIABLES--------------------

def parseFile(file):
    lines = 0
    layers = 0
    f = open(file)
    for line in f:
        lines += 1
        layerMatch = re.search(r'[Z][0-9]*',line,)
        if layerMatch:
            layers += 1
        else:
            pass

    print 'There are %d lines in the file' %(lines)
    print 'There are %d layers in the file' %(layers)

def removeAAxis(gcode):
    option = str(raw_input('Do you want to remove A Axis from the G-code? '))
    if option == "yes":
        #let's do This
        print 'Reading the entire file...'
        parseFile(gcode)
        #print 'Removing A Axis from the file...'
        #print 'Done!'
    elif option == "no":
        pass
    else:
        print 'Type yes or no please'
        removeAAxis()

# Define a main() function that prints a little greeting.
def main():
    print 'Welcome to the G-code Modifier Utility'
    #Get the arguments of the program and decide what to do
    if len(sys.argv) >= 2:
        #the argument should be a .gcode file
        if sys.argv[1].endswith(".gcode"):
            gcodeFile = sys.argv[1]
            print 'The file selected is: ', gcodeFile
        else:
            #There has been an Error
            print 'The file is not valid. Write it exactly as it is.'
            print '\n\n\n'
            main()
    else:
        #We should print all the available .gcode files in the working directory
        print 'No input file detected. Here are the available .gcode files in '
        print os.getcwd() + ' :'
        for file in glob.glob('*.gcode'):
            print '->' + file + '\n'
        #Now we have to select the file we want to work with
        rawInput = str(raw_input('Please type the g-code file you want to work with: '))
        if rawInput.endswith(".gcode"):
            #The input file is a valid file!
            gcodeFile = rawInput
            print 'The file selected is: ', gcodeFile
        else:
            #There has been an Error
            print 'The file is not valid. Write it exactly as it is.'
            print '\n\n\n'
            main()
    #Now let's make a copy of the file to modify it
    gcodeFileModified = gcodeFile[:gcodeFile.find(".")] + '_prepared.gcode'
    #print gcodeFileModified
    print 'Making a copy of the file...'
    shutil.copy2(gcodeFile, gcodeFileModified)
    print 'Done! Copied to ' + gcodeFileModified
    #Now let's start modifying the gcodeFileModified itself
    removeAAxis(gcodeFileModified)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()