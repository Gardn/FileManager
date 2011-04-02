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
print ListChildren()
print ListChildren(1)
