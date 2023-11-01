"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_10.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

import math     # Nécessaire pour pi

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

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

ma_liste1 = []
print("Contenu de la ma_liste1 :",ma_liste1,"Elle est vide, ce qui est normal !")
print("Type de list est :",type(ma_liste1))
print(help(ma_liste1))

# -------------------------------------------- Exemple N°2 -------------------------------------------------------------

ma_liste2 = [1,20,3.14]                         # Liste de nombre entier ou à virgule
ma_liste3 = ['''a''',"b",'c']                   # Liste de caractères qui peuvent être mis entre",' ou '''
ma_liste4 = ["une","chaîne","de","caractères"]  # Chaque élément est bien un ensemble non dissociable !
autre_liste = [12,'a']
print("Contenu de la ma_liste2 :",ma_liste2)
print("Contenu de la ma_liste3 :",ma_liste3)
print("Contenu de la ma_liste4 :",ma_liste4)
print(autre_liste)

#
# # -------------------------------------------- Exemple N°3 -------------------------------------------------------------
#
# # Ajouter une valeur à une liste à la suite
# # Méthode append (ajouter en anglais)
ma_liste4.append("plus")
ma_liste4.append("longue")
print("Contenu de ma_liste4 :",ma_liste4)
#
# # Afficher un item d'une liste
print("Le 2ème élément de ma liste qui est ma_liste4[1] contient :",ma_liste4[1])
# # Dans la console, écrire ma_liste4[1] puis Entrée suffirait pour faire apparaître le contenu, pas besoin de print.
#
# # Supprimer une entrée avec un index
del ma_liste4[5]
# del ma_liste4[10]             # Python vous prévient que le 10ème élément n'existe pas.
# print("Contenu de la ma_liste4 :",ma_liste4)
#
# # Supprimer une entrée avec sa valeur
ma_liste4.remove("plus")
print("Contenu de ma_liste4 :",ma_liste4)
#
# # -------------------------------------------- Exemple N°4 -------------------------------------------------------------
#
# # Inverser les valeurs d'une liste
ma_liste4.reverse()
print("Contenu de ma_liste4 :",ma_liste4)
#
# # Compter le nombre d'items d'une liste
print ("Le nombre de constituants de ma_liste4 :",len(ma_liste4))
#
# # Compter le nombre d'occurences d'une valeur
# # Python fait bien la distincton dans la liste, à la casse et aux accents !
ma_liste5=("camille","Camille","camille","CAMILLE","stéphanie","stephanie","stéphanie")
print("Le nombre de chaîne de caractères dans ma_liste5 qui correspond à camille est :",ma_liste5.count("camille"))
print("Le nombre de chaîne de caractères dans ma_liste5 qui correspond à stéphanie est :",ma_liste5.count("stéphanie"))
print("Le nombre de fois qu'apparaît dans ma_liste2 3.14 est de :",ma_liste2.count(3.14))
#
#
# # Trouver l'index d'une valeur
# # Attention, la position 0 compte pour un emplacement.
print("La position de Camille dans ma_liste5 est de :",ma_liste5.index("Camille"))
#
# # Plantage car plusieurs occurences portent la même chaîne de caractères... Seule la 1ère occurence est prise en compte.
print("La position de camille dans ma_liste5 est de :",ma_liste5.index("camille"))
#
# # -------------------------------------------- Exemple N°5 -------------------------------------------------------------
#
# # Manipuler une liste
#
# # Afficher directement la dernière occurence de la liste
print ("Voici le dernier élément de la liste ma_liste4 :",ma_liste4[-1])
#
# # Afficher directement les dernières occurences de la liste
print ("Voici les 3 derniers éléments de la liste ma_liste4 :",ma_liste4[-3:])
#
# # Afficher directement les occurences 3 et 4 de la liste... Attention, l'occurence de départ est la 3éme.
print ("Voici les 2 derniers éléments de la liste ma_liste4 :",ma_liste4[2:4])
#
# # Afficher la liste par une autre méthode
print ("Voici la liste ma_liste4 :",ma_liste4[:])
#
# #Savoir si une occurence est dans la liste
print("Est-ce que Camille est dans ma_liste_5 ?","Camille" in ma_liste5)
print("Est-ce que STEPHANIE est dans ma_liste_5 ?","STEPHANIE" in ma_liste5)
#
# # -------------------------------------------- Exemple N°6 -------------------------------------------------------------
# # Faire des boucles avec des listes... Ce que l'on a déjà fait avec des chaînes de caractères.
#
ma_liste6=["V","i","v","e","","P","y","t","h","o","n"]
for occurence in ma_liste6:
     print(occurence)
print('\n')
#
# # Énumérer chaque occurence de la liste de façon automatique
for occurence in enumerate(ma_liste6):
    print(occurence)
print('\n')
#
# # Transformer une string en liste
ma_chaine="Cette formation sur Python 3 est formidable !"
ma_liste7=ma_chaine.split(" ")
print("ma_liste7 vaut:",ma_liste7)
#
# # Transformer une liste en string
ma_liste8=["REANT","Denis","est","un","super","formateur!","LOL"]
ma_chaine2=" ".join(ma_liste8)
print("ma_liste8 devient une chaîne qui est :",ma_chaine2)
#
# # -------------------------------------------- Exemple N°7 -------------------------------------------------------------
#
# # On peut effectuer des opérations sur des listes
print("Multiplication d'une liste par un entier, ici 2 :",ma_liste8*2)
#
# # On concatène les 2 listes
print ("Addition de 2 listes ma_liste_7+ma_liste_8=",ma_liste7+ma_liste8)
#
# # On fait une extension
ma_liste7.extend(ma_liste8)
print("ma_liste7 et ma_liste8 en mode extend :",ma_liste7)
ma_liste9=[1,2,3,[10,20,30],[ma_liste8]]
#
# # Une liste dans une liste... On effectue toutes les manipulations précédentes
print("Contenu de ma_liste9 :",ma_liste9)
