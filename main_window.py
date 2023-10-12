import tkinter as tk
import second_window

def open_second_window():
    second_window.create_second_window(root)

root = tk.Tk()
root.title("Main Window")

open_second_button = tk.Button(root, text="Open Second Window", command=open_second_window)
open_second_button.pack()

root.mainloop()
