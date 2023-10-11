import tkinter as tk
import splashscreen

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry("+{}+{}".format(x, y))

def main_app():
    main_window = tk.Tk()
    main_window.title("Lord of the Rings")
    main_window.geometry("1200x800")
    center_window(main_window)

    label = tk.Label(main_window, text="Lord of the rings", font=("Helvetica", 20))
    label.pack()

    main_window.mainloop()

if __name__ == "__main__":
    splashscreen.main()
    main_app()
