import tkinter as tk
from tkinter import messagebox

class IA_Morpion:
    def __init__(self, symbole):
        self.symbole = symbole
        self.profondeur_max = 3 # profondeur 3 (minmax rapide)

    # En checkant les cellules vides
    def trouver_meilleur_coup(self, grille):
        meilleur_score = float("-inf")
        meilleur_coup = None
        for y in range(4):
            for x in range(4):
                if grille[y][x] == " ":
                    grille[y][x] = self.symbole
                    score = self.minimax(grille, 0, False)
                    grille[y][x] = " "
                    if score > meilleur_score:
                        meilleur_score = score
                        meilleur_coup = (x, y)
        return meilleur_coup

    # Implémentation algorithme Minimax
    def minimax(self, grille, profondeur, maximise):
        if self.verifier_gagnant(grille, "O"): return 1
        if self.verifier_gagnant(grille, "X"): return -1
        if self.est_plein(grille) or profondeur == self.profondeur_max: return 0

        if maximise:
            score = float("-inf")
            symbole = "O"
        else:
            score = float("inf")
            symbole = "X"

        for y in range(4):
            for x in range(4):
                if grille[y][x] == " ":
                    grille[y][x] = symbole
                    score_temp = self.minimax(grille, profondeur + 1, not maximise)
                    grille[y][x] = " "
                    score = max(score, score_temp) if maximise else min(score, score_temp)
        return score

    # Vérifie le gain
    def verifier_gagnant(self, grille, joueur):
        for ligne in grille:
            if all(cell == joueur for cell in ligne): return True
        for col in range(4):
            if all(ligne[col] == joueur for ligne in grille): return True
        if all(grille[i][i] == joueur for i in range(4)) or all(grille[i][3-i] == joueur for i in range(4)):
            return True
        return False

    # Vérifie si la grille est pleine
    def est_plein(self, grille):
        return all(cell != " " for ligne in grille for cell in ligne)

class JeuMorpion:
    def __init__(self, master):
        self.master = master
        self.master.title("l'imbattable tictactoe 4x4")
        self.initialiser_interface()

    def initialiser_interface(self):
        self.grille = [[" " for _ in range(4)] for _ in range(4)]
        self.joueur_courant = "X"
        self.ia = IA_Morpion("O")
        self.canvas = tk.Canvas(self.master, width=320, height=320, bg='white')
        self.canvas.pack()
        self.dessiner_grille()
        self.canvas.bind("<Button-1>", self.gerer_clic)

    def dessiner_grille(self):
        for y in range(4):
            for x in range(4):
                self.canvas.create_rectangle(x*80, y*80, (x+1)*80, (y+1)*80, outline="black")
                if self.grille[y][x] == "X":
                    self.dessiner_symbole(x, y, "X")
                elif self.grille[y][x] == "O":
                    self.dessiner_symbole(x, y, "O")

    def dessiner_symbole(self, x, y, symbole):
        if symbole == "X":
            self.canvas.create_line(x*80, y*80, (x+1)*80, (y+1)*80, fill="blue", width=2)
            self.canvas.create_line((x+1)*80, y*80, x*80, (y+1)*80, fill="blue", width=2)
        else:  #  "O" ----> IA
            self.canvas.create_oval(x*80 + 2, y*80 + 2, (x+1)*80 - 2, (y+1)*80 - 2, outline="red", width=2)

    def gerer_clic(self, evenement):
        x, y = evenement.x // 80, evenement.y // 80
        if self.grille[y][x] == " ":
            self.grille[y][x] = self.joueur_courant
            fini = self.verifier_fin_de_jeu(self.joueur_courant)
            if not fini and self.joueur_courant == "X":
                self.coup_ia()
            self.dessiner_grille()

    # coup de l'IA
    def coup_ia(self):
        coup = self.ia.trouver_meilleur_coup(self.grille)
        if coup:
            self.grille[coup[1]][coup[0]] = "O"
            self.verifier_fin_de_jeu("O")

    # Vérifie si le jeu est termine
    def verifier_fin_de_jeu(self, joueur):
        if self.ia.verifier_gagnant(self.grille, joueur):
            messagebox.showinfo(f"{joueur} a gagné !")
            self.initialiser_interface()
            return True
        if self.ia.est_plein(self.grille):
            messagebox.showinfo("Match nul !")
            self.initialiser_interface()
            return True
        return False

if __name__ == "__main__":
    racine = tk.Tk()
    jeu = JeuMorpion(racine)
    racine.mainloop()
