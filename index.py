import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Chargement de l'image de fond (assure-toi d'avoir une image dans le dossier)
BACKGROUND_IMAGE = "image.png"  # Remplace par le nom de ton fichier

# Dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 600

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 102, 204)

# Création de la fenêtre
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Menu Principal")

# Chargement de l'image de fond
if os.path.exists(BACKGROUND_IMAGE):
    background = pygame.image.load(BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))
else:
    background = None

# Police pour les boutons
font = pygame.font.Font(None, 50)

# Fonction pour dessiner un bouton
def dessiner_bouton(texte, x, y, largeur, hauteur, couleur, action=None):
    pygame.draw.rect(screen, couleur, (x, y, largeur, hauteur), border_radius=10)
    text = font.render(texte, True, BLANC)
    text_rect = text.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    screen.blit(text, text_rect)
    return pygame.Rect(x, y, largeur, hauteur), action

# Fonction principale du menu
def menu():
    while True:
        screen.fill(BLANC)

        # Affichage du fond d'écran
        if background:
            screen.blit(background, (0, 0))

        # Création des boutons
        bouton_morpion, action_morpion = dessiner_bouton("Jouer au Morpion", 300, 250, 200, 60, BLEU, "morpion")
        bouton_quitter, action_quitter = dessiner_bouton("Quitter", 300, 350, 200, 60, NOIR, "quitter")

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_morpion.collidepoint(event.pos):
                    os.system("python morpion/main.py")  # Exécute le jeu Morpion
                    sys.exit()
                if bouton_quitter.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Lancer le menu
menu()
