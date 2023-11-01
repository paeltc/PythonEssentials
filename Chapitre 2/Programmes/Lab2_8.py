"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_8.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'importw' de modules
#-----------------------------------------------

import math     # Nécessaire pour pi

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Fonction avec 1 paramètre->avec valeur retournée non « formatée » (brut)
def volumeCube(valeur_cote):
    return valeur_cote**3

# -------------------------------------------- Exemple N°2 -------------------------------------------------------------
# Puisqu'il y a surcharge, c'est cette dernière fonction qui sera exécutée.
# Le valeur retournée est « formatée ».
def volumeCube(valeur_cote):
    return print("Le volume du cube est de :",valeur_cote**3,"m3.")

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

# Fonction avec 3 paramètres->longueur,largeur,hauteur
# Ce qui fonctionne... Un seul return
def volumeParallelepipede(longueur,largeur,hauteur):
    return print("Le volume du parallélépipède est de : %.2f"%(longueur*largeur*hauteur),"m3.")


#-------------------------------------------- Exemple N°4 --------------------------------------------------------------

# Fonction avec 3 paramètres->longueur,largeur,hauteur
# Ce qui ne fonctionne pas... Plusieurs return
# Seule la première variable n'est pas grisée... Donc la seule valide !

def volumeFigure(longueur,largeur,hauteur,rayon):
    return print("Le volume du cube est de : %.2f"%(longueur**3),"m3.")
    return print("Le volume du parallélépipède est de : %.2f"%(longueur*largeur*hauteur),"m3.")    # Ne sera pas traité
    return print("Le volume de la sphère est de : %.2f"%(4/3*math.pi*rayon**3),"m3.")              # Ne sera pas traité

#-------------------------------------------- Exemple N°5 --------------------------------------------------------------

def volumesFigures():

    valeur_saisie=input("Entrez la longueur du parallélépipède :")
    ma_longueur=float(valeur_saisie)

    valeur_saisie=input("Entrez la largeur du parallélépipède :")
    ma_largeur=float(valeur_saisie)

    valeur_saisie=input("Entrez la hauteur du parallélépipède :")
    ma_hauteur=float(valeur_saisie)

    valeur_saisie=input("Entrez le rayon de la sphère :")
    mon_rayon=float(valeur_saisie)

    return print("Le volume du cube est de : %.2f"%(ma_longueur**3),"m3, Le volume du parallélépipède est de : %.2f"%(ma_longueur*ma_largeur*ma_hauteur),
             "m3 le volume de la sphère est de : %.2f" % (4 / 3 * math.pi * mon_rayon ** 3),"m3.")

#-------------------------------------------- Exemple N°6 --------------------------------------------------------------
# Portée globale d'une variable
rayon = 10
def valeurRayon():
    global rayon
    rayon=20
    print("La valeur du rayon dans la fonction est :",rayon)

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Appel du module ici

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# print("Exemple 1")
# volumeCube(2.3)
# print("Fin exemple N°1\n")

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------
# print("Exemple 3 - Les paramètres sont directement mis")
# volumeParallelepipede(3.1,2,4.3)
# print("Fin exemple N°3\n")
#
# #-------------------------------------------- Exemple N°4 --------------------------------------------------------------
# print("Exemple 4 - Python est une passoire !")
# volumeFigure(3.1,4,3.2,6)
# print("Fin exemple N°4... Le pire est qu'il n'y a pas d'erreur pour l'interpréteur.\n")
#
#
# #-------------------------------------------- Exemple N°5 --------------------------------------------------------------
# print("Exemple 5 - Les paramètres sont inclus dans la fonction !")
# volumesFigures()
# print("Fin exemple N°5\n")
# #
# #-------------------------------------------- Exemple N°6 -------------------------------------------------------
#
print("Valeur du rayon en dehors de la fonction avant son appel :",rayon)
valeurRayon()
# La variable rayon a gardé la valeur attribuée dans la fonction valeurRayon().
print("Valeur du rayon en dehors de la fonction :",rayon)

#-----------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-----------------------------------------------------------

# On peut écrire les modules ici aussi.
