import tkinter as tk
from hoofdscherm import MainFrame
from second_frame import SecondFrame

def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.mainloop()

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Frame Switching Example")
        self.master.geometry("800x400")
        self.pack()
        self.current_frame = None
        self.create_frames()

    def create_frames(self):
        self.main_frame = MainFrame(self)
        self.second_frame = SecondFrame(self)
        self.show_main_frame()

    def show_main_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.main_frame
        self.main_frame.pack()

    def show_second_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.second_frame
        self.second_frame.pack()

if __name__ == "__main__":
    main()
