"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_5 executer.py


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
from PyQt5.QtWidgets import QMessageBox


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

        self.setGeometry(200, 200, 400, 100)
        self.setWindowTitle("Ma 2ème fenêtre sous PyQt5 !")
        self.setWindowIcon(QIcon('icon.ico'))

        # Les widgets
        self.objetMonLabel = QtWidgets.QLabel("Vive la formation sur Python 3 : utilisation d'une 'messageBox'")
        self.objetMonBoutonEffacer = QtWidgets.QPushButton ("Effacer")
        self.objetMonBoutonRecopier = QtWidgets.QPushButton("Recopier")
        self.objetMonLineEdit = QtWidgets.QLineEdit("Entrez le message que vous voulez copier !")

        # Le placement des widgets
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.objetMonLabel)
        v_box.addWidget(self.objetMonLineEdit)
        v_box.addWidget(self.objetMonBoutonRecopier)
        v_box.addWidget(self.objetMonBoutonEffacer)


        # Application du maillage
        self.setLayout(v_box)

        # Connexion du bouton entre l'évènement et la fonction
        self.objetMonBoutonRecopier.clicked.connect(self.fonctionClickRecopier)
        self.objetMonBoutonEffacer.clicked.connect (self.fonctionClickEffacer)

    def fonctionClickRecopier(self):
        QMessageBox.about(self,"Le message copié est :",self.objetMonLineEdit.text())


    def fonctionClickEffacer(self):
        buttonReponse = QMessageBox.question(self,"Question ?","Voulez-vous vraiment effacer le message ?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReponse == QMessageBox.Yes:
            self.objetMonLineEdit.clear()
            print('Vous avez cliqué sur Yes !')
        else:
            print('Vous avez cliqué sur No !')
            self.objetMonLineEdit.setText("Vous avez cliqué sur No !")

