import tkinter as tk
from tkinter import messagebox

class IA_Morpion:
    def __init__(self, symbole):
        pass

    def trouver_meilleur_coup(self, grille):
        pass

    def minimax(self, grille, profondeur, maximise):
        pass

    def verifier_gagnant(self, grille, joueur):
        pass

    def est_plein(self, grille):
        pass

class JeuMorpion:
    def __init__(self, master):
        pass

    def dessiner_grille(self):
        pass

    def gerer_clic(self, evenement):
        pass

    def coup_ia(self):
        pass

    def verifier_fin_de_jeu(self, joueur):
        pass

    def reinitialiser_grille(self):
        pass

    def fermer(self):
        pass

if __name__ == "__main__":
    racine = tk.Tk()
    jeu = JeuMorpion(racine)
    racine.mainloop()
