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

    # venster = Frame(venster)
    # venster.pack(expand=True)

    button_font = ("Footlight MT Light", 12, "bold")
    label1 = Label(knoppen_frame, text="Welk karakter wilt u kiezen?", font=("Footlight MT Light", 18))
    button_1 = Button(knoppen_frame, text=karakter_data[0]['naam'], width=30, height=7,
                      command=lambda: karakter_gekozen(venster, karakter_data[0]), font=button_font)
    button_2 = Button(knoppen_frame, text=karakter_data[1]['naam'], width=30, height=7,
                      command=lambda: karakter_gekozen(venster, karakter_data[1]), font=button_font)
    button_3 = Button(knoppen_frame, text=karakter_data[2]['naam'], width=30, height=7,
                      command=lambda: karakter_gekozen(venster, karakter_data[2]), font=button_font)

    button_2_image = PhotoImage(file="images/gimli.png")
    button_2 = Button(knoppen_frame, image=button_2_image, command=lambda: karakter_gekozen(venster, karakter_data[1]))
    button_2_image.image = button_2_image
    button_2.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[1]))
    button_2.pack()

    button_3_image = PhotoImage(file="images/legolas.png")
    button_3 = Button(knoppen_frame, image=button_3_image, command=lambda: karakter_gekozen(venster, karakter_data[2]))
    button_3_image.image = button_3_image
    button_3.bind("<Button-1>", lambda event: karakter_gekozen(venster, karakter_data[2]))
    button_3.pack()

    label1.place()
    karakternaam.place(x=100, y=500)
    button_1.pack(side="left", padx=10)
    button_2.pack(side="left", padx=100)
    button_3.pack(side="left", padx=10)
    button_hoofdmenu.place(x=1250, y=600)
