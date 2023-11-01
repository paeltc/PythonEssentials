"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_8.py


"""
# -----------------------------------------------------------------------------
# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/random.html
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

import time
from tkinter import *
import random
import math

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------

LARGEUR = 500 # Largeur de la fenêtre d'évolution de la balle
HAUTEUR = 300 # Hauteur de la fenêtre d'évolution de la balle
RAYON = 20    # Rayon de la balle

# Position initiale au milieu
X = LARGEUR / 2
Y = HAUTEUR / 2
coef_vitesse = 5

# Direction initiale aléatoire
vitesse = random.uniform(1.8, 2)*coef_vitesse
angle = random.uniform(0, 2 * math.pi)
DX = vitesse * math.cos(angle)
DY = vitesse * math.sin(angle)


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

def cycle_1s():
    # On arrive ici toutes les 1000 ms.
    heure.set(time.strftime('Nous sommes le: %A-%d-%B-%Y-%Hh-%Mmin-%Ss'))
    fenetre.after(1000,cycle_1s)


def deplacement():
    """ Déplacement de la balle """
    global X, Y, DX, DY, RAYON, LARGEUR, HAUTEUR

    # rebond à droite
    if X + RAYON + DX > LARGEUR:
        X = 2 * (LARGEUR - RAYON) - X
        DX = -DX

    # rebond à gauche
    if X - RAYON + DX < 0:
        X = 2 * RAYON - X
        DX = -DX

    # rebond en bas
    if Y + RAYON + DY > HAUTEUR:
        Y = 2 * (HAUTEUR - RAYON) - Y
        DY = -DY

    # rebond en haut
    if Y - RAYON + DY < 0:
        Y = 2 * RAYON - Y
        DY = -DY

    X = X + DX
    Y = Y + DY

    # Affichage
    Canevas.coords(Balle, X - RAYON, Y - RAYON, X + RAYON, Y + RAYON)
    fenetre.after(20, deplacement)




# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
#fenetre graphique
# fenetre = Tk()
# fenetre.title("Donne-moi l'heure !")
# fenetre.geometry("700x200")
# fenetre.iconbitmap("book.ico")  # L'emplacement est au même endroit que le fichier source.
# fenetre['bg']=''                # blanc par défaut
#
#
# # Création des widgets label
# Label(fenetre,text="Voici l'heure courante de mon 'Operating System'",font=("Arial",20,"bold")).pack(padx=10,pady=10)
# heure = StringVar()
# Label(fenetre,textvariable=heure,font=("Arial",14,"bold",),bg="grey").pack(padx=10,pady=10)
#
# cycle_1s()
#
# fenetre.mainloop()


#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Animation Balle")

# Création d'un widget canvas
Canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, bg='grey')
Canevas.pack(padx=5, pady=5)

# Création d'un objet graphique
Balle = Canevas.create_oval(X - RAYON, Y - RAYON, X + RAYON, Y + RAYON, width=1, fill='green')

deplacement()

fenetre.mainloop()