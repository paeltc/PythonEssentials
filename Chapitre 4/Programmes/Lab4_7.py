"""

Nom du projet : Apprendre le langage Python 3

Date de la dernière révision :

Auteur(s) : Denis RÉANT

Révision N° : Version 1

Client : e-learning

Fichiers du projet :
					-	Lab4_7.py


"""

################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

from random import randint  # entier aléatoire
from tkinter import *

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------

ton_score = 0
mon_score = 0

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

def augmenter_scores(mon_coup,ton_coup):
    global mon_score, ton_score
    if mon_coup == 1 and ton_coup == 2:
        ton_score += 1
    elif mon_coup == 2 and ton_coup == 1:
        mon_score += 1
    elif mon_coup == 1 and ton_coup == 3:
        mon_score += 1
    elif mon_coup == 3 and ton_coup == 1:
        ton_score += 1
    elif mon_coup == 3 and ton_coup == 2:
        mon_score += 1
    elif mon_coup == 2 and ton_coup == 3:
        ton_score += 1

def jouer(ton_coup):
    global mon_score, ton_score, score1, score2
    mon_coup = randint(1,3)
    if mon_coup==1:
        lab3.configure(image=pierre)
    elif mon_coup==2:
        lab3.configure(image=feuille)
    else:
        lab3.configure(image=ciseaux)
    augmenter_scores(mon_coup,ton_coup)
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))

def jouer_pierre():
    jouer(1)
    lab1.configure(image=pierre)

def jouer_feuille():
    jouer(2)
    lab1.configure(image=feuille)

def jouer_ciseaux():
    jouer(3)
    lab1.configure(image=ciseaux)

def reinit():
    global mon_score,ton_score,score1,score2,lab1,lab3
    ton_score = 0
    mon_score = 0
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    lab1.configure(image=rien)
    lab3.configure(image=rien)

# On peut déclarer et écrire les fonctions (ou modules) avant, pendant ou après le programme principal.

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------


# Fenêtre graphique
fenetre = Tk()
fenetre.title("Pierre, feuille, ciseaux")


# Images
rien = PhotoImage(file ='nulle.gif')
versus = PhotoImage(file ='fight.gif')
pierre = PhotoImage(file ='pierre.gif')
feuille = PhotoImage(file ='feuille.gif')
ciseaux = PhotoImage(file ='ciseaux.gif')

# Label
texte1 = Label(fenetre, text="Humain :", font=("Arial", 20, "bold"))
texte1.grid(row=0,column=0)

texte2 = Label(fenetre, text="Machine :", font=("Arial", 20, "bold"))
texte2.grid(row=0,column=2)

texte3 = Label(fenetre, text="Pour jouer, cliquez sur une des icônes ci-dessous.",font=("Arial", 20, "bold"))
texte3.grid(row=3, columnspan =3, pady =5)

score1 = Label(fenetre, text="0", font=("Arial", 20, "bold"))
score1.grid(row=1, column=0)

score2 = Label(fenetre, text="0", font=("Arial", 20, "bold"))
score2.grid(row=1, column=2)

lab1 = Label(fenetre, image=rien)
lab1.grid(row =2, column =0)

lab2 = Label(fenetre, image=versus)
lab2.grid(row =2, column =1)

lab3 = Label(fenetre, image=rien)
lab3.grid(row =2, column =2)

# Boutons
bouton1 = Button(fenetre,command=jouer_pierre)
bouton1.configure(image=pierre)
bouton1.grid(row =4, column =0)

bouton2 = Button(fenetre,command=jouer_feuille)
bouton2.configure(image=feuille)
bouton2.grid(row =4, column =1,)

bouton3 = Button(fenetre,command=jouer_ciseaux)
bouton3.configure(image=ciseaux)
bouton3.grid(row =4, column =2)

bouton4 = Button(fenetre,text='Recommencer',command=reinit,font=("Arial", 20, "bold"))
bouton4.grid(row =5, column =0, pady =10, sticky=E)

bouton5 = Button(fenetre,text='Quitter',command=quit,font=("Arial", 20, "bold"))
bouton5.grid(row =5, column =2, pady =10, sticky=W)

# Démarrage :
fenetre.mainloop()