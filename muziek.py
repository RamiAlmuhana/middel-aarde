from pygame import mixer

mixer.init()

music_playing = True


def toggle_music(music_button):
    global music_playing
    if music_playing:
        mixer.music.pause()
        music_playing = False
        music_button.config(text="Speel muziek")
    else:
        mixer.music.unpause()
        music_playing = True
        music_button.config(text="Pauzeer muziek")


def play_startup_music():
    mixer.music.load('audio/Evenstar.mp3')
    mixer.music.play()


play_startup_music()