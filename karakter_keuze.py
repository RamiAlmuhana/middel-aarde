from tkinter import Tk, Label, Button, Frame, PhotoImage
from beschrijving_karakters import *



def maak_karakter_dict(file):
    with open(file) as bestand:
        verhaaldata = bestand.read()
    verhaaldata = verhaaldata.splitlines()
    export = []
    for line in verhaaldata:
        split_data = line.split(';;')
        verhaal_dict = {
            "naam": split_data[0],
            "ras": split_data[1],
            "beschrijving": split_data[2],
            "eigenschap": split_data[3],
            "foto": split_data[4]
        }
        export.append(verhaal_dict)
    return export


def kies_karakter(venster):
    from main import hoofd_menu
    custom_karakter = maak_karakter_dict('database/karakters.txt')
    karakter_data = maak_karakter_dict('database/karakterdata.txt')
    for widget in venster.winfo_children():
        widget.destroy()

    background_image = PhotoImage(file="images/karakter_background.png")

    background_label = Label(venster, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    schermnaam = Label(venster, text="Welk karakter wilt u kiezen?", font=("Footlight MT Light", 18))
    schermnaam.place(x=550, y=25)

    button_1_image = PhotoImage(file="images/frodo.png")
    button_1 = Button(venster, image=button_1_image, command=lambda: karakter_gekozen(venster, karakter_data[0]))
    button_1_image.image = button_1_image
    button_1.place(x=100, y=125)

    karakternaam_1 = Label(venster, text="Frodo", font=("Footlight MT Light", 18))
    karakternaam_1.place(x=200, y=600)

    button_2_image = PhotoImage(file="images/gimli.png")
    button_2 = Button(venster, image=button_2_image, command=lambda: karakter_gekozen(venster, karakter_data[1]))
    button_2_image.image = button_2_image
    button_2.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[1]))
    button_2.place(x=400, y=125)

    karakternaam_2 = Label(venster, text="Gimli", font=("Footlight MT Light", 18))
    karakternaam_2.place(x=500, y=600)

    button_3_image = PhotoImage(file="images/legolas.png")
    button_3 = Button(venster, image=button_3_image, command=lambda: karakter_gekozen(venster, karakter_data[2]))
    button_3_image.image = button_3_image
    button_3.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[2]))
    button_3.place(x=700, y=125)

    karakternaam_3 = Label(venster, text="Legolas", font=("Footlight MT Light", 18))
    karakternaam_3.place(x=800, y=600)

    button_4_image = PhotoImage(file="images/custom_karakter.png")
    button_4 = Button(venster, image=button_4_image, command=lambda: karakter_gekozen(venster, custom_karakter[0]))
    button_4_image.image = button_4_image
    button_4.bind("<Button-1>", lambda event: karakter_gekozen(venster, custom_karakter[0]))
    button_4.place(x=1000, y=125)

    karakternaam_4 = Label(venster, text=custom_karakter[0]['naam'], font=("Footlight MT Light", 18))
    karakternaam_4.place(x=1100, y=600)

    terugknop = Button(venster, text="Terug naar main menu", width=30, height=2, borderwidth=4,
                          command=lambda: hoofd_menu(venster))
    terugknop.place(x=100, y=650)