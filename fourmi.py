#######################################
#RAFIL Akli Yacine
#JOUAN Maxime
#https://github.com/uvsq22105831/projet_fourmi_de_langton
########################################
import tkinter as tk

LARGEUR = 500
HAUTEUR = 500
NOMBRECARRE=80
Cellule =LARGEUR // NOMBRECARRE

#########################
#fonctions
def fairesol():
    """créé le sol du fait que si la case est de valeur 1
    cela représente une case noir. Et si la case est de 
    valeur 0 cela représente une case blanche"""
    global grille, sol
    grille =[]
    sol =[]
    for i in range(Cellule):
        sol.append([0]*Cellule)
        grille.append([0]*Cellule)
          
    for i in range(Cellule):
        for j in range(Cellule):
            largeur = LARGEUR // Cellule
            hauteur = HAUTEUR // Cellule
            x0, y0 = i * largeur, j * hauteur
            x1, y1 = (i + 1) * largeur, (j + 1) * hauteur
            rectangle =can.create_rectangle((x0, y0), (x1, y1), fill="white",outline="")




##########################################
#programme principal
fourmi = tk.Tk()
fourmi.title("fourmi de Langton")
can = tk.Canvas(fourmi, width= LARGEUR, height=HAUTEUR)
bouton_play = tk.Button(fourmi,text="continuer")
fairesol()
can.grid(column=1, row=0)
bouton_play.grid(column=1,row=1)
fourmi.mainloop()
