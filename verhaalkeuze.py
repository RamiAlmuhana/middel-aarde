from tkinter import Label, Button, Tk
from keuzemomenten import maak_keuzemoment


def maak_verhaal_dict(root, karakter, verhaal):
    with open(verhaal) as bestand:
        verhaaldata = bestand.read()
    verhaaldata = verhaaldata.splitlines()
    export = []
    for line in verhaaldata:
        split_data = line.split(';;')
        verhaal_dict = {
            'naam': split_data[0],
            'stap': int(split_data[1]),
            'tekst_1': split_data[2],
            'plaatje_1': split_data[3],
            'tekst_2': split_data[4],
            'plaatje_2': split_data[5],
            'tekst_3': split_data[6],
            'plaatje_3': split_data[7],
            'eig_tekst': split_data[8],
            'eig_plaatje': split_data[9],
            'keuze_1': split_data[10],
            'keuze_2': split_data[11],
            'keuze_3': split_data[12],
        }
        export.append(verhaal_dict)
    maak_keuzemoment(root, karakter, export, 0, 'tekst_1')


def kies_verhaal(root, karakter):
    for widget in root.winfo_children():
        widget.destroy()
    instructie = Label(root, text='In welk verhaal wil je je verdiepen?')
    button_1 = Button(root, text='verhaal 1', command=lambda: maak_verhaal_dict(root, karakter, 'verhaal_1.txt'))
    button_2 = Button(root, text='verhaal 2', command=lambda: maak_verhaal_dict(root, karakter, 'verhaal_2.txt'))
    button_3 = Button(root, text='verhaal 3', command=lambda: maak_verhaal_dict(root, karakter, 'verhaal_3.txt'))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()
