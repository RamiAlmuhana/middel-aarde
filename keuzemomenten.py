from tkinter import Label, Button, PhotoImage
import tkinter as tk


def maak_keuzemoment(main_window, karakter, verhaal, stage, keuzetekst, keuzeplaatje, eigenschap):
    from PIL import Image, ImageTk
    from main import hoofd_menu
    from verhaalkeuze import kies_verhaal
    button_font = ("Footlight MT Light", 12, "bold")
    for widget in main_window.winfo_children():
        widget.destroy()
    if stage < 8:
        progress = Label(main_window, text=f'Verhaal: {verhaal[stage]["naam"]} \nVoortgang: '
                                           f'{str(verhaal[stage]["stap"])}/8', font=("Footlight MT Light", 16))
        if karakter['eigenschap'] == eigenschap:
            keuze_image = Image.open(verhaal[stage]['eig_plaatje'])
            keuze_image = keuze_image.resize((300, 200))
            keuze_image = ImageTk.PhotoImage(keuze_image)
            verhaaltekst = Label(text=verhaal[stage]['eig_tekst'], font=("Footlight MT Light", 16),
                                 wraplength=1200, justify="left")
            verhaalplaatje = Label(main_window, image=keuze_image)
            keuze_image.image = keuze_image
        else:
            keuze_image = Image.open(verhaal[stage][keuzeplaatje])
            keuze_image = keuze_image.resize((500, 350))
            keuze_image = ImageTk.PhotoImage(keuze_image)
            verhaaltekst = Label(text=verhaal[stage][keuzetekst], font=("Footlight MT Light", 16),
                                 wraplength=1200, justify="left")
            verhaalplaatje = Label(main_window, image=keuze_image)
            keuze_image.image = keuze_image
        button_1 = Button(main_window, text=verhaal[stage]['keuze_1'], width=40, height=7,
                          command=lambda: maak_keuzemoment(main_window, karakter, verhaal, verhaal[stage]['stap'],
                                                           'tekst_1', 'plaatje_1', ''),
                          font=button_font, bg='lightgreen')
        button_2 = Button(main_window, text=verhaal[stage]['keuze_2'], width=40, height=7,
                          command=lambda: maak_keuzemoment(main_window, karakter, verhaal, verhaal[stage]['stap'],
                                                           'tekst_2', 'plaatje_2', ''),
                          font=button_font, bg='lightgreen')
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
        verhaalplaatje.pack()
        button_verhaal.place(x=1250, y=600)
        button_hoofdmenu.place(x=1250, y=650)
        # verhaalplaatje.pack()
        if '   ' not in verhaaltekst['text']:
            button_1.place(x=100, y=450)
            button_2.place(x=500, y=450)
            button_3.place(x=900, y=450)
        else:
            from karakter_keuze import kies_karakter
            dood = Label(main_window, text='je hebt verloren', font=button_font)
            verhaalkeuzeknop = Button(main_window, text='terug naar verhaalkeuze', width=40, height=7,
                                      command=lambda: kies_verhaal(main_window, karakter), font=button_font,
                                      bg='light green')
            karakterkeuzeknop = Button(main_window, text='terug naar karakterkeuze', width=40, height=7,
                                       command=lambda: kies_karakter(main_window), font=button_font, bg='light green')
            dood.pack()
            verhaalkeuzeknop.place(x=250, y=500)
            karakterkeuzeknop.place(x=700, y=500)

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
