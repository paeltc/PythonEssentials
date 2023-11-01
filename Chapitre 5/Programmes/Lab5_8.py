"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_8.py


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
from numpy import *
from sympy import *


#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------



# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

#http://docs.sympy.org/latest/tutorial/

x = symbols('x')
y = symbols('y')
z = symbols('z')

print("Simplification de (sin(x)**2 + cos(x)**2)=",simplify(sin(x)**2 + cos(x)**2))
print("Simplification de (x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)=",simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

print ("Développement de (x + 1)**2 =",expand((x + 1)**2))
print ("Développement de (x + 2)*(x - 3) =",expand((x + 2)*(x - 3)))
print ("Développement de sin (x + y) =",expand_trig (sin (x + y)))

print("Mise en facteur de (x**2*z + 4*x*y*z + 4*y**2*z) =",factor(x**2*z + 4*x*y*z + 4*y**2*z))
print("Mise en facteur de (cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2) =",factor(cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2))


print ("Écrire la dérivée de cos(x)=",diff(cos(x), x))
print ("Écrire la dérivée 3ème de (x**4, x, 3)=",diff(x**4, x, 3))

print("Calculer l'intégrale de 1/x=",integrate (1/x,x))
print("Calculer l'intégrale de exp(-x) par rapport à x entre 0 et +l'infini=",integrate(exp(-x), (x, 0, oo)))

print("Donner la limite de sin(x)/x quand x tend vers 0=",limit( sin ( x ) / x ,  x ,  0 ))
print("Donner la limite de 1/x quand x tend vers 0+ (condition limite)=",limit(1/x, x, 0, '+'))

