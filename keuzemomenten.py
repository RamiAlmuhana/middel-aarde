from tkinter import Label, Button, PhotoImage


def maak_keuzemoment(root, menu, karakter, verhaal, stage, keuzetekst, keuzeplaatje, eigenschap):
    button_font = ("Footlight MT Light", 12, "bold")
    for widget in root.winfo_children():
        widget.destroy()
    if stage < 8:
        progress = Label(root, text=f'Verhaal: {verhaal[stage]["naam"]} \nVoortgang: {str(verhaal[stage]["stap"])}/8', font=("Footlight MT Light", 16))
        if karakter['eigenschap'] == eigenschap:
            verhaaltekst = Label(root, text=verhaal[stage]['eig_tekst'], font=("Footlight MT Light", 16))
        #     verhaalplaatje = verhaal[stage]['eig_plaatje']
        else:
            # keuze_image = PhotoImage(file=verhaal[stage][keuzeplaatje])
            # verhaaltekst = Label(root, image=keuze_image, text=verhaal[stage][keuzetekst], compound='center', font=("Footlight MT Light", 16), fg='white')
            # keuze_image.image = keuze_image
            verhaaltekst = Label(root, wraplength=600, justify="left", text=verhaal[stage][keuzetekst], font=button_font)
        button_1 = Button(root, text=verhaal[stage]['keuze_1'], width=40, height=7, command=lambda: maak_keuzemoment(root, menu, karakter, verhaal, verhaal[stage]['stap'], 'tekst_1', 'plaatje_1', ''), font=button_font, bg='lightgreen')
        button_2 = Button(root, text=verhaal[stage]['keuze_2'], width=40, height=7, command=lambda: maak_keuzemoment(root, menu, karakter, verhaal, verhaal[stage]['stap'], 'tekst_2', 'plaatje_2', ''), font=button_font, bg='lightgreen')
        button_3 = Button(root, text=verhaal[stage]['keuze_3'], width=40, height=7, command=lambda: maak_keuzemoment(root, menu, karakter, verhaal, verhaal[stage]['stap'], 'tekst_3', 'plaatje_3', verhaal[stage]['eigenschap']), font=button_font, bg='lightgreen')
        button = Button(root, text='ga terug', command=lambda: menu(root), font=button_font, bg='lightgreen')

        progress.pack()
        verhaaltekst.pack()
        # verhaalplaatje.pack()
        if '   ' not in verhaaltekst['text']:
            button_1.pack(side="left", pady=10, padx=10)
            button_2.pack(side="left", pady=50, padx=20)
            button_3.pack(side="left", pady=50, padx=10)
            button.place(x=1100, y=600)
        else:
            from karakter_keuze import kies_karakter
            from verhaalkeuze import kies_verhaal
            dood = Label(root, text='je hebt verloren', font=button_font)
            verhaalkeuzeknop = Button(root, text='terug naar verhaalkeuze', width=40, height=7,
                                      command=lambda: kies_verhaal(root, menu, karakter), font=button_font)
            karakterkeuzeknop = Button(root, text='terug naar karakterkeuze', width=40, height=7,
                                       command=lambda: kies_karakter(root, menu), font=button_font)
            dood.pack()
            verhaalkeuzeknop.pack(side='left', pady=50, padx=20)
            karakterkeuzeknop.pack(side='left', pady=50, padx=20)

    else:
        logo_image = PhotoImage(file=verhaal[stage][keuzeplaatje])
        logo_frame = Label(root, image=logo_image, text=verhaal[stage][keuzetekst], font=('Footlight MT Light', 20),
                           fg='white', compound='center')
        logo_frame.image = logo_image
        logo_frame.pack()
        button = Button(root, text='ga terug', command=lambda: menu(root), font=button_font, bg='lightgreen')
        button.place(x=630, y=550)
        return root
