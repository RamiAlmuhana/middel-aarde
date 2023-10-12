from tkinter import Label, Button


def ga_naar_scherm_a(venster):
    from workshop.sherm_a import maak_scherm_a_aan
    maak_scherm_a_aan(venster)


def maak_scherm_b_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    label = Label(venster, text='dit is scherm B')
    button = Button(venster, text='ga naar scherm A', command=lambda: ga_naar_scherm_a(venster))

    label.pack()
    button.pack()
