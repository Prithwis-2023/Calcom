import tkinter as tk
from tkinter import *
from math import *
def evaluate(event):
  res.configure(text = "Result: " + str(eval(entry.get())))
w = tk.Tk()
tk.Label(w, text="Expression:").pack()
entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
