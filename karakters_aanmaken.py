import tkinter
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button

main_window = Tk()
main_window.geometry("400x400")


def karakter_aanmaken():
    main_window.title("Personage aangemaakt")

    # Verwijder de huidige widgets
    for widget in main_window.winfo_children():
        widget.destroy()

    # Bevestigingsscherm maken
    confirmation_label = Label(main_window, text="Personage is aangemaakt!", font=('Helvetica bold', 20))
    confirmation_label.pack(pady=50)

    # Terugknop naar het beginscherm
    back_button = Button(main_window, text="Naar het hoofdmenu", command=lambda: hoofdmenu_scherm())
    back_button.pack()


def hoofdmenu_scherm():
    main_window.title("Hoofdmenu")

    # Verwijder de huidige widgets
    for widget in main_window.winfo_children():
        widget.destroy()

    # Terugpagina maken
    return_label = Label(main_window, text="Hoofdmenu", font=('Helvetica bold', 20))
    return_label.pack(pady=50)

    # Terugknop naar het beginscherm
    back_button = Button(main_window, text="Karakter aanmaken", command=lambda: main())
    back_button.pack()


def personages_wegschrijven(text_File, selected_rassen, selected_eigenschappen):
    with open("karakters.txt", "a") as file:
        user_Input = text_File.get()
        selected_option_rassen = selected_rassen.get()
        selected_option_eigenschappen = selected_eigenschappen.get()
        file.write(f"{user_Input};{selected_option_rassen};{selected_option_eigenschappen}\n")
        text_File.delete(0, tkinter.END)


def main():
    main_window.title("Personage aanmaken")

    # Verwijder de huidige widgets
    for widget in main_window.winfo_children():
        widget.destroy()

    # Labels
    titel = Label(main_window, text="Karakter aanmaken", font=('Helvetica bold', 20))
    karakter_naam_kiezen = Label(main_window, text="Naam kiezen")
    Karakter_ras_kiezen = Label(main_window, text="Rassen")
    Karakter_eigenschap_kiezen = Label(main_window, text="Eigenschappen")

    # Buttons
    terug_knop = Button(main_window, text="Terug", command=lambda: hoofdmenu_scherm())
    aanmaak_knop = Button(main_window, text="Aanmaken", command=lambda: personages_wegschrijven(gebruikers_input, rassen_clicked, eigenschappen_clicked))

    # Invoerveld
    gebruikers_input = Entry(main_window)


    # Keuzemenu's
    rassen = ["Mens", "Elf", "Hobbit", "Dwerg"]
    eigenschappen = ["Supersterk", "Zwaard", "Boog", "Magie", "Toverstaf"]

    rassen_clicked = StringVar()
    eigenschappen_clicked = StringVar()

    rassen_clicked.set(rassen[0])
    eigenschappen_clicked.set(eigenschappen[0])

    rassen_menu = OptionMenu(main_window, rassen_clicked, *rassen)
    eigenschappen_menu = OptionMenu(main_window, eigenschappen_clicked, *eigenschappen)

    karakter_naam_kiezen.place(relx=0.5, rely=0.25, anchor="center")
    gebruikers_input.place(relx=0.5, rely=0.3, anchor="center")
    Karakter_ras_kiezen.place(relx=0.5, rely=0.38, anchor="center")
    rassen_menu.place(relx=0.5, rely=0.45, anchor="center")
    Karakter_eigenschap_kiezen.place(relx=0.5, rely=0.55, anchor="center")
    eigenschappen_menu.place(relx=0.5, rely=0.62, anchor="center")
    titel.pack()
    terug_knop.place(relx=0.25, rely=0.75, anchor="center")
    aanmaak_knop.place(relx=0.75, rely=0.75, anchor="center")


if __name__ == '__main__':
    main()
    main_window.mainloop()
