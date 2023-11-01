"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_2.py


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



# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

#-----------------------------------------------  Exemple 1  -----------------------------------------------------------
#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

# Pas besoin de faire de boucle sur une liste... On applique directement la fonction mathématique.
# tableau_angles = num.array([0,30,45,60,90])
# print("Contenu des angles en degrés du tableau :",tableau_angles)
# print ("Sinus des différents angles du vecteur :",num.sin(tableau_angles*num.pi/180),"\n")
# print ("Cosinus des différents angles du vecteur :",num.cos(tableau_angles*num.pi/180),"\n")
# print ("Tangente des différents angles du vecteur :",num.tan(tableau_angles*num.pi/180),"\n")
#
# tableau_sinus=num.sin(tableau_angles*num.pi/180)
# print ("Arcsinus des différents angles du vecteur en radians :",num.arcsin(tableau_sinus),"\n")
# tableau_arcsinus=num.arcsin(tableau_sinus)
# print ("Valeurs des différents angles en degrés :",num.degrees(tableau_arcsinus),"\n")

#-----------------------------------------------  Exemple 2  -----------------------------------------------------------

# tableau_valeurs = num.array([1.0,5.55, 123, 0.567, 25.532])
#
# print ("Valeurs initiales du tableau :",tableau_valeurs,"\n")
# print ("Valeurs du tableau après les arrondis :",num.around(tableau_valeurs, decimals = 1),"ou",num.around(tableau_valeurs, decimals = -1))
#
#
# # Cette fonction renvoie l'entier le plus grand qui n'est pas supérieur au paramètre d'entrée.
# # 'floor' renvoie le scalaire x qui est le plus grand entier i,
# # tel que i <= x . Notez qu'en Python, le "floor" est toujours arrondi à 0.
# tableau_valeurs = num.array([-1.7, 1.5, -0.2, 0.6, 10])
#
# print ("Valeurs initiales du tableau :",tableau_valeurs,"\n")
# print ("Valeurs du tableau après les arrondis :",num.floor(tableau_valeurs))
# # 'ceil' renvoie le scalaire x qui est le plus petit entier i ,
# # tel que i >= x .
# print ("Valeurs du tableau après les arrondis :",num.ceil(tableau_valeurs))

#-----------------------------------------------  Exemple 3  -----------------------------------------------------------

# Tableau à 2 dimensions de 9 éléments de type float 3 colonnes, 3 lignes
tableau_valeurs_1 = num.arange(9, dtype = num.float_).reshape(3,3)
print ("Valeurs du tableau à 2 dimensions :\n",tableau_valeurs_1,"\n")

tableau_valeurs_2 = num.array([10,10,10])
print ("Valeurs du tableau à 1 dimension :\n",tableau_valeurs_2,"\n")

print ("Addition des 2 tableaux :\n",num.add(tableau_valeurs_1,tableau_valeurs_2),"\n")
print ("Soustraction des 2 tableaux :\n",num.subtract(tableau_valeurs_1,tableau_valeurs_2),"\n")
print ("Multiplication des 2 tableaux :\n",num.multiply(tableau_valeurs_1,tableau_valeurs_2),"\n")
print ("Division des 2 tableaux :\n",num.divide(tableau_valeurs_1,tableau_valeurs_2),"\n")

