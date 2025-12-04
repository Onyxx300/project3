## Imports
import tkinter as tk
import tkinter.ttk as ttk
from apps import tempconverter, calculator, texteditor

## Initialize screen
window = tk.Tk()
window.title('Fun Land')
window.resizable(width=False, height=False)

## Initialize functions
def temp():
    temp = tempconverter.TempConvert(window=window)
def calc():
    calc = calculator.Calculate(window=window)
def game():
    import evasion
    from gameassets import player, collectables, enemy, inner_workings
def text_edit():
    text = texteditor.TextEdit(window=window)
def game_2():
    from apps import caterpillar
def game_3():
    from apps import caterpillar_xtreme
def test_butt():
    print('TEST')
def exit_butt():
    print('QUIT')
    window.destroy()
    exit()

## Initialize button (Temp Converter)
button_temp = tk.Button(
    master=window,
    text='Temperature Converter',
    command=temp
).grid(row=0, column=0, padx=10, pady=10)

## Initialize button (Wattage Calculator)
button_calc = tk.Button(
    master=window,
    text='Wattage Calculator',
    command=calc
).grid(row=0, column=1, padx=10, pady=10)

## Initialize button (Evasion Game)
button_game = tk.Button(
    master=window,
    text='Play Evasion Game',
    command=game
).grid(row=0, column=2, padx=10, pady=10)

## Initialize button (Text Editor)
button_textedit = tk.Button(
    master=window,
    text="Text Editor",
    command=text_edit
).grid(row=1, column=0, padx=10, pady=10)

button_exit = tk.Button(
    master=window,
    text='Exit',
    command=exit_butt
).grid(row=1, column=1, padx=10, pady=10)

button_snake = tk.Button(
    master=window,
    text='Play Hungry Caterpillar',
    command=game_2
).grid(row=1, column=2, padx=10, pady=10)

button_snake2 = tk.Button(
    master=window,
    text='Play Hungry Caterpillar X-Treme',
    command=game_3
).grid(row=2, column=0, padx=10, pady=10)

button_lm = tk.Button(
    master=window,
    text='Test',
    command=test_butt
).grid(row=2, column=1, padx=10, pady=10)

button_lr = tk.Button(
    master=window,
    text='Test',
    command=test_butt
).grid(row=2, column=2, padx=10, pady=10)

## Draw screen
window.mainloop()
