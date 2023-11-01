"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_6.py
					
				
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

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Fonction sans paramètre-> () vide
def compteur3():
    increment = 0                   # Variable locale à la fonction, la portée de cette variable ne concerne que compteur3().
    while increment < 3:
        print("Compte",increment,"fois")
        increment = increment + 1

# -------------------------------------------- Exemple N°2 --------------------------------------------------------------

# Fonction qui appelle une autre fonction

def doubleCompteur3():
    compteur3()
    print ("Compte encore une 2ème fois")
    compteur3()

# -------------------------------------------- Exemple N°3 --------------------------------------------------------------
# Surcharge de définition... C'est la dernière définition de la fonction qui compte, elle écrase les premières.
def volumeCube():
    cote = 5                   # Variable locale à la fonction
    print("Le volume du cube de 5 m de côté est de :",5**3,"m3.")
    print("Normalement, on obtient 125 m3.")

def volumeCube():
    cote = 10                   # Variable locale à la fonction
    print("Le volume du cube de 10 m de côté est de :",10*10*10,"m3.")
    print("Normalement, on obtient 1000 m3.")

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Appel du module ici

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------
# print("Exemple 1")
# compteur3()
# print("Fin exemple N°1\n")
# #-------------------------------------------- Exemple N°2 --------------------------------------------------------------
# print("Exemple 2")
# doubleCompteur3()
# print("Fin exemple N°2\n")
# #-------------------------------------------- Exemple N°3 --------------------------------------------------------------
print("Exemple 3")
volumeCube()
print("Fin exemple N°3\n")
# #
print("On essaie d'afficher une variable dont la portée est locale à une fonction qui est cote =",cote,"ou incrément =",increment)




#-----------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-----------------------------------------------------------

# On peut écrire les modules ici aussi.
def volumeCube():
    cote = 10                   # Variable locale à la fonction
    print("Le volume du cube de 10 m de côté est de :",10*10*10,"m3.")
    print("Normalement, on obtient 1000 m3.")