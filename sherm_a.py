from tkinter import Label, Button


def ga_naar_scherm_b(venster):
    from scherm_b import maak_scherm_b_aan
    maak_scherm_b_aan(venster)


def maak_scherm_a_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    label = Label(venster, text='dit is scherm A')
    button = Button(venster, text='ga naar scherm B', command=lambda: ga_naar_scherm_b(venster))

    label.pack()
    button.pack()
