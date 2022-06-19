from window import Window
from modlist import ModList
import subprocess

def main():
    modlist = ModList()
    window = Window(640, 480, "Friday Night Funkin' Mod Selector")
    window.add_text("Choose a mod")
    window.combobox_run(modlist.modfiles)
    window.run_button("Select")
    window.run_window()
    modfile = modlist.select_mod(window.press_button())
    subprocess.call(modfile, shell=True)
    
if __name__ == "__main__":
    main()