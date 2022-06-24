import os
from tkinter import filedialog as fd

class ModList:
    def __init__(self):
        self.mods_folder = fd.askdirectory()
        mods = []
        for (dirpath, dirnames, filenames) in os.walk(self.mods_folder):
            mods.extend(dirnames)
            break

        mod_execs = []
        for (dirpath, dirnames, filenames) in os.walk(mods):
            mod_execs.extend(filenames)
            break

        for element in mod_execs:
            if ".exe" not in element:
                mod_execs.remove(element)

        self.modnames = mods
        self.modfiles = mod_execs
    
    def print_mods(self):
        print(self.modfiles)

    def select_mod(self, modname):
        filename = modname + ".lnk"
        for dirpath, dirnames, files in os.walk(self.path_mods):
            if filename in files:
                file_found = os.path.join(dirpath, filename)

        return file_found