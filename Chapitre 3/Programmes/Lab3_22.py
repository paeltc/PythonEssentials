"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_21.py
					-	Lab3_23.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------



#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.
class Tva(object):

	def CalculTva (prix,taux):
		  taux_saisie = input("Entrez le taux de la TVA à appliquer en %")
		  taux = int(taux_saisie)
		  prix_saisie = input("Entrez le prix hors Taxe en euros")
		  prix = int(prix_saisie)
		  return print("La valeur TTC est de :",prix*taux/100+prix,"euros")