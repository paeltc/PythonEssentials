"""

Nom du projet : Apprendre le Python 3

Date de la dernière révision :

Auteur(s) : Denis REANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_4 fenetre_principale.py


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

import sys
from PyQt5.QtWidgets import QApplication
from fenetre_principale import fenetrePrincipale

#----------------------------------------------------
#		Zone de déclarations des variables globales
#----------------------------------------------------



#-------------------------------------------------------
#		Zone de déclarations des modules ou fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

if __name__ == '__main__':                  # On peut se passer de cette ligne !
                                            # On ne peut mettre la visualisation ici car fenetre est un objet
                                            # Encapsuler dans la fonction
    application = QApplication(sys.argv)
    objetfenetre=fenetrePrincipale()
    # Visualisation
    objetfenetre.show()
    applicationExec = application.exec_()
    sys.exit(applicationExec)