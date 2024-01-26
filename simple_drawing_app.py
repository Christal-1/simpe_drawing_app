import tkinter as tk
from tkinter import colorchooser

def draw(event):
    global start_x, start_y
    x, y = event.x, event.y
    if start_x is not None and start_y is not None:
        canvas.create_line(start_x, start_y, x, y, width = line_width, fill = draw_color)
    start_x = x
    start_y = y

def reset(event):
    global start_x, start_y
    start_x = None
    start_y = None

def clear_canvas():
    canvas.delete("all")

def choose_your_color():
    global draw_color
    color = colorchooser.askcolor()[1]
    if color:
        draw_color = color

start_x, start_y = None, None
draw_color = "black"
line_width = 2

root = tk.Tk()
root.title("Simple Drawing App")

canvas = tk.Canvas(root, bg = "white", width = 600, height = 600)
canvas.pack()

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)

clear_button = tk.Button(root, text = "Clear", command = clear_canvas)
clear_button.pack(side = tk.BOTTOM)

color_button = tk.Button(root, text = "Choose Your Color", command = choose_your_color)
color_button.pack(side = tk.BOTTOM)

root.mainloop()
