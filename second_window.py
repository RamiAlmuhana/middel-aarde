import tkinter as tk

def create_second_window(previous_window):
    previous_window.destroy()  # Close the previous window

    second_root = tk.Tk()
    second_root.title("Second Window")

    go_back_button = tk.Button(second_root, text="Go Back", command=lambda: main_window.open_main_window(second_root))
    go_back_button.pack()

    second_root.mainloop()
