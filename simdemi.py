
from tkinter import *
from random import randrange
import random
haut = 150
larg = 150
cote = 7.5 
vivant = 1
mort = 0
compta = 2
bleu = 3
comptat = 4
pourcompta = 20
pourcdeath = 3
pourcheal = 50
pourcres = 14
global jour
jour = 0
global t
t = 0
global it
it = 0
global an
an = 0
global main
man = 0
xp = 0
global comp
comp = 0
# Créer les matrices
cell = [[0 for row in range(haut)] for col in range(larg)]
matrice = [[mort for row in range(haut)] for col in range(larg)]
temp = [[mort for row in range(haut)] for col in range(larg)]
# Calculer et dessiner le prochain tableau
def tableau():
    global jour
    global t
    global it
    global an
    global xp
    global man
    main()
    aff()
    if t != 0:
        jour = jour + 14
        it = it + 1
        if it == 26:
            xp = xp + man
            man =  t - xp 
            an = an +1
            it = 0
    print("nombre de jour: "+str(jour)+ " nombre de mort: " +str(t)+ " Année numeros: "+str(an)+" nombre de mort l'annéee d'avant: "+str(man)+" Nombre d'infecter : ", comp)
    fenetre.after(100, tableau)

def init():
    global pourcompta
    global pourcdeath
    global pourcheal
    global pourcres
    for y in range(haut):
        for x in range(larg):
            matrice[x][y] = vivant
            temp[x][y] = vivant
            cell[x][y] = canvas.create_rectangle((x*cote, y*cote,
                (x+1)*cote, (y+1)*cote), outline="gray", fill="white")
    matrice[35] [35] = compta
    matrice[35+1] [35] = compta
    matrice[35] [35+1] = compta
    matrice[35+1] [35+1] = compta
    choice  = int(input("Chargez des données perso(0), chargez données de base du corona (1)"))
    if choice == 0:
        pourcompta = int(input("chance de comptamination par cellule (1/?) "))
        pourcdeath = int(input("chance de mourrir par cellule infecte (1/?)"))
        pourcheal = int(input("chance d'etre soigne par cellule infecte (1/?)"))
        pourcres = int(input("chance de devenir resistant par cellule soigner (1/?)"))
def main():
    global t
    global comp
    for y in range(haut):
        for x in range(larg):
            nb_voisins = malade(x,y)
            
            if matrice[x][y] == vivant and nb_voisins > 0:
                nb = nb_voisins
                while nb != 0:
                    rand = random.randint(1,100)
                    if rand < pourcompta:
                        temp[x][y] = compta
                        comp = comp + 1
                    nb -= 1
            if matrice[x][y] == bleu and nb_voisins > 0:
                nb = nb_voisins
                while nb != 0:
                    rand = random.randint(1,200)
                    if rand < pourcompta:
                        temp[x][y] = comptat
                    nb -= 1
            if matrice[x][y] == compta  or matrice[x][y] == comptat :
                ra = random.randint(1,100)
                if ra < pourcheal:
                    rand = random.randint(1,100)
                    if rand < pourcres or matrice[x][y] == comptat:
                        temp[x][y] = bleu
                    else:
                        temp[x][y] = vivant
                if ra < pourcdeath:
                    temp[x][y] = mort
                    t += 1
            #if matrice[x][y] == vivant:
             ##   rand = random.randint(1,1000000)
            #    if rand == 5:
              #      temp[x][y] = compta
            #if matrice[x][y] == mort:
             #   rand = random.randint(1,10)
              #  if rand == 2:
               #     temp[x][y] = vivant
    for y in range(haut):
        for x in range(larg):
            matrice[x][y] = temp[x][y]

# Compter les voisins vivants - tableau torique
def malade(a,b):
    nb_voisins = 0
    if matrice[(a-1)%larg][(b+1)%haut] == 2:
        nb_voisins += 1
    if matrice[a][(b+1)%haut] == 2:
        nb_voisins += 1
    if matrice[(a+1)%larg][(b+1)%haut] == 2:
        nb_voisins += 1
    if matrice[(a-1)%larg][b] == 2:
        nb_voisins += 1
    if matrice[(a+1)%larg][b] == 2:
        nb_voisins += 1
    if matrice[(a-1)%larg][(b-1)%haut] == 2:
        nb_voisins += 1
    if matrice[a][(b-1)%haut] == 2:
        nb_voisins += 1
    if matrice[(a+1)%larg][(b-1)%haut] == 2:
        nb_voisins += 1
    return nb_voisins
def aff():
    red = 0
    for y in range(haut):
        for x in range(larg):
            if matrice[x][y] == 0:
                coul = "black"
            elif matrice [x][y] == 1:
                coul = "green"
            elif matrice [x][y] == 3:
                coul = "blue"
            elif matrice [x][y] == 2:
                coul = "red" 
                red += 1
            elif matrice [x][y] == 4:
                coul = "red" 
                red += 1
            canvas.itemconfig(cell[x][y], fill=coul)
fenetre = Tk()
fenetre.title("Simdemie")
canvas = Canvas(fenetre, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas.pack()
init()
tableau()
fenetre.mainloop()
