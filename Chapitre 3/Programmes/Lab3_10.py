"""

Nom du projet : Apprendre le langafe Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_10.py


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

def Calcule_nombre_mots(texte):     # Fonction qui calcule le nombre de mots d'un texte donné
    nombre_de_mots = 1              # Compteur du nombre de mots
    for variable in texte:          # Parcourt du texte
        if variable < 'A' or 'Z' < variable < 'a' or variable > 'z':    # On considère que les mots sont séparés.
                                                                        # Par un et un seul symbole (autre que lettres).
            nombre_de_mots += 1
    return nombre_de_mots


def creer_fichier(nom_fichier):
    f = open(nom_fichier,"w")  # L'ouverture du fichier en mode écriture.
                                # Si le fichier existe son contenu sera écrasé sinon il sera créé.
                                # Python va générer une erreur (exception) si le fichier en cours
                                # d'utilisation par une autre application ou s'il est ouvert.
    f.close()


def Ajouter_lignes(nom_fichier):
    ce_fichier = open(nom_fichier,"a")  # L'ouverture du fichier en mode ajout
                                # Pour ajouter de texte dans le fichier sans écraser leur contenu
    while True:  # Boucle ouverte
        ligne = input("Entrer une ligne, ligne vide pour terminer : ")  # Demande de la saisie d'une ligne
        if ligne == "": break  # Arrêt de la boucle si l'utilisateur n'a rien saisi (chaîne vide)
        ce_fichier.write(ligne + "\n")  # La méthode write permet d'écrire la ligne saisie en ajoutant le caractère spécial '\n' pour le retour à la ligne dans le fichier f
    ce_fichier.close()


def Afficher(nom_fichier):
    ce_fichier = open(nom_fichier,"r")  # Ouverture du fichier nom_fichier en mode lecture
    texte = ce_fichier.read()  # La méthode read permet de lire (récupérer) le contenu dans le fichier f qui sera stocké dans la variable texte.
    print(texte)
    ce_fichier.close()  # Fermeture du fichier


def propriete(nom_fichier):

    f = open(nom_fichier,"r")          # Ouverture du fichier nom_fichier en mode lecture
    liste_lignes = f.readlines()        # Retourner le contenu du fichier sous forme d'une liste dont chaque élément est une ligne du fichier
    nombre_lignes = len(liste_lignes)   # Le nombre des lignes du fichier correspond au nombre d'éléments de la liste liste_lignes
    nombre_caracteres = 0               # Compteur de calcul de nombre des caractères
    nombre_mots = 0                     # Compteur de calcul de nombre des mots

    for ligne in liste_lignes:
        nombre_caracteres += len(ligne)
        nombre_mots += Calcule_nombre_mots(ligne)   # Calcule_nombre_mots(ligne) retourne le nombre de mot du texte ligne
    taille = os.path.getsize(nom_fichier);          # getsize retourne la taille du fichier
    print("Nombre de lignes=",nombre_lignes)       # Affichage des informations
    print("Nombre de mots=",nombre_mots)
    print("Nombre de caractères=",nombre_caracteres)
    print("Taille=",taille,"octets")
    f.close()  # Fermeture du fichier


# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

#-------------------------------------------- Exemple N°1 ----------------------------------------------------
 # Écrire un programme en Python qui permet de créer un fichier texte appelé "teste1.txt" et d'écrire la ligne "Vive la formation sur Python 3" dans ce fichier

#  # Permet de choisir le répertoire de contenu du fichier
# os.chdir("C:/Denis")
# print(os.getcwd())      # Permet de voir le chemin d'accès du répertoire de travail
#
# f=open("texte1.txt","w") # Ouverture du fichier texte1 en mode écriture... Ce sont des / et non des \ comme dans Windows
# # Si le fichier existe son contenu sera écrasé, sinon il sera créé.
# # "w" est le mode d'accès en écriture.
# # Python va générer une erreur (exception) si le fichier est en cours d'utilisation par une autre application ou s'il est ouvert.
# # texte1.txt est le nom physique du fichier.
# # f est le nom logique du fichier
# ligne='Vive la formation sur Python 3.\n'
# ligne2="Votre formateur est ravi de vous accompagner dans cette formation !"
# f.write(ligne) # La méthode write permet d'écrire un texte dans le fichier f (1 seul paramètre).
# f.write(ligne2)
# f.close() # Fermeture du fichier

#-------------------------------------------- Exemple N°2 ----------------------------------------------------
#  # Écrire un programme en Python qui permet de lire (récupérer) et d'afficher le contenu du fichier texte  "C:/Users/Denis/Documents/texte1.txt"
#  # Chemin absolu de l'endroit du fichier
# f=open("C:/Denis/texte1.txt","r") # Ouverture du fichier texte1 en mode lecture,
#  # Python va générer une erreur (exception) si le fichier n'existe pas.
#  # texte1.txt est le nom physique du fichier.
#  # f est le nom logique du fichier.
# le_texte=f.read() # La méthode read permet de récupérer le contenu du fichier f et de le stocker dans la variable le_texte.
# print("Contenu du fichier : \n"+le_texte) # Affichage du contenu du fichier
# f.close() # Fermeture du fichier

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

while True:
    print("\n\n**************************************************")
    print("1-->; Pour créer un fichier")
    print("2-->; Pour ajouter des lignes au fichier")
    print("3-->; Pour afficher le fichier")
    print("4-->; Pour afficher les propriétés d'un fichier")
    print("5-->; Pour quitter")
    choix = (input("\nEntrer votre choix : "))       # Attention, on travaille avec le caractère et pas le chiffre.
    print("**************************************************")
    if choix.isdecimal():                           # Ou utiliser une exception ValueError.
        if choix == '1':
            nom_fichier = input("Entrer le nom de votre fichier à créer : ")
            creer_fichier(nom_fichier)
        elif choix == '2':
            Ajouter_lignes(nom_fichier)
        elif choix == '3':
            Afficher(nom_fichier)
        elif choix == '4':
            propriete(nom_fichier)
        elif choix == '5':
            break;
    else:
        print("Erreur choix : ")


