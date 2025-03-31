import random

jeu = [['.', '.', '.'],
       ['.', '.', '.'],
       ['.', '.', '.']]
joueur = random.choice(['x', 'o'])
gagne = False

#Hugro
# fonction permettant d'afficher les lignes
def afficher_grille():
    print("  1   2   3")
    print("  ---------")
    for i in range(3):
        print(i + 1, "|".join(jeu[i]))
        if i < 2:
            print("  ---------")
    print()

#Nour Habibi
# Le but est de Vérifier toutes les lignes 
def verifier_victoire():
    for ligne in jeu:
        if ligne.count(joueur) == 3:
            return True
    for col in range(3):
        if all(jeu[row][col] == joueur for row in range(3)):
            return True
    if all(jeu[i][i] == joueur for i in range(3)) or all(jeu[i][2 - i] == joueur for i in range(3)):
        return True
    return False

#Manomano.fr
# on va faire une fonction qui permet de sélectionner un joueur x ou o aléatoirement
def changer_joueur():
    global joueur
    joueur = 'o' if joueur == 'x' else 'x'

#Maxime
# fonction permettant de lancer le jeux
def jouer():
    global gagne
    while not gagne:
        afficher_grille()  # à chaque tour, afficher la grille
        try:
            ligne, colonne = map(int, input(f"Joueur {joueur}, entrez ligne et colonne (ex: 1 2) : ").split())
            if jeu[ligne - 1][colonne - 1] == '.':
                jeu[ligne - 1][colonne - 1] = joueur
                if verifier_victoire():
                    afficher_grille()
                    print(f"Le joueur {joueur} a gagné !")
                    gagne = True
                else:
                    changer_joueur()  # changer de joueur après chaque tour
            else:
                print("Case déjà prise")
        except (ValueError, IndexError):
            print("Valeur invalide, veuiller rentrée une valeur entre 1 et 3")

jouer()