import os

class ModList:
    def __init__(self):
        self.path_mods = "C:\\Users\\aleja\\Documents\\Friday Night Funkin"
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.path_mods):
            files.extend(filenames)
            break
        
        files = [(element.replace(".lnk", "")) for element in files]
        self.modfiles = files
    
    def print_mods(self):
        print(self.modfiles)

    def select_mod(self, modname):
        filename = modname + ".lnk"
        for dirpath, dirnames, files in os.walk(self.path_mods):
            if filename in files:
                file_found = os.path.join(dirpath, filename)

        return file_found