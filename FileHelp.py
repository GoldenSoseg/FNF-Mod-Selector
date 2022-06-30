from win32com.client import Dispatch
import os

#Thank you so fucking much, Mouse vs Python
def createShortcut(path, target='', wDir='', icon=''):    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    if icon == '':
        pass
    else:
        shortcut.IconLocation = icon
    shortcut.save()

def makelistsLines(path):
    filesupp = open(path, "r")
    mod_lines = []
    for line in filesupp:
        mod_lines.append(line)
    
    supported_mods = []
    for element in mod_lines:
        supported_mods.append(element.replace("\n", "").split(","))
    
    return supported_mods

def supportedList(folder):
    listSupport = []
    for filename in os.listdir(folder):
        listSupport = listSupport + makelistsLines(folder + "/" + filename)
    
    return listSupport