from tkinter import Button, Label


def kies_karakter_1(venster):
    for widget in venster.winfo_children():
        widget.destroy()
    label_1 = Label(venster, text="Wilt u verder?", width=30, height=7)
    button1 = Button(venster, text= "Ja", width=30, height=7)
    button2 = Button(venster, text= "Nee",width=30, height=7, command= lambda: on_back_button_clicked(venster))


    label_1.pack(side="top", pady= 50, padx=10)
    button1.pack(side="left", pady= 50, padx=10)
    button2.pack(side="left",pady= 50, padx=10)


def kies_karakter_2(venster):
    for wiget in venster.winfo_children():
        wiget.destroy()
    label_1 = Label(venster, text="Wilt u verder?")

    label_1.pack(side="left", padx=10)


def kies_karakter_3(venster):
    for widget in venster.winfo_children():
        widget.destroy()
    label_1 = Label(venster, text="Wilt u verder?")

    label_1.pack(side="left", padx=10)


def on_back_button_clicked(venster):
    from karakter_keuze import kies_karakter
    for widget in venster.winfo_children():
        widget.destroy()
    kies_karakter(venster)

