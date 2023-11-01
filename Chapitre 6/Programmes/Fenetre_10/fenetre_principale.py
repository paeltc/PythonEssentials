"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-   Dossier Fenetre_10 executer.py


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



from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox,QMainWindow, QAction


# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------


# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------



class fenetrePrincipale (QMainWindow):          # QMainWindow

    def __init__(self):
        super(fenetrePrincipale,self).__init__()
        self.initialisationInterface()

    def initialisationInterface(self):

        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("Ma 2ème fenêtre sous PyQt5 !")
        self.setWindowIcon(QIcon('icon.ico'))


        # Les widgets
        objetMonBarreMenu = self.menuBar()   # QMainWindow en héritage... Plus besoin du self pour l'objet et QtWidgets...

        # Éléments de la barre de menu
        objetFichier = objetMonBarreMenu.addMenu("Fichier")
        objetEditer = objetMonBarreMenu.addMenu("Éditer")
        objetAide = objetMonBarreMenu.addMenu("Aide")

        # Actions pour le menu Fichier
        ActionNouveau=QAction("Nouveau",self)
        ActionNouveau.setShortcut("Ctrl+N")

        ActionSauver = QAction("Sauvegarder",self)
        ActionSauver.setShortcut("Ctrl+S")

        ActionQuitter = QAction("Quitter",self)
        ActionQuitter.setShortcut("Ctrl+Q")

        # Actions pour le menu Éditer
        ActionCopier=QAction("Copier",self)
        ActionCopier.setShortcut("Ctrl+C")

        ActionColler = QAction("Coller",self)
        ActionColler.setShortcut("Ctrl+V")

        # Actions pour le menu Aide
        ActionOS = QAction("Aide compatibilité du système opérationnel",self)
        ActionOS.setShortcut("Ctrl+A")

        ActionAide = QAction("À propos de....",self)
        ActionEnvoyerMail =QAction("Envoyer un e-mail",self)

        # Ajouter les actions au menu
        objetFichier.addAction(ActionNouveau)
        objetFichier.addAction(ActionSauver)
        objetFichier.addAction(ActionQuitter)

        objetEditer.addAction(ActionCopier)
        objetEditer.addAction(ActionColler)

        objetAide.addAction(ActionOS)
        objetMenuAide=objetAide.addMenu ("Contacts")
        objetMenuAide.addAction(ActionAide)
        objetMenuAide.addAction(ActionEnvoyerMail)

        # Évènements
        ActionQuitter.triggered.connect(self.fonctionQuitter)
        ActionNouveau.triggered.connect(self.fonctionNouveau)
        ActionAide.triggered.connect(self.fonctionAProposDe)

    # Les fonctions liées aux fonctions

    def fonctionQuitter(self):
        quit()

    def fonctionNouveau(self):
        QMessageBox.about(self,"Menu Fichier","Vous pourriez créer un nouveau fichier !")

    def fonctionAProposDe(self):
        QMessageBox.about(self,"Sous-menu à propos de...","Fichier exercice de Denis RÉANT")

