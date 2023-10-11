from tkinter import Label, Button


def maak_keuzemoment(root, karakter, verhaal, stage, keuzetekst):
    for widget in root.winfo_children():
        widget.destroy()
    if stage < 8:
        instructie = Label(root, text=verhaal[stage][keuzetekst])
        button_1 = Button(root, text='verhaal 1', command=lambda: maak_keuzemoment(root, karakter, verhaal, verhaal[stage]['stap'], 'tekst_1'))
        button_2 = Button(root, text='verhaal 2', command=lambda: maak_keuzemoment(root, karakter, verhaal, verhaal[stage]['stap'], 'tekst_2'))
        button_3 = Button(root, text='verhaal 3', command=lambda: maak_keuzemoment(root, karakter, verhaal, verhaal[stage]['stap'], 'tekst_3'))

        instructie.pack()
        button_1.pack()
        button_2.pack()
        button_3.pack()
