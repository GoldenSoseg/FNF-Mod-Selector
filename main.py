from filemethods import FileHandling
from window import Window
from modlist import ModList

def main():
    window = Window(640, 480, "Friday Night Funkin' Mod Selector")
    filehandler = FileHandling()
    filehandler.open_or_create()
    filehandler.check_directory()
    dir = filehandler.open_or_create()
    modlist = ModList(dir)
    window.add_text("Choose a mod")
    window.combobox_run(modlist.modnames)
    window.run_button("Select")
    window.run_window()

    modlist.select_mod(window.modsvar.get())
    
    
if __name__ == "__main__":
    main()