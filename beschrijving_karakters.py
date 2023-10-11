from tkinter import Button, Label
from verhaalkeuze import *


def karakter_gekozen(venster, karakter):
    for widget in venster.winfo_children():
        widget.destroy()
    label_font = ("Footlight MT Light", 14, "bold")
    karakternaam = Label(venster, text=karakter['naam'] + '\n' + karakter["beschrijving"] + '\n' + karakter["specialiteit"] + '\n' + karakter["ras"] + '\n', font=label_font)
    label_1 = Label(venster, text="Wilt u verder?", width=40, height=7, font=("Footlight MT Light", 18))
    button1 = Button(venster, text="Ja", width=30, height=7, command=lambda: kies_verhaal(venster, karakter), font=("Footlight MT Light", 12))
    button2 = Button(venster, text="Nee", width=30, height=7, command=lambda: on_back_button_clicked(venster), font=("Footlight MT Light", 12))

    karakternaam.pack()
    label_1.pack(side="left", pady=50, padx=10)
    button1.pack(side="left", pady=50, padx=100)
    button2.pack(side="left", pady=50, padx=10)


def on_back_button_clicked(venster):
    from karakter_keuze import kies_karakter
    for widget in venster.winfo_children():
        widget.destroy()
    kies_karakter(venster)
