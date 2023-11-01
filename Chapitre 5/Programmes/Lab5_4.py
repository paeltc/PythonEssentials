"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_4.py


"""
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

import numpy as num
import math
#import matplotlib.pyplot as affiche

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------



#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

vecteur_nombre_complexe = num.array([ 2 + 3j, 1j, 1])
print("Notre vecteur1 est constitué de 3 nombres complexes :",vecteur_nombre_complexe)
print ("Les valeurs réelles des nombres précédents sont :",num.real(vecteur_nombre_complexe),"\n")

vecteur_nombre_complexe = num.array([ 2.,  0.,  1.])
print("Notre vecteur2 est constitué de 3 nombres complexes :",vecteur_nombre_complexe)
print ("Les valeurs imaginaires des nombres précédents sont :",num.imag(vecteur_nombre_complexe),"\n")

vecteur_nombre_complexe = num.array([ 3.60555128, 3+3j, 4+3j])
print("Notre vecteur3 est constitué de 3 nombres complexes :",vecteur_nombre_complexe)
print ("Les valeurs des modules des nombres précédents sont :",num.abs(vecteur_nombre_complexe),"\n")

vecteur_nombre_complexe = num.array([ 2 + 3j, 1j, 1])
print("Notre vecteur4 est constitué de 3 nombres complexes :",vecteur_nombre_complexe)
print ("Les valeurs des arguments en degrés des nombres précédents sont :",num.angle(vecteur_nombre_complexe)*360/math.pi,"\n")

vecteur_nombre_complexe = num.array([ 2.-3.j,  0.-1.j,  1.-0.j])
print("Notre vecteur5 est constitué de 3 nombres complexes :",vecteur_nombre_complexe)
print ("Les conjugués des nombres précédents sont :",num.conj(vecteur_nombre_complexe),"\n")



