import tkinter as tk
from tkinter import *

counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
counter_label(label)

root.mainloop()
