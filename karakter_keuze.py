from tkinter import Tk, Label, Button, Frame, PhotoImage
from beschrijving_karakters import *


def maak_karakter_dict():
    with open("database/karakterdata.txt") as bestand:
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
    karakter_data = maak_karakter_dict()
    for widget in venster.winfo_children():
        widget.destroy()

    label1 = Label(venster, text="Welk karakter wilt u kiezen?", font=("Footlight MT Light", 18))
    button_1_image = PhotoImage(file="images/frodo.png")
    button_1 = Button(venster, image=button_1_image, command=lambda: karakter_gekozen(venster, karakter_data[1]))
    button_1_image.image = button_1_image
    button_1.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[0]))
    button_1.pack()

    button_2_image = PhotoImage(file="images/gimli.png")
    button_2 = Button(venster, image=button_2_image, command=lambda: karakter_gekozen(venster, karakter_data[1]))
    button_2_image.image = button_2_image
    button_2.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[1]))
    button_2.pack()

    button_3_image = PhotoImage(file="images/legolas.png")
    button_3 = Button(venster, image=button_3_image, command=lambda: karakter_gekozen(venster, karakter_data[2]))
    button_3_image.image = button_3_image
    button_3.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[2]))
    button_3.pack()

    label1.place(x=550, y=50)
    button_1.pack(side="left", padx=10)
    button_2.pack(side="left", padx=100)
    button_3.pack(side="left", padx=10)
