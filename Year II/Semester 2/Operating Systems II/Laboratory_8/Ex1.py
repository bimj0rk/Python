import tkinter as tk
import string
import os

window = tk.Tk()
label = tk.Label("Enter the path: ")
label.pack()
folderPath = tk.StringVar()
folderPath.set("path...")
entry = tk.Entry(window, textvariable=string, width=40)
entry.pack()
window.mainloop()
