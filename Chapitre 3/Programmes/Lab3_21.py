"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_22.py
					-	Lab3_23.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

import math

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.
class geometrie(object):

	def carreCube (cote):
		  cote_saisie=input("Entrez la cote du carré")
		  cote=int(cote_saisie)
		  print("La surface du carré est de :",cote**2,"unités d'aire")
		  print("Le volume du cube équivalent vaut",cote**3,"unités de volume")


	def cercleCylindre (rayon, hauteur):
		  rayon_saisie = input("Entrez le rayon du cercle")
		  rayon = int(rayon_saisie)
		  hauteur_saisie = input("Entrez la hauteur du cylindre")
		  hauteur = int(hauteur_saisie)
		  print("La surface du cercle est",math.pi*rayon**2,"unités d'aire")
		  print("Le volume du cylindre est",math.pi*rayon**2*hauteur,"unités de volume")
		  print("Le volume de la sphère est",4/3*math.pi*rayon**3,"unités de volume")
