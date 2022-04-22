#######################################
#RAFIL Akli Yacine
#JOUAN Maxime
#https://github.com/uvsq22105831/projet_fourmi_de_langton
########################################
import tkinter as tk


LARGEUR = 700
HAUTEUR = 700
NOMBRECARRE=95
Cellule =LARGEUR // NOMBRECARRE
direction= (1,0)
LPOS=LARGEUR//Cellule
tempsetape =100
position =(LPOS//2-10,LPOS//2+19)
sol = [[0] * LPOS for _ in range(LPOS)]


#########################
#fonctions



def deplacement(position,direction, sol):
    """créé le déplacement a partir de la liste sol"""
    i, j = position
    a, b = direction
    aa, bb = (b, -a) if sol[i][j] == 0 else (-b, a)
    return (i + aa, j + bb), (aa, bb)

def dessine(position, direction, sol):
    """va donner la nouvelle direction et position de la fourmi"""
    (ii, jj), nouvelledir = deplacement(position, direction, sol)
    i, j = position
    colorcarre = sol[i][j]

    if colorcarre == 0:
        colorcarre = creesol(i, j)
        sol[i][j] = colorcarre
    else:
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
        tempsetape =100
        fourmi.after(tempsetape, etape)
    else:
        tempsetape =9999999999

def changebout():
    if bouton_play['text'] =="pause":
        bouton_play['text']="play"
    else:
        bouton_play['text']="pause"
##########################################
#programme principal
fourmi = tk.Tk()
fourmi.title("fourmi de Langton")
can = tk.Canvas(fourmi, width= LARGEUR, height=HAUTEUR)
bouton_play = tk.Button(fourmi,text="pause",command= fonctionboutplay)
can.grid(column=1, row=0)
etape()
bouton_play.grid(column=1,row=2)
fourmi.mainloop()
