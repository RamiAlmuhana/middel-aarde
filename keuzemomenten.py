from tkinter import Label, Button


def maak_keuzemoment(root, karakter, verhaal, stage, keuzetekst, keuzeplaatje, eigenschap):
    button_font = ("Footlight MT Light", 12, "bold")
    for widget in root.winfo_children():
        widget.destroy()
    if stage < 8:
        progress = Label(root, text=f'Verhaal: {verhaal[stage]["naam"]} \nVoortgang: {str(verhaal[stage]["stap"])}/8', font=("Footlight MT Light", 16))
        if karakter['eigenschap'] == eigenschap:
            verhaaltekst = Label(root, text=verhaal[stage]['eig_tekst'], font=("Footlight MT Light", 16))
        #     verhaalplaatje = verhaal[stage]['eig_plaatje']
        else:
            verhaaltekst = Label(root, text=verhaal[stage][keuzetekst], font=("Footlight MT Light", 16))
        #     verhaalplaatje = verhaal[stage][keuzeplaatje]
        button_1 = Button(root, text=verhaal[stage]['keuze_1'], width=30, height=7, command=lambda: maak_keuzemoment(root, karakter, verhaal, verhaal[stage]['stap'], 'tekst_1', 'plaatje_1', ''), font=button_font)
        button_2 = Button(root, text=verhaal[stage]['keuze_2'], width=30, height=7, command=lambda: maak_keuzemoment(root, karakter, verhaal, verhaal[stage]['stap'], 'tekst_2', 'plaatje_2', ''), font=button_font)
        button_3 = Button(root, text=verhaal[stage]['keuze_3'], width=30, height=7, command=lambda: maak_keuzemoment(root, karakter, verhaal, verhaal[stage]['stap'], 'tekst_3', 'plaatje_3', verhaal[stage]['eigenschap']), font=button_font)

        progress.pack()
        verhaaltekst.pack()
        # verhaalplaatje.pack()
        if '   ' not in verhaaltekst['text']:
            button_1.pack(side="left", pady=50, padx=10)
            button_2.pack(side="left", pady=50, padx=250)
            button_3.pack(side="left", pady=50, padx=10)
        else:
            dood = Label(root, text='je hebt verloren')
            dood.pack()
    else:
        eindscherm = Label(root, text='eindscherm')
        eindscherm.pack()
