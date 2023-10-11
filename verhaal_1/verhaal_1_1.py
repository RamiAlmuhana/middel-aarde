from tkinter import Label, Button


def verhaal_1(venster, karakter):
    from verhaal_1_2 import keuze_2_1, keuze_2_2, keuze_2_3
    for widget in venster.winfo_children():
        widget.destroy()
    instructie = Label(venster, text='verhaaltekst 1 1')
    button_1 = Button(venster, text='keuze 1', command=lambda: keuze_2_1(venster, karakter))
    button_2 = Button(venster, text='keuze 2', command=lambda: keuze_2_2(venster, karakter))
    button_3 = Button(venster, text='keuze 3', command=lambda: keuze_2_3(venster, karakter))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()
