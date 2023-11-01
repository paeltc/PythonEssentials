"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_7.py


"""
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------

# Le packing et l'unpacking sont deux concepts Python complémentaires qui offrent la possibilité de transformer
# une succession d'arguments, nommés ou non, en liste/tuple ou en dictionnaire, et vice-versa.

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

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# Unpacking explicite avec une liste, puis un dictionnaire
def aire_rectangle(longueur, largeur):
    return longueur*largeur

def aire_rectangle(cote_longueur=0, cote_largeur=0):
    return cote_longueur*cote_largeur

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

# Packing explicite
def aire_rectangle_1(*args):  # Les arguments passés en paramètres sont paquetés dans args qui se comporte comme un tuple.
    if len(args) == 2:
        return args[0]*args[1]
    else:
        print('Merci de stipuler deux paramètres')

def aire_rectangle_2(**kwargs):  # Les arguments passés en paramètres sont paquetés dans kwargs qui se comporte comme un dictionnaire.
    if len(kwargs) == 2:
        result = 1
        for key, value in kwargs.items():
            result *=value
        return result
    else:
        print('Merci de stipuler deux paramètres')


#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

if __name__ == '__main__':

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

     # Les différentes utilisations de l'opérateur *

     # Opérateur splat... Pour une multiplication
     print(2 * 3)

     # Opérateur splat... Pour une puissance
     print(2 ** 3)

     # Opérateur splat... Pour une duplication
     ma_liste = [1, 2, 3]
     print(3 * ma_liste)

     # Unpacking : fonctionne avec des tuples, des listes, des strings et tout autre itérable.
     # Le tuple (2,3) va être depaqueté et sauvegardé dans les variables a et b.
     element_a,element_b = (2, 3)
     print(element_a)
     print(element_b)

     # Packing
     # Les valeurs de element1 et element2 sont empaquetées dans ma_liste.
     ma_liste = [element_a, element_b]
     print(ma_liste)

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

     dimension_rectangle_1 = [3, 8]
     dimension_rectangle_2 = {'cote_longueur':4, 'cote_largeur':8}
     # La liste dimension_rectangle_1 va être dépaquetée en arguments unitaires.
     print ("Rectangle 1 a pour surface:",aire_rectangle(*dimension_rectangle_1),"unités d'aire... Les paramètres proviennent d'une liste.")
     # Le dictionnaire dimension_rectangle_2 va être dépaqueté en arguments unitaires.
     print ("Rectangle 2 a pour surface:",aire_rectangle(**dimension_rectangle_2),"unités d'aire... Les paramètres proviennent d'un dictionnaire.")

#-------------------------------------------- Exemple N°3 --------------------------------------------------------------

     # Une liste va être créée à partir des arguments fournis.
     print ("Rectangle 1 a pour surface:",aire_rectangle_1(3,8),"unités d'aire... Les paramètres proviennent d'un tuple.")
     # Un dictionnaire va être créé à partir des arguments nommés.
     print("Rectangle 2 a pour surface:",aire_rectangle_2(cote_longueur=4, cote_largeur=8),"unités d'aire... Les paramètres proviennent d'un dictionnaire.")

