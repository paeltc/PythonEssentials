"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_8.py


"""
# -----------------------------------------------------------------------------
# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/random.html
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
import builtins

ma_variable=10
ma_variable2=100
ma_variable3=1
mon_exception=0

menbreDeLaFamille = ['Moi', 'Stéphanie', 'Camille', 'Jacques']

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

def une_fonction():
    return 1 / 0

def une_autre_fonction():
    une_fonction()

# Lever ses propres exceptions
# Quand une exception est activée, on dit qu’elle est « levée ».


def maFonction(parametre):
    if parametre not in (1, 2, 3):
        raise ValueError("'parametre' ne peut prendre que les valeurs 1, 2 ou 3.")
    # Reste du code...


def plusieursExceptions():
    try:
        return menbreDeLaFamille[100 / ma_variable2]
    # Est exécuté pour ces deux exceptions
    except (IndexError, ZeroDivisionError):
        return print("Aïe, division par 0 et un index inconnu")
    # Est exécuté pour cette exception
    except TypeError:
        print("Houlaaa, c'est quoi cette histoire ? Mon indice est un float !")

def exceptionEnglobante ():
    try:
        return menbreDeLaFamille[100 / ma_variable2]
    except Exception:
        return print("Il y a eu un problème mais on ne connaît pas sa nature !")

def exceptionElse():
    try:
        return print(menbreDeLaFamille[100 / ma_variable2]) #ma_variable3
    except (IndexError, ZeroDivisionError):
        return None         # À ne pas faire !
    except TypeError:
        print("Houlaaa, c'est quoi cette histoire ? Mon indice est un float !")
    #else est le bloc exécuté si aucune exception n’est levée :
    else:
        print('En fait, tout va bien.')

def exceptionFinally():
    try:
        return menbreDeLaFamille[100 / ma_variable2]
    except (IndexError, ZeroDivisionError):
        return None          # À ne pas faire !
    except TypeError:
        print("Houlaaa, c'est quoi cette histoire ? Mon indice est un float !")
    finally:
        print("Finalement, c'est Flash que je préfére !")

def exceptionManipuler():
    try:
        return menbreDeLaFamille[100 / ma_variable2]
    except TypeError as mon_exception:
        print("Arguments de TypeError",mon_exception.args)
        #raise mon_exception



# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


# help(builtins)

#-------------------------------------------- Exemple N°1 ----------------------------------------------------
# # Quelques exceptions natives de Python
#
# 1 / 0 # Division par zéro
# # Donne ZeroDivisionError: division by zero
#
# Liste = [1, 2, 3, 4, 5]
# Liste[10] # Dépassement d'un tableau
# # # Donne IndexError: list index out of range
# #
# dictionnaire = {'prenom': "Jacques"}
# dictionnaire['pierre'] # Élément de dictionnaire inconnu
# # # KeyError: 'pierre'
# #
# 3+"3"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# import abraCadaBra # Ce module n'existe pas... Enfin pas encore
# ModuleNotFoundError: No module named 'abraCadaBra'
#
# open('fichierVirtuel') # Le fichier n'existe pas.
# FileNotFoundError: [Errno 2] No such file or directory: 'fichierVirtuel'
#
# print(ce n'est pas comme ça que l'on écrit un texte) # La variable n'existe pas.
# SyntaxError: invalid syntax
#
# print(variable_non_declaree)
# NameError: name 'variable_non_declaree' is not defined
#
# int('a') # La valeur passée n'a aucun sens, c'est une lettre et ce n'est pas un entier.
# ValueError: invalid literal for int() with base 10: 'a'

#-------------------------------------------- Exemple N°2 ----------------------------------------------------
# Dans une fonction

# une_autre_fonction()
# #ZeroDivisionError: division by zero

#-------------------------------------------- Exemple N°3 ----------------------------------------------------
# Gérer une erreur avec raise
# maFonction(4)

#-------------------------------------------- Exemple N°4 ----------------------------------------------------
# Les exceptions servent d’abord et avant tout à gérer les cas exceptionnels et on peut donc les détecter,
# et réagir quand elles surviennent, à l’aide de l’instruction try/except.
#
# try:
#     resultat = menbreDeLaFamille[ma_variable]
#     # ma_variable est plus grand que la taille du tableau
# except IndexError:
#     resultat = None  # mot clé, je ne fais rien! Il ne faut pas le faire sinon cela cache la nature du problème.
#     print("On a géré l'exception de type IndexError") # On affiche ceci.

#-------------------------------------------- Exemple N°5 ----------------------------------------------------

# plusieursExceptions()

#-------------------------------------------- Hiérarchie des exceptions --------------------------------------
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EnvironmentError
#       |    +-- IOError
#       |    +-- OSError
#       |         +-- WindowsError (Windows)
#       |         +-- VMSError (VMS)
#       +-- EOFError
#       +-- ImportError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning

#-------------------------------------------- Exemple N°6 ----------------------------------------------------

# exceptionEnglobante ()

#-------------------------------------------- Exemple N°7 ----------------------------------------------------

# exceptionElse()

#-------------------------------------------- Exemple N°8 ----------------------------------------------------

#exceptionElse()

#-------------------------------------------- Exemple N°9 ----------------------------------------------------
# finally est un bloc qui est exécuté après que tous les autres blocs aient été exécutés, peu importe
# qu’il y ait eu une exception ou non, et même si le programme crash.

exceptionFinally()

#-------------------------------------------- Exemple N°10 ----------------------------------------------------

# exceptionManipuler()