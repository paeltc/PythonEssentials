"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab9.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

import os # On importe le module os qui dispose de variables
          # et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation.

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


valeur_saisie=input("Indiquez la table de multiplication que vous désirez obtenir !\n")
valeur_table=int(valeur_saisie)               # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez la valeur maximale de multiplieur\n")
valeur_max_multiplieur=int(valeur_saisie)     # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez la valeur minimale de multiplieur\n")
valeur_min_multiplieur=int(valeur_saisie)     # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez le pas de calcul de la table\n")
valeur_pas=int(valeur_saisie)                 # On écrase la variable "valeur_saisie".

print("Voici la table de",valeur_table,"\n")

# Gros avantage par rapport au while, vous contrôlez le pas dans l'initiation de la boucle.
# On ajoute +1 à valeur_max_multiplieur car la valeur 0 compte.

for valeur_pas in range (valeur_min_multiplieur,valeur_max_multiplieur+1):
    print(valeur_pas,"*",valeur_table,"=",valeur_pas*valeur_table,";")


print("\nC'est la fin !")

# En utilisant le paramètre du pas de calcul... On retrouve le même résultat.
for une_variable in range (valeur_min_multiplieur,valeur_max_multiplieur+1,valeur_pas):
     print(une_variable,"*",valeur_table,"=",une_variable*valeur_table,";")

print("\nC'est la fin !")
# On met le programme en pause pour éviter qu'il ne se referme (Windows).
os.system("pause")