from tkinter import Tk, Label


def main():
    root = Tk()
    root.geometry('400x400')
    hello_world_label = Label(root, text= 'hello world')
    hello_world_label.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
