import tkinter as tk
import splashscreen
from karakters_aanmaken import karakter_aanmaken
from instellingen import open_instellingen


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
    create_main_app_frame(window)

def create_main_app_frame(main_window):
    # main_menu_frame = tk.Frame(main_window)
    # main_menu_frame.place(x=0, y=0, relwidth=1, relheight=1)
    for widget in main_window.winfo_children():
        widget.destroy()
    font = ("Footlight MT Light", 16, 'bold')
    background_image = tk.PhotoImage(file="images/main_menu.png")

    background_label = tk.Label(main_window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    personage_kiezen = tk.Button(main_window, text="Personage kiezen", bg='lightgreen', width=55, height=2, borderwidth=4)
    personage_kiezen.place(x=325, y=175)
    personage_kiezen.config(font=font)

    personage_aanmaken = tk.Button(main_window, text="Personage aanmaken", bg='lightgreen', width=55, height=2,
                                   borderwidth=4,
                                   command=lambda: karakter_aanmaken(main_window), font=font)
    personage_aanmaken.place(x=325, y=275)
    personage_aanmaken.config(font=font)

    instellingen = tk.Button(main_window, text="Instellingen", bg='lightgreen', width=55, height=2, borderwidth=4,
                             command=lambda: open_instellingen(main_window), font=font)
    instellingen.place(x=325, y=375)
    instellingen.config(font=font)

    sluiten = tk.Button(main_window, text="Sluiten", command=lambda: knop_sluiten(main_window), bg='lightgreen',
                        width=55, height=2, borderwidth=4)
    sluiten.place(x=325, y=475)
    sluiten.config(font=font)

# if __name__ == "__main__":
#     # splashscreen.main()
