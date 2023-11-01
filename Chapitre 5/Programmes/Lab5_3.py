"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_3.py


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

def lignes_trigonométriques():

    print ("On ne gère pas d'exception alors faites attention de rentrer un entier !")
    valeur_saisie=input("Entrez la valeur de l'angle de départ :")        # angle entré en radians
    debut=int(valeur_saisie)
    valeur_saisie = input("Entrez la valeur finale de l'angle :")
    fin = int(valeur_saisie)
    valeur_saisie = input("Entrez la valeur du pas de l'angle :")
    pas = int(valeur_saisie)

    for increment in range (debut,fin,pas) :         # Attention in range() ne gère que des int !
        print("Valeur de cosinus si teta=",increment,"est en degrés la valeur du cosinus est :",
            round (math.cos(math.radians(increment)),2))
        print("Valeur de sinus si teta=",increment,"est en degrés la valeur du sinus est :",
            round(math.sin(math.radians(increment)), 2))
        print("Valeur de tangente si teta=",increment,"est en degrés la valeur de tangente est :",
            round(math.tan(math.radians(increment)), 2),"\n")

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

#-----------------------------------------------  Exemple 1  -----------------------------------------------------------

# print("------------------- Conversion radians en degrés ----------------------")
# print("Convertir des radians en degrés : 0 radian =",math.degrees(0),"degrés !")
# print("Convertir des radians en degrés : pi/2 radian =",math.degrees(math.pi/2),"degrés !")
# print("Convertir des radians en degrés : 3*pi/4 radian =",math.degrees(3*math.pi/2),"degrés !")
# print("Convertir des radians en degrés : 5*pi/12 radian =",math.degrees(5*math.pi/12),"degrés !")

#-----------------------------------------------  Exemple 2  -----------------------------------------------------------


# print("\n------------------- Conversion degrés en radians ----------------------")
# print("Convertir des degrés en radians : 0 degrés =%.2f"%math.radians(0),"radians !")
# print("Convertir des degrés en radians : 90 degrés =%.2f"%math.radians(90),"radians !")
# print("Convertir des degrés en radians : 120 degrés =%.2f"%math.radians(120),"radians !")
# print("Convertir des degrés en radians : 270 degrés =%.2f"%math.radians(270),"radians !")

#-----------------------------------------------  Exemple 3  -----------------------------------------------------------

#Ce qui ne fonctionne pas !
# variable_1 = math.cos(1) # 1 radian
# variable_2 = variable_1 * 180 / math.pi     # On croit convertir l'angle en degrés, en fait, on convertit le cos(teta) en degrés.
# print (variable_2,"C'est faux !)")           # Il s'agit d'un non-sens.
#
#
# print ("Cosinus d'un angle de 1 radian",math.cos(math.degrees(1)),"C'est vrai\n")

#-----------------------------------------------  Exemple 4  -----------------------------------------------------------

lignes_trigonométriques()