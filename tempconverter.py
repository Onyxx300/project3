## Imports
import tkinter as tk

## Initialize class
class TempConvert(tk.Tk):
    def __init__(self, window: tk.Tk) -> None:
        self.window = tk.Tk()
        window.destroy()
        self.start()
    
    ## Window initialization
    def start(self):
        self.window.title("Temperature Converter")
        self.window.resizable(width=True, height=False)

        ## Asset initialization (F)
        frm_entry_f = tk.Frame(master=self.window)
        self.ent_temp_f = tk.Entry(master=frm_entry_f, width=5)
        lbl_temp_f = tk.Label(master=frm_entry_f, text="\N{DEGREE FAHRENHEIT}")
        self.ent_temp_f.grid(row=0, column=0, sticky="e")
        lbl_temp_f.grid(row=0, column=1, sticky="w")
        
        ## Asset initialization (Exit)
        exit_lbl_l = tk.Label(master=self.window, text="Exit to Menu " \
        "\N{RIGHTWARDS WHITE ARROW}")
        exit_lbl_r = tk.Label(master=self.window, text="\N{LEFTWARDS WHITE ARROW}" \
        " Exit to Menu")
        exit_lbl_l.grid(row=1, column=0)
        exit_lbl_r.grid(row=1, column=2)

        ## Asset initialization (C)
        frm_entry_c = tk.Frame(master=self.window)
        self.ent_temp_c = tk.Entry(master=frm_entry_c, width=5)
        lbl_temp_c = tk.Label(master=frm_entry_c, text="\N{DEGREE CELSIUS}")
        self.ent_temp_c.grid(row=2, column=2, sticky="e")
        lbl_temp_c.grid(row=2, column=1, sticky="w")


        ## Button initialization (F to C)
        btn_convert_c = tk.Button(
            master=self.window,
            text="\N{DEGREE FAHRENHEIT}\N{RIGHTWARDS BLACK ARROW}\N{DEGREE CELSIUS}",
            command=self.fahrenheit_celsius_converter
        ).grid(row=0, column=1, pady=10)

        ## Button initialization (C to F)
        btn_convert_f = tk.Button(
            master=self.window,
            text="\N{DEGREE FAHRENHEIT}\N{LEFTWARDS BLACK ARROW}\N{DEGREE CELSIUS}",
            command=self.celsius_fahrenheit_converter
        ).grid(row=2, column=1, padx=10, pady=10)

        ## Button initialization (return)
        btn_return = tk.Button(
            master=self.window,
            text="Return",
            command=self.return_to_sender
        ).grid(row=1, column=1, padx=10)

        ## Interaction (F to C)
        self.lbl_result_c = tk.Label(master=self.window, text="")
        frm_entry_f.grid(row=0, column=0, padx=10)
        self.lbl_result_c.grid(row=0, column=2, padx=10)

        ## Interaction (C to F)
        self.lbl_result_f = tk.Label(master=self.window, text="")
        frm_entry_c.grid(row=2, column=2, padx=10)
        self.lbl_result_f.grid(row=2, column=0, padx=10)

        ## Draw screen
        self.window.mainloop()

    ## Format converter (F to C)
    def fahrenheit_celsius_converter(self):
        """Converts Fahrenheit to Celsius and plugs the result into lbl_result_c"""
        fahrenheit = self.ent_temp_f.get()
        celsius = (5/9) * (float(fahrenheit) - 32)
        self.lbl_result_c["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
        return ""

    ## Format converter (C to F)
    def celsius_fahrenheit_converter(self):
        """Converts Celsius to Fahrenheit and plugs the result into lbl_result_f"""
        celsius = self.ent_temp_c.get()
        fahrenheit = ((9/5) * (float(celsius))) + 32
        self.lbl_result_f["text"] = f'{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}'
        return ""
        
    ## Return to welcome
    def return_to_sender(self):
        """Kills the Temperature Converter and loads the Welcome program"""
        self.window.destroy()
        import main