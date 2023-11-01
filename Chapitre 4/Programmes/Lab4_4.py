"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_4.py
					
				
"""
#-----------------------------------------------------------------------------
#PyQT5 designer : https://sourceforge.net/projects/pyqt/files/latest/download
#-----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

# Import de la bibliothèque graphique TK
from tkinter import *
from tkinter.messagebox import *
import webbrowser

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------
#from tkinter.messagebox import *
def messageNouveauProjet():
        showinfo("Logo INFO","Vous venez de créer un nouveau projet.")

def messageOuvrir():
    showinfo("Logo INFO", "Vous venez d'ouvrir un fichier.")

def messageCopier():
    showinfo("Logo INFO", "Vous venez de copier la sélection.")

def messageColler():
    showinfo("Logo INFO", "Vous venez de coller la sélection.")

def nouvelleFenetre():
    nouvelleFenetre=Toplevel(fenetre)
    label1=Label(nouvelleFenetre,text="1 - Vous devez déclarer chacun des sous-menus.",padx=50,pady=10)
    label2=Label(nouvelleFenetre, text="2 - Vous devez entrer chaque item du sous-menu.", padx=50, pady=10)
    label1.pack()
    label2.pack()

def lien_html():
    webbrowser.open('http://www.lmiot.fr')

def choix():
    choix="Vous avez fait le choix N°"+str(varGr.get())
    label.config(text=choix)


#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# Voir aussi http://tkinter.fdex.eu/doc/
# Voir https://www.tutorialspoint.com/python/.htm

#
#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# Barre de menu

# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.
#
# barreDeMenu=Menu(fenetre)
#
#
# # #------------------------------------Menu 1-----------------------------------
#
# itemMenu1=Menu(barreDeMenu,tearoff=0)
# # Si tearoff=0, le menu n’a plus d’élément graphique de «détachement»,
# # et les choix sont ajoutés à partir de la position 0.
#
# itemMenu1.add_command(label="Nouveau projet", command=messageNouveauProjet)
# itemMenu1.add_command(label="Ouvrir", command=messageOuvrir)
# itemMenu1.add_separator()
# itemMenu1.add_command(label="Quitter", command=quit)
# barreDeMenu.add_cascade(label="Fichier",menu=itemMenu1)
#
# #------------------------------------Menu 2-----------------------------------
#
# itemMenu2=Menu(barreDeMenu,tearoff=1)
# itemMenu2.add_command(label="Copier", command=messageCopier)
# itemMenu2.add_command(label="Coller", command=messageColler)
# barreDeMenu.add_cascade(label="Editer",menu=itemMenu2)
#
# #------------------------------------Menu 3-----------------------------------
#
# itemMenu3=Menu(barreDeMenu,tearoff=0)
# itemMenu3.add_command(label="Aller voir sur la documentation", command=nouvelleFenetre)
# itemMenu3.add_command(label="Vers le site...", command=lien_html)
# barreDeMenu.add_cascade(label="Aide",menu=itemMenu3)
#
#
# # Indispensable pour générer la barre de menu
# fenetre.config(menu=barreDeMenu)
# fenetre.mainloop()

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
# Bouton radio

# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x300")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.
#
# label1 = Label(fenetre, text="Bloc de boutons radio", padx=20, pady=20)
# label1.pack()
#
# valeurs = [1,2,3]
# etiquette = ['Choix N°1', 'Choix N°2', 'Choix N°3']
# varGr = StringVar()
# varGr.set(valeurs[0]) # par défaut c'est le "Choix N°1"
# for i in range(3):
#    # boutonRadio = Radiobutton(fenetre, variable=varGr, text=etiquette[i], value=valeurs[i], indicatoron=0)
#     boutonRadio = Radiobutton(fenetre, variable=varGr, text=etiquette[i], value=valeurs[i], command=choix)
#     boutonRadio.pack(expand=1) # expand=1 permet d'afficher sur toute la longueur de la fenêtre
#
#
# bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit, anchor=CENTER)
# bouton_quitter.pack(pady=20)
#
# label = Label(fenetre,pady=20)
# label.pack()
# # On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre.
# fenetre.mainloop()

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------
# Les grilles
fenetre = Tk()
fenetre.title("Vive la programmation sous Python 3 !")
fenetre.geometry("420x310")
fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.

for ligne in range(5):
    for colonne in range(5):
        Label(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=5, relief=GROOVE, padx=20,pady=15,).grid(row=ligne, column=colonne)

# Button(fenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
# Button(fenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)
# Button(fenetre, text='L2-C3', borderwidth=1).grid(row=2, column=3)
# Button(fenetre, text='L2-C4', borderwidth=1).grid(row=2, column=4)
# Button(fenetre, text='L3-C3', borderwidth=1).grid(row=3, column=3)


fenetre.mainloop()

