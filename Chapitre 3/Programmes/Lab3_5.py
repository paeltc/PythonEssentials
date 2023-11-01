"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_5.py


"""
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# À lire : https://docs.python.org/3/tutorial/classes.html
# À lire : https://docs.python.org/3/reference/datamodel.html

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------


#-------------------------------------------------------
#		     Zone de déclaration des classes
#-------------------------------------------------------



#-*- coding: utf-8 -*-
# Définition de la classe voiture... Attention, normalement, il y a une classe par fichier !

class Rectangle(object):         # Définition
    "Classe de rectangle"
    def __init__(self, longueur =0, largeur =0):
        self.cetteLongueur = longueur
        self.cetteLargeur = largeur
        self.ceNom ="rectangle"

    def perimetre(self):
        return "(%d + %d) * 2 = %d" % (self.cetteLongueur, self.cetteLargeur,(self.cetteLongueur + self.cetteLargeur)*2)

    def surface(self):
        return "%d * %d = %d" % (self.cetteLongueur, self.cetteLargeur, self.cetteLongueur*self.cetteLargeur)

    def afficher(self):
        print("Un %s de %d sur %d" % (self.ceNom, self.cetteLongueur, self.cetteLargeur))
        print("a une surface de %s" % (self.surface()))
        print("et un périmètre de %s\n" % (self.perimetre()))

class Carre(Rectangle):# La classe carre hérite de la classe mère rectangle,donc la classe fille carre hérite tous les attributs et toutes les méthodes de la classe mère rectangle
    "Classe de carré"
    def __init__(self, cote):                   # Redéfinir le constructeur "Polymorphisme d'héritage"
        Rectangle.__init__(self, cote, cote)    # Instanciation de la classe mère (appeler le constructeur de la classe mère dans le constructeur de la classe fille)
                                                # Le nombre de paramètres doit être le même.
        self.ceNom ="carré"                     # Redéfinir la valeur de l'attribut nom au sein de la classe fille

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



if __name__ == '__main__':
    objetRectangle=Rectangle(10,20)
    objetRectangle.afficher()
    objetCarre=Carre(5)
    objetCarre.afficher()