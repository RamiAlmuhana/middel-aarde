import tkinter as tk
import pygame


def button_play():
    pygame.mixer.init()
    pygame.mixer.music.load("audio/button_sound.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)


def music_play():
    pygame.mixer.init()
    pygame.mixer.music.load("audio/1.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.5)


def music_stop():
    pygame.mixer.music.stop()


def test_menu():
    root = tk.Tk()
    root.title("Muziek")
    button = tk.Button(root, text="Klik voor button geluidje", command=music_play)
    root.geometry('400x400')
    button.pack()
    root.mainloop()


def main():
    music_play()
    test_menu()


if __name__ == '__main__':
    main()
