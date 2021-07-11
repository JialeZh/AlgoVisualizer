from tkinter import *
from tkinter import ttk
import random

WHITE = '#FFFFFF'
Gray = '#C4C5BF'


window = Tk()
window.title("Algorithms Visualizer")
window.maxsize(1200, 900)
window.config(bg = WHITE)


UI_frame = Frame(window, width= 1200, height=600, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

algo_name = StringVar()
algo_list = ['Bubble Sort']
data = []
speed_name = StringVar()
speed_list = ['Fast', 'Normal', 'Slow']

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algo_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=0, column=3, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=0, column=5, padx=5, pady=5)
speed_menu.current(0)

def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.005

def drawData(data, colorArray):
    pass

def generate():
    pass

def sort():
    pass

b1 = Button(UI_frame, text="Sort", command=sort, bg=Gray)
b1.grid(row=2, column=3, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=Gray)
b3.grid(row=2, column=2, padx=5, pady=5)

canvas = Canvas(window, width=1200, height=600, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)



window.mainloop()
