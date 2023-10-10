from tkinter import *


def verander_tekst(label, tekst):
    label['text'] = tekst


def main():
    root = Tk()
    root.geometry('1400x650')
    hello_world_label = Label(root, text='hello world')
    funny_button = Button(root, text='funny', command=lambda: verander_tekst(hello_world_label, type_thing.get()))
    type_thing = Entry(root, bd=1)

    hello_world_label.pack()
    type_thing.pack()
    funny_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
