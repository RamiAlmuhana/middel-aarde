import tkinter as tk
import time


def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry("+{}+{}".format(x, y))


def fade_in(splash_window):
    for alpha in range(0, 256, 8):
        splash_window.attributes("-alpha", alpha / 255)
        splash_window.update_idletasks()
        time.sleep(0.03)

def fade_out(splash_window):
    for alpha in range(255, -1, -8):
        splash_window.attributes("-alpha", alpha / 255)
        splash_window.update_idletasks()
        time.sleep(0.03)

def main():
    splash_window = tk.Tk()
    splash_window.overrideredirect(True)
    splash_window.geometry("500x380")
    center_window(splash_window)

    splash_image = tk.PhotoImage(file="images/splashscreen_logo.png")

    splash_label = tk.Label(splash_window, image=splash_image, borderwidth=0)
    splash_label.pack()

    fade_in(splash_window)

    splash_window.after(800, lambda: [splash_window.destroy()])

    splash_window.mainloop()

if __name__ == "__main__":
    main()
