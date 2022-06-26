import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd

class Window:
    def __init__(self, w, h, ttl):
        self.window = tk.Tk()
        self.window.geometry(str(w) + "x" + str(h))
        self.window.title(ttl)

    def askdirectory(self):
        root = tk.Tk()
        directory = tkfd.askdirectory()
        root.withdraw()
        
        return directory

    def run_window(self):
        self.window.mainloop()

    def add_text(self, txt):
        label = ttk.Label(text=txt)
        label.pack()

    def combobox_run(self, value_list):
        self.modsvar = tk.StringVar()
        self.mods = ttk.Combobox(self.window, textvariable=self.modsvar)
        self.mods['values'] = value_list
        
        self.mods.pack()

    def run_button(self, txt):
        self.button = ttk.Button(self.window, text=txt, command=self.press_button)
        self.button.pack()

    def quit(self):
        self.window.destroy()
        self.window.quit()
        

    def press_button(self):
        self.quit()
        