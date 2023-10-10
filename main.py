import tkinter as tk
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("audio/beep.mp3")

def play_sound():
    sound.play()

root = tk.Tk()
root.title("Beep")

play_button = tk.Button(root, text="Play Sound", command=play_sound)
play_button.pack()

root.mainloop()
