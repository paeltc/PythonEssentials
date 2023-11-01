"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_7.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

import math     # Nécessaire pour pi

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------

ma_hauteur = 5
ma_longueur = 3
ma_largeur = 2
mon_rayon = 4

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Fonction avec 1 paramètre->nombre_de_repetitions->locale à la fonction
def compteur(nombre_de_repetitions):
    increment = 0                   # Variable locale à la fonction, la portée de cette variable ne concerne que compteur3().
    while increment < nombre_de_repetitions:
        print("Compte",nombre_de_repetitions,"fois")
        increment = increment + 1

# -------------------------------------------- Exemple N°2 --------------------------------------------------------------

# Fonction avec 4 paramètres->longueur,largeur,hauteur,rayon->locales à la fonction
def volume(longueur, largeur, hauteur, rayon):
    print("Le volume du cube est de : %.2f"%(longueur**3),"m3.")
    print("Le volume du parallélépipède est de : %.2f"%(longueur*largeur*hauteur),"m3.")
    print("Le volume de la sphère est de : %.2f"%(4/3*math.pi*rayon**3),"m3.")


#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Appel du module ici

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# print("Exemple 1")
# compteur(5)
# print("Fin exemple N°1\n")
#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
# print("Exemple 2 - Les paramètres sont directement mis")
# volume(3,2,4,5)
# print("Fin exemple N°2\n")
# #-------------------------------------------- Exemple N°3 --------------------------------------------------------------
# print("Exemple 3 - Les paramètres sont des variables déclarées de façon globale")
# volume(ma_longueur,ma_largeur,ma_hauteur,mon_rayon)
# print("Fin exemple N°3\n")
#
# print("On affiche les variables dont la portée est globale longueur(m) =",ma_longueur,"ma_largeur(m) =",ma_largeur,
#       "ma_hauteur(m)=",ma_hauteur,"mon_rayon(m)=",mon_rayon)
#
# #-------------------------------------------- Exemple N°4 --------------------------------------------------------------
#
# On écrase les valeurs précédentes des paramètres des volumes.
valeur_saisie=input("Entrez la longueur du parallélépipède :")
# On 'cast' avec une valeur qui peut être un nombre à virgule.
ma_longueur=float(valeur_saisie)

valeur_saisie=input("Entrez la largeur du parallélépipède :")
ma_largeur=float(valeur_saisie)

valeur_saisie=input("Entrez la hauteur du parallélépipède :")
ma_hauteur=float(valeur_saisie)

valeur_saisie=input("Entrez le rayon de la sphère :")
mon_rayon=float(valeur_saisie)

print("\nExemple 4 - Les paramètres sont des variables déclarées de façon globale")
volume(ma_longueur,ma_largeur,ma_hauteur,mon_rayon)
print("\nFin exemple N°4\n")



#-----------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-----------------------------------------------------------

# On peut écrire les modules ici aussi.
