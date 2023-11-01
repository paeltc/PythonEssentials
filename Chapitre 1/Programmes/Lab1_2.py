##############################
#    LAB 1_2 - Les variables   #
##############################

# On respecte cette notation pour une bonne pratique ma_variable_est
variable_1 = 10

# Attention les noms sont sensibles à la casse, variable_1 est différent de VARIABLE_1
Variable_1 = 20

# On évitera de mettre une majuscule au nom de la variable.
variable_1+Variable_1

# Pas besoin de déclarer le type de la variable, de plus, on peut la déclarer à la volée mais il faut
# qu'elle soit déclarée en premier.
# Ceci ne fonctionne pas.
Variable_1 = variable_2

# Ceci ne fonctionne pas. L'affectation se fait de la gauche vers la droite.
variable_2 = Variable_1 

# Encore une autre variable
somme=variable_1+variable_2

# On ajoute une valeur.
somme_2 = somme + 55/2.0

#--------------------------------------------------------
# Pour aller plus vite, on peut utiliser des abréviations :
#--------------------------------------------------------

# On ajoute 10 à somme.
somme=somme+10
# On ajoute 10 à somme.
somme+=10

# On soustrait.
somme-=10

# On multiplie la variable somme.
somme=somme*10 
# On multiplie encore par 10.
somme*=10

# On divise par 10 la variable somme.
somme = somme/10
# On divise encore par 10.
somme/=10

# Effectuer une permutation
ma_variable_1 = 10
ma_variable_2 = 20
ma_variable_1
ma_variable_2
ma_variable_1,ma_variable_2=ma_variable_2,ma_variable_1
ma_variable_1
ma_variable_2

#---------------------------------------------------------------------
# Les noms des variables que vous ne pouvez pas utiliser (33 en tout) :
#---------------------------------------------------------------------
# and del from none true as elif global nonlocal try assert
# else if not while break except import or with class false in
# pass yield continue finally is raise def for lambda return

#-------------------
# Type de variable :
#-------------------

# Le type int, c'est-à-dire entier, donc sans virgule
type (somme)
# Le type float, c'est-à-dire avec une virgule
type (somme_2)
# Le type chaîne de caractères
ma_chaine_de_caratère_1= "Bonjour à tous et bienvenue dans cette formation sur Python 3"
type (ma_chaine_de_caratère_1)

#-----------------------------------------------------
# Différentes façons d'afficher une chaîne de caractères
#-----------------------------------------------------

ma_chaine_de_caratère_2= 'Encore bonjour à tous entre simples apostrophes'
ma_chaine_de_caratère_3= '''Bonjour entre triples apostrophes'''
ma_chaine_de_caratère_4= """Bonjour entre triples guillemets"""

# Problème d'apostrophe dans la chaîne de caractères
ma_chaine_de_caratère_5= 'J'aime le e-learning !'
# Si on utilise les apostrophes, on ajoute un anti-slash.
ma_chaine_de_caratère_6= 'J\'aime le e-learning !'
# On n'a jamais de problème avec les guillemets.
ma_chaine_de_caratère_7= "J'aime le e-learning !"

