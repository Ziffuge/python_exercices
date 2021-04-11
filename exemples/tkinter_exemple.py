
import tkinter
from tkinter import messagebox

def show_modal_window():
    messagebox.showerror("ERREUR", "Un problème est survenu")

"""
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
""" 

mainapp = tkinter.Tk()
mainapp.title("Exemple d'interface graphique") #définir le titre
mainapp.minsize(480, 360) #définir les dimensions minimales

#mainapp.geometry("X x Y + 0 + 0", ) 
#"+0+0"=position du point d'origine
screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()
window_x = 720
window_y = 480
#centrer la page au milieu de l'écran
pos_x = (screen_x // 2) - (window_x // 2)
pos_y = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y)

mainapp.geometry(geo) #définir les dimensions

label_welcome = tkinter.Label(mainapp, text="Bienvenue") #zone de texte

entry_name = tkinter.Entry(mainapp) #zone d'input de texte

button_quit = tkinter.Button(mainapp, text="Quitter", command=mainapp.quit) #button

check_widget = tkinter.Checkbutton(mainapp, text="Recevoir les notifications") #case à cocher ou non

radio_widget = tkinter.Radiobutton(mainapp, text="Homme", value=0) #cases à choix unique
radio_widget2 = tkinter.Radiobutton(mainapp, text="Femme", value=1)

scale_widget = tkinter.Scale(mainapp, from_=2, to=10, orient="horizontal") #échelle graduée

spin_widget = tkinter.Spinbox(mainapp, from_=0, to=100) #comme les PV sur roll20

lb_widget = tkinter.Listbox(mainapp) #liste de choix
lb_widget.insert(1, "Aujourd'hui")
lb_widget.insert(2, "Demain")
lb_widget.insert(3, "Dans trois jours")

error_button = tkinter.Button(mainapp, text="Erreur", command=show_modal_window)


label_welcome.pack()
entry_name.pack()
button_quit.pack()
check_widget.pack()
radio_widget.pack()
radio_widget2.pack()
scale_widget.pack()
spin_widget.pack()
lb_widget.pack()
error_button.pack()

mainapp.mainloop()