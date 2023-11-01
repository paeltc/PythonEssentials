"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab1_5.py
					
				
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

ma_variable_int = 2007
ma_variable_long = 99999999999999999999999999999999999999999999999999999999
ma_variable_float = 2810.1976
ma_variable_string = "un message"
mon_nom = 'RÉANT'
mon_prenom = 'Denis'

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

print ('Bonjour 1')       # Écrit Bonjour dans le mode console entre simples '
print("Bonjour 2")        # Écrit Bonjour dans le mode console entre doubles " et sans espace
print ("Bonjour 3")       # Écrit Bonjour dans le mode console entre doubles " et avec un espace
print ("Bonjour 4\n")     # Écrit Bonjour dans le mode console avec un retour à la ligne
print ("Bonjour 5\n avec un retour\n à la ligne\n")     # Écrit Bonjour dans le mode console avec plusieurs retours à la ligne
print ("\tBon"+"j"+"our 6\n") # Je peux concaténer mes chaînes de caractères

print ("La somme de 4+3 vaut" ,4+3) # Ça fonctionne !

# Déclaration d'une variable à la volée....
somme = 4+5                     # Pas de typage ni de zone de déclaration...
print ("La somme de 4+5 vaut",somme) # Bonus la méthode print ajoute d'elle-même un espace

print ("Que vaut 4/5 ? Cela vaut",4/5) # Naturellement, le résultat est au format à virgule (type float).

# On respecte les priorités de calcul (4/8)+3-(7.87*45)
print ("On peut faire des calculs compliqués ! "+"4/8+3-7.87*45=",4/8+3-7.87*45)

# Utiliser d'autres paramètres
print ("Vive","le","Python","3",sep="_espace_",end='_END')  #pas de retour à la ligne
print (" Vive "+"le "+"Python "+"3 "+"mais çà ne fonctionne pas avec un +",sep="_espace_")

# Utiliser la méthode format
# Le numéro de la première accolade est toujours 0.
print("{0} a eu {1} ans. On a fêté les {1} ans de {0}." .format("Camille", 10))

# Différentes représentations d'un nombre ou d'un caractère
monA=12
monB=35.6
monC="abcd"
monD=7.8251896
print("A=%d, B=%f, D=%.3f, C=%s et Z=%f " %(monA,monB,monD,monC,483))

# On peut rappeler le type des variables dans le print.
print("ma_variable_int est de type :",type(ma_variable_int)," ma_variable_long est de type :",type(ma_variable_long),
      "Et oui le type long n'existe plus depuis la version 3 ! "
	  "ma_variable_float est de type",type(ma_variable_float),"ma_variable_string est de type :",type(ma_variable_string))

# On peut concaténer plusieurs chaînes.
print (mon_nom,mon_prenom)

# Ou peut tout mettre dans une variable à la volée.
# Mais nous n'avons plus l'espace à moins de l'intégrer dans la chaîne.
mon_nom_complet=mon_nom+mon_prenom
print(mon_nom_complet)

# On peut appeler des éléments dans la chaîne.
# Attention, l'élément 1 de la chaîne a le numéro 0.
# On aura toujours un espace entre chaque caractère.
print(mon_nom[0],mon_nom[1],mon_nom[2],mon_nom[3],mon_nom[4])

# On peut partir à l'envers.
print(mon_nom[0],mon_nom[-1],mon_nom[-2],mon_nom[-3],mon_nom[-4])

# On peut extraire une partie de la chaîne de caractères.
print(mon_nom_complet[:5])          # Les 5 premiers caractères de ma chaîne sont extraits.
print(mon_nom_complet[5:])          # Les 5 derniers caractères de ma chaîne sont extraits.
print(mon_nom_complet[2:7])         # Les caractères de 3 (on commence à 0) à 8 sont extraits.


# On peut répéter une chaîne de caractères.
mon_nom_fois_4=mon_nom*4
print(mon_nom_fois_4)

# Juste pour rire
print("Égocentrique ce formateur ! Il met son nom partout !")



