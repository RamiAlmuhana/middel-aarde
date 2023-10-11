from tkinter import Label, Button


def keuze_3_1(venster, karakter):
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaal 3 stap 3 keuze 1')
    button_1 = Button(venster, text='keuze 1')
    button_2 = Button(venster, text='keuze 2')
    button_3 = Button(venster, text='keuze 3')

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()


def keuze_3_2(venster, karakter):
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaal 3 stap 3 keuze 2')
    button_1 = Button(venster, text='keuze 1')
    button_2 = Button(venster, text='keuze 2')
    button_3 = Button(venster, text='keuze 3')

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()


def keuze_3_3(venster, karakter):
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaal 3 stap 3 keuze 3')
    button_1 = Button(venster, text='keuze 1')
    button_2 = Button(venster, text='keuze 2')
    button_3 = Button(venster, text='keuze 3')

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()
