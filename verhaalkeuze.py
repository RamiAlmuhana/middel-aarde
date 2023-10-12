from tkinter import Label, Button, Tk
from keuzemomenten import maak_keuzemoment


def maak_verhaal_dict(root, menu, karakter, verhaal):
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
            'eigenschap': split_data[13]        }
        export.append(verhaal_dict)
    maak_keuzemoment(root, menu, karakter, export, 0, 'tekst_1', '', '')


def kies_verhaal(root, menu, karakter):
    for widget in root.winfo_children():
        widget.destroy()

    button_font = ("Footlight MT Light", 13, "bold")

    instructie = Label(root, text='In welk verhaal wil je je verdiepen?', font=("Footlight MT Light", 18))
    button_1 = Button(root, text='Avontuur in de Shire', width=30, height=7, command=lambda: maak_verhaal_dict(root, menu, karakter, 'verhaal_1.txt'), font=button_font)
    button_2 = Button(root, text='Zoektocht naar het Zwaard', width=30, height=7, command=lambda: maak_verhaal_dict(root, menu, karakter, 'verhaal_2.txt'), font=button_font)
    button_3 = Button(root, text='Ontwakenen van de Enten', width=30, height=7, command=lambda: maak_verhaal_dict(root, menu, karakter, 'verhaal_3.txt'), font=button_font)

    instructie.pack()
    button_1.pack(side="left", pady=50, padx=12)
    button_2.pack(side="left", pady=50, padx=200)
    button_3.pack(side="left", pady=50, padx=10)
