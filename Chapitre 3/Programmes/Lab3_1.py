"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_1.py
					
				
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


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------
import math
import random
import builtins

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Pour toutes informations complémentaires, allez consulter https://docs.python.org/3/library/index.html
# help(element)
# Cette fonction vous retourne des informations sur l'utilisation de l'élément qui vous intéresse.

#print(help(float))         # Vous avez toutes les informations concernant les méthodes appplicables à la classe
#print(help(int))           # dont l'objet hérite.

# print(help(builtins))

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
print("Quelques exemples de méthodes natives !")

print("La valeur absolue de -1 est :",abs(-1))
print("Une valeur aléatoire:",random.random())
print("Une valeur aléatoire d'une liste random.choice([1,2,3,4,5]):",random.choice([1,2,3,4,5]),"2ème valeur",
      random.choice([1, 2, 3, 4, 5]))

chaine_0="Bonjour à tous !"
print("Compter le nombre de lettres identique d'une chaîne, il y a",chaine_0.count("o"),"o dans cette chaîne")
# Attention, toutes les méthodes de bibliothèques builtins ne sont plus forcément d'actualité.
# print("La méthode add(1,2)",add(1,2))

print ("Valeurs arrondies round(1.2), round(1.9), round(-1.5)",round(1.2), round(1.9),round(-1.5),round(-1.7))

print("Effectuer un tri dans l'ordre croissant d'une liste(12,9,-5,50,1,3.14):",sorted((12,9,-5,50,1,3.14)))

#----------------------------------------------- Exemple N°3 ----------------------------------------------------------
# Travail sur les caractères d'une chaîne

chaine_1="Python3"
chaine_2="JustePython"
chaine_3="Juste Python"

print ("Méthodes pour trouver le nombre d'éléments de la chaîne, ex: y est",chaine_1.find("y"),"fois dans chaîne_1")
print ("Méthodes pour trouver s'il existe un nombre dans la chaîne. Mais la valeur n'est pas donnée.",chaine_1.isalnum())
print ("Méthodes pour trouver s'il n'existe que des caractères dans la chaîne. Mais la valeur n'est pas donnée.",chaine_1.isalpha())
print ("Même chose mais appliqué sur chaîne_2 et chaîne_3, retourne",chaine_2.isalpha(),"-",chaine_3.isalpha())
print("Vérifier qu'une chaîne de caractères se termine par une portion de caractères Python3, le 3",chaine_1.endswith("3"),
      "ou encore on3",chaine_1.endswith("on3"),"mais pas ON3",chaine_1.endswith("ON3"))


ma_variable1 = 2
ma_variable2 = math.pi
chaine_4="4"                # isalnum() va permettre d'extraire la valeur du caractére.
print("Méthode pour savoir si une variable ou une chaîne comporte des entiers, ma_variable1=2 :",ma_variable2.is_integer(),
      "ma_variable2=pi :",ma_variable2.is_integer(),"chaine_4='4':",chaine_4.isalnum())
print("Ajouter une chaîne à une autre chaîne :",chaine_3.__add__('3'),"ou",chaine_3,chaine_3.join('3'))

# En faisant un tuple, on vérifie si la chaîne est en majuscules ou minuscules.
chaine_5,chaine_6='camille','RÉANT'
print("camille en minuscules et RÉANT en majuscules :",chaine_5.islower(),"et",chaine_6.isupper())
print("camille en majuscules et RÉANT en minuscules :",chaine_5.upper(),"et",chaine_6.lower())
print("Remplace des lettres d'une chaîne",chaine_5.replace('c','C'),"et",chaine_1.replace('3',''))

chaine_7="Apprendre le langage Python au format e-learning, c'est plutôt sympathique !"
print ("Utiliser un séparateur, une chaîne devient alors une liste :",chaine_7.split(' '))

print("Mettre au format titre, c'est-à-dire, mettre une majuscule à chaque mot",chaine_7.title())