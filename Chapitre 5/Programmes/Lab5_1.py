"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab5_1.py


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


#import matplotlib.pyplot as affiche

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
#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

tableau_1dimension = num.array([1,2,3])
print("Tableau ou liste... Quelle est la différence...",tableau_1dimension)

tableau = num.array([[1,2,3],
                     [4,5,6]])      # Meilleure visibilité.
print("Tableau ou matrice... Quelle est la différence...\n",tableau)

#-----------------------------------------------  Exemple 2  -----------------------------------------------------------

tableau_1dimension2 = num.array([1,2,3,4,5,6],ndmin=2)
print("Tableau ou liste... Quelle est la différence...",tableau_1dimension2)


tableau_1dimension3 = num.array([1,2+5j,3,4,5-3j,6],dtype=complex)
print("Les éléments du tableau deviennent des complexes",tableau_1dimension3)

#-----------------------------------------------  Exemple 3  -----------------------------------------------------------
# Types de donnée

# bool_
# Booléen (True ou False) stocké en tant que byte
#
# int_
# Type d'entier par défaut (identique à C long, normalement int64 ou int32)
#
# intc
# Identique à C int (normalement int32 ou int64)
#
# intp
# Entier utilisé pour l'indexation (identique à C ssize_t; normalement int32 ou int64)
#
# int8
# Octet (-128 à 127)
#
#
# int16
# Entier (-32768 à 32767)
#
# int32
# Entier (-2147483648 à 2147483647)
#
# int64
# Entier (-9223372036854775808 à 9223372036854775807)
#
# uint8
# Entier non signé (0 à 255)
#
# uint16
# Entier non signé (0 à 65535)
#
# uint32
# Entier non signé (0 à 4294967295)
#
# uint64
# Entier non signé (0 à 18446744073709551615)
#
# flotte_
# Sténographie pour float64
#
# float16
# Flotteur demi-précision : bit de signe, exposant 5 bits, mantisse 10 bits
#
# float32
# Flotteur simple précision : bit de signe, exposant 8 bits, mantisse 23 bits
#
# float64
# Flotteur double précision : bit de signe, exposant 11 bits, mantisse 52 bits
#
# complexe_
# Sténographie pour complexe128
#
# complex64
# Nombre complexe, représenté par deux flottants 32 bits (composants réels et imaginaires)
#
# complexe128
# Nombre complexe, représenté par deux flottants 64 bits (composants réels et imaginaires)

#int8, int16, int32, int64 equivalent string à 'i1', 'i2','i4'


tableau_1dimension4 = num.dtype('i1')
tableau_1dimension5 = num.dtype('i4')
print ("tableau_1dimension4 est de type:",tableau_1dimension4)
print ("tableau_1dimension5 est de type:",tableau_1dimension5)

#-----------------------------------------------  Exemple 4  -----------------------------------------------------------
# Création d'une structure de données
tableau_1dimension6 = num.dtype([('des_nombres_au_hasard',num.int8)])   # Attention à l'ordre des () et []
print ("tableau_1dimension6 est de type:",tableau_1dimension6)

# Application sur un objet
tableau_1dimension_nombre = num.array([(10,),(100,),(258,)],dtype=tableau_1dimension6)
# Là, est importante dans (10,)... Signifie que c'est un int. Sinon, ça ne fonctionne pas !
print ("tableau_1dimension6 donne des nombres où l'on applique le type int8 :",tableau_1dimension_nombre,"Oups ! int8 sait compter jusqu'à 255 !")
print ("tableau_1dimension6 donne les valeurs des nombres en chaîne de caractères :",tableau_1dimension_nombre['des_nombres_au_hasard'])


#-----------------------------------------------  Exemple 5  -----------------------------------------------------------
# Les fonctions appliquées aux fonctions.
# char est un nom d'une classe.
print ("Application de la fonction titre num.char.title('vive le Python 3')",num.char.title('vive le Python3'))
#OU
print ("Application de la fonction capitalize num.char.capitalize('vive le Python 3')",num.char.capitalize('vive le Python3'))
print ("De même avec upper et lower ('Vive Le Python 3')",num.char.upper('vive le Python3  - '),num.char.lower('vive le Python3'))

print("J'aime les messages codés, ça fait agent secret... Encodage cp500")
tableau_encode = num.char.encode("Denis Reant",'cp500')
print ("Le nom de notre agent est :",tableau_encode)
tableau_decode=num.char.decode(tableau_encode,'cp500')
print ("Bon maintenant, il est drôlement moins secret... Décodage cp500:",tableau_decode)

print ("On remplace des fragments de chaînes. 'Vive le Python 3'",num.char.replace ('Vive le Python 3', '3', '2'))

# http://epydoc.sourceforge.net/stdlib/encodings-module.html

# https://www.tutorialspoint.com/numpy/numpy_data_types.htm