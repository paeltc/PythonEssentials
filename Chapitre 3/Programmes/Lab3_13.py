"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_13.py


"""


################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

from xlwt import Workbook
import xlrd

compteur_de_passage = 1
reponse = 0

# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------


# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.




# -------------------------------------------------------
#						PROGRAMME
# -------------------------------------------------------


# -------------------------------------------- Exemple N°1 --------------------------------------------------------------

# # création
# fichierCSV = Workbook()
#
# # création de la feuille 1
# feuil1 = fichierCSV.add_sheet('feuille 1')
#
# # ajout des en-têtes
# feuil1.write(0, 0, 'Identifiant sécurité sociale')
# feuil1.write(0, 1, 'Nom')
# feuil1.write(0, 2, 'Prenom')
# feuil1.write(0, 3, 'Age')
# feuil1.write(0, 4, 'Mutuelle')
#
# # ajout des valeurs dans la ligne suivante
# ligne1 = feuil1.row(1)
# ligne1.write(0, '1 76 10 xx xxx xxx xx')
# ligne1.write(1, 'REANT')
# ligne1.write(2, 'Denis')
# ligne1.write(3, 41)
# ligne1.write(4, 'Mutuelle A')
#
# # ajustement éventuel de la largeur d'une colonne
# feuil1.col(0).width = 7000
# feuil1.col(1).width = 7000
# feuil1.col(2).width = 7000
# feuil1.col(3).width = 2000
# feuil1.col(4).width = 7000
#
#
# while reponse is not "S":
#     compteur_de_passage=compteur_de_passage+1
#     print(compteur_de_passage)
#     reponse = input("Est-ce la dernière personne ? 'S' pour STOP, une autre touche pour continuer !")
#     numero_matricule=input("Entrez le numéro de matricule")
#     nom=input("Entrez le nom.")
#     prenom=input("Entrez le prénom.")
#     age=int(input("Entrez l'âge."))
#     mutuelle=input("Entrez la mutuelle.")
#     ligne_compteur_de_passage = feuil1.row(compteur_de_passage)
#     ligne_compteur_de_passage.write(0,numero_matricule)
#     ligne_compteur_de_passage.write(1,nom)
#     ligne_compteur_de_passage.write(2,prenom)
#     ligne_compteur_de_passage.write(3,age)
#     ligne_compteur_de_passage.write(4,mutuelle)
#
# # éventuellement ajout d'une autre feuille 2
# feuil2 = fichierCSV.add_sheet('feuille 2')
#
# # création matérielle du fichier résultant
# fichierCSV.save('Fichier_excel.xls')

#-------------------------------------------- Exemple N°2 --------------------------------------------------------------

# ouverture du fichier Excel
porte_folio = xlrd.open_workbook('Fichier_excel.xls')

# feuilles dans le classeur
print (porte_folio.sheet_names())


# lecture des données dans la première feuille
feuille = porte_folio.sheet_by_name(u'feuille 1')
for rownum in range(feuille.nrows):
    print (feuille.row_values(rownum))

# lecture par colonne
colonne1 = feuille.col_values(0)
print (colonne1)

colonne2 = feuille.col_values(1)
print (colonne2)

# extraction d'un élément particulier
print (colonne1[1], colonne2[1])
