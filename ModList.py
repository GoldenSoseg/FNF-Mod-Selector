from Mod import Mod
import os
import os.path as op

class ModList:
    def __init__(self, supportedMods, folder):
        self.mods = []
        directoriesTemp = []
        for (dirpath, dirnames, filenames) in os.walk(folder):
            directoriesTemp.extend(dirnames)
            break
        
        directories = []
        names = []
        fullnames = []
        for name in directoriesTemp:
            i = 0
            while i < len(supportedMods):
                if name in supportedMods[i][0]:
                    names.append(name)
                    directories.append(folder + "/" + name)
                    fullnames.append(supportedMods[i][1])
                    break
                i += 1
        
        exefilesTemp = []
        for element in directories:
            for (dirpath, dirnames, filenames) in os.walk(element):
                exefilesTemp.extend(filenames)
        
        exefiles = []
        for element in exefilesTemp:
            if "UnityCrashHandler64.exe" in element: continue #Vs Hecker
            elif "FE-CrashDialog.exe" in element: continue #SMB Funk Mix/Game Over

            else:
                if ".exe" in element:
                    exefiles.append(element)
    
        i = 0            
        while i < len(exefiles):
            exefiles[i] = directories[i] + "/" + exefiles[i]
            i += 1
        
        
        banners = []
        icons = []
        
        for element in names:
            banners.append("modData/banners/" + element + ".png")
            icons.append("modData/icons/" + element + ".png")
            
        i = 0
        while i < len(names):
            if not op.exists(banners[i]):
                if not op.exists(icons[i]):
                    mod = Mod(names[i], directories[i], fullnames[i], "modData/defaultBanner.png", "modData/defaultIcon.png", exefiles[i])
                    self.mods.append(mod)
                else:
                    mod = Mod(names[i], directories[i], fullnames[i], "modData/defaultBanner.png", icons[i], exefiles[i])
                    self.mods.append(mod)
            elif not op.exists(icons[i]):
                mod = Mod(names[i], directories[i], fullnames[i], banners[i], "modData/defaultIcon.png", exefiles[i])
                self.mods.append(mod)
            else:
                mod = Mod(names[i], directories[i], fullnames[i], banners[i], icons[i], exefiles[i])
                self.mods.append(mod)
            i += 1
        
    def displayNames(self):
        displayNames = []
        for element in self.mods:
            name = element.getFullName()
            displayNames.append(name)
            
        return displayNames
    
    def listBanners(self):
        bannerList = []
        for element in self.mods:
            banner = element.getBanner()
            bannerList.append(banner)
            
        return bannerList
            
    def listIcons(self):
        iconList = []
        for element in self.mods:
            icon = element.getIcon()
            iconList.append(icon)
        
        return iconList
    
    def getMod(self, n):
        mod = self.mods[n]
        
        return mod