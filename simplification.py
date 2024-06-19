import tkinter as tk
from tkinter import messagebox
import random

# Initialise la grille et le joueur courant
grille = [[" " for _ in range(3)] for _ in range(3)]
joueur_courant = "X"

def dessiner_grille(canvas):
    """Dessine la grille de jeu et les symboles sur le canvas."""
    canvas.delete("all")
    for y in range(3):
        for x in range(3):
            canvas.create_rectangle(x*80, y*80, (x+1)*80, (y+1)*80, outline="black")
            if grille[y][x] == "X":
                dessiner_symbole(canvas, x, y, "X")
            elif grille[y][x] == "O":
                dessiner_symbole(canvas, x, y, "O")

def dessiner_symbole(canvas, x, y, symbole):
    """Dessine le symbole (X ou O) sur le canvas à la position spécifiée."""
    if symbole == "X":
        canvas.create_line(x*80, y*80, (x+1)*80, (y+1)*80, fill="blue", width=2)
        canvas.create_line((x+1)*80, y*80, x*80, (y+1)*80, fill="blue", width=2)
    else:
        canvas.create_oval(x*80 + 2, y*80 + 2, (x+1)*80 - 2, (y+1)*80 - 2, outline="red", width=2)

def gerer_clic(event, canvas):
    """Gère les clics de l'utilisateur sur le canvas."""
    x, y = event.x // 80, event.y // 80
    if grille[y][x] == " ":
        grille[y][x] = joueur_courant
        dessiner_grille(canvas)
        if verifier_fin_de_jeu(joueur_courant):
            return
        changer_joueur()
        if joueur_courant == "O":
            coup_ia(canvas)

def coup_ia(canvas):
    """Fait jouer l'IA en choisissant une case vide aléatoire."""
    cases_vides = [(x, y) for y in range(3) for x in range(3) if grille[y][x] == " "]
    if cases_vides:
        x, y = random.choice(cases_vides)
        grille[y][x] = "O"
        dessiner_grille(canvas)
        verifier_fin_de_jeu("O")
        changer_joueur()

def changer_joueur():
    """Change le joueur courant."""
    global joueur_courant
    joueur_courant = "O" if joueur_courant == "X" else "X"

def verifier_fin_de_jeu(joueur):
    """Vérifie si le jeu est terminé (victoire ou match nul)."""
    if verifier_gagnant(joueur):
        messagebox.showinfo("Fin de partie", f"{joueur} a gagné !")
        initialiser_interface(root)
        return True
    if est_plein():
        messagebox.showinfo("Fin de partie", "Match nul !")
        initialiser_interface(root)
        return True
    return False

def verifier_gagnant(joueur):
    """Vérifie si le joueur spécifié a gagné."""
    for y in range(4):
        for x in range(4):
            if (x + 2 < 4 and grille[y][x] == joueur and grille[y][x + 1] == joueur and grille[y][x + 2] == joueur) or \
               (y + 2 < 4 and grille[y][x] == joueur and grille[y + 1][x] == joueur and grille[y + 2][x] == joueur) or \
               (x + 2 < 4 and y + 2 < 4 and grille[y][x] == joueur and grille[y + 1][x + 1] == joueur and grille[y + 2][x + 2] == joueur) or \
               (x - 2 >= 0 and y + 2 < 4 and grille[y][x] == joueur and grille[y + 1][x - 1] == joueur and grille[y + 2][x - 2] == joueur):
                return True
    return False

def est_plein():
    """Vérifie si la grille est pleine."""
    return all(grille[y][x] != " " for y in range(4) for x in range(4))

def initialiser_interface(master):
    """Initialise l'interface du jeu."""
    global grille, joueur_courant
    grille = [[" " for _ in range(4)] for _ in range(4)]
    joueur_courant = "X"
    canvas = tk.Canvas(master, width=320, height=320, bg='white')
    canvas.pack()
    dessiner_grille(canvas)
    canvas.bind("<Button-1>", lambda event: gerer_clic(event, canvas))

# Créer la fenêtre principale
root = tk.Tk()
root.title("Tic Tac Toe 4x4")
initialiser_interface(root)
root.mainloop()
