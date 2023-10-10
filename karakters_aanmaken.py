from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button


def main():
    root = Tk()
    root.geometry("400x400")
    root.title("Personage aanmaken")

    # Labels
    karakter_naam_kiezen = Label(root, text="Naam kiezen")
    Karakter_ras_kiezen = Label(root, text="Rassen")
    Karakter_eigenschap_kiezen = Label(root, text="Eigenschappen")

    # Buttons
    terug_knop = Button(root, text="Terug knop")
    aanmaak_knop = Button(root, text="Aanmaken")

    # Invoerveld
    gebruikers_input = Entry(root)

    # Keuzemenu's
    rassen = ["Mens", "Elf", "Dwerg"]
    eigenschappen = ["Supersterk", "Zwaard", "Mes"]

    rassen_clicked = StringVar()
    eigenschappen_clicked = StringVar()

    rassen_clicked.set("Mens")
    eigenschappen_clicked.set("Supersterk")

    rassen_menu = OptionMenu(root, rassen_clicked, *rassen)
    eigenschappen_menu = OptionMenu(root, eigenschappen_clicked, *eigenschappen)

    # Plaatsing in het midden van het venster
    karakter_naam_kiezen.place(relx=0.5, rely=0.25, anchor="center")
    gebruikers_input.place(relx=0.5, rely=0.3, anchor="center")
    Karakter_ras_kiezen.place(relx=0.5, rely=0.38, anchor="center")
    rassen_menu.place(relx=0.5, rely=0.45, anchor="center")
    Karakter_eigenschap_kiezen.place(relx=0.5, rely=0.55, anchor="center")
    eigenschappen_menu.place(relx=0.5, rely=0.62, anchor="center")
    terug_knop.place(relx=0.25, rely=0.75, anchor="center")
    aanmaak_knop.place(relx=0.75, rely=0.75, anchor="center")

    root.mainloop()


if __name__ == '__main__':
    main()
