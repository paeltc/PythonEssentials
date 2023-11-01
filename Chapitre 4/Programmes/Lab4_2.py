"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RANTÉ

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_2.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

# Import de la bibliothèque graphique TK
from tkinter import *

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# Voir aussi http://tkinter.fdex.eu/doc/


#
#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source
# fenetre['bg']='grey'          # Définition de la couleur de fond de la fenêtre principale
#
# cadre1 = Frame(fenetre)
# cadre1.pack(side=BOTTOM)                    # Toujours en bas et au centre
# #Label(cadre1, text="Cadre 1").pack()        # Ajusté à l'écriture du contenu
# #Label(cadre1, text="Cadre 1").pack(pady=20) # On impose une hauteur de 20px
# Label(cadre1, text="Cadre 1").pack(padx=20,pady=20) # On impose une hauteur de 20px et une marge de 10px
# fenetre.mainloop()

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source
# fenetre['bg']='orange'            # Définition de la couleur de fond de la fenêtre principale
#
# cadre2 = Frame(fenetre)
# #cadre2.pack(side=LEFT)                  # Toujours à gauche et au centre
# #cadre2.pack(side=RIGHT)                 # Toujours à droite et au centre
# cadre2.pack(side=TOP)                    # Toujours à droiteen haut et au centre
# Label(cadre2, text="Cadre 2").pack()      # Ajusté à l'écriture du contenu
#
# fenetre.mainloop()

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.
# fenetre['bg']='navy'            # Définition de la couleur de fond de la fenêtre principale
#
# cadre2 = Frame(fenetre)
# cadre2.pack(side=LEFT)                  # Toujours à gauche et au centre
#
# Label1=Label(cadre2, text="Cadre 1 à gauche", fg="grey").pack(side=LEFT) # Les cadres sont placés les uns à la suite des autres
# Label2=Label(cadre2, text="Cadre 2 à gauche", fg="grey").pack(side=LEFT) # dans un même cadre.
# Label3=Label(cadre2, text="Cadre 3 en bas", fg="grey").pack(side=BOTTOM)
# Label4=Label(cadre2, text="Cadre 4 à droite", fg="grey").pack(side=RIGHT)
# Label5=Label(cadre2, text="Cadre 5 en haut", fg="grey").pack(side=TOP)
# fenetre.mainloop()

#-------------------------------------------- Exemple N°4 --------------------------------------------------------------
# Associer un cadre pour chaque élément
# # Créer un container avec les onglets Ouvrir, Fermer et Réduire
# fenetre = Tk()
# fenetre.title("Vive la programmation sous Python 3 !")
# fenetre.geometry("400x200")
# fenetre.iconbitmap("book.ico") # L'emplacement est au même endroit que le fichier source.
# fenetre['bg']='green'
#
# # cadre 1
# cadre1 = Frame(fenetre, borderwidth=2, relief=RAISED)
# cadre1.pack(side=TOP, padx=20, pady=10) # pady est sans effet car side impose le centre.
#
# # Cadre 2
# cadre2 = Frame(fenetre, borderwidth=2, relief=SUNKEN)
# cadre2.pack(side=LEFT, padx=10, pady=10)
#
# # Cadre 3
# cadre3 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
# cadre3.pack(side=RIGHT, padx=5, pady=5)
#
# # Cadre 4
# cadre4 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
# cadre4.pack(side=BOTTOM, padx=5, pady=5)
#
# # Ajouter des composants
# Bouton=Button(cadre1, text="Le bouton 1 ici").pack(padx=10, pady=10)
# Label1= Label(cadre2, text="Cadre 1").pack(padx=10, pady=10)
# Bouton=Button(cadre3, text="Le bouton 2 ici").pack(padx=10, pady=10)
# Label2= Label(cadre4, text="Cadre 2").pack(padx=10, pady=10)
#
# fenetre.mainloop()

#-------------------------------------------- Exemple N°4 --------------------------------------------------------------
# Associer un cadre dans un cadre

# Créer un container avec les onglets Ouvrir, Fermer et Réduire
fenetre = Tk()
fenetre.title("Vive la programmation sous Python 3 !")
fenetre.geometry("400x200")
fenetre.iconbitmap("book.ico") # L'emplacement est au même endroit que le fichier source.
fenetre['bg']='yellow'

# Grand cadre
cadreGrand = Frame(fenetre, borderwidth=2, relief=RAISED)
cadreGrand.pack(side=TOP, padx=20, pady=40)

# Cadre 2
cadre2 = Frame(cadreGrand, borderwidth=2, relief=SUNKEN)
cadre2.pack(side=LEFT, padx=20, pady=10)

# Cadre 3
cadre3 = Frame(cadreGrand, borderwidth=2, relief=GROOVE)
cadre3.pack(side=BOTTOM, padx=10, pady=10)

Bouton=Button(cadre2, text="Le bouton 1 ici").pack(padx=10, pady=10)
Bouton=Button(cadre2, text="Le bouton 2 ici").pack(padx=10, pady=10)
Bouton=Button(cadre3, text="Le bouton 3 ici").pack(padx=10, pady=10)
fenetre.mainloop()

