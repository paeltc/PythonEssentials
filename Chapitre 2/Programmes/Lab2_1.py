"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_1.py
					
				
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
# # On "cast" la valeur de la touche en un entier de façon à ce que la valeur soit non plus un caractère mais un entier.
# valeur=int(valeur_saisie)
#
# if valeur<0:                                                # Indentation
#     print("Votre valeur est négative !")                     # Bloc if
#     print("Vous devez entrer une valeur positive !")         # Bloc if
# # Fin bloc if
#
# if valeur>0:                                                                        # Indentation
#     print("Votre valeur est positive, c'est bien !")                                 # Bloc N°1 if
#     print("bloc N°1 if")
#     if valeur>5:                                                                    # Indentation
#         print ("Vous vous approchez, la 8valeur mystère est supérieure à 5 !")        # Bloc N°2 if
#         print("bloc N°2 if")
#         if valeur==8:                                                               # Indentation
#             print("Bravo ! Vous avez trouvé la valeur mystère !")                    # Bloc N°3 if
#             print("bloc N°3 if")
#         # Fin bloc N°3 if
#     # Fin bloc N°2 if
# # Fin bloc N°1 if

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------


valeur_saisie=input("Entrez une valeur comprise entre 0 et 10, ceci est le chiffre mystère dans le programme :")
valeur=int(valeur_saisie)

if (valeur<0 or valeur>10):                                                         # Indentation
    print("Vous devez entrer une valeur comprise entre 0 et 10 !")                   # Bloc if

if (valeur is not 8):                                                               # Indentation
    print("Vous n'avez pas trouvé le nombre mystère !")                              # Bloc if

if ((valeur is not 8) and (valeur==7)):                                             # Indentation
    print("Vous n'avez pas trouvé le nombre mystère mais vous y êtes presque !")     # Bloc if

# Ce code sera toujours exécuté si la valeur est >10 ou <0
if (valeur is 8):                                                                   # Indentation
    print("BRAVO, vous avez trouvé le nombre mystère !")                             # Bloc if

#--------------------------------------------  En résumé  --------------------------------------------------------------

# Les comparateurs standards
# <; <=; >; >=; ==; !=; is; is not; and (condition et non logique); or (condition ou non logique).