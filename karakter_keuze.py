from tkinter import Tk, Label, Button, Frame
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
    label1 = Label(venster, text="Welk karakter wilt u kiezen?", font=("Footlight MT Light", 18))
    button_1 = Button(venster, text=karakter_data[0]['naam'], width=30, height=7, bg='light green',
                      command=lambda: karakter_gekozen(venster, karakter_data[0]), font=button_font)
    button_2 = Button(venster, text=karakter_data[1]['naam'], width=30, height=7, bg='light green',
                      command=lambda: karakter_gekozen(venster, karakter_data[1]), font=button_font)
    button_3 = Button(venster, text=karakter_data[2]['naam'], width=30, height=7, bg='light green',
                      command=lambda: karakter_gekozen(venster, karakter_data[2]), font=button_font)
    button_hoofdmenu = Button(venster, text='hoofdmenu', command=lambda: hoofd_menu(venster),
                              font=button_font, bg='lightgreen', width=10, height=1)

    label1.pack()
    button_1.pack(side="left", padx=10)
    button_2.pack(side="left", padx=100)
    button_3.pack(side="left", padx=10)
    button_hoofdmenu.place(x=1250, y=600)
