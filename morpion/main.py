import random
import pygame
import sys

# on initialise pygame
pygame.init()


# pour plus que ce soit plus pratique, on vient définir les couleurs ici : 
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

# ainsi que les Dimensions
LARGEUR = 600
HAUTEUR = 600
TILE_SIZE = LARGEUR // 3


screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Morpion')

# Plateau du jeu
jeu = [['.', '.', '.'],
       ['.', '.', '.'],
       ['.', '.', '.']]

# Joueur actuel
joueur = random.choice(['x', 'o'])
gagne = False

# Fonction qui permet d'afficher le plateau
def afficher_grille():
    screen.fill(BLANC)
    
    # création du plateau
    for x in range(1, 3):
        pygame.draw.line(screen, NOIR, (x * TILE_SIZE, 0), (x * TILE_SIZE, HAUTEUR), 5)
        pygame.draw.line(screen, NOIR, (0, x * TILE_SIZE), (LARGEUR, x * TILE_SIZE), 5)
    
    # Dessiner les symboles x et o
    font = pygame.font.Font(None, 150)
    for i in range(3):
        for j in range(3):
            if jeu[i][j] != '.':
                text = font.render(jeu[i][j], True, ROUGE if jeu[i][j] == 'x' else BLEU)
                screen.blit(text, (j * TILE_SIZE + TILE_SIZE // 4, i * TILE_SIZE + TILE_SIZE // 4))
    
    pygame.display.update()

# Fonction qui permet de naviguer dans le tableau pour vérifier si un joueur a gagné 
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

# Fonction permettant de changer le joueur a chaque tour
def changer_joueur():
    global joueur
    joueur = 'o' if joueur == 'x' else 'x'

# Fonction qui nous permet de gerer les cliques de la souris
def gestion_clic(x, y):
    global jeu
    ligne = y // TILE_SIZE
    colonne = x // TILE_SIZE
    if jeu[ligne][colonne] == '.':
        jeu[ligne][colonne] = joueur
        if verifier_victoire():
            return True
        changer_joueur()
    return False

# Fonction qui gére le déroulement du jeu
def jouer():
    global gagne
    while gagne == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if gestion_clic(x, y):
                    afficher_grille()
                    pygame.time.wait(500)
                    print(f"Le joueur {joueur} a gagné !")
                    gagne = True
                if est_plein():
                    print("Match nul !")
                    pygame.quit()
                    sys.exit()
        afficher_grille()
        pygame.display.update()

# Vérifie si le plateau est plein
def est_plein():
    return all(cell != '.' for row in jeu for cell in row)

# On lance le jeux apres avoir défini toute l'algorythmie du jeux
jouer()
