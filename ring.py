#!/usr/bin/python

###########################################################
#File Browser
#Ring Style
#Written by
#Andrew Gardner

import os
import glob
Home = "/home/gardn227/"

def GoHome():
    '''
    Jump to Home Directory.
    '''
    os.chdir(Home)

def Action(child):
    if os.path.isdir(child) and child in os.listdir(os.getcwd()):
        os.chdir(os.getcwd() + '/' + child)
        return "now in: " + os.getcwd()
    elif child.lower() == 'up':
        return "going UP"
    elif child.lower() == 'home':
        GoHome()
        return "now in: " + os.getcwd()
    elif child.lower() == 'exit':
        exit()
        return "quitting"
    elif child in  os.listdir(os.getcwd()):
        os.system('xdg-open "' + child + '"')
        return "Opening file"
    else:
        return "not valid, retry"
        

def ListChildren(ShowHidden = 0):
    '''
    This program lists the Children files and directories of the current
    directory.
        if ShowHidden is 0 (default), hidden files and folders are not shown.
        otherwise, They are shown
    '''
    InnerDirectories = []
    if ShowHidden == 0:
        for folder in os.listdir(os.getcwd()):
            if folder[0] != '.':
                InnerDirectories.append(folder)
    else:
        for folder in os.listdir(os.getcwd()):
            InnerDirectories.append(folder)
    InnerDirectories.sort()
    return InnerDirectories

GoHome()
currentkids = ListChildren()
print "The contents of this directory are: "
print currentkids

print "Either input a file or directory name, or use 'up' or 'home'"
while True:
    UserChoice = raw_input('Choose a file or directory: ')
    print Action(UserChoice)

