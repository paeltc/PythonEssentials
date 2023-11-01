"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_12.py
					
				
"""

################################################
#				Programme principal
################################################

#-----------------------------------------------
#		    Zone des 'imports' de modules
#-----------------------------------------------



#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------


#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Un dictionnaire en Python est une sorte de liste mais au lieu d'utiliser des index, on utilise des clés, c'est-à-dire des valeurs autres que numériques.

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Un dictionnaire se déclare toujours entre {}, contrairement aux listes entre [].
mon_dictionnaire = {}
print("Contenu de mon_dictionnaire :",mon_dictionnaire,"il est vide, ce qui est normal !")
print("Type de classe est :",type(mon_dictionnaire))
print(help(mon_dictionnaire))

# -------------------------------------------- Exemple N°2 -------------------------------------------------------------

mon_carnet = {}                                 # Création d'un dictionnaire
# Création des clés... Ici Prénom, Nom, Âge
mon_carnet["Prénom"] = ("Stéphanie","Camille","Yvonne","Raymonde","Alia")
mon_carnet["Nom"] = ("RÉANT","FamilleY")
mon_carnet["Âge"] = (40,10,66,61,85)

print("Contenu de mon_carnet :",mon_carnet)
print("Contenu de mon_carnet['Prénom'] :",mon_carnet["Prénom"])
print("Contenu de mon_carnet['Nom'] :",mon_carnet["Nom"])
print("Contenu de mon_carnet['Âge'] :",mon_carnet["Âge"])

# Une autre façon de déclarer un dictionnaire à une occurence par clé
mon_carnet2={'Prénom' : 'Denis', 'Nom' : 'RÉANT', 'Âge': 41}
mon_carnet3=dict(zip(['Prénom','Nom', 'Âge'], ['Denis', 'RÉANT',41]))
mon_carnet4=dict([('Prénom','Denis'), ('Nom','RÉANT'), ('Âge',41)])
mon_carnet5=dict({'Prénom' : 'Denis', 'Nom' : 'RÉANT', 'Âge': 41})
print("mon_carnet2=mon_carnet3=mon_carnet4=mon_carnet5 donne :",mon_carnet2==mon_carnet3==mon_carnet4==mon_carnet5)

# Utiliser un tuple comme clé... Cela permet de jouer avec l'utilisation des coordonnées, notamment pour des jeux.
position_X1,position_X2=10,100
position_Y1,position_Y2=20, 200
coordonnees={}
coordonnees[(position_X1,position_Y1)]= "rempart"
coordonnees[(position_X2,position_Y2)]= "ennemi"
print(coordonnees)
print("Que se passe t'il en X1,Y1 et en X2,Y2",coordonnees.keys(),"il y a un",coordonnees[position_X1,position_Y1],"et un",coordonnees[position_X2,position_Y2])

# -------------------------------------------- Exemple N°3 -------------------------------------------------------------

# Allez voir du côté de https://docs.python.org/2/library/stdtypes.html#dictionary-view-objects
# exemple has_key n'est plus utilisé !

# Ajouter une valeur au dictionnaire... Pas possible directement.
mon_carnet["Prénom"] = ("Denis","Jacques") # On écrase les occurences de la clé "Prénom".
print("Contenu de mon_carnet['Prénom'] :",mon_carnet["Prénom"])

# Récupérer une valeur dans un dictionnaire
mon_carnet["Prénom"] = ("Stéphanie","Camille","Yvonne","Raymonde","Alia")
print("Contenu mon_carnet.get('Prénom') :",mon_carnet.get('Prénom'))

# Effacer une clé d'un dictionnaire
del mon_carnet["Âge"]
print("Contenu de mon_carnet :",mon_carnet)

# Efface la clé et renvoi la valeur de l'occurence effacée... Attention, la clé ne doit avoir qu'une occurence.
# mon_carnet ne fonctionne pas !

print("Supprime la clé et renvoie l'occurence associée mon_carnet2.pop() :",mon_carnet2.pop("Âge"))

# Longueur d'un dictionnaire
print("Le nombre de clés dans mon_carnet, len(mon_carnet) :",len(mon_carnet))

# Liste des clés dans le dictionnaire
print("Le nombre de clés dans mon_carnet, mon_carnet.keys() :",mon_carnet.keys())

# Liste des occurences dans le dictionnaire
print("Le nombre d'occurences dans mon_carnet, mon_carnet.values() :",mon_carnet.values())

# Insérer une clé d'un dictionnaire... Il suffit de rappeller le clé et ses occurences.
mon_carnet["Âge"] = (40, 10, 66, 61, 85)



# -------------------------------------------- Exemple N°4 -------------------------------------------------------------

# Récupérer les clés par une boucle
for cle in mon_carnet.keys():
    print("Voici l'ensemble des clés de mon_carnet :",cle)

# Récupérer les valeurs par une boucle
for occurences in mon_carnet.values():
    print("Voici l'ensemble des occurences de mon_carnet :",occurences)

# Tester si une clé existe dans le dictionnaire
if "Nom" in mon_carnet.keys():
    print("Cette clé fait partie du dictionnaire ! C'est Nom")
else:
    print("Cette clé ne fait pas partie du dictionnaire !")

# Récapituler les clés et les occurences qui sont à l'intérieur
for cle,occurence in mon_carnet.items():
    print("La clé {} contient la valeur {}.".format(cle, occurence))


