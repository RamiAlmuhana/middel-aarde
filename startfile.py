import tkinter as tk
from main import center_window
import splashscreen


def start_window():
    main_window = tk.Tk()
    main_window.title("Lord of the Rings")
    main_window.geometry("1400x700")
    center_window(main_window)
    main_window.resizable(False, False)
    logo = tk.PhotoImage(file="images/ring_logo.png")
    main_window.iconphoto(True, logo)

    main_window.mainloop()


if __name__ == "__main__":
    splashscreen.main()
    start_window()
