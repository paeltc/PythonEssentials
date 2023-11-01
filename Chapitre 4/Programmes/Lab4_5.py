"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_5.py
					
				
"""


################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

# Import de la bibliothèque graphique TK
from tkinter import *
import random
# https://pypi.python.org/pypi/Pillow pour gérer le svg

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------
#from tkinter.messagebox import *
def trouDeLaBalle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    x = random.randint(0, Largeur)
    y = random.randint(0, Hauteur)
    r = 10

    # On dessine un cercle dans la zone graphique.
    trou = Canevas.create_oval(x - r, y - r, x + r, y + r, outline='black', fill='red')
    print("Création du cercle (item", trou, ")")
    # Affichage de tous les items de Canevas
    print(Canevas.find_all())


def retour():
    """ Efface le dernier cercle"""
    if len(Canevas.find_all()) > 1:
        item = Canevas.find_all()[-1]
        # On efface le cercle.
        Canevas.delete(item)

        print("Suppression du cercle (item", item, ")")
        # Affichage de tous les items de Canevas
        print(Canevas.find_all())


def toutEffacer():
    """ Efface tous les cercles"""
    while len(Canevas.find_all()) > 1:
        retour()


# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# Voir aussi http://tkinter.fdex.eu/doc/
# http://tkinter.fdex.eu/doc/caw.html#les-bitmaps

# Cannevas

# Parce qu’un canevas peut être plus large que sa fenêtre de visualisation et qu’il peut être équipé de barres de
# défilement / déplacement, il y a deux systèmes de coordonnées pour chaque canevas :
#
# Les coordonnées d’un point dans la fenêtre de vue; elles sont relatives au bord supérieur gauche de cette fenêtre
# Les coordonnées d’un point dans le canevas lui-même.

fenetre = Tk()
fenetre.title("Tire au pistolet")
fenetre.geometry("400x400")
fenetre.iconbitmap("balle_icone.ico")  # L'emplacement est au même endroit que le fichier source.

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# Lignes - rectangle

# Création de la fenêtre où va se situer le dessin
mon_canvas = Canvas(fenetre, width=400, height=200)
mon_canvas.pack()
# #
# ligne1=mon_canvas.create_line(0, 0, 200, 100, 20, 50)                   # x0,y0,x1,x1,x2,y2 par défaut: noir et plein
# ligne2=mon_canvas.create_line(0, 100, 200, 0, fill="red", dash=(10, 1)) # Couleur rouge - pointillés de 10px pleins, 1 vide
#
# mon_canvas.create_rectangle(50, 25, 150, 75, fill="blue")        # Ajout d'un rectangle plein bleu
# mon_canvas.delete(ligne1)
# mon_canvas.delete(ALL)
# fenetre.mainloop()

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
# Ovales
#cercle=mon_canvas.create_oval(20, 20, 90, 90, width=5, outline="green")
#oval=mon_canvas.create_oval(120, 130, 190, 180, width=10, fill="red")
#mon_canvas.delete(ALL)
#fenetre.mainloop()
#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

# largeur,hauteur=400,200
# mon_canvas = Canvas(fenetre, width=largeur, height=hauteur, bg="yellow")
# mon_canvas.pack()
# epaisseur=10
# points = [(epaisseur,hauteur/2),(largeur/2,hauteur-epaisseur),(largeur-epaisseur,hauteur/2),(largeur/2,epaisseur)]
# mon_canvas.create_polygon(points, dash=(30, 10), fill="magenta", outline="black", width=3)
#
# mon_canvas.delete(ALL)


#------------------------------------------------ JEU ------------------------------------------------------------------

# Image de fond
# La fonction PhotoImage de tkinter ne prend que les formats GIF et PPM / PGM, donc PNG ou JPEG ne sont pas supportés.
# Il faut convertir l'image au bon format(en utilisant par exemple un logiciel tierce).
photo = PhotoImage(file="cible_pistolet.png")

# Création d'un widget Canvas (zone graphique)
Largeur = 350
Hauteur = 350
Canevas = Canvas(fenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(5,5,anchor=NW, image=photo)
print("Image de fond (item",item,")")
Canevas.pack()

# Création d'un widget Button
BoutonGo = Button(fenetre, text ='Tirer', command = trouDeLaBalle)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button
BoutonEffacer = Button(fenetre, text ='Effacer le dernier tir', command = retour)
BoutonEffacer.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button
BoutonEffacerTout = Button(fenetre, text ='Effacer', command = toutEffacer)
BoutonEffacerTout.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(fenetre, text ='Quitter', command = quit)
BoutonQuitter.pack(side = LEFT, padx = 10, pady = 10)

fenetre.mainloop()