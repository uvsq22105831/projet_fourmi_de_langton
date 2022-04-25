#######################################
#RAFIL Akli Yacine
#JOUAN Maxime
#https://github.com/uvsq22105831/projet_fourmi_de_langton
########################################
import tkinter as tk
import time

LARGEUR =500
HAUTEUR = 500
NOMBRECARRE=60
Cellule =LARGEUR // NOMBRECARRE
direction= (1,0)
LPOS=LARGEUR//Cellule
tempsetape =9999999999
position =(LPOS//2-10,LPOS//2+19)
sol = [[0] * LPOS for _ in range(LPOS)]
dirfourm="bas"
fourmimi =0

#########################
#fonctions



def deplacement(position,direction, sol):
    """créé le déplacement a partir de la liste sol"""
    i, j = position
    a, b = direction
    aa, bb = (-b, a) if sol[i][j] == 0 else (b, -a)
    return (i + aa, j + bb), (aa, bb)

def dessine(position, direction, sol):
    """va donner la nouvelle direction et position de la fourmi"""
    global fourmimi,dirfourm
    (ii, jj), nouvelledir = deplacement(position, direction, sol)
    i, j = position
    x, y = i * Cellule, j * Cellule
    colorcarre = sol[i][j]

    if colorcarre == 0:
        if dirfourm=="bas":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x, (y+Cellule)), (x+Cellule, (y+2*Cellule)),fill="red",outline='')
            dirfourm="gauche"
        elif dirfourm=="gauche":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x, y), (x-Cellule, y+Cellule),fill="red",outline='')
            dirfourm="haut"
        elif dirfourm=="haut":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x, y), (x +Cellule, y-Cellule),fill="red",outline='')
            dirfourm="droite"
        elif dirfourm=="droite":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x+Cellule, y), (x +2*Cellule, y+Cellule),fill="red",outline='')
            dirfourm= "bas"
        colorcarre = creesol(i, j)
        sol[i][j] = colorcarre
    else:
        if dirfourm=="bas":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x, y), (x +Cellule, y-Cellule),fill="red",outline='')
            dirfourm="droite"
        elif dirfourm=="gauche":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x+Cellule, y), (x +2*Cellule, y +Cellule),fill="red",outline='')
            dirfourm= "bas"
        elif dirfourm=="haut":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x, y+Cellule), (x +Cellule, y+2*Cellule),fill="red",outline='')
            dirfourm="gauche"
        elif dirfourm=="droite":
            can.delete(fourmimi)
            fourmimi=can.create_rectangle((x, y), (x-Cellule, y+Cellule),fill="red",outline='')
            dirfourm="haut"
        can.delete(colorcarre)
        sol[i][j] = 0

    return (ii, jj), nouvelledir

def creesol(i, j):
    x, y = i * Cellule, j * Cellule
    colorcarre = can.create_rectangle((x, y), (x +Cellule , y + Cellule),fill="black",outline='')
    return colorcarre

def etape():
    global position, direction
    position, direction = dessine(position, direction, sol)
    fourmi.after(tempsetape, etape)

def fonctionboutplay():
    pause()
    changebout()

def pause():
    global tempsetape
    if tempsetape == 9999999999:
        tempsetape =1000
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
    if tempsetape > 51:
        tempsetape-=50

def ralentemps():
    global tempsetape
    tempsetape+=50


def effectetape():
    global position, direction
    position, direction = dessine(position, direction, sol)

##########################################
#programme principal
fourmi = tk.Tk()
fourmi.title("fourmi de Langton")
can = tk.Canvas(fourmi, width= LARGEUR, height=HAUTEUR,bd=100)
bouton_play = tk.Button(fourmi,text="play",command= fonctionboutplay)
bouton_etape =tk.Button(fourmi,text="étape",command=effectetape)
bouton_tmsplus=tk.Button(fourmi,text="accélérer le temps",command=accelletemps)
bouton_tmsmoins=tk.Button(fourmi,text="ralentir le temps",command=ralentemps)
can.grid(column=1, row=0, rowspan=10)
bouton_play.grid(column=2,row=2)
bouton_etape.grid(column=2,row=4)
bouton_tmsplus.grid(column=2,row=6)
bouton_tmsmoins.grid(column=2,row=8)
etape()
fourmi.mainloop()
