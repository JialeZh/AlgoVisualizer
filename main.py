from tkinter import *
from tkinter import ttk
import random
from bubble import *
from merge import *
from quick import *

WHITE = '#FFFFFF'
Green = '#05F50E'

window = Tk()
window.title("Algorithms Visualizer")
window.maxsize(1200, 900)
window.config(bg = WHITE)


UI_frame = Frame(window, width= 1200, height=600, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

algo_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
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
        return 0.1
    elif speed_menu.get() == 'Medium':
        return 0.005
    else:
        return 0.001

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 1200
    canvas_height = 600
    x_width = canvas_width / (len(data) + 6)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    
    window.update_idletasks()

def generate():
    global data

    for i in range(0, 45):
        random_value = random.randint(1, 100)
        data.append(random_value)

    drawData(data, [Green for x in range(len(data))])

def reset():
    global data
    data.clear()
    drawData(data, [Green for x in range(len(data))])
def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quicksort(data, drawData, timeTick)
        
b1 = Button(UI_frame, text="Sort",width=12, command=sort)
b1.grid(row=2, column=5, padx=5, pady=5)

b2 = Button(UI_frame, text="Reset",width=12, command=reset)
b2.grid(row=2, column=3, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array",width=12, command=generate)
b3.grid(row=2, column=1, padx=5, pady=5)

canvas = Canvas(window, width=1200, height=600, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)



window.mainloop()
