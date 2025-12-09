## Imports
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

## Initialize program
class TextEdit(tk.Tk):
    def __init__(self, window: tk.Tk) -> None:
        self.window = tk.Tk()
        self.start()

    ## Initialize window
    def start(self):
        self.window.title("Text Editor")
        self.window.resizable(width=True, height=True)
        self.window.rowconfigure(0, minsize=800, weight=1)
        self.window.columnconfigure(1, minsize=800, weight=1)

        ## Initialize assets
        self.txt_edit = tk.Text(self.window)
        frm_buttons = tk.Frame(self.window, relief=tk.RAISED, bd=2)
        self.txt_edit.grid(row=0, column=1, sticky="nsew")
        frm_buttons.grid(row=0, column=0, sticky="ns")

        ## Initialize open file button
        open_file_btn = tk.Button(
            frm_buttons, 
            text="Open File", 
            command=self.open_file
        ).grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        ## Initialize save file button
        save_file_btn = tk.Button(
            frm_buttons, 
            text="Save File As...", 
            command=self.save_file
        ).grid(row=1, column=0, sticky="ew", padx=5)

        ## Initialize exit button
        exit_btn = tk.Button(
            frm_buttons, 
            text="Exit",
            command=self.return_to_sender
        ).grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        ## Draw screen
        self.window.mainloop()

    ## Initialize open file function
    def open_file(self):
        path = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not path:
            return
        self.txt_edit.delete("1.0", tk.END)
        with open(path, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
        self.window.title(f"Text Editor - {path}")

    ## Initialize save file function
    def save_file(self):
        path = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not path:
            return
        with open(path, mode="w", encoding="utf-8") as output_file:
            text = self.txt_edit.get("1.0", tk.END)
            output_file.write(text)
        self.window.title(f"Text Editor - {path}")
        
    ## Initialize quit function
    def return_to_sender(self):
        self.window.destroy()