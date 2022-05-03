#######################################
#RAFIL Akli Yacine
#JOUAN Maxime
#https://github.com/uvsq22105831/projet_fourmi_de_langton
########################################
import tkinter as tk
import time

LARGEUR =600
HAUTEUR = 600
NOMBRECARRE=100
Cellule =LARGEUR // NOMBRECARRE
direction= (1,0)
LPOS=LARGEUR//Cellule
tempsetape =9999999999
position =(LPOS//2-10,LPOS//2+19)
sol = [[0] * LPOS for _ in range(LPOS)]
dirfourm="bas"
fourmimi =0
premiertour=1
positionavant=0,0
#########################
#fonctions



def deplacement(position,direction, sol):
    """créé le déplacement a partir de la liste sol"""
    i, j = position
    a, b = direction
    if j==NOMBRECARRE:
        j=1
    if j==0:
        j=NOMBRECARRE-1
    if i==0:
        i=NOMBRECARRE-1
    if i==NOMBRECARRE:
        i=1
    aa, bb = (-b, a) if sol[i][j] == 0 else (b, -a)
    return (i + aa, j + bb), (aa, bb)

def dessinefourmi(position, sol):
    """va donner la nouvelle direction et position de la fourmi"""
    global fourmimi,dirfourm,positionavant,premiertour
    (ii, jj), nouvelledir = deplacement(position, direction, sol)
    print(position)
    m, n = position
    if n==NOMBRECARRE:
        position=(m,1)
        n=1
    if n==0:
        position=(m,NOMBRECARRE-1)
        n=NOMBRECARRE-1
    if m==0:
        position=(NOMBRECARRE-1,n)
        m=NOMBRECARRE-1
    if m==NOMBRECARRE:
        position=(1,n)
        m=1
    x, y = m * Cellule, n * Cellule
    colorfourm = sol[m][n]
    print(colorfourm)
    c, d =positionavant
    f,g = c * Cellule, d * Cellule
    colorcarre=sol[c][d]

    can.delete(fourmimi)
    if dirfourm=="bas"and colorfourm==0 or dirfourm =="haut" and colorfourm!=0:
        fourmimi=can.create_rectangle((x+2, y), (x+Cellule-2, y+Cellule-1.5),fill="red",outline='')
        dirfourm="gauche"
    elif dirfourm=="gauche"and colorfourm==0 or dirfourm =="droite" and colorfourm!=0:
        fourmimi=can.create_rectangle((x, y+2), (x+Cellule-1.5, y+Cellule-2),fill="red",outline='')
        dirfourm="haut"
    elif dirfourm=="haut"and colorfourm==0 or dirfourm =="bas" and colorfourm!=0:
        fourmimi=can.create_rectangle((x+2, y), (x+Cellule-2, y+Cellule-1.5),fill="red",outline='')
        dirfourm="droite"
    elif dirfourm=="droite"and colorfourm==0 or dirfourm =="gauche" and colorfourm!=0:
        fourmimi=can.create_rectangle((x+1.5, y+2), (x +Cellule, y+Cellule-2),fill="red",outline='')
        dirfourm= "bas"

    if premiertour ==0:
        if colorcarre == 0:
            colorcarre = creesol(c, d)
            sol[c][d] = colorcarre
        else:
            can.delete(colorcarre)
            sol[c][d] = 0
    else:
        premiertour=0
    positionavant=position
    return (ii, jj), nouvelledir

def creesol(c, d):
    f, g = c * Cellule, d * Cellule
    colorcarre = can.create_rectangle((f, g), (f +Cellule , g + Cellule),fill="black",outline='')
    return colorcarre

def etape():
    global position, direction
    position, direction = dessinefourmi(position, sol)
    fourmi.after(tempsetape, etape)



def fonctionboutplay():
    pause()
    changebout()

def pause():
    global tempsetape
    if tempsetape == 9999999999:
        tempsetape =510
        fourmi.after(tempsetape, etape)
    else:
        tempsetape =9999999999

def changebout():
    if bouton_play['text'] =="pause":
        bouton_play['text']="play"
    else:
        bouton_play['text']="pause"


def accelletemps():
    global tempsetape
    if tempsetape > 11:
        tempsetape-=50

def ralentemps():
    global tempsetape
    tempsetape+=50


def effectetape():
    global position, direction
    position = dessinefourmi(position, sol)

def sauvegarde():
    fic = open("sauvegarde.txt","w")
    fic.write(str(NOMBRECARRE)+"\n")
    for i in range(NOMBRECARRE):
        for j in range(NOMBRECARRE):
            fic.write(str(sol[i][j])+"\n")
    fic.close()

def charge():
    global NOMBRECARRE
    fic = open("sauvegarde.txt", "r")
    ligne = fic.readline()
    NOMBRECARRE = int(ligne)
    i = j = 0
    for ligne in fic:
        n = int(ligne)
        sol[i][j] = n
        colorcarre = n
        if colorcarre!=0: 
            colorcarre = creesol(i, j)
            sol[i][j] = colorcarre
        else :
            can.delete(colorcarre)
            sol[i][j] = 0
        j += 1
        if j == NOMBRECARRE:
            j = 0
            i += 1
    fic.close()
    
##########################################
#programme principal
fourmi = tk.Tk()
fourmi.title("fourmi de Langton")

#création du canevas
can = tk.Canvas(fourmi, width= LARGEUR, height=HAUTEUR)

#création des boutons
bouton_play = tk.Button(fourmi,text="play",command= fonctionboutplay)
bouton_etape =tk.Button(fourmi,text="étape",command=effectetape)
bouton_tmsplus=tk.Button(fourmi,text="accélérer le temps",command=accelletemps)
bouton_tmsmoins=tk.Button(fourmi,text="ralentir le temps",command=ralentemps)
bouton_sauv=tk.Button(fourmi,text="sauvegarder",command=sauvegarde)
bouton_charge=tk.Button(fourmi,text="charger",command=charge)

#placement du canevas
can.grid(column=0, row=0, rowspan=10,columnspan=3)

#placements des boutons
bouton_play.grid(column=3,row=2)
bouton_etape.grid(column=3,row=4)
bouton_tmsplus.grid(column=3,row=6)
bouton_tmsmoins.grid(column=3,row=8)
bouton_sauv.grid(column=1,row=11)
bouton_charge.grid(column=2,row=11)

##################################
#déroulement principal
etape()

fourmi.mainloop()
