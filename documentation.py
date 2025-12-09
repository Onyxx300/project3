## Imports
import tkinter as tk

## Initialize class
class Docs(tk.Tk):
    def __init__(self, window: tk.Tk) -> None:
        self.window = tk.Tk()
        self.start()
        self.defaultdoc()

    ## Initialize window
    def start(self):
        self.window.title("Documentation")
        self.window.resizable(width=False, height=False)

        ## Initialize text block
        self.doc = tk.Label(master=self.window, text="")
        self.doc.grid(row=4, column=1)

        ## Set up button (default)
        btn_default = tk.Button(
            master=self.window,
            text="Software Suite Credits",
            command=self.defaultdoc
        ).grid(row=0, column=1, padx=10, pady=10)
        
        ## Set up button (Evasion)
        btn_evasion = tk.Button(
            master=self.window,
            text="Read Evasion Documentation",
            command=self.evasion
        ).grid(row=1, column=1, padx=10, pady=10)
        
        ## Set up button (Hungry Caterpillar)
        btn_caterpillar = tk.Button(
            master=self.window,
            text="Hungry Caterpillar Documentation",
            command=self.caterpillar
        ).grid(row=2, column=1, padx=10, pady=10)
        
        ## Set up button (Hungry Caterpillar X-Treme)
        btn_xcaterpillar = tk.Button(
            master=self.window,
            text="Hungry Caterpillar X-Treme Documentation",
            command=self.xtreme
        ).grid(row=3, column=1, padx=10, pady=10)

        ## Set up button (exit)
        btn_exit = tk.Button(
            master=self.window,
            text="Exit",
            command=self.exitapp
        ).grid(row=5, column=1, padx=10, pady=10)

    ## Load documentation (Evasion)
    def evasion(self):
        '''Loads documentation for Evasion game'''
        path = "docus/evasiondoc.md"
        with open(path, "r", encoding="utf-8") as md_file:
            content = md_file.read()
            self.doc["text"] = content

    ## Load documentation (Hungry Caterpillar)
    def caterpillar(self):
        '''Loads documentation for Hungry Caterpillar game'''
        path = "docus/caterpillardoc.md"
        with open(path, "r", encoding="utf-8") as md_file:
            content = md_file.read()
            self.doc["text"] = content

    ## Load documentation (Hungry Caterpillar X-Treme)
    def xtreme(self):
        '''Loads documentation for Hungry Caterpillar X-Treme game'''
        path = "docus/xtremecaterpillardoc.md"
        with open(path, "r", encoding="utf-8") as md_file:
            content = md_file.read()
            self.doc["text"] = content

    ## Default documentation
    def defaultdoc(self):
        '''Loads default documentation string'''
        path = "docus/default_doc.md"
        with open(path, "r", encoding="utf-8") as md_file:
            content = md_file.read()
            self.doc["text"] = content

    ## Quit
    def exitapp(self):
        '''Closes window upon click'''
        self.window.destroy()