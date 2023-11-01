"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_10 fenetre_principale.py


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

import sys
from PyQt5.QtWidgets import QApplication
from fenetre_principale import fenetrePrincipale

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

if __name__ == '__main__':                  # On peut se passer de cette ligne !
                                            # On ne peut pas mettre la visualisation ici car la fenêtre est un objet.
                                            # Encapsuler dans la fonction
    application = QApplication(sys.argv)
    objetfenetre=fenetrePrincipale()
    # Visualisation
    objetfenetre.show()
    applicationExec = application.exec_()
    sys.exit(applicationExec)