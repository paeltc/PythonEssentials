"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_9.py


"""
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# À lire : https://www.python.org/dev/peps/pep-0318

################################################
#				Programme principal
################################################



# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------



#-------------------------------------------------------
#		     Zone de déclaration des classes
#-------------------------------------------------------




#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# Les décorateurs sont des fonctions « classiques » de Python, dans leur définition. Ils
# prennent en paramètre une fonction et renvoient une fonction.
# Le décorateur s'exécute au moment de la définition de fonction et non lors de l'appel.

def verification (fonction):
    def wrapper (*args,**kwargs):
        for valeur in args:
            if(type(valeur) is not int):
                raise TypeError ("L'un des paramètres n'est pas un entier!")
        return fonction (*args,**kwargs)
    return wrapper

@verification
def addition(nombre1, nombre2):
    return nombre1+nombre2

@verification
def soustraction(nombre1, nombre2):
    return nombre1-nombre2
#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


if __name__ == "__main__":
    resultat=addition(1,2)
    print ("L'addition donne:",resultat)

    resultat = soustraction(4, 2)
    print("La soustraction donne:", resultat)

    resultat = addition(1,"2")
    print("L'addition donne:", resultat)

    resultat = soustraction(4, "2")
    print("La soustraction donne:", resultat)