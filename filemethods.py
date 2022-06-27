import pathlib
import tkinter.filedialog as tkfd
import os
import tkinter as tk

class FileHandling:
    def __init__(self):
        self.path = pathlib.Path("mods_path.txt")
    
    def askdirectory(self):
        root = tk.Tk()
        directory = tkfd.askdirectory()
        root.withdraw()
        
        return directory
    
    def open_or_create(self):
        if self.path.exists():
            return self.path.read_text()
        else:
            with open("mods_path.txt", "w") as file:
                file.write(self.askdirectory())
                file.close()
            
            return self.path.read_text()
    
    def check_directory(self):
        pathmods = self.path.read_text()
        if os.path.isdir(pathmods):
            pass
        else:
            os.remove("mods_path.txt")
