"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_3.py
					
				
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

# global increment=1 s'il existe des fonctions
# increment=1 sinon global à tout ce fichier

nombre_mystere = 8
nombre_de_fois=1

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# print("Je vous demande de vous taire !")
#
# # On ne peut pas déclarer la variable à la volée dans une structure de contrôle de type while.
# while nombre_de_fois<=5:
#      print("Cela fait",nombre_de_fois,"que je vous le demande !")
#      nombre_de_fois=nombre_de_fois+1            # Il faut absolument modifier la variable de condition pour ne pas boucler à l'infini.
# # Le nombre d'itérations commence à 0.
# print("0 fois, cela ne veut rien dire !\n")
#
#
# # On initialise la variable de façon à commencer à 1.
#
#
# while nombre_de_fois<=5:
#      print("Cela fait",nombre_de_fois,"que je vous le demande !")
#      nombre_de_fois=nombre_de_fois+1            # Il faut absolument modifier la variable de condition pour ne pas boucler à l'infini.
# print("\n")
#

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# valeur_saisie=input("Entrez une valeur comprise entre 0 et 10, pour trouver le chiffre mystère dans le programme :")
# valeur=int(valeur_saisie)
#
# while valeur is not nombre_mystere:
#      valeur_saisie=input("Ce n'est pas le nombre mystère ! Réessayez !")
#      valeur=int(valeur_saisie)               # On écrase les valeurs des variables "valeur" et "valeur_saisie".
# print ("Bravo ! Vous avez trouvé le nombre mystère qui est",nombre_mystere)



# #-------------------------------------------- Exemple N°3 --------------------------------------------------------------


valeur_saisie=input("Indiquez la table de multiplication que vous désirez obtenir !\n")
valeur_table=int(valeur_saisie)               # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez la valeur maximale de multiplieur\n")
valeur_max_multiplieur=int(valeur_saisie)     # On écrase la variable "valeur_saisie".
valeur_saisie=input("Indiquez le pas du calcul de la table\n")
valeur_pas=int(valeur_saisie)                 # On écrase la variable "valeur_saisie".

# On déclare à la volée ou dans le global pour être vu par l'ensemble du fichier.
increment=1  # global increment=1
print("Voici la table de",valeur_table,"\n")

# valeur_max_multiplieur+1 car on sort de la boucle lorsque increment==valeur_max_multiplieur.
# Si on rentre 10 pour valeur_max_multiplieur lorsque increment=10 on n'exécute pas la boucle... On sort.

while increment is not valeur_max_multiplieur+1:
    print(increment,"*",valeur_table,"=",increment*valeur_table,";")
    increment=increment+valeur_pas

print("\nC'est la fin !")
