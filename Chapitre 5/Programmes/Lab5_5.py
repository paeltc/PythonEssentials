"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_5.py


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
import matplotlib.pyplot as pyplot #Settings -> Project Settings -> Project Interpreter.
from pylab import * # Pour tout importer dans le namespace




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

#-----------------------------------------------  Exemple 1  -----------------------------------------------------------
# marker :[ ‘+’ | ‘*’ | ‘,’ | ‘.’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘<’ | ‘>’ | ‘D’ | ‘H’ | ‘^’ | ‘_’ | ‘d’ | ‘h’ | ‘o’ | ‘p’ |
# ‘s’ | ‘v’ | ‘x’ | ‘|’ | TICKUP | TICKDOWN | TICKLEFT | TICKRIGHT | ‘None’ | ‘ ‘ | ‘’ ].
# x = num.arange(-20,20)
# y = 2 * x**2 + 1
# pyplot.title("Représentation graphique de la fonction y=2x²-1")
# pyplot.xlabel("x axe des abscisses")
# pyplot.ylabel("y axe des ordonnées")
# pyplot.plot(x,y) # marker='o' ,marker='v'
# pyplot.show()

#-----------------------------------------------  Exemple 2  -----------------------------------------------------------
# Couleurs disponibles
# 'b'	Blue
# 'g'	Green
# 'r'	Red
# 'c'	Cyan
# 'm'	Magenta
# 'y'	Yellow
# 'k'	Black
# 'w'	White


# Vecteur partant de 0 à 4pi avec un pas de 0.1 radian
# x = num.arange(0, 4 * num.pi, 0.1)
#
# y_sinus = num.sin(x-num.pi/4)  # Déphasage de -pi/4
# y_cosinus = num.cos(x)
#
# # Hauteur de grille = 2 emplacements
# # Largeur de la grille = 1 emplacement
# # Grille active = emplacement 1 en haut
# pyplot.subplot(2, 1, 1)
#
# pyplot.plot(x, y_sinus,"green")
# pyplot.title('f(x)=sin(x-pi/4)')
#
# # Hauteur de grille = 2 emplacements
# # Largeur de la grille = 1 emplacement
# # Grille active = emplacement 2 en bas
# pyplot.subplot(2, 1, 2)
#
# pyplot.plot(x, y_cosinus,"black")
# pyplot.title('f(x)=cos(x)')
#
# # Affichage
# pyplot.show()

#-----------------------------------------------  Exemple 3  -----------------------------------------------------------

# x=num.linspace(-5,5,100)
# y1=pyplot.plot(x,num.sin(x),marker='o',label="$f(x)=sin(x)$")
# y2=pyplot.plot(x,num.cos(x),marker='v')
# pyplot.title("Fonctions trigonometriques")  # Problèmes avec accents (plot_directive) !
# #pyplot.legend([y1, y2], ["Sinus","Cosinus"])
# pyplot.show()

#-----------------------------------------------  Exemple 4  -----------------------------------------------------------

#Valeurs des couples x et y
# x = [5,8,10]
# y = [12,16,6]
#
# x2 = [6,9,11]
# y2 = [6,15,7]
# pyplot.bar(x, y, align = 'center')
# pyplot.bar(x2, y2, color = 'g', align = 'center')
# pyplot.title('Histogramme')
# pyplot.ylabel('Valeurs des Y')
# pyplot.xlabel('Valeurs des X')
#
# pyplot.show()

#-----------------------------------------------  Exemple 5  -----------------------------------------------------------
# # Loi normale de moyenne mu et d'écart type sigma
# # x= mu+sigma*(valeur alétoire de 0 à 10 000
# # mu = axe de symétrie
# mu, sigma = 100, 15
# x = mu + sigma * num.random.randn(10000)
# #  histogramme des données
# n, bins, patches = pyplot.hist(x, 50, normed=1, facecolor='red', alpha=0.5)
# pyplot.xlabel('Donnees')
# pyplot.ylabel('Probabilite')
# pyplot.title('Histogramme')
# pyplot.text(60, .025, r'$\mu=100,\ \sigma=15$')
# pyplot.axis([40, 160, 0, 0.03])
# pyplot.grid(True)
# pyplot.show()

#-----------------------------------------------  Exemple 6  -----------------------------------------------------------

x=num.linspace(1,1000,50)
pyplot.loglog()
pyplot.plot(x,1./(1+1/30*x))            # Diagramme de Bode d'un filtre passe bas wc=1/30
pyplot.plot(x,1./20*x/(1+1/20*x))       # Diagramme de Bode d'un filtre passe haut wc=1/20
pyplot.grid(True)
pyplot.show()
