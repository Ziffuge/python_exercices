from tkinter import *
from tkinter import ttk
import webbrowser

def launch_tutorial():
    webbrowser.open_new("https://youtu.be/N4M4W7JPOL4")

window = Tk()

window.title("My first interface")
window.geometry("480x360")
window.minsize(480, 360)
window.maxsize(1366, 768)
window.wm_iconbitmap(r'C:\Users\eliot\Projets_Python\Interface graphique\icone_ionia.ico')
window.config(background='#5CCB6B')

frame1 = Frame(window, bg='#5CCB6B')

label_title = Label(frame1, text="Bienvenue sur l'application", font=("Arial", 30), bg='#5CCB6B', fg='black')
label_title.pack()

label_subtitle = Label(frame1, text="Premier test de sous-titre", font=("Arial", 20), bg='#5CCB6B', fg='black')
label_subtitle.pack()

tuto_button = Button(frame1, text="Lancer le tutoriel", font=("Arial", 20), bg="white", fg='#5CCB6B', command=launch_tutorial)
tuto_button.pack(pady=10)

frame1.pack(expand=YES)

window.mainloop()