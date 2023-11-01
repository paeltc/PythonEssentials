"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_11.py


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

import os
import os.path  # Importation de la bibliothèque os.path pour utiliser la fonction getsize()

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

class MonIterateurInverse():

    def __init__(self, donnee):         # Constructeur
        self.donnee = donnee
        self.index = len(donnee)

    def __iter__(self):                 # Itération
        return self

    def __next__(self):

        if self.index == 0:             # Fin de la chaîne de caractères
            raise StopIteration
        else:
            self.index=self.index-1

        return self.donnee[self.index]

# -------------------------------------------- Exemple N°3 --------------------------------------------------------------

def generateur (donnee):
    # for index in range(0, len(donnee) - 1, 1):
    for index in range (len(donnee)-1,-1,-1):
        yield donnee[index]

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Un itérateur est une sorte de curseur qui a pour mission de se déplacer dans une séquence d'objets.
# L'itérateur permet de parcourir chaque objet d'une séquence sans se préoccuper de la structure sous-jacente.

# L'itérateur apporte un niveau d'abstraction plus élévé, c'est-à-dire qu'on ajoute une couche de code en plus pour réaliser une action,
# si un jour on devait changer des éléments du code - exemple d'une mise à jour d'une lib ou changement de base de données.
# Par exemple, on n'a pas besoin de changer tout notre code puisque cette couche d'abstraction en plus permet de ne changer
# que ce qui est nécessaire au niveau de la classe et non plus du code.
# L'itérateur est un objet peu coûteux en utilisation de mémoire.

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# Liste de 10 éléments identiques de type int
ma_liste1 = [1,2,3,4,5,6,7,8,9,10]
#
for x in ma_liste1:
    print ("Voici l'élément",x,"de ma_liste1")

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------
# Création de son itérateur personnel

# Création de l'objet
phrase = MonIterateurInverse("Vive la formation sur Python 3 !")
for x in phrase:
    print (x)

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------
# On remarque qu'il existe un nouveau mot clé, spécialement créé pour les générateurs : yield. ' \
# Ce mot clé est un peu similaire au return des fonctions sauf qu'il ne signifie pas la fin de l'exécution de la fonction,
# mais une mise en pause, et à la prochaine itération, la fonction recherchera le prochain yield.

phrase = generateur("Vive la formation sur Python 3 !")
for x in phrase:
    print (x)