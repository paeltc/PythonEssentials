"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_3.py
					
				
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
#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------
#from tkinter.messagebox import *
def messageYesNo():
    if askyesno("Boîte de message formatée OUI/NON","Voulez-vous me donner 10 000 euros ?"):
        showwarning('Logo ATTENTION',"Merci, c'est cool!")
    else:
        showinfo("Logo INFO","Tant pis... j'aurais essayé.")
        showerror("Logo ERREUR","Ce n'est pas grave, je finirai par les avoir !")

def messageCancel():
    if askokcancel("Boîte de message formatée OK/ANNULER", "Voulez-vous me donner 10 000 euros ?"):
        showinfo("LOGO info", "D'accord... Pas de problème.")
    else:
        showwarning("LOGO attention", "Vous avez tout annulé... c'est-à-dire pas grand chose.")

def messageRetryCancel():
    if askretrycancel("Boîte de message formatée REESSAYER/ANNULER", "Voulez-vous me donner 10 000 euros ?"):
        showinfo("LOGO info","C'est bien de réessayer mais il faut le faire !")
    else:
        showwarning("LOGO attention","Vous annulez... vous ne voulez vraiment pas !")


# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# Voir aussi http://tkinter.fdex.eu/doc/

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# Conteneur de fenêtres

# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.
#
# separateurDeFenetre = PanedWindow(fenetre, orient=VERTICAL,relief=RAISED)
# separateurDeFenetre.pack(side=TOP, expand=Y, fill=BOTH, pady=10, padx=10)
#
# # Cette méthode de déclaration ne fonctionne pas.
# # Label1=Label(separateurDeFenetre, text='Volet 1', background='blue', anchor=CENTER)
# # Label2=Label(separateurDeFenetre, text='Volet 2', background='blue', anchor=CENTER)
# # Label3=Label(separateurDeFenetre, text='Volet 3', background='blue', anchor=CENTER)
# # separateurDeFenetre.pack()
#
# separateurDeFenetre.add(Label(separateurDeFenetre, text='Volet 1', background='blue', anchor=CENTER))
# separateurDeFenetre.add(Label(separateurDeFenetre, text='Volet 2', background='orange', anchor=CENTER) )
# separateurDeFenetre.add(Label(separateurDeFenetre, text='Volet 3', background='red', anchor=CENTER) )
# separateurDeFenetre.pack()
#
# fenetre.mainloop()

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

# Label de cadre
fenetre = Tk()
fenetre.title("Vive la programmation sous Python 3 !")
fenetre.geometry("500x200")
fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.
fenetre['bg']='yellow'

# Grand cadre
cadreGrand = Frame(fenetre, borderwidth=2, relief=RAISED, bg="red")
cadreGrand.pack(side=TOP, padx=20, pady=40)

# cadre 2
cadre2 = Frame(cadreGrand, borderwidth=2, relief=SUNKEN)
cadre2.pack(side=LEFT, padx=20, pady=10)

# cadre 2
cadre3 = Frame(cadreGrand, borderwidth=2, relief=SUNKEN)
cadre3.pack(side=RIGHT, padx=10, pady=10)


# Les icônes pour les messageBox sont les mêmes que l'icône de la fenêtre principale

Bouton=Button(cadre2, text="Le bouton Annuler ici",command=messageCancel,cursor="circle").pack(padx=10, pady=10)
Bouton=Button(cadre3, text="Le bouton Oui/Non ici",command=messageYesNo,cursor="cross").pack(padx=10, pady=10)
Bouton=Button(cadre3, text="Le bouton Essayer/Annuler ici",command=messageRetryCancel,cursor="pirate").pack(padx=10, pady=10)


fenetre.mainloop()




