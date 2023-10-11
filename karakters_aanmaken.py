import tkinter
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button

root = Tk()
root.geometry("400x400")


def karakter_aanmaken():
    root.title("Personage aangemaakt")

    # Verwijder de huidige widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Bevestigingsscherm maken
    confirmation_label = Label(root, text="Personage is aangemaakt!", font=('Helvetica bold', 20))
    confirmation_label.pack(pady=50)

    # Terugknop naar het beginscherm
    back_button = Button(root, text="Naar het hoofdmenu", command=lambda: hoofdmenu_scherm())
    back_button.pack()


def hoofdmenu_scherm():
    root.title("Hoofdmenu")

    # Verwijder de huidige widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Terugpagina maken
    return_label = Label(root, text="Hoofdmenu", font=('Helvetica bold', 20))
    return_label.pack(pady=50)

    # Terugknop naar het beginscherm
    back_button = Button(root, text="Karakter aanmaken", command=lambda: main())
    back_button.pack()


def personages_wegschrijven(text_File, selected_rassen, selected_eigenschappen):
    with open("karakters.txt", "a") as file:
        user_Input = text_File.get()
        selected_option_rassen = selected_rassen.get()
        selected_option_eigenschappen = selected_eigenschappen.get()
        file.write(f"{user_Input};{selected_option_rassen};{selected_option_eigenschappen}\n")
        text_File.delete(0, tkinter.END)


def main():
    root.title("Personage aanmaken")

    # Verwijder de huidige widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Labels
    titel = Label(root, text="Karakter aanmaken", font=('Helvetica bold', 20))
    karakter_naam_kiezen = Label(root, text="Naam kiezen")
    Karakter_ras_kiezen = Label(root, text="Rassen")
    Karakter_eigenschap_kiezen = Label(root, text="Eigenschappen")

    # Buttons
    terug_knop = Button(root, text="Terug", command=lambda: hoofdmenu_scherm())
    aanmaak_knop = Button(root, text="Aanmaken", command=lambda: personages_wegschrijven(gebruikers_input, rassen_clicked, eigenschappen_clicked))

    # Invoerveld
    gebruikers_input = Entry(root)


    # Keuzemenu's
    rassen = ["Mens", "Elf", "Hobbit", "Dwerg"]
    eigenschappen = ["Supersterk", "Zwaard", "Boog", "Magie", "Toverstaf"]

    rassen_clicked = StringVar()
    eigenschappen_clicked = StringVar()

    rassen_clicked.set(rassen[0])
    eigenschappen_clicked.set(eigenschappen[0])

    rassen_menu = OptionMenu(root, rassen_clicked, *rassen)
    eigenschappen_menu = OptionMenu(root, eigenschappen_clicked, *eigenschappen)

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
    root.mainloop()
