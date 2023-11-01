"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_11 executer.py


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

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# Les widgets utilisés pour créer l'interface graphique agissent comme la source de tels évènements. Chaque widget PyQt, 
# dérivé de la classe QObject, est conçu pour émettre un signal en réponse à un ou plusieurs évènements.
# Le signal en lui-même n'effectue aucune action. Au lieu de cela, il est « connecté » à un « slot ». 
# Le slot peut être n'importe quelle fonction Python appelable.
# En PyQt, la connexion entre un signal et un slot peut être réalisée de différentes manières.
# Voici les techniques les plus couramment utilisées -
#
# QtCore.QObject.connect(widget, QtCore.SIGNAL(‘signalname’), slot_function)
#
# Un moyen plus pratique d'appeler une fonction de slot, quand un signal est émis par un widget est la suivante :
#
# widget.signal.connect(slot_function)

class fenetrePrincipale(QDialog):
    def __init__(self):
        super(fenetrePrincipale, self).__init__()
        loadUi('fenetre_11.ui',self)
        self.pushButtonValider.clicked.connect(self.click_push_button_valider)

    @pyqtSlot()
    def click_push_button_valider(self):
        self.labelReponse.setText("Bienvenue dans cette formation Python 3 : "+
                                  self.lineEditPrenom.text()+" "+self.lineEditNom.text())
