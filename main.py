import tkinter as tk
from instellingen import open_instellingen, open_inlogscherm, perform_login, show_admin_page

# Define username and password entry as global variables
username_entry = None
password_entry = None


def knop_sluiten(main_window):
    main_window.destroy()


def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry("+{}+{}".format(x, y))


def main():
    global main_window
    main_window = tk.Tk()
    main_window.title("Lord of the Rings")
    main_window.geometry("1400x700")
    center_window(main_window)
    main_window.configure(bg="darkgreen")

    font = ("Helvetica", 16)

    spel_naam = tk.Label(text='Lord of the Rings', bg='darkgreen', font=font)
    spel_naam.place(x=525, y=75)

    personage_kiezen = tk.Button(main_window, text="Personage kiezen", bg='lightgreen', width=55, height=2)
    personage_kiezen.place(x=375, y=175)
    personage_kiezen.config(font=font)

    personage_aanmaken = tk.Button(main_window, text="Personage aanmaken", bg='lightgreen', width=55, height=2)
    personage_aanmaken.place(x=375, y=275)
    personage_aanmaken.config(font=font)

    instellingen = tk.Button(main_window, text="Instellingen", bg='lightgreen', width=55, height=2,
                             command=lambda: open_instellingen(main_window))
    instellingen.place(x=375, y=375)
    instellingen.config(font=font)

    sluiten = tk.Button(main_window, text="Sluiten", command=lambda: knop_sluiten(main_window), bg='lightgreen',
                        width=55, height=2)
    sluiten.place(x=375, y=475)
    sluiten.config(font=font)

    main_window.mainloop()


if __name__ == "__main__":
    main()
