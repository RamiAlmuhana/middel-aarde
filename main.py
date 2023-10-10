import tkinter as tk
import time

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry("+{}+{}".format(x, y))

def fade_in():
    for alpha in range(0, 256, 8):
        splash_window.attributes("-alpha", alpha / 255)
        splash_window.update_idletasks()
        time.sleep(0.02)

def fade_out():
    for alpha in range(255, -1, -8):
        splash_window.attributes("-alpha", alpha / 255)
        splash_window.update_idletasks()
        time.sleep(0.02)

def change_image():
    splash_label.configure(image=splash_image2)
    splash_label.image = splash_image2

    fade_in()

    splash_window.after(5000, fade_out)

def main():
    global splash_window
    splash_window = tk.Tk()
    splash_window.overrideredirect(True)
    splash_window.geometry("400x400")
    center_window(splash_window)

    global splash_image1
    splash_image1 = tk.PhotoImage(file="images/team gandalf logo.png")

    global splash_image2
    splash_image2 = tk.PhotoImage(file="images/tolkien estate logo.png")

    global splash_label
    splash_label = tk.Label(splash_window, image=splash_image1, borderwidth=0)
    splash_label.pack()

    fade_in()

    splash_window.after(3000, change_image)

    splash_window.mainloop()

if __name__ == "__main__":
    main()
