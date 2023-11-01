"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_6.py


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


#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# Le polymorphisme permet "d'appeler la même méthode" sur plusieurs objets différents sans se préoccuper
# de comment se comportera l'objet dans ce cas.
# En Python, ça se fait en redéfinissant la méthode dans la classe fille quand cela est nécessaire.
# Dans ce cas, quand il est nécessaire d'implémenter un héritage, il faut explicitement le demander.

class Mere (object):

    def affiche(self):
            print("Cet affichage vient de la fonction de la classe 'Mere'")

class filleA(Mere):
    """ Cette classe a besoin d'avoir le comportement d'origine plus le sien propre et elle est alors obligée d'appeler
    la fonction de la classe mère de façon explicite"""

    def affiche(self):
        Mere.affiche(self)
        print("Cet affichage vient de la fonction de la classe 'filleA'")

class filleB(Mere):
    """ Cette classe, elle, n'ayant pas besoin de la fonction d'origine,
    se contente de redéfinir un autre comportement totalement différent"""

    def affiche(self):
        print("Cet affichage vient de la fonction de la classe 'filleB'")

class filleC(Mere):
    """ Ne fait que recopier la définition de la fonction dont elle hérite de façon implicite"""
    pass                # Ne fait rien...



# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

if __name__ == '__main__':
    objetMere=Mere
    objetMere.affiche(Mere)
    objetMere.affiche(object)
    print("\n")

    objetFilleA=filleA
    objetFilleA.affiche(filleA)  # Affiche Mere + filleA
    objetFilleA.affiche(Mere)
    print("\n")

    objetFilleB=filleB
    objetFilleB.affiche(filleB)  # Affiche filleB
    objetFilleB.affiche(Mere)
    print("\n")

    objetFilleC = filleC
    objetFilleC.affiche(filleC)  # Affiche Mere
    objetFilleC.affiche(Mere)
