"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_6.py


"""
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

import numpy as num
import math
import numpy.matlib
from fractions import *
from numpy import *


#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-----------------------------------------------  Exemple 3  -----------------------------------------------------------
# 3x-2y=-1
# x+y=8

# e1[0]+e1[1]=-1    e1[0]=3  e1[1]=-2
# e2[0]+e2[1]=-8    e2[0]=1  e2[1]=-1

def resoudre(e1,e2):
    determinant=e1[0]*e2[1]-e1[1]*e2[0]
    print ("Valeur du déterminant :",determinant)
    if determinant==0:
        print('Pas de solution unique')
    else:
        x=Fraction(e1[2]*e2[1]-e1[1]*e2[2],determinant)
        y=Fraction(e1[0]*e2[2]-e1[2]*e2[0],determinant)
        print('La solution est x=',x,'et y=',y)
        print("Vérification de l'équation 1:",e1[0],"*",x,"+",e1[1],"*",y,"=" ,e1[0] * x + e1[1] * y)
        print("Vérification de l'équation 2:",e2[0],"*",x,"+",e2[1],"*",y,"=",e2[0] * x + e2[1] * y)

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

#-----------------------------------------------  Exemple 1  -----------------------------------------------------------
# #numpy.matlib.empty(shape, dtype, order)
# print ("\nCeci est une matrice 2*2 remplie de façon aléatoire :\n",num.matlib.empty((2,2),dtype=int))
# print ("\nCeci est une matrice 3*3 remplie de façon aléatoire sans type :\n",num.matlib.rand(3,3))
# print ("\nCeci est une matrice 3*3 remplie de façon voulu :\n",num.matrix('1,2,3;4,5,6;7,8,9'))
# print ("\nCeci est une matrice 3*3 nulle :\n",num.matlib.zeros((3,3)))
# print ("\nCeci est une matrice 3*3 unitaire :\n",num.matlib.ones((3,3)))
# print ("\nCeci est une matrice 3*3 identité... Ou presque :\n",num.matlib.eye(3, 3, 1, int))
# print ("\nCeci est une matrice 4*4 identité :\n",num.matlib.identity(4,int))



#-----------------------------------------------  Exemple 2  -----------------------------------------------------------
# 3x-2y=-1
# x+y=8

# A=num.matrix([[3,-2],[1,1]])
# B=num.matrix([[-1],[8]])
# solution=linalg.solve(A,B)   # from numpy import *
# print("La solution du système d'équation à 2 inconnues est :\n[x]\n[y]\n",solution)


#-----------------------------------------------  Exemple 3  -----------------------------------------------------------

# Le module fractions permet d'avoir la valeur exacte de la solution chaque fois que les coefficients
# du système sont entiers :

# 3x-2y=-1
# x+y=8

equation1=[3,-2,-1]
equation2=[1,1,8]
print("Calcul du déterminant par la méthode num.linag.det =",num.linalg.det([[3, -2], [1, 1]]))
resoudre(equation1,equation2)


