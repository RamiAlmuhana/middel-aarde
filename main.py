import tkinter as tk

from karakters_aanmaken import karakter_aanmaken
from instellingen import open_instellingen
from karakter_keuze import kies_karakter


def knop_sluiten(main_window):
    main_window.destroy()


# Define username and password entry as global variables
username_entry = None
password_entry = None


def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry("+{}+{}".format(x, y))
    hoofd_menu(window)


def hoofd_menu(main_window):
    for widget in main_window.winfo_children():
        widget.destroy()
    font = ("Footlight MT Light", 16, 'bold')
    background_image = tk.PhotoImage(file="images/main_menu.png")

    background_label = tk.Label(main_window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    personage_kiezen = tk.Button(main_window, text="Personage kiezen", width=55, height=2,
                                 borderwidth=4,
                                 command=lambda: kies_karakter(main_window), font=font)
    personage_kiezen.place(x=345, y=200)
    personage_kiezen.config(font=font)

    personage_aanmaken = tk.Button(main_window, text="Personage aanmaken", width=55, height=2,
                                   borderwidth=4,
                                   command=lambda: karakter_aanmaken(main_window), font=font)
    personage_aanmaken.place(x=345, y=300)
    personage_aanmaken.config(font=font)

    instellingen = tk.Button(main_window, text="Instellingen", width=55, height=2, borderwidth=4,
                             command=lambda: open_instellingen(main_window), font=font)
    instellingen.place(x=345, y=400)
    instellingen.config(font=font)

    sluiten = tk.Button(main_window, text="Sluiten", command=lambda: knop_sluiten(main_window),
                        width=55, height=2, borderwidth=4)
    sluiten.place(x=345, y=500)
    sluiten.config(font=font)
