import tkinter as tk

class SecondFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Second Frame", font=("Arial", 24))
        self.label.pack()

        go_back_button = tk.Button(self, text="Go Back to Main Frame", command=self.master.show_main_frame)
        go_back_button.pack()
