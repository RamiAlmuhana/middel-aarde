from tkinter import Label, Button, Tk


def kies_verhaal(root, karakter):
    from verhaal_1.verhaal_1_1 import verhaal_1
    from verhaal_2.verhaal_2_1 import verhaal_2
    from verhaal_3.verhaal_3_1 import verhaal_3
    for widget in root.winfo_children():
        widget.destroy()
    instructie = Label(root, text='In welk verhaal wil je je verdiepen?')
    button_1 = Button(root, text='verhaal 1', command=lambda: verhaal_1(root, karakter))
    button_2 = Button(root, text='verhaal 2', command=lambda: verhaal_2(root, karakter))
    button_3 = Button(root, text='verhaal 3', command=lambda: verhaal_3(root, karakter))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()

    root.mainloop()


def test_start():
    root = Tk()
    root.geometry('400x400')
    kies_verhaal(root, 'frodo')


test_start()
