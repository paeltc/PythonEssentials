"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_4.py


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

# Quelque soit le langage, pour la programmation orientée objet, il est préférable de passer par des propriétés
# pour changer les valeurs des attributs. Alors, bien que cela ne soit pas obligatoire, il existe une convention
# de passer par des getters (ou accesseurs en francais) et des setters (mutateurs) pour changer la valeur d'un attribut.
# Cela permet de garder une cohérence pour le programmeur ; si je change un attribut souvent, cela peut également.
# Impacter d'autres attributs et les mutateurs permettent de faire cette modification une fois pour toutes.

#-*- coding: utf-8 -*-
# Définition de la classe voiture

class Voiture (object):

    # Attributs valides dans toute la classe
    nombre_de_roues=0

#--------------------------------------  Surcharge de méthodes ---------------------------------------------------------
    """
     Constructeur : par défaut une voiture a 100 roues
    """
    def __init__(self):
        self.nombre_de_roues=100        # Ce n'est pas une valeur très réaliste ;-)

# C'est cette méthode qui sera exécutée.
    """
        Constructeur : par défaut une voiture a 4 roues
    """

    def __init__(self):
        self.nombre_de_roues = 4

    # --------------------  Modifier le patron du code de la classe : c'est le mal -------------------------------------

    # Si l'on veut modifier le nombre de roues, on doit le faire dans la classe et non pas depuis le main.
    # On ne respecte pas l'encapsulation.

    """
        fonction sans accès depuis le main
    """
    def nombre_de_roues_sans_get(self):
        return 10                       # C'est ici que l'on doit modifier.

    """"
        getter : permet de connaître le nombre de roues de l'objet voiture
        getter = accesseur 
    """

    def getter_nombre_roues(self):
        return print ("Récupération du nombre de roues par le getter",self.nombre_de_roues)

    """
    setter : permet de connaître le nombre de roues de l'objet voiture
    """

    def setter_nombre_roues(self, nouveau_nombre_de_roues):
        print ("Changement du nombre de roues")
        self.nombre_de_roues = nouveau_nombre_de_roues
        return self.nombre_de_roues


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

    # Instanciation de l'objet ma_voiture créé depuis la classe voiture()... Ceci est un constructeur.
    # La variable n'est accessible hors de la classe, ce qui est conforme au principe d'encapsulation.
    # print(nombre_de_roues)
    ma_Voiture=Voiture()
    print("Le nombre de roues par défaut de notre voiture est de :",ma_Voiture.nombre_de_roues)        # Constructeur
    # On ne peut pas accéder au nombre de roues donc à l'attribut directement.
    # print("Le nombre de roues par défaut de notre voiture est de :",ma_Voiture.nombre_de_roues(100))

    # Oui mais ce n'est plus modifiable depuis l'extérieur de la classe.
    # print("Le nombre de roues sans getter est de :",ma_Voiture.nombre_de_roue_sans_get())

    ma_Voiture.getter_nombre_roues()
    print("Le nombre de roues avec setter est de :",ma_Voiture.setter_nombre_roues(5),"car il y a une vraie roue de secours.")

help(ma_Voiture)



