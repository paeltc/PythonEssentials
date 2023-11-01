"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_2.py
					
				
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

valeur_mystere = 8

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


#-------------------------------------------- Exemple N°1 --------------------------------------------------------------


# # L'utilisateur entre une valeur de touche de clavier suite au message qui est affiché.
# valeur_saisie=input("Entrez une valeur comprise entre 0 et 10, ceci est le chiffre mystère dans le programme :")
# # On "cast" la valeur de la touche en un entier de façon à ce que la valeur soit non plus un caractère mais un entier
# valeur=int(valeur_saisie)
#
# if valeur<0:                                                # Indentation
#     print("Votre valeur est négative !")                     # Bloc if
#     print("Vous devez entrer une valeur positive !")         # Bloc if
# else:                                                       # Pas de conditions et indentation
#     print("Votre valeur est positive, c'est bien !")         # Bloc else
#     print("Fin bloc else")                                  # Fin bloc else
#
# if (valeur is 8):                                           # Indentation
#     print("BRAVO, vous avez trouvé le nombre mystère !")     # Bloc if
# else:                                                       # Pas de conditions et indentation
#     print("Vous n'avez trouvé le nombre mystère !")          # Bloc else
#     # Fin bloc else

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------



# À chaque fois, on relance la simulation... On peut faire cela de façon plus intelligente.
valeur_saisie=input("Entrez une valeur comprise entre 0 et 10, ceci est le chiffre mystère dans le programme :")
valeur=int(valeur_saisie)

if (valeur<0 or valeur>10):                                                         # Indentation
    print("Vous devez entrer une valeur comprise entre 0 et 10 !")                   # Bloc if

elif (valeur==0):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==1):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==2):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==3):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==4):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==5):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
    print("Vous chauffez... Le nombre mystère est supérieur à 5 !")                   # Bloc elif
elif (valeur==6):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==7):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
elif (valeur==8):                                                                   # Indentation
    print("Bravo ! Vous avez pas trouvé le nombre mystère !")                         # Bloc elif
elif (valeur==9):                                                                   # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
else:                                                                               # Pas de conditions et indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc elif
