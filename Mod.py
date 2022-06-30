import os
from FileHelp import createShortcut

class Mod:
    def __init__(self, name, folder, fullname, banner, icon, exefile):
        self.name = name
        self.folder = folder
        self.fullname = fullname
        self.banner = banner
        self.icon = icon
        self.exefile = exefile
        
    def getName(self):
        return self.name
    
    def getFolder(self):
        return self.folder
    
    def getFullName(self):
        return self.fullname
    
    def getBanner(self):
        return self.banner
    
    def getIcon(self):
        return self.icon
    
    def loadMod(self):
        lnk_path = self.exefile.removesuffix(".exe") + ".lnk"

        createShortcut(lnk_path, self.exefile, self.folder, self.exefile)
        os.system('cmd /c "' + lnk_path + '"')
        os.remove(lnk_path)