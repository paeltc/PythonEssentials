"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_4.py
					
				
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
#		Zone de déclarations des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# La variable peut être déclarée à la volée dans une structure for.
# On utilise la méthode range().

# for increment in range(5):  # Pour increment allant de 0 à 4
#     print("C'est",increment,"fois mieux d'apprendre Python qu'un autre langage de programmation !")
# print("C'est un peu trop d'affirmer ça !")

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# for increment in range(10, 20, 2):  # Pour increment allant de 10 à 20 avec un pas de 2
#     print("C'est",increment,"fois mieux d'apprendre Python qu'un autre langage de programmation !")
#     print("C'est un peu trop d'affirmer ça !")
#
# #-------------------------------------------- Exemple N°3 --------------------------------------------------------------
#
# On peut afficher des chaînes de caractères
# sans utiliser range().

# for champ in ['Python',"c'est",'génial','comme',"langage\n"]:
#     print(champ)

# #-------------------------------------------- Exemple N°4 --------------------------------------------------------------
#
# # Échanger un caractère dans la chaîne
# message ="Python 3.6 est génial"
# for lettre in message:
#     if lettre in "6":
#         print("X")
#     else:
#         print(lettre)
# print("\n")
#
#
# #-------------------------------------------- Exemple N°5 --------------------------------------------------------------
#
valeur_saisie=input("Indiquez la table de multiplication que vous désirez obtenir !\n")
valeur_table=int(valeur_saisie)               # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez la valeur maximale de multiplieur.\n")
valeur_max_multiplieur=int(valeur_saisie)     # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez la valeur minimale de multiplieur.\n")
valeur_min_multiplieur=int(valeur_saisie)     # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez le pas de calcul de la table.\n")
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