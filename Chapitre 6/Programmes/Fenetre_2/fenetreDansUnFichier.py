"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Dossier Fenetre_2

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
from PyQt5 import QtWidgets, QtGui
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
    objetMonLabel = QtWidgets.QLabel(fenetre)
    objetMonLabel.setText("Vive Python 3")
    objetMonLabel.move(200,20)

    objetMonLabel2=QtWidgets.QLabel(fenetre)
    objetMonLabel2.setPixmap(QtGui.QPixmap("icon.jpg"))
    objetMonLabel2.move(130,50)

    objetMonbouton = QtWidgets.QPushButton (fenetre)
    objetMonbouton.setText("Cliquez moi")           # La taille du bouton est réglée en fonction du texte.
    #objetMonbouton.move(400,250)                   # Placer dans la fenêtre.
    objetMonbouton.setGeometry(380,250,100,30)      # On fait les deux à la fois.

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



