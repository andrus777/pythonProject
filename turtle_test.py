import turtle as tr
import tkinter as tk

a = 2
b = -4
c = -3

for x in range(-10,10):
    y = a*x*x - b*x + c
    tr.goto(x + 100 , y+100)

window = tk.Tk()
window.geometry("380x350")
window.resizable(False, False)

window.mainloop()