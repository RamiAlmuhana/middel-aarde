import tkinter as tk
from tkinter import Menu


def main():
    def on_new():
        pass
    def on_open():
        pass
    def on_save():
        pass
    def on_exit():
        root.quit()


    root= tk.Tk()
    root.title("main menu")

    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Bestand", menu=file_menu)
    file_menu.add_command(label="Nieuw", command=on_new)
    file_menu.add_command(label="Openen", command=on_open)
    file_menu.add_command(label="Opslaan", command=on_save)
    file_menu.add_separator()
    file_menu.add_command(label="Afsluiten", command=on_exit)

    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Bewerken", menu=edit_menu)


    root.mainloop()


if __name__ == '__main__':
    main()
