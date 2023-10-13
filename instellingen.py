import tkinter as tk
from muziek import toggle_music, play_startup_music


def open_instellingen(main_window):
    from main import hoofd_menu
    font = ("Footlight MT Light", 16, 'bold')
    instellingen_frame = tk.Frame(main_window)
    instellingen_frame.place(x=0, y=0, relwidth=1, relheight=1)
    background_image = tk.PhotoImage(file="images/main_menu.png")

    background_label = tk.Label(main_window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    muziek_button = tk.Button(main_window, text="Pauzeer muziek", width=55, height=2,
                              borderwidth=4,
                              command=lambda: toggle_music(muziek_button), font=font)
    muziek_button.place(x=345, y=200)
    muziek_button.config(font=font)

    admin_inloggen = tk.Button(main_window, text="Admin inloggen", width=55, height=2,
                               borderwidth=4,
                               command=lambda: open_inlogscherm(main_window), font=font)
    admin_inloggen.place(x=345, y=300)
    admin_inloggen.config(font=font)

    terugknop = tk.Button(main_window, text="Terug naar main menu", width=55, height=2, borderwidth=4,
                          command=lambda: hoofd_menu(main_window), font=font)
    terugknop.place(x=345, y=400)
    terugknop.config(font=font)


def open_main(main_window):
    for widget in main_window.winfo_children():
        widget.destroy()
    open_instellingen(main_window)


def open_inlogscherm(main_window):
    global username_entry, password_entry  # Make these variables global

    inlog_frame = tk.Frame(main_window)
    inlog_frame.place(x=0, y=0, relwidth=1, relheight=1)

    inlog_label = tk.Label(inlog_frame, text="Inloggen als admin", font=("Helvetica", 16))
    inlog_label.place(x=275, y=100)

    username_label = tk.Label(inlog_frame, text="Gebruikersnaam:")
    username_label.place(x=275, y=150)
    username_entry = tk.Entry(inlog_frame)
    username_entry.place(x=400, y=150)

    password_label = tk.Label(inlog_frame, text="Wachtwoord:")
    password_label.place(x=275, y=200)
    password_entry = tk.Entry(inlog_frame, show="*")
    password_entry.place(x=400, y=200)

    inlog_button = tk.Button(inlog_frame, text="Inloggen", command=lambda: perform_login(main_window))
    inlog_button.place(x=275, y=250)

    go_back_button = tk.Button(inlog_frame, text="sluiten", command=lambda: open_main(main_window))
    go_back_button.place(x=500, y=250)


def perform_login(main_window):
    global username_entry, password_entry  # Make these variables global
    # Voeg hier je inloglogica toe
    username = username_entry.get()
    password = password_entry.get()

    # Voorbeeld: controleer of de inloggegevens overeenkomen met "admin" en "password"
    if username == "admin" and password == "password":
        show_admin_page(main_window)
    else:
        message_label = tk.Label(main_window, text="Ongeldige inloggegevens", fg="red")
        message_label.place(x=275, y=300)


def show_admin_page(main_window):
    from main import hoofd_menu
    for widget in main_window.winfo_children():
        widget.destroy()

    admin_frame = tk.Frame(main_window)
    admin_frame.pack()

    admin_label = tk.Label(admin_frame, text="Dit is de admin-pagina")
    admin_label.pack()

    terugknop = tk.Button(main_window, text="Log out", bg='lightgreen', width=55, height=2,
                          command=lambda: hoofd_menu(main_window))
    terugknop.place(x=400, y=400)
