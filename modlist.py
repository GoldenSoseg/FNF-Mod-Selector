import os
import subprocess

class ModList:
    def __init__(self, folder):
        self.mods_folder = folder
        mods = []
        for (dirpath, dirnames, filenames) in os.walk(self.mods_folder):
            mods.extend(dirnames)
            break

        mod_execs = []
        for element in mods:
            for (dirpath, dirnames, filenames) in os.walk(self.mods_folder + "/" + element):
                mod_execs.extend(filenames)
                break

        self.modfiles = []
        for element in mod_execs:
            #Non-Game executable files
            if "UnityCrashHandler64.exe" in element: continue #Vs Hecker
            elif "FE-CrashDialog.exe" in element: continue #SMB Funk Mix/Game Over

            else:
                if ".exe" in element:
                    self.modfiles.append(element)

        i = 0
        while i < len(mods):
            self.modfiles[i] = self.mods_folder + "/" + mods[i] + "/" + self.modfiles[i]
            i= i + 1

        self.modnames = mods
    
    def print_mods(self):
        print(self.modfiles)

    def select_mod(self, mod_selected):
        for element in self.modfiles:
            if mod_selected in element:
                cmd = "cd " + self.mods_folder + "/" + mod_selected
                os.system(cmd)
                filename = '\"\"' + element.removeprefix(cmd.removesuffix("cd ") + "/") + '\"\"'
                os.system(filename)
                break
        