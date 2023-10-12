from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, messagebox
import tkinter as tk


def personages_wegschrijven(text_File, selected_rassen, selected_eigenschappen):
    if len(text_File.get()) == 0:
        messagebox.showerror("Error", "Voer een naam in!")
    else:
        with open("database/karakters.txt", "w") as file:
            user_Input = text_File.get().capitalize()
            selected_option_rassen = selected_rassen.get()
            selected_option_eigenschappen = selected_eigenschappen.get()
            file.write(f"{user_Input};;{selected_option_rassen};;Custom karakter;;{selected_option_eigenschappen};; ")
            text_File.delete(0, tk.END)
            messagebox.showinfo("Succes", "Karakter is aangemaakt!!!!")


def karakter_aanmaken(main_window):
    from main import hoofd_menu
    karakter_aanmaken_frame = tk.Frame(main_window)
    karakter_aanmaken_frame.place(x=0, y=0, relwidth=1, relheight=1)
    main_window.title("Personage aangemaakt")

    gebruikers_input_karakter_naam = Entry(main_window)

    rassen = ["Mens", "Elf", "Hobbit", "Dwerg"]
    eigenschappen = ["bijl", "boog", "super slim"]

    rassen_clicked = StringVar()
    eigenschappen_clicked = StringVar()

    rassen_clicked.set(rassen[0])
    eigenschappen_clicked.set(eigenschappen[0])

    rassen_menu = OptionMenu(main_window, rassen_clicked, *rassen)
    eigenschappen_menu = OptionMenu(main_window, eigenschappen_clicked, *eigenschappen)

    # Buttons
    font = ("Helvetica", 13)
    terugknop = tk.Button(main_window, text="Terug naar main menu", bg='lightgreen', width=33, height=2,
                          command=lambda: hoofd_menu(main_window), font=font)
    terugknop.place(x=200, y=500)
    aanmaak_knop = Button(main_window, text="Aanmaken", bg='lightgreen', width=33, height=2,
                          command=lambda: personages_wegschrijven(gebruikers_input_karakter_naam, rassen_clicked,
                                                                  eigenschappen_clicked), font=font)
    aanmaak_knop.place(x=900, y=500)

    titel = Label(main_window, text="Karakter aanmaken", font=('Helvetica bold', 20))
    karakter_naam_kiezen = Label(main_window, text="Naam kiezen")
    Karakter_ras_kiezen = Label(main_window, text="Rassen")
    Karakter_eigenschap_kiezen = Label(main_window, text="Eigenschappen")

    karakter_naam_kiezen.place(relx=0.5, rely=0.25, anchor="center")
    gebruikers_input_karakter_naam.place(relx=0.5, rely=0.3, anchor="center")
    Karakter_ras_kiezen.place(relx=0.5, rely=0.38, anchor="center")
    rassen_menu.place(relx=0.5, rely=0.45, anchor="center")
    Karakter_eigenschap_kiezen.place(relx=0.5, rely=0.55, anchor="center")
    eigenschappen_menu.place(relx=0.5, rely=0.62, anchor="center")
    titel.pack()
