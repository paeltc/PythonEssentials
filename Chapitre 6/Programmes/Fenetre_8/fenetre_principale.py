"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
						-   Dossier Fenetre_8 executer.py


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
        self.objetMonLabel = QtWidgets.QLabel("Vive la formation sur Python 3 : utilisation des boutons radio")
        self.objetMonBoutonRadioEffacer = QtWidgets.QRadioButton ("Effacer")
        self.objetMonBoutonRadioRecopier = QtWidgets.QRadioButton("Recopier")
        self.objetMonLineEdit = QtWidgets.QLineEdit("Entrez le message que vous voulez copier !")
        self.objetMonBoutonEffacer = QtWidgets.QPushButton("Effacer")
        self.objetMonBoutonRecopier = QtWidgets.QPushButton("Recopier")


        # Le placement des widgets
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.objetMonLabel)
        v_box.addWidget(self.objetMonBoutonRadioRecopier)
        v_box.addWidget(self.objetMonBoutonRadioEffacer)
        v_box.addWidget(self.objetMonLineEdit)
        v_box.addWidget(self.objetMonBoutonRecopier)
        v_box.addWidget(self.objetMonBoutonEffacer)

        # Application du maillage
        self.setLayout(v_box)

        # Connexion du bouton entre l'évènement et la fonction... Lambda rend bien des services.
        self.objetMonBoutonRecopier.clicked.connect(lambda :self.fonctionClickRecopier(self.objetMonBoutonRadioRecopier.isChecked()))
        self.objetMonBoutonEffacer.clicked.connect (lambda :self.fonctionClickEffacer(self.objetMonBoutonRadioEffacer.isChecked()))


    def fonctionClickRecopier(self,verfier):
         if verfier:
             QMessageBox.about(self,"Le message copié est :",self.objetMonLineEdit.text())
         else:
             self.objetMonBoutonRecopier.setDisabled(True)
             self.objetMonBoutonEffacer.setDisabled(False)




    def fonctionClickEffacer(self,verifier):
        if verifier:
            buttonReponse = QMessageBox.question(self,"Question ?","Voulez-vous vraiment effacer le message ?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReponse == QMessageBox.Yes:
                self.objetMonLineEdit.clear()
                print('Vous avez cliqué sur Yes !')
            else:
                print('Vous avez cliqué sur No !')
                self.objetMonLineEdit.setText("Vous avez cliqué sur No !")
        else:
            self.objetMonBoutonRecopier.setDisabled(False)
            self.objetMonBoutonEffacer.setDisabled(True)
