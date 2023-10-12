from tkinter import Label, Button, PhotoImage
import tkinter as tk


def maak_keuzemoment(main_window, karakter, verhaal, stage, keuzetekst, keuzeplaatje, eigenschap):
    from main import hoofd_menu
    from verhaalkeuze import kies_verhaal
    button_font = ("Footlight MT Light", 12, "bold")
    for widget in main_window.winfo_children():
        widget.destroy()
    if stage < 8:
        progress = Label(main_window,
                         text=f'Verhaal: {verhaal[stage]["naam"]} \nVoortgang: {str(verhaal[stage]["stap"])}/8',
                         font=("Footlight MT Light", 16))
        if karakter['eigenschap'] == eigenschap:
            verhaaltekst = Label(main_window, text=verhaal[stage]['eig_tekst'], font=("Footlight MT Light", 16))
        #     verhaalplaatje = verhaal[stage]['eig_plaatje']
        else:
            # keuze_image = PhotoImage(file=verhaal[stage][keuzeplaatje])
            # verhaaltekst = Label(main_window, image=keuze_image, text=verhaal[stage][keuzetekst], compound='center', font=("Footlight MT Light", 16), fg='white')
            # keuze_image.image = keuze_image
            verhaaltekst = Label(main_window, wraplength=600, justify="left", text=verhaal[stage][keuzetekst],
                                 font=button_font)
        button_1 = Button(main_window, text=verhaal[stage]['keuze_1'], width=40, height=7,
                          command=lambda: maak_keuzemoment(main_window, karakter, verhaal, verhaal[stage]['stap'],
                                                           'tekst_1', 'plaatje_1', ''), font=button_font,
                          bg='lightgreen')
        button_2 = Button(main_window, text=verhaal[stage]['keuze_2'], width=40, height=7,
                          command=lambda: maak_keuzemoment(main_window, karakter, verhaal, verhaal[stage]['stap'],
                                                           'tekst_2', 'plaatje_2', ''), font=button_font,
                          bg='lightgreen')
        button_3 = Button(main_window, text=verhaal[stage]['keuze_3'], width=40, height=7,
                          command=lambda: maak_keuzemoment(main_window, karakter, verhaal, verhaal[stage]['stap'],
                                    'tekst_3', 'plaatje_3', verhaal[stage]['eigenschap']),
                                            font=button_font, bg='lightgreen')
        button_hoofdmenu = Button(main_window, text='hoofdmenu', command=lambda: hoofd_menu(main_window),
                                            font=button_font, bg='lightgreen', width=10, height=1)
        button_verhaal = Button(main_window, text='kies verhaal', command=lambda: kies_verhaal(main_window, karakter),
                                            font=button_font, bg='lightgreen', width=10, height=1)

        progress.pack()
        verhaaltekst.pack()
        button_verhaal.place(x=1250, y=500)
        button_hoofdmenu.place(x=1250, y=550)
        # verhaalplaatje.pack()
        if '   ' not in verhaaltekst['text']:
            button_1.pack(side="left", pady=10, padx=10)
            button_2.pack(side="left", pady=50, padx=20)
            button_3.pack(side="left", pady=50, padx=10)
        else:
            from karakter_keuze import kies_karakter
            dood = Label(main_window, text='je hebt verloren', font=button_font)
            verhaalkeuzeknop = Button(main_window, text='terug naar verhaalkeuze', width=40, height=7,
                                      command=lambda: kies_verhaal(main_window, karakter), font=button_font)
            karakterkeuzeknop = Button(main_window, text='terug naar karakterkeuze', width=40, height=7,
                                       command=lambda: kies_karakter(main_window), font=button_font)
            dood.pack()
            verhaalkeuzeknop.pack(side='left', pady=50, padx=20)
            karakterkeuzeknop.pack(side='left', pady=50, padx=20)

    else:
        logo_image = PhotoImage(file=verhaal[stage][keuzeplaatje])
        logo_frame = Label(main_window, image=logo_image, text=verhaal[stage][keuzetekst],
                           font=('Footlight MT Light', 20),
                           fg='white', compound='center')
        logo_frame.image = logo_image
        logo_frame.pack()
        terugknop = tk.Button(main_window, text="Terug naar main menu", bg='lightgreen', width=55, height=2,
                              command=lambda: hoofd_menu(main_window))
        terugknop.place(x=400, y=400)
