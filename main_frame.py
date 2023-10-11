import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Main Frame", font=("Arial", 24))
        self.label.pack()

        switch_button = tk.Button(self, text="Switch to Second Frame", command=self.master.show_second_frame)
        switch_button.pack()
