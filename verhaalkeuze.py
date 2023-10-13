from tkinter import Label, Button, Tk, PhotoImage
from keuzemomenten import maak_keuzemoment


def maak_verhaal_dict(main_window, karakter, verhaal):
    with open(verhaal) as bestand:
        verhaaldata = bestand.read()
    verhaaldata = verhaaldata.splitlines()
    export = []
    for line in verhaaldata:
        split_data = line.split(';;')
        verhaal_dict = {
            'naam': split_data[0],
            'stap': int(split_data[1]),
            'tekst_1': split_data[2],
            'plaatje_1': split_data[3],
            'tekst_2': split_data[4],
            'plaatje_2': split_data[5],
            'tekst_3': split_data[6],
            'plaatje_3': split_data[7],
            'eig_tekst': split_data[8],
            'eig_plaatje': split_data[9],
            'keuze_1': split_data[10],
            'keuze_2': split_data[11],
            'keuze_3': split_data[12],
            'eigenschap': split_data[13]
        }
        export.append(verhaal_dict)
    maak_keuzemoment(main_window, karakter, export, 0, 'tekst_1', 'plaatje_1', '')


def kies_verhaal(main_window, karakter):
    for widget in main_window.winfo_children():
        widget.destroy()

    background_image = PhotoImage(file="images/karakter_background.png")

    background_label = Label(main_window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    schermnaam = Label(main_window, text="In welk verhaal wil je verdiepen?", font=("Footlight MT Light", 18))
    schermnaam.place(x=550, y=25)

    button_1_image = PhotoImage(file="images/the_shire.png")
    button_1 = Button(main_window, image=button_1_image,
                      command=lambda: maak_verhaal_dict(main_window, karakter, 'database/verhaal_1.txt'))
    button_1_image.image = button_1_image
    button_1.bind("<Button-1>", lambda: maak_verhaal_dict(main_window, karakter, 'database/verhaal_1.txt'))
    button_1.place(x=125, y=125)

    verhaal_1 = Label(main_window, text="Avontuur in de Shire", font=("Footlight MT Light", 18))
    verhaal_1.place(x=150, y=550)

    button_2_image = PhotoImage(file="images/elendil sword.png")
    button_2 = Button(main_window, image=button_2_image,
                      command=lambda: maak_verhaal_dict(main_window, karakter, 'database/verhaal_2.txt'))
    button_2_image.image = button_2_image
    button_2.bind("<Button-1>", lambda: maak_verhaal_dict(main_window, karakter, 'database/verhaal_2.txt'))
    button_2.place(x=500, y=125)

    verhaal_2 = Label(main_window, text="Zoektocht naar het Zwaard", font=("Footlight MT Light", 18))
    verhaal_2.place(x=500, y=550)

    button_3_image = PhotoImage(file="images/the_ents.png")
    button_3 = Button(main_window, image=button_3_image,
                      command=lambda: maak_verhaal_dict(main_window, karakter, 'database/verhaal_3.txt'))
    button_3_image.image = button_3_image
    button_3.bind("<Button-1>", lambda: maak_verhaal_dict(main_window, karakter, 'database/verhaal_3.txt'))
    button_3.place(x=900, y=125)

    verhaal_3 = Label(main_window, text="Ontwakenen van de Enten", font=("Footlight MT Light", 18))
    verhaal_3.place(x=890, y=550)
