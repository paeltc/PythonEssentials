"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_9 executer.py


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
        self.objetMonLabel = QtWidgets.QLabel("Vive la formation sur Python 3 : utilisation des fichiers")
        self.objetMonTextEdit = QtWidgets.QTextEdit("Entrez le message que vous voulez enregistrer !")
        self.objetMonBoutonSauver = QtWidgets.QPushButton("Sauvegarder")



        # Le placement des widgets
        disposotion = QtWidgets.QVBoxLayout()
        disposotion.addWidget(self.objetMonLabel)
        disposotion.addWidget(self.objetMonTextEdit)
        disposotion.addWidget(self.objetMonBoutonSauver)

        # Application du maillage
        self.setLayout(disposotion)

        # Connexion du bouton entre l'évènement et la fonction
        self.objetMonBoutonSauver.clicked.connect(self.fonctionSauvegarder)


    def fonctionSauvegarder(self):

        with open ("Sauvegarde_de_mon_fichier.txt","w") as fichier:
            mon_texte = self.objetMonTextEdit.toPlainText()
            fichier.write(mon_texte)
            print("Votre fichier est sauvegardé dans la racine de votre projet.")
            QMessageBox.about(self,"Information concernant votre fichier.","Votre fichier a été enregistré avec succès !")







