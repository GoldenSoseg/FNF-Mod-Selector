import Mod
import ModList
import FileHelp

suppmods = FileHelp.supportedList("supportedMods")
modlist = ModList.ModList(suppmods, "C:/Users/aleja/Documents/Friday Night Funkin/Files")
mod = modlist.getMod(16)
modFullName = mod.getFullName()
print(modlist.displayNames())
print(modFullName)
