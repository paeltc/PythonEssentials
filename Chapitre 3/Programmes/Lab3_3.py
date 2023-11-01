"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab3_3.py


"""
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


################################################
#				Programme principal
################################################

# À lire : https://docs.python.org/3/tutorial/classes.html
# À lire :https://docs.python.org/3/reference/datamodel.html

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

import builtins
#-------------------------------------------------------
#		     Zone de déclaration des classes
#-------------------------------------------------------


# Définition de la classe compte

class compteEnBanque(object):
   """Un exemple de classe :
   gestion d'un compte bancaire...
   Dans cette classe on pourra effectuer toutes les opérations de base
   que l'on puisse faire sur un compte"""

   # Définition de la méthode spéciale __init__ (constructeur)
   def __init__(self,solde_initial):
      """Initialisation du compte avec la valeur soldeInitial. Cette valeur sera à rentrer par l'utilisateur
      lors de l'instanciation de l'objet par défaut qui est le constructeur"""
      # Assignation de l'attribut d'instance solde
      self.solde = float(solde_initial)

   # Définition de la méthode NouveauSolde()
   def nouveauSoldeDuCompte(self,somme):
         """Nouveau solde de compte avec la valeur somme.
            Une méthode possède au moins un paramètre qui s'appelle self.
            Le paramètre self désigne toutes les instances qui seront créées par cette classe."""
         self.solde = float(somme)

   # Définition de la méthode Solde()
   def soldeDucCompte(self):
      """Retourne le solde."""
      return self.solde

   # Définition de la méthode Credit()
   def creditDuCompte(self,somme):
      """Crédite le compte de la valeur somme. Retourne le solde."""
      self.solde += somme
      return self.solde

   # Définition de la méthode Debit()
   def debitDuCompte(self,somme):
      """Débite le compte de la valeur somme. Retourne le solde."""
      self.solde -= somme
      return self.solde

   # Définition de la méthode spéciale __add__ (surcharge de l'opérateur +)
      def __add__(self, somme):
       """x.__add__(somme) <=> x+somme
       Crédite le compte de la valeur somme.
       Affiche 'Nouveau solde : somme'"""
       self.solde += somme
       print("Nouveau solde : {:+.2f} euros".format(self.solde))

   # Définition de la méthode spéciale __sub__ (surcharge de l'opérateur -)
   def __sub__(self, somme):
       """x.__sub_(somme) <=> x-somme
       Débite le compte de la valeur somme.
       Affiche 'Nouveau solde : somme'"""
       self.solde -= somme
       print("Nouveau solde : {:+.2f} euros".format(self.solde))


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



if __name__ == '__main__':
    # Ce bloc d'instructions est exécuté si le module est lancé en tant que programme autonome.
    # Instanciation de l'objet  monObjetCompteEnBanque de la classe compte.
    Mon_Objet_Compte = compteEnBanque(1000)
    # Formatage des données pour afficher deux chiffres après la virgule et le signe.
    print("Votre solde est de %.2f"%(Mon_Objet_Compte.soldeDucCompte()))
    print("Votre solde est de %.2f"%(Mon_Objet_Compte.creditDuCompte(200)))
    print("Votre solde est de %.2f"%(Mon_Objet_Compte.debitDuCompte(50)))
    print("Votre solde est de %.2f"%(Mon_Objet_Compte.soldeDucCompte()))
    Mon_Objet_Compte.nouveauSoldeDuCompte(5000)
    Mon_Objet_Compte + 253.2
    Mon_Objet_Compte - 210
    Mon_Objet_Compte - Mon_Objet_Compte.soldeDucCompte()
    print("\t...ça veut dire que c'est la ruine !\n")

help(Mon_Objet_Compte)
dir (Mon_Objet_Compte)
