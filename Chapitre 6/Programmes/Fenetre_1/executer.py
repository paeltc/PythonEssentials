"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Dossier Fenetre_1


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

#http://zetcode.com/gui/pyqt5/firstprograms/

#! / usr / bin / python3
# - * - codage: utf-8 - * -
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget



#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# Les étapes d'une création d'une fenêtre sous PyQt5 sont :
# 1 - Importer les bibliothèques widgets (pyQt5,pyQt5-tools... dans PyCharm)
# 2 - Créer un conteneur = fenêtre (icône, titre, taille, etc.)
# 3 - Insérer les widgets
# 4 - Générer des fonctions associeées aux évènements appliqués sur les widgets
# 5 - Afficher la fenêtre
# 6 - sys.exit(application.exec())

# Pas de besoin de passer par Qt Designer
class Exemple(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Ma fenêtre avec PyQT5 !')
        self.setWindowIcon(QIcon('icon.ico'))

        # http://convertir-une-image.com/edition/recadrer-une-image.asp?i=20180207-124449-arxwv

        self.show()



#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


if __name__ == '__main__':

    application = QApplication(sys.argv)
    objetExemple = Exemple()
    sys.exit(application.exec_())
