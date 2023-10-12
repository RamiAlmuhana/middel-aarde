from tkinter import Tk, Label

root = Tk()
root.geometry('500x500')
root.title('workshop app')


# wisselen van schermen:
from sherm_a import maak_scherm_a_aan
maak_scherm_a_aan(root)


# fonts:
# from tkinter.font import Font
# label_font = Font(family='impact', size=23, weight='bold')
# label = Label(root, text='hello world', font=label_font)
# label.pack()
#
#
# images resizen:
from PIL import Image, ImageTk

im = Image.open("ybear.jpg")
resize = im.resize((200, 200))
voorbeeld = ImageTk.PhotoImage(resize)

label_image = Label(root, image=voorbeeld)
label_image.image = voorbeeld
#
#
# # (globals):
# # variabelen die door het hele bestand werken
# # kan verwarrend worden als je deze te vaak verandert
# # global scherm
# # scherm = root
#
#
# # Label omzetten naar button:
# label_image.bind('Button-1>', lambda click_event: maak_scherm_a_aan(root))
# label_image.pack()


root.mainloop()
