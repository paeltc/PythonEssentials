"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_6.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

from turtle import *

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------



#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# INDISPENSABLE D'ALLER VOIR https://docs.python.org/3/library/tkinter.html
# https://docs.python.org/3.2/library/turtle.html


#
#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
Turtle

# reset()
# variable=0
# while variable<12:
#     variable+=1
#     forward(150)
#     left(150)
#
# reset()

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

color('red', 'green')
begin_fill()

for i in range(5):
    forward(200)
    right(144)
end_fill()
done()
