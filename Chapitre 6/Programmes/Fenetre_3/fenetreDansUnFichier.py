"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Dossier Fenetre_3


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
from PyQt5.QtWidgets import QApplication

# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------



# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------



def fonctionFenetre():
    fenetre = QtWidgets.QWidget()
    fenetre.setGeometry(200, 200, 500, 300)     # setGeometry ( int x (point de départ de la fenêtre)
                                                #  , int y (point de départ de la fenêtre) , int w , int h ) en pixels
    fenetre.setWindowTitle("Ma 2ème fenêtre sous PyQt5 !")
    fenetre.setWindowIcon(QIcon('icon.ico'))

    # Les widgets
    objetMonLabel = QtWidgets.QLabel('Vive la formation sur Python 3')
    objetMonbouton = QtWidgets.QPushButton ("Cliquez-moi")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(objetMonLabel)     # On peut intervertir le bouton et le label pour voir la différence.
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(objetMonbouton)
    v_box.addStretch()

    v_box.addLayout(h_box)

    fenetre.setLayout(v_box)

    # Visualisation
    fenetre.show()
    applicationExec = application.exec_()
    sys.exit(applicationExec)


# -------------------------------------------------------
#		            Programme principal
# -------------------------------------------------------


if __name__ == '__main__':                  # On peut se passer de cette ligne !
                                            # On ne peut pas mettre la visualisation ici car la fenêtre est un objet.
                                            # Encapsuler dans la fonction
    application = QApplication(sys.argv)
    fonctionFenetre()



