from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button
import tkinter as tk


def personages_wegschrijven(text_File, selected_rassen, selected_eigenschappen):
    with open("karakters.txt", "a") as file:
        user_Input = text_File.get()
        selected_option_rassen = selected_rassen.get()
        selected_option_eigenschappen = selected_eigenschappen.get()
        file.write(f"{user_Input};{selected_option_rassen};{selected_option_eigenschappen}\n")
        text_File.delete(0, tk.END)

def karakter_aanmaken(main_window):
    from main import create_main_app_frame
    karakter_aanmaken_frame = tk.Frame(main_window)
    karakter_aanmaken_frame.place(x=0, y=0, relwidth=1, relheight=1)
    main_window.title("Personage aangemaakt")

    # Bevestigingsscherm maken
    # confirmation_label = Label(main_window, text="Personage is aangemaakt!", font=('Helvetica bold', 20))
    # confirmation_label.pack(pady=50)

    # Terugknop naar het beginscherm
    back_button = Button(main_window, text="Naar het hoofdmenu", command=lambda: main_window())
    back_button.pack()

    gebruikers_input = Entry(main_window)

    rassen = ["Mens", "Elf", "Hobbit", "Dwerg"]
    eigenschappen = ["Bijl", "Boog", "Superslim"]

    rassen_clicked = StringVar()
    eigenschappen_clicked = StringVar()

    rassen_clicked.set(rassen[0])
    eigenschappen_clicked.set(eigenschappen[0])

    rassen_menu = OptionMenu(main_window, rassen_clicked, *rassen)
    eigenschappen_menu = OptionMenu(main_window, eigenschappen_clicked, *eigenschappen)

    # Buttons
    font = ("Helvetica", 16)
    terugknop = tk.Button(main_window, text="Terug naar main menu", bg='lightgreen', width=55, height=2,
                          command=lambda: create_main_app_frame(main_window), font=font)
    terugknop.place(x=400, y=400)
    aanmaak_knop = Button(main_window, text="Aanmaken",
                          command=lambda: personages_wegschrijven(gebruikers_input, rassen_clicked,
                                                                  eigenschappen_clicked))

    # karakters_scherm_aanmaken = tk.Frame(main_window)
    # karakters_scherm_aanmaken.place(x=0, y=0, relwidth=1, relheight=1)
    # Labels
    titel = Label(main_window, text="Karakter aanmaken", font=('Helvetica bold', 20))
    karakter_naam_kiezen = Label(main_window, text="Naam kiezen")
    Karakter_ras_kiezen = Label(main_window, text="Rassen")
    Karakter_eigenschap_kiezen = Label(main_window, text="Eigenschappen")

    karakter_naam_kiezen.place(relx=0.5, rely=0.25, anchor="center")
    gebruikers_input.place(relx=0.5, rely=0.3, anchor="center")
    Karakter_ras_kiezen.place(relx=0.5, rely=0.38, anchor="center")
    rassen_menu.place(relx=0.5, rely=0.45, anchor="center")
    Karakter_eigenschap_kiezen.place(relx=0.5, rely=0.55, anchor="center")
    eigenschappen_menu.place(relx=0.5, rely=0.62, anchor="center")
    titel.pack()
    # terug_knop.place(relx=0.25, rely=0.75, anchor="center")
    aanmaak_knop.place(relx=0.75, rely=0.75, anchor="center")
