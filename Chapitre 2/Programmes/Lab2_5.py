"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_5.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

import random

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------

increment_while=0

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# for increment in range(11):
#      if increment==3:            # On arrête la boucle lorsque increment vaut 3... Ne pas confondre increment==3 et increment=3.
#          break
#      print (increment)

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# for increment in range(11):
#     if increment is 3:             # On affiche tout sauf le 3.
#          continue
#     print (increment)


# #-------------------------------------------- Exemple N°4 --------------------------------------------------------------
#
# while increment_while<11:
#      if increment_while==5:        # On arrête la boucle while à partir de 5, donc on affiche les 4 premières valeurs.
#          break
#      print(increment_while)
#      increment_while+=1            # On n'oublie pas modifier la variable de conditions.
# print ("On sort de la boucle while")


# #-------------------------------------------- Exemple N°5 --------------------------------------------------------------
#
print("Cherchez le nombre mystère compris entre 1 et 10.")

valeur_max = 9
 # On ajoute +1 pour ne pas avoir 0.
nombre_mystere = int(valeur_max * random.random()) + 1
nombre = 0

print("À titre pédagogique, on affiche le nombre mystère qui est :",nombre_mystere)

while nombre != nombre_mystere:
     nombre = int(input("Nouveau nombre : "))
     print("Entrez un nombre négatif pour abandonner.")
     if nombre>0:
         if nombre > nombre_mystere:
             print("Ce nombre est plus grand que le nombre mystère !")
         elif nombre < nombre_mystere:
             print("Ce nombre est plus petit que le nombre mystère !")
     else:
        print("Vous avez abandonné !")
        break
else:
     print("Bravo, c'est lui !")
