"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_7.py


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

# x+2y=3
# 3x-4y=1
# On peut se faire plaisir sur un système à 3 inconnues : utiliser la méthode du pivot de Gauss.

entrees = num.array([[1 ,2],[3 ,-4]])
sorties =num.array([[3],[1]])

solution = num.linalg.solve(entrees,sorties)
print("La valeur de x =",solution[0 ,0],"et y=",solution[1,0])

#-----------------------------------------------  Exemple 1  -----------------------------------------------------------

num.save ("Resultats",solution) # Création d'un fichier de type .npy par défaut... Pas possible de le lire avec Notepad++.
copie=num.load("Resultats.npy") # Le répertoire de création est le répertoire courant de travail.

print("Voici ce qui est dans le fichier Resulats.npy :",copie)

#-----------------------------------------------  Exemple 2  -----------------------------------------------------------

#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savetxt.html
x  =  y  =  z  =  num.arange ( 0.0 , 5.0 , 1.0 )
num.savetxt("fichier1EX2.txt",x,delimiter=',',newline=' ',fmt="%1.2f") # newline ne sert à rien... Un seul vecteur
num.savetxt("fichier2EX2.txt",(x,y,z),newline='\n') # Newline implicite, forme exponentielle implicite
num.savetxt("fichier3EX2.txt",x,fmt='%1.4e',) # Forme exponentielle

#-----------------------------------------------  Exemple 3  -----------------------------------------------------------
noms  = num.array(['Denis', 'REANT', 'Formateur'])
matricules = num.array([ 0.0701 ,  15.5895 ,  0.11723 ])

donnees = num.zeros(noms.size, dtype=[('variable1',"U7"), ('variable2', float)]) #U7 = 7 caractères
donnees['variable1'] = noms
donnees['variable2'] = matricules

num.savetxt('fichier1Ex3.txt', donnees, fmt="%10s %2.3f",newline='',header="Liste et matricule du formateur:",
            footer="C'est le footer !",comments="Ceci est le commentaire !")
# 10 caractères pour afficher le nom et les espaces blancs pour compléter.

