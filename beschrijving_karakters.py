from tkinter import *
from verhaalkeuze import *

def center_venster(venster):
    venster.update_idletasks()
    screen_width = venster.winfo_screenwidth()
    screen_height = venster.winfo_screenheight()
    x = (screen_width - venster.winfo_width()) // 2
    y = (screen_height - venster.winfo_height()) // 2
    venster.geometry("+{}+{}".format(x, y))
    center_venster(venster)

def karakter_gekozen(venster, karakter):
    for widget in venster.winfo_children():
        widget.destroy()

    background_image = PhotoImage(file="images/img_1.png")

    background_label = Label(venster, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label_font = ("Footlight MT Light", 14, "bold")
    karakternaam = Label(venster,
                         text=f"Naam: {karakter['naam']} '\n' Beschrijving: {karakter['beschrijving']} '\n' Eigenschap: {karakter['eigenschap']} '\n' Ras: {karakter['ras']}",
                         font=label_font, bg="black", fg="white")
    label_1 = Label(venster, text="Wilt u verder? \n Kies:", width=40, height=7, font=("Footlight MT Light", 18), bg="black", fg="white")
    button1 = Button(venster, text="Ja", width=30, height=7, command=lambda: kies_verhaal(venster, karakter),
                     font=("Footlight MT Light", 12), fg="black")
    button2 = Button(venster, text="Nee", width=30, height=7, command=lambda: on_back_button_clicked(venster),
                     font=("Footlight MT Light", 12),  fg="black")

    karakternaam.pack(pady=40)
    label_1.pack(side="left", pady=50, padx=10)
    button1.pack(side="left", pady=50, padx=100)
    button2.pack(side="left", pady=50, padx=10)


def on_back_button_clicked(venster):
    from karakter_keuze import kies_karakter
    for widget in venster.winfo_children():
        widget.destroy()
    kies_karakter(venster)
