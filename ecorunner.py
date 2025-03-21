import pyglet

# Crée une fenêtre de 480x270 pixels
window = pyglet.window.Window(width=480, height=270, caption="Ecran titre")

# Charge une image de fond (si disponible)
background = pyglet.resource.image('background.jpg')

# Crée le titre du jeu
title = pyglet.text.Label(
    'ECORUNNER', 
    font_name='Arial', 
    font_size=36,
    x=window.width // 2, 
    y=window.height - 50,
    anchor_x='center', 
    anchor_y='center'
)

# Crée le bouton "Jouer"
play_button = pyglet.text.Label(
    'Jouer', 
    font_name='Arial', 
    font_size=24,
    x=window.width // 2, 
    y=window.height // 2 + 20,
    anchor_x='center', 
    anchor_y='center'
)

# Crée le bouton "Options" en bas à droite
options_button = pyglet.text.Label(
    'Options', 
    font_name='Arial', 
    font_size=20,
    x=window.width - 20,  # Marge de 20 pixels depuis le bord droit
    y=20,                 # Marge de 20 pixels depuis le bas
    anchor_x='right', 
    anchor_y='bottom'
)

# Fonction pour afficher l'écran d'accueil
@window.event
def on_draw():
    window.clear()
    # Affiche l'image de fond (si elle existe)
    if background:
        background.blit(0, 0, width=window.width, height=window.height)
    
    # Affiche le titre et les boutons
    title.draw()
    play_button.draw()
    options_button.draw()

# Fonction appelée lorsqu'on clique avec la souris
@window.event
def on_mouse_press(x, y, button, modifiers):
    # Vérifie si le clic est dans la zone du bouton "Jouer"
    if (play_button.x - play_button.content_width // 2 < x < play_button.x + play_button.content_width // 2) and \
       (play_button.y - play_button.content_height // 2 < y < play_button.y + play_button.content_height // 2):
        print("Lancement du jeu...")
        start_game()

    # Vérifie si le clic est dans la zone du bouton "Options"
    if (options_button.x - options_button.content_width < x < options_button.x) and \
       (options_button.y < y < options_button.y + options_button.content_height):
        print("Ouverture des options...")
        open_options()

# Fonction appelée lorsqu'on appuie sur une touche
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        print("Lancement du jeu...")
        start_game()

# Fonction pour démarrer le jeu
def start_game():
    print("Le jeu commence ici !")
    # → Code pour changer d'écran ou lancer une nouvelle fenêtre

# Fonction pour ouvrir les options
def open_options():
    print("Options ouvertes")
    # → Code pour afficher le menu des options

# Lance la boucle principale
pyglet.app.run()