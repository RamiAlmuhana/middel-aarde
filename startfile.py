from tkinter import Tk

from karakter_keuze import kies_karakter


def test_star(venster):
    kies_karakter(venster, test_star)
    venster.geometry("1400x700")
    venster.title("Karakter Kiezen")
    venster.mainloop()



root = Tk()
test_star(root)
