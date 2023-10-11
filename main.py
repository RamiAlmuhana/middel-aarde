import tkinter as tk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("audio/1.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)


root = tk.Tk()
root.title("Muziek")

play_button = tk.Button(root, text="Hoi")
play_button.pack()

root.mainloop()
