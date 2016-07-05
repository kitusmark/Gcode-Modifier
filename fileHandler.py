#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#Marc Cobler Cosmen - June 2016
#Released under MIT LICENSE
#https://opensource.org/licenses/MIT

"""Custom Python module to control some file handling stuff"""

from shutil import copy2
import os

def getFileExtension(name):
    """
    Gets the file extension of the file. Including the '.'
    """

    extension = name[name.find("."):]
    #print extension
    return extension

def findFileInDir(filename, dir='.'):
    """
    Returns boolean. if the file is in the directory specified or not.
    By default the directory is the same as the running script
    """
    found = False
    filesList = os.listdir(dir)
    if filename in filesList:
        found = True
    else:
        pass
    #print found
    return found

def copyFile(file, extension=''):
    """
    Makes an exact copy of the file especified. If you specify an extension, the function put it before the '.'
    For example file='test.txt', extension='_copy' --> copied file will be test_copy.txt
    Returns the name of the new copied file
    """
    #Now let's make a copy of the file to modify it
    gcodeFileModified = file[:file.find(".")] + extension + file[file.find("."):]
    #print gcodeFileModified
    print 'Making a copy of the file...'
    shutil.copy2(file, gcodeFileModified)
    print 'Done! Copied to ' + gcodeFileModified
    return gcodeFileModified

def makeBlankFile(basename, extension = '', format = '.txt'):
    """
    Makes a new file in the current directory. You can specify an extension for the file and a file format.
    Return the name of the new blank file just created
    """
    fileName = basename[:basename.find(".")] + extension + format
    blankFile = open(fileName, 'w+')
    blankFile.close()
    return fileName
