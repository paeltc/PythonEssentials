"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_21.py
					-	Lab2_22.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------

import math
from Lab3_21 import geometrie
from Lab3_22 import Tva

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.



#------------------------------------------------------
#		   		Programme principal
#------------------------------------------------------

if __name__ == '__main__':                  # On peut se passer de cette ligne !
	
	# Vient de la classe geometrie
	geometrie.carreCube(5)
	geometrie.cercleCylindre (2,3)
	
	# Vient de la classe tva
	Tva.CalculTva (100,20)