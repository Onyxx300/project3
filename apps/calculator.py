## Imports
import tkinter as tk

## Initialize class
class Calculate(tk.Tk):
    def __init__(self, window: tk.Tk) -> None:
        self.window = tk.Tk()
        window.destroy()
        self.start()

    ## Initialize window
    def start(self):
        self.window.title('Wattage Calculator')
        self.window.resizable(width=True, height=False)

        ##Initialize asset (Volts)
        ent_volt = tk.Frame(master=self.window)
        self.volt_entry = tk.Entry(master=ent_volt, width=4)
        self.volt_entry.grid(row=0, column=1, sticky='e')
        r_lbl_volt = tk.Label(master=ent_volt, text='\N{LEFTWARDS WHITE ARROW}' \
        'Volts')
        l_lbl_volt = tk.Label(master=ent_volt, text='Volts' \
        '\N{RIGHTWARDS WHITE ARROW}')
        ent_volt.grid(row=0, column=1)
        r_lbl_volt.grid(row=0, column=2)
        l_lbl_volt.grid(row=0, column=0)

        ## Initialize asset (Amps)
        ent_amp = tk.Frame(master=self.window)
        self.amp_entry = tk.Entry(master=ent_amp, width=3)
        self.amp_entry.grid(row=1, column=1, sticky='w')
        self.result = tk.Label(master=self.window, text="")
        self.result.grid(row=3, column=1)
        r_lbl_amp = tk.Label(master=ent_amp, text='\N{LEFTWARDS WHITE ARROW}' \
        'Amps')
        l_lbl_amp = tk.Label(master=ent_amp, text='Amps' \
        '\N{RIGHTWARDS WHITE ARROW}')
        ent_amp.grid(row=1, column=1)
        r_lbl_amp.grid(row=1, column=2)
        l_lbl_amp.grid(row=1, column=0)

        ##Initialize button (calculate)
        convert_btn = tk.Button(
            master=self.window,
            text='\N{DOWNWARDS BLACK ARROW}Calculate Wattage' \
            '\N{DOWNWARDS BLACK ARROW}',
            command=self.wattage
        ).grid(row=2, column=1)
       
       ## Initialize button (Exit)
        exit_btn = tk.Button(
            master=self.window,
            text='Exit',
            command=self.return_to_sender
        ).grid(row=4, column=1)

        ## Draw screen
        self.window.mainloop()
    
    ## Initialize calculate function
    def wattage(self):
        volts = self.volt_entry.get()
        amps = self.amp_entry.get()
        watts = float(volts) * float(amps)
        self.result["text"] = f'{round(watts, 2)} Watts'

    ## Initialize quit function
    def return_to_sender(self):
        self.window.destroy()
        import main




