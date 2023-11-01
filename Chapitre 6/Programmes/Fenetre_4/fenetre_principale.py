"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Dossier Fenetre_4 executer.py


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

# http://zetcode.com/gui/pyqt5/firstprograms/

# ! / usr / bin / python3
# - * - codage: utf-8 - * -


import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------


# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

class fenetrePrincipale (QtWidgets.QWidget):

    def __init__(self):
        super(fenetrePrincipale,self).__init__()
        self.initialisationInterface()

    def initialisationInterface(self):

        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Ma 2ème fenêtre sous PyQt5 !")
        self.setWindowIcon(QIcon('icon.ico'))

        # Les widgets
        self.objetMonLabel = QtWidgets.QLabel('Vive la formation sur Python 3')
        self.objetMonbouton = QtWidgets.QPushButton ("Cliquez-moi")

        # Le placement des widgets
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.objetMonLabel)     # On peut intervertir le bouton et le label pour voir la différence.
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.objetMonbouton)

        v_box.addLayout(h_box)

        # Application du maillage
        self.setLayout(v_box)

        # Connexion du bouton entre l'évènement et la fonction
        self.objetMonbouton.clicked.connect(self.fonctionClick)

    def fonctionClick(self):
            self.objetMonLabel.setText("Hourra, vous m'avez cliqué !")

