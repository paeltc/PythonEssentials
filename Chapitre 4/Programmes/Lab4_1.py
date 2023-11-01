"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_1.py
					
				
"""

# Indispensable hors contexte de PyCharm->en bas à droite
# -*- coding:Utf-8 -*-

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
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# Voir aussi http://tkinter.fdex.eu/doc/


#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Création d'un container avec les onglets Ouvrir, Fermer et Réduire
# fenetre = Tk()
#
# label = Label(fenetre, text="Vive la programmation sous Python 3")
#
# label.pack()
#
# fenetre.mainloop()

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# fenetre = Tk()
#
# label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()
# TireCadre=LabelFrame(fenetre,text="Le titre du cadre")
# TireCadre.pack(fill="both",expand="yes")
#
# # Widget Bouton
# # Bouton est dans le container... commande associée quit
# bouton=Button(fenetre, text="Fermer cette fenêtre", command=fenetre.quit)
# bouton.pack()
#
#
# fenetre.mainloop()
#----------------------------------------------- Exemple N°3 ----------------------------------------------------------

# fenetre = Tk()
#
# label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()
#
# # Widget label
# # bg = background
# label = Label(fenetre, text="Un autre label", bg="red")
# label.pack()
#
# # Widget label
# label = Label(fenetre, text="Le bouton ci-dessous permet de fermer la fenêtre.", background="yellow")
# label.pack()
#
# # Widget label couleur avec le code hexadécimal
# # Trouvez votre couleur sur http://www.code-couleur.com/
# label = Label(fenetre, text="Le bouton ci-dessous permet de fermer la fenêtre.", background= '#40E0D0')
# label.pack()
#
# # Widget Bouton
# # Bouton est dans le container... commande associée quit... on modifie la couleur de l'écriture
# bouton=Button(fenetre, text="Fermer cette fenêtre",fg="white",bg='#001FFF', command=fenetre.quit)
# bouton.pack()
#
#
# fenetre.mainloop()

#----------------------------------------------- Exemple N°4 ------------------------------------------


# fenetre = Tk()
# fenetre.title("Titre de la fenêtre")
# fenetre.geometry("500x500")
# fenetre.iconbitmap("book.ico") # L'emplacement est au même endroit que le fichier source.
#
# label = Label(fenetre, text="Vive la programmation sous Python 3")
# label.pack()
#
# # Widget Bouton
# # Bouton est dans le container... commande associée quit
# bouton1 = Button(fenetre, text ="style de type FLAT",fg="red", relief=FLAT, command=fenetre.quit).pack()
# bouton2 = Button(fenetre, text ="style de type RAISED",fg="orange", relief=RAISED, command=fenetre.quit).pack()
# bouton3 = Button(fenetre, text ="style de type SUNKEN", bg="green",relief=SUNKEN, command=fenetre.quit).pack()
# bouton4 = Button(fenetre, text ="style de type GROOVE", relief=GROOVE, command=fenetre.quit).pack()
# bouton5 = Button(fenetre, text ="style de type RIDGE", relief=RIDGE, command=fenetre.quit).pack()
#
# fenetre.mainloop()

#----------------------------------------------- Exemple N°5 -----------------------------------------

fenetre = Tk()
fenetre.title("Vive la programmation sous Python 3 !")
fenetre.geometry("700x1000")
fenetre.iconbitmap("book.ico") # L'emplacement est au même endroit que le fichier source.

label = Label(fenetre, text="On va mettre de tout dans cette fenêtre!")
label.pack()

# Case à cocher
caseACocher1 = Checkbutton(fenetre, text="case N°1").pack()
caseACocher2 = Checkbutton(fenetre, text="case N°2").pack()
caseACocher3 = Checkbutton(fenetre, text="case N°3")  # Si on n'appelle pas la méthode pack
caseACocher3.pack() #Il faut le faire ici.

# entrée

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Ligne 1") # La méthode .pack() n'est prise en charge.
liste.insert(2, "Ligne 2") # L'index ne correspond pas à la position dans la liste.
liste.insert(3, "Ligne 3")
liste.insert(5, "Ligne 4")
liste.insert(4, "Ligne 5")
liste.pack()

label2 = Label(fenetre,text=liste.size(),fg="red")
label2.pack()

valeur = DoubleVar()
# Par défaut, l'échelle est de 0 à 100.
scale1 = Scale(fenetre, variable=valeur,orient='horizontal', from_=0, to=50,
      resolution=1, tickinterval=5, length=350,
      label='Scale horizontal de 0 à 50')
scale1.pack()

scale2 = Scale(fenetre, variable=valeur,orient='vertical', from_=200, to=-200,
      resolution=5, tickinterval=50, length=400,
      label='Scale horizontal de 200 à -200')
scale2.pack()

# La variable 'valeur' est commune aux 2 échelles... Il y aura donc influence.
# https://www.tutorialspoint.com/python/tk_spinbox.htm
# SpinBox
spinbox1 = Spinbox(fenetre, from_=-50, to=50, textvariable=valeur)
spinbox1.pack()

label3 = Label(fenetre,text=valeur,fg="red")
label3.pack()
print(valeur)
fenetre.mainloop()







