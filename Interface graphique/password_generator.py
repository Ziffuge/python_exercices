
import string
from tkinter import *
from random import randint, choice

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.wm_iconbitmap(r'C:\Users\eliot\Projets_Python\Interface graphique\icone_ionia.ico')
window.config(background="#115890")

frame1 = Frame(window, bg="#115890")

width = 300
height = 300
image1 = PhotoImage(file="automotive-generator.png")
canvas1 = Canvas(frame1, width=width, height=height, bg="#115890", bd=0, highlightthickness=0)
canvas1.create_image(width/2, height/2, image = image1)
canvas1.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame1, bg="#115890")

label_title = Label(right_frame, text="Mot de passe", font=("Arial", 20), bg="#115890", fg="white")
label_title.pack()

password_entry = Entry(right_frame, font=("Arial", 20), bg="#115890", fg="white")
password_entry.pack()

button1 = Button(right_frame, text="Générer", font=("Arial", 20), bg="#115890", fg="white", command=generate_password)
button1.pack()

right_frame.grid(row=0, column=1, sticky=W)

frame1.pack(expand=YES)

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()