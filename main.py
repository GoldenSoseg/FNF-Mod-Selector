from window import Window
from modlist import ModList

def main():
    window = Window(640, 480, "Friday Night Funkin' Mod Selector")
    dir = window.askdirectory()
    modlist = ModList(dir)
    window.add_text("Choose a mod")
    window.combobox_run(modlist.modnames)
    window.run_button("Select")
    window.run_window()

    modlist.select_mod(window.modsvar.get())
    
    
if __name__ == "__main__":
    main()