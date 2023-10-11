from tkinter import Label, Button


def keuze_2_1(venster, karakter):
    from verhaal_3.verhaal_3_3 import keuze_3_1, keuze_3_2, keuze_3_3
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaal 3 stap 2 keuze 1')
    button_1 = Button(venster, text='keuze 1', command=lambda: keuze_3_1(venster, karakter))
    button_2 = Button(venster, text='keuze 2', command=lambda: keuze_3_2(venster, karakter))
    button_3 = Button(venster, text='keuze 3', command=lambda: keuze_3_3(venster, karakter))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()


def keuze_2_2(venster, karakter):
    from verhaal_3.verhaal_3_3 import keuze_3_1, keuze_3_2, keuze_3_3
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaal 3 stap 2 keuze 2')
    button_1 = Button(venster, text='keuze 1', command=lambda: keuze_3_1(venster, karakter))
    button_2 = Button(venster, text='keuze 2', command=lambda: keuze_3_2(venster, karakter))
    button_3 = Button(venster, text='keuze 3', command=lambda: keuze_3_3(venster, karakter))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()


def keuze_2_3(venster, karakter):
    from verhaal_3.verhaal_3_3 import keuze_3_1, keuze_3_2, keuze_3_3
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaal 3 stap 2 keuze 3')
    button_1 = Button(venster, text='keuze 1', command=lambda: keuze_3_1(venster, karakter))
    button_2 = Button(venster, text='keuze 2', command=lambda: keuze_3_2(venster, karakter))
    button_3 = Button(venster, text='keuze 3', command=lambda: keuze_3_3(venster, karakter))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()
