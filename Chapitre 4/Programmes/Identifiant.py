#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Feb 02, 2018 12:53:28 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Identifiant_support

# ----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
# ----------------------------------------------------------------------------------------------------------------------

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Gestion_des_mots_de_passe (root)
    Identifiant_support.init(root, top)
    root.mainloop()

w = None
def create_Gestion_des_mots_de_passe(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Gestion_des_mots_de_passe (w)
    Identifiant_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Gestion_des_mots_de_passe():
    global w
    w.destroy()
    w = None


class Gestion_des_mots_de_passe:

# ----------------------------------------------------------------------------------------------------------------------
    def quitterClick(self):
        message=messagebox.askyesno ("Fenêtre de connexion...","Êtes-vous certain de quitter ?")
        if message:
            exit()
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def annulerClick(self):
        self.EntryIdentifiant.delete(0,END)
        self.EntryMotsDePass.delete(0,END)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def connexionClick(self):
        identifiant=self.EntryIdentifiant.get()
        mot_de_passe=self.EntryMotsDePass.get()

        if identifiant == "Denis" and mot_de_passe=="1976":
            messagebox.showinfo("Fenêtre de connexion...","Bienvenue dans votre session.")
            self.EntryMotsDePass.delete(0, END)
            self.EntryIdentifiant.delete(0, END)
        else:
            messagebox.showerror("Erreur de connexion","Vérifiez votre identifiant ou/et votre mot de passe !")
            self.EntryMotsDePass.delete(0, END)
            self.EntryIdentifiant.delete(0, END)

# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("574x328+553+213")
        top.title("Gestion des mots de passe")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.ButtonConnexion = Button(top)
        self.ButtonConnexion.place(relx=0.12, rely=0.73, height=24, width=97)
        self.ButtonConnexion.configure(activebackground="#d9d9d9")
        self.ButtonConnexion.configure(activeforeground="#000000")
        self.ButtonConnexion.configure(background="#d9d9d9")
        self.ButtonConnexion.configure(disabledforeground="#a3a3a3")
        self.ButtonConnexion.configure(foreground="#000000")
        self.ButtonConnexion.configure(highlightbackground="#d9d9d9")
        self.ButtonConnexion.configure(highlightcolor="black")
        self.ButtonConnexion.configure(overrelief="sunken")
        self.ButtonConnexion.configure(pady="0")
        self.ButtonConnexion.configure(text='''Connexion''')
# ----------------------------------------------------------------------------------------------------------------------
        self.ButtonConnexion.configure(command=self.connexionClick)
# ----------------------------------------------------------------------------------------------------------------------


        self.ButtonAnnuler = Button(top)
        self.ButtonAnnuler.place(relx=0.38, rely=0.73, height=24, width=117)
        self.ButtonAnnuler.configure(activebackground="#d9d9d9")
        self.ButtonAnnuler.configure(activeforeground="#000000")
        self.ButtonAnnuler.configure(background="#d9d9d9")
        self.ButtonAnnuler.configure(disabledforeground="#a3a3a3")
        self.ButtonAnnuler.configure(foreground="#000000")
        self.ButtonAnnuler.configure(highlightbackground="#d9d9d9")
        self.ButtonAnnuler.configure(highlightcolor="black")
        self.ButtonAnnuler.configure(pady="0")
        self.ButtonAnnuler.configure(text='''Annuler''')
# ----------------------------------------------------------------------------------------------------------------------
        self.ButtonAnnuler.configure(command=self.annulerClick)
# ----------------------------------------------------------------------------------------------------------------------


        self.LabelIdentifiant = Label(top)
        self.LabelIdentifiant.place(relx=0.07, rely=0.3, height=31, width=114)
        self.LabelIdentifiant.configure(activebackground="#f9f9f9")
        self.LabelIdentifiant.configure(activeforeground="black")
        self.LabelIdentifiant.configure(background="#d9d9d9")
        self.LabelIdentifiant.configure(disabledforeground="#a3a3a3")
        self.LabelIdentifiant.configure(font=font9)
        self.LabelIdentifiant.configure(foreground="#000000")
        self.LabelIdentifiant.configure(highlightbackground="#d9d9d9")
        self.LabelIdentifiant.configure(highlightcolor="black")
        self.LabelIdentifiant.configure(text='''Identifiant''')

        self.EntryIdentifiant = Entry(top)
        self.EntryIdentifiant.place(relx=0.38, rely=0.3, height=30
                , relwidth=0.39)
        self.EntryIdentifiant.configure(background="white")
        self.EntryIdentifiant.configure(disabledforeground="#a3a3a3")
        self.EntryIdentifiant.configure(font="TkFixedFont")
        self.EntryIdentifiant.configure(foreground="#000000")
        self.EntryIdentifiant.configure(highlightbackground="#d9d9d9")
        self.EntryIdentifiant.configure(highlightcolor="black")
        self.EntryIdentifiant.configure(insertbackground="black")
        self.EntryIdentifiant.configure(selectbackground="#c4c4c4")
        self.EntryIdentifiant.configure(selectforeground="black")
# ----------------------------------------------------------------------------------------------------------------------
        self.EntryIdentifiant.insert(0, "Votre identifiant !")
# ----------------------------------------------------------------------------------------------------------------------

        self.LabelMotDePass = Label(top)
        self.LabelMotDePass.place(relx=0.05, rely=0.46, height=31, width=154)
        self.LabelMotDePass.configure(activebackground="#f9f9f9")
        self.LabelMotDePass.configure(activeforeground="black")
        self.LabelMotDePass.configure(background="#d9d9d9")
        self.LabelMotDePass.configure(disabledforeground="#a3a3a3")
        self.LabelMotDePass.configure(font=font9)
        self.LabelMotDePass.configure(foreground="#000000")
        self.LabelMotDePass.configure(highlightbackground="#d9d9d9")
        self.LabelMotDePass.configure(highlightcolor="black")
        self.LabelMotDePass.configure(text='''Mot de passe :''')

        self.EntryMotsDePass = Entry(top)
        self.EntryMotsDePass.place(relx=0.38, rely=0.46, height=30
                , relwidth=0.39)
        self.EntryMotsDePass.configure(background="white")
        self.EntryMotsDePass.configure(disabledforeground="#a3a3a3")
        self.EntryMotsDePass.configure(font="TkFixedFont")
        self.EntryMotsDePass.configure(foreground="#000000")
        self.EntryMotsDePass.configure(highlightbackground="#d9d9d9")
        self.EntryMotsDePass.configure(highlightcolor="black")
        self.EntryMotsDePass.configure(insertbackground="black")
        self.EntryMotsDePass.configure(selectbackground="#c4c4c4")
        self.EntryMotsDePass.configure(selectforeground="black")
# ----------------------------------------------------------------------------------------------------------------------
        self.EntryMotsDePass.insert(0, "Votre mot de passe !")
# ----------------------------------------------------------------------------------------------------------------------


        self.ButtonQuitter = Button(top)
        self.ButtonQuitter.place(relx=0.7, rely=0.73, height=24, width=107)
        self.ButtonQuitter.configure(activebackground="#d9d9d9")
        self.ButtonQuitter.configure(activeforeground="#000000")
        self.ButtonQuitter.configure(background="#d9d9d9")
        self.ButtonQuitter.configure(disabledforeground="#a3a3a3")
        self.ButtonQuitter.configure(foreground="#000000")
        self.ButtonQuitter.configure(highlightbackground="#d9d9d9")
        self.ButtonQuitter.configure(highlightcolor="black")
        self.ButtonQuitter.configure(pady="0")
        self.ButtonQuitter.configure(text='''Quitter''')
        self.ButtonQuitter.configure(width=107)
#-----------------------------------------------------------------------------------------------------------------------
        self.ButtonQuitter.configure(command=self.quitterClick)
# -----------------------------------------------------------------------------------------------------------------------

        self.LabelTitre = Label(top)
        self.LabelTitre.place(relx=0.1, rely=0.12, height=31, width=454)
        self.LabelTitre.configure(background="#d9d9d9")
        self.LabelTitre.configure(disabledforeground="#a3a3a3")
        self.LabelTitre.configure(font=font9)
        self.LabelTitre.configure(foreground="#000000")
        self.LabelTitre.configure(relief=SUNKEN)
        self.LabelTitre.configure(text='''Vive la formation sur Python 3''')
        self.LabelTitre.configure(width=454)






if __name__ == '__main__':
    vp_start_gui()


