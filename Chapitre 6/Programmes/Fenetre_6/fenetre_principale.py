"""

Nom du projet : Apprendre le Python 3

Date de la dernière révision :

Auteur(s) : Denis REANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_6 executer.py


"""
# -----------------------------------------------------------------------------
#
#
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'import' de modules
# -----------------------------------------------

# http://zetcode.com/gui/pyqt5/firstprograms/

# ! / usr / bin / python3
# - * - codage: utf-8 - * -





from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QSlider, QLCDNumber


# ----------------------------------------------------
#		Zone de déclarations des variables globales
# ----------------------------------------------------


# -------------------------------------------------------
#		Zone de déclarations des modules ou fonctions
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
        self.objetMonLabel = QtWidgets.QLabel("Vive la formation sur python 3 : utilisation d'une 'messageBox'")
        self.objetMonBoutonEffacer = QtWidgets.QPushButton ("Effacer")
        self.objetMonBoutonRecopier = QtWidgets.QPushButton("Recopier")
        self.objetMonLcd=QtWidgets.QLCDNumber(self)
        self.objetMonLineEdit = QtWidgets.QLineEdit("Entrez le message que vous voulez copier !")
        self.objetMonLabelModifiable= QtWidgets.QLabel("Texte à taille modifiable")
        self.objetMonSlider = QtWidgets.QSlider(Qt.Horizontal)

        # Le placement des widgets
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.objetMonLabel)
        v_box.addWidget(self.objetMonLcd)
        v_box.addWidget(self.objetMonLineEdit)
        v_box.addWidget(self.objetMonBoutonRecopier)
        v_box.addWidget(self.objetMonBoutonEffacer)
        v_box.addWidget(self.objetMonSlider)

        # Caractéristiques du Slider
        self.objetMonSlider.setMinimum(1)
        self.objetMonSlider.setMaximum(20)
        self.objetMonSlider.setTickInterval(20)
        self.objetMonSlider.setTickPosition(QSlider.TicksBothSides)
        self.objetMonSlider.setSingleStep(1)


        # Caractéristiques du LCD
        self.objetMonLcd.setSegmentStyle(QLCDNumber.Flat)


        # Application du maillage
        self.setLayout(v_box)

        # Connexion du bouton entre l'évènement et la fonction
        self.objetMonBoutonRecopier.clicked.connect(self.fonctionClickRecopier)
        self.objetMonBoutonEffacer.clicked.connect (self.fonctionClickEffacer)
        self.objetMonSlider.valueChanged.connect(self.fonctionChangeSlider)

    def fonctionClickRecopier(self):
        QMessageBox.about(self,"Le message copié est :",self.objetMonLineEdit.text())


    def fonctionClickEffacer(self):
        buttonReponse = QMessageBox.question(self,"Question ?","Voulez vous vraiment effacer le message ?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReponse == QMessageBox.Yes:
            self.objetMonLineEdit.clear()
            print('Vous avez cliquez sur Yes !')
        else:
            print('Vous avez cliquez sur No !')
            self.objetMonLineEdit.setText("Vous avez cliquez sur No !")

    def fonctionChangeSlider(self):
        ma_valeur_slider = str(self.objetMonSlider.value())
        print("Valeur donnée par le slider :" + ma_valeur_slider)
        self.objetMonLineEdit.setText("Valeur donnée par le slider :" + ma_valeur_slider)
        self.objetMonSlider.valueChanged.connect(self.objetMonLcd.display)





