from tkinter import Tk, Label, Button, Frame
from scherm_1 import *

def maak_karakter_dict():

def kies_karakter(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    knoppen_frame = Frame(venster)
    knoppen_frame.pack(expand=True)

    button_1 = Button(knoppen_frame, text="Aragorn", width=30, height=7, command=lambda: kies_karakter_1(venster))
    button_2 = Button(knoppen_frame, text="Gandalf", width=30, height=7, command=lambda: kies_karakter_2(venster))
    button_3 = Button(knoppen_frame, text="Frodo", width=30, height=7, command=lambda: kies_karakter_3(venster))

    button_1.pack(side="left", padx=10)
    button_2.pack(side="left", padx=10)
    button_3.pack(side="left", padx=10)

def test_star(venster):
    kies_karakter(venster)
    venster.geometry("600x600")
    venster.title("Karakter Kiezen")



venster = Tk()
test_star(venster)
venster.mainloop()
