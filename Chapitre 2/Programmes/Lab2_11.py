"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab2_11.py
					
				
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
# tuple pour les tables de multiplication de 2, 7 et 9
# Attention à l'ordre d'affectation !
prenom_1,prenom_2,prenom_3="Yvonne","Patricia","Bruno"
table_2,table_7,table_9,nombre_min, nombre_max,pas=2,7,9,0,11,1
increment=0
#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

# Cependant, il y a certains avantages à implémenter un tuple sur une liste.
#
# Nous utilisons généralement le tuple pour les types de données hétérogènes (différentes) et la liste pour les types de données homogènes (similaires).
# Puisque tuple est immuable, l'itération à travers le tuple est plus rapide qu'avec la liste. Il y a donc une légère amélioration des performances.
# Les tuples qui contiennent des éléments immuables peuvent être utilisés comme clé pour un dictionnaire. Avec liste, ce n'est pas possible.
# Si vous avez des données qui ne changent pas, l'implémenter comme tuple garantira qu'il restera protégé en écriture.

#-------------------------------------------- Exemple N°1 --------------------------------------------------------------

# Un tuple se déclare toujours entre (), contrairement aux listes entre [].
mon_tuple1 = ()
print("Contenu de la mon_tuple1 :",mon_tuple1,"il est vide, ce qui est normal !")
print("Type de classe est :",type(mon_tuple1))
print (help(mon_tuple1))

# -------------------------------------------- Exemple N°2 -------------------------------------------------------------

mon_tuple2 = (1,20,3.14)                         # tuple de nombre entier ou à virgule
mon_tuple3 = ('''a''',"b",'c')                   # tuple de caractères qui peuvent être mis entre",' ou '''
mon_tuple4 = ("une","chaîne","de","caractères")  # Chaque élément est bien un ensemble non dissociable !
print("Contenu de mon_tuple2 :",mon_tuple2)
print("Contenu de mon_tuple3 :",mon_tuple3)
print("Contenu de mon_tuple4 :",mon_tuple4)

# Python est très permissif car il admet les [], voire sans rien.
mon_tuple5 = [1,20,3.14,'a',"Python3"]                               # tuple de contenu varié
mon_tuple6 = 10,200,3.142,'A',"python 3",["A",10000,1976.10]          # tuple de contenu varié

print("Contenu de mon_tuple5 :",mon_tuple5)
print("Contenu de mon_tuple6 :",mon_tuple6)
print("Contenu de l'occurence d'un liste dans un tuple...mon_tuple6[5][2] :",mon_tuple6[5][2])

# -------------------------------------------- Exemple N°3 -------------------------------------------------------------

mon_tuple2 = (1)
print("Le type de mon_tuple2 est :",type(mon_tuple2),"ce n'est pas tuple !") # Renvoi le type du premier élément
mon_tuple2 = (1,2)
print("Le type de mon_tuple2 est :",type(mon_tuple2),"c'est un tuple") # 2 éléments donc de type tuple
mon_tuple2 = ("Python 3")
print("Le type de mon_tuple2 est :",type(mon_tuple2),"ce n'est pas tuple !") # Renvoi le type du premier élément
mon_tuple2 = ("Python 3",)
print("Le type de mon_tuple2 est :",type(mon_tuple2),"c'est un tuple!")

# -------------------------------------------- Exemple N°4 -------------------------------------------------------------
# À quoi servent les tuples
# C'est une liste de constantes
print("Contenu de mon_tuple6[1] en 1ère position :",mon_tuple6[1])
# Tentative de modification
# mon_tuple6[1]=90#.....ERREUR

# Tentative d'effacement d'une occurence
#del mon_tuple6[1].....ERREUR

# Ceci est un tuple implicite ! Python le considère comme ceci.
ma_variable1,ma_variable2,ma_variable3=100,200,300
print("Les valeurs de ma_variable1, ma_variable2, ma_variable3 sont :",ma_variable1,ma_variable2,ma_variable3)

# Ceci donne le même résultat.
mon_tuple7=1000,2000,3000
ma_variable1,ma_variable2,ma_variable3=mon_tuple7
print("Les valeurs de ma_variable1, ma_variable2, ma_variable3 sont :",ma_variable1,ma_variable2,ma_variable3)

# -------------------------------------------- Exemple N°5 -------------------------------------------------------------
# On peut effectuer les mêmes manipulations qu'avec une liste.

print("Le contenu de mon_tuple6[-1] :",mon_tuple6[-1])    # Qui correspond à notre liste
print("Le contenu de mon_tuple6[2:3] :",mon_tuple6[1:3])  # Qui correspond à notre liste l'occurence en positions 2 et 3
print("Le contenu de mon_tuple6[:4] :",mon_tuple6[:4])    # Qui correspond aux 4 premières occurences
print("Le contenu de mon_tuple6[4:] :",mon_tuple6[4:])    # Qui supprime les 4 premières occurences
print("Le contenu de mon_tuple6[5][:1] :",mon_tuple6[5][:1]) # Qui correspond à la 1ère occurence de liste en 6ème position du tuple
print("Somme mon_tuple3+ mon_tuple3",mon_tuple3+mon_tuple3) # Concaténation
print("Produit mon_tuple3*3",mon_tuple3*3)                 # Il faut forcément que le nombre soit un entier, sinon il n'y a pas erreur et pas d'interprétation possible.

# -------------------------------------------- Exemple N°6 -------------------------------------------------------------
# Test de tuples

tuple_prenom = 2007,1950,1957,"Camille","Jacques","François",
print("Méthodes count(), mon_tuple[6] :",tuple_prenom.count(2007))
print("Méthodes index(), mon_tuple[6] :",tuple_prenom.index("Camille"))
print("Test pour savoir si Camille est dans le tuple :",'Camille' in tuple_prenom)
print("Test pour savoir si camille est dans le tuple :",'camille' in tuple_prenom)
print("Test pour savoir si camille n'est pas dans le tuple :",'camille' not in tuple_prenom)
print("Méthodes __len__() tuple_prenom :",tuple_prenom.__len__())      # 3 types d'occurences différentes dans ce tuple
print("Méthodes len() tuple_prenom :",len(tuple_prenom))

# -------------------------------------------- Exemple N°7 -------------------------------------------------------------
# Structure de contrôle
for increment in [prenom_1,prenom_2,prenom_3]:                  # in = balayage des occurences dans les () ou []
    print ("\n","Liste des prénoms :",increment)

for variable_table in [table_2,table_7,table_9]:                # in = balayage des occurences dans les () ou []
    print("Voici la table de :",variable_table,"\n")
    for increment in range (nombre_min,nombre_max,pas) :         # in range (min, max,pas)-> pas de [] que des ()
            print (variable_table,"*",increment,"=",variable_table*increment)







