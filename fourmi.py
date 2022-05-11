#######################################
#RAFIL Akli Yacine
#JOUAN Maxime
#BARRERE Manon
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
inverse=0
#########################
#fonctions



def deplacement(position,direction, sol):
    """créé le déplacement a partir de la liste sol"""
    """Inspiration de la ligne 42 et 43 via le site 
    http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html"""
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

def deplacement_inverse(position, direction, sol):
    """créé le déplacement contraire a partir de la liste sol"""
    """fonction ne fonctionne pas totalement"""
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
    
    aa, bb = (b, -a) if sol[i][j] == 0 else (-b, a)
    return (i + aa, j + bb), (aa, bb)

def etape_inverse():
    """fonction ne fonctionne pas totalement"""
    global position, direction, inverse
    inverse = 1
    position, direction = dessinefourmi_inverse(position, sol)


def dessinefourmi(position, sol):
    """va modeliser la fourmi à partir de la fonction deplacement et creer le principe du tore.
    Va montrer l'emplacement de la creation du sol
    inspirationde la création du sol via le site 
    http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html"""
    global fourmimi,dirfourm,positionavant,premiertour
    (ii, jj), nouvelledir = deplacement(position, direction, sol)
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
    c, d =positionavant
    f,g = c * Cellule, d * Cellule
    colorcarre=sol[c][d]

    can.delete(fourmimi)
    if dirfourm=="bas"and colorfourm==0 or dirfourm =="haut" and colorfourm!=0:
        fourmimi=can.create_polygon((x+Cellule/2, y+Cellule),(x,y),(x+Cellule, y),fill="red",outline='')
        dirfourm="gauche"
    elif dirfourm=="gauche"and colorfourm==0 or dirfourm =="droite" and colorfourm!=0:
        fourmimi=can.create_polygon((x, y+Cellule/2),(x+Cellule,y), (x+Cellule, y+Cellule),fill="red",outline='')
        dirfourm="haut"
    elif dirfourm=="haut"and colorfourm==0 or dirfourm =="bas" and colorfourm!=0:
        fourmimi=can.create_polygon((x+Cellule/2, y),(x, y+Cellule), (x+Cellule, y+Cellule),fill="red",outline='')
        dirfourm="droite"
    elif dirfourm=="droite"and colorfourm==0 or dirfourm =="gauche" and colorfourm!=0:
        fourmimi=can.create_polygon((x+Cellule, y+Cellule/2),(x,y), (x, y+Cellule),fill="red",outline='')

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

def dessinefourmi_inverse(position, sol):
    """va modeliser la fourmi à partir de la fonction deplacement et creer le principe du tore.
    Va montrer l'emplacement de la creation du sol(dans le sens contraire)."""
    """fonction ne fonctionne pas totalement"""
    global fourmimi,dirfourm,positionavant,premiertour
    (ii, jj), nouvelledir = deplacement_inverse(position, direction, sol)
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
    c, d =positionavant
    f,g = c * Cellule, d * Cellule
    colorcarre=sol[m][n]

    can.delete(fourmimi)
    if dirfourm=="bas"and colorfourm==0 or dirfourm =="haut" and colorfourm!=0:
        fourmimi=can.create_polygon((x+Cellule/2, y+Cellule),(x,y),(x+Cellule, y),fill="red",outline='')
        dirfourm="gauche"
    elif dirfourm=="gauche"and colorfourm==0 or dirfourm =="droite" and colorfourm!=0:
        fourmimi=can.create_polygon((x, y+Cellule/2),(x+Cellule,y), (x+Cellule, y+Cellule),fill="red",outline='')
        dirfourm="haut"
    elif dirfourm=="haut"and colorfourm==0 or dirfourm =="bas" and colorfourm!=0:
        fourmimi=can.create_polygon((x+Cellule/2, y),(x, y+Cellule), (x+Cellule, y+Cellule),fill="red",outline='')
        dirfourm="droite"
    elif dirfourm=="droite"and colorfourm==0 or dirfourm =="gauche" and colorfourm!=0:
        fourmimi=can.create_polygon((x+Cellule, y+Cellule/2),(x,y), (x, y+Cellule),fill="red",outline='')

    if colorcarre == 0:
        colorcarre = creersol_inverse(m, n)
        sol[m][n] = colorcarre
    else:
        can.delete(colorcarre)
        sol[m][n] = 0
    return (ii, jj), nouvelledir


def creesol(c, d):
    """creer le sol à partir de la fonction dessinefourmi"""
    """inspiration via le site
    http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html"""
    f, g = c * Cellule, d * Cellule
    colorcarre = can.create_rectangle((f, g), (f + Cellule, g + Cellule),fill="black",outline='')
    return colorcarre

def creersol_inverse(m, n):
    """creer le sol à partir de la fonction dessinefourmi_inverse"""
    """fonction ne fonctionne pas totalement"""
    f, g = m * Cellule, n * Cellule
    colorcarre = can.create_rectangle((f, g), (g - Cellule, f - Cellule),fill="white",outline='')
    return colorcarre

def etape():
    """permet à la fourmi d'avancer en boucle"""
    global position, direction
    position, direction = dessinefourmi(position, sol)
    fourmi.after(tempsetape, etape)


def fonctionboutplay():
    """permet d'arreter la boucle a partir de la fonction pause,
    ainsi que changer le nom du bouton"""
    pause()
    changebout()

def pause():
    """permet d'arreter la boucle"""
    global tempsetape
    if tempsetape == 9999999999:
        tempsetape =510
        fourmi.after(tempsetape, etape)
    else:
        tempsetape =9999999999

def changebout():
    """change le nom du bouton play/pause"""
    if bouton_play['text'] =="pause":
        bouton_play['text']="play"
    else:
        bouton_play['text']="pause"


def accelletemps():
    """permet d'effectuer une étape plus rapidement"""
    global tempsetape
    if tempsetape > 11:
        tempsetape-=50

def ralentemps():
    """permet d'effectuer une étape plus lentement"""
    global tempsetape
    tempsetape+=50


def effectetape():
    """permet de passer une étape manuellement"""
    global position, direction
    position, direction = dessinefourmi(position, sol)

def sauvegarde():
    """enregistre les sols noir et blanc de la fourmi dans le fichier sauvegarde.txt"""
    fic = open("sauvegarde.txt","w")
    fic.write(str(NOMBRECARRE)+"\n")
    for i in range(NOMBRECARRE):
        for j in range(NOMBRECARRE):
            fic.write(str(sol[i][j])+"\n")
    fic.close()

def charge():
    """recupere la sauvegarde du fichier sauvegarde.txt"""
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
bouton_revenir=tk.Button(fourmi,text="revenir en arriere", command=etape_inverse)
"""fonction ne fonctionne pas totalement"""

#placement du canevas
can.grid(column=0, row=0, rowspan=10,columnspan=3)

#placements des boutons
bouton_play.grid(column=3,row=2)
bouton_etape.grid(column=3,row=4)
bouton_tmsplus.grid(column=3,row=6)
bouton_tmsmoins.grid(column=3,row=8)
bouton_sauv.grid(column=1,row=11)
bouton_charge.grid(column=2,row=11)
bouton_revenir.grid(column=3, row=10)
##################################
#déroulement principal
etape()

fourmi.mainloop()