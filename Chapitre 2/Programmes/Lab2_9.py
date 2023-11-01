"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_9.py
					
				
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


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

# Fonctions anonymes en Python (ou lambda)

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Fonction avec 1 paramètre->avec valeur retournée non « formatée » (brut)
volumeCube=lambda cote:cote**3

# -------------------------------------------- Exemple N°2 -------------------------------------------------------------
# Puisqu'il y a surcharge, c'est cette dernière fonction qui sera exécutée.
# Le valeur retournée est « formatée ».
volumeCube=lambda cote:print("Le volume du cube est de %.2f : "%cote**3,"m3.")

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

# Une fonction qui comporte des fonctions lambda ne fonctionne pas !
# C'est logique car chacune des fonctions a ses propres variables.
# On ne peut les écrire que sur une ligne.
# On ne peut pas avoir plus d’une instruction dans la fonction.

def volumesFigures():
    volumeCube = lambda cote: print("Le volume du cube est de :",cote ** 3,"m3.")
    volumeSphere = lambda rayon: print("Le volume de la sphère est de :",4/3*math.pi*rayon**3,"m3.")



#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Appel du module ici

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
print("Exemple 1")
volumeCube(2.2)
print("Fin exemple N°1\n")


#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
print("Exemple 2 - Ça ne fonctionne pas !")
volumesFigures(3)
print("Fin exemple N°2\n")

#-----------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-----------------------------------------------------------

# On peut écrire les modules ici aussi.
