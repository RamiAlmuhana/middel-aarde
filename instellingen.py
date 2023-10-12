import tkinter as tk


def open_instellingen(main_window):
    font = ("Helvetica", 16)
    instellingen_frame = tk.Frame(main_window)
    instellingen_frame.place(x=0, y=0, relwidth=1, relheight=1)
    instellingen_frame.configure(bg="darkgreen")

    admin_inloggen = tk.Button(instellingen_frame, text="Admin inloggen", bg='lightgreen', width=55, height=2,
                               command=lambda: open_inlogscherm(main_window), font=font)
    admin_inloggen.place(x=400, y=300)


def open_main(main_window):
    from main import main
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
    for widget in main_window.winfo_children():
        widget.destroy()

    # Maak een frame voor de admin-pagina
    admin_frame = tk.Frame(main_window)
    admin_frame.pack()

    # Voeg hier widgets toe voor de admin-pagina
    admin_label = tk.Label(admin_frame, text="Dit is de admin-pagina")
    admin_label.pack()
