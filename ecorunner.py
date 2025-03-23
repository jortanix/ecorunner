import pyglet

# Paramètres du bouton
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60
BUTTON_COLOR = (50, 150, 250)       # Bleu clair (RGB)
BUTTON_HOVER_COLOR = (30, 120, 220)  # Bleu foncé (RGB)

# Crée une fenêtre de 480x270 pixels
window = pyglet.window.Window(width=480, height=270, caption="Écran titre")

# Charge une image de fond (si disponible)
background = pyglet.resource.image('assets/images/background.jpg')

# Charge une police personnalisée
pyglet.font.add_file(r'C:\Users\laura\ecorunner\assets\fonts\BebasNeue-Regular.ttf')

# Crée le titre du jeu
title = pyglet.text.Label(
    'ECORUNNER',
    font_name='Bebas Neue',
    font_size=36,
    x=window.width // 2,
    y=window.height - 50,
    anchor_x='center',
    anchor_y='center'
)

# État du survol du bouton
is_hovered = False

# Crée un batch pour optimiser le rendu
batch = pyglet.graphics.Batch()

# Crée le bouton avec `shapes.Rectangle`
button = pyglet.shapes.Rectangle(
    x=window.width // 2 - BUTTON_WIDTH // 2,
    y=window.height // 2 - BUTTON_HEIGHT // 2,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    color=BUTTON_COLOR,
    batch=batch
)

# Crée le texte du bouton
button_label = pyglet.text.Label(
    'Jouer',
    font_name='Bebas Neue',
    font_size=24,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x='center',
    anchor_y='center',
    color=(255, 255, 255, 255),  # Blanc
    batch=batch
)

# Fonction pour mettre à jour la couleur du bouton en fonction du survol
def update_button_color():
    if is_hovered:
        button.color = BUTTON_HOVER_COLOR
    else:
        button.color = BUTTON_COLOR

# Fonction pour afficher l'écran d'accueil
@window.event
def on_draw():
    window.clear()
    if background:
        background.blit(0, 0, width=window.width, height=window.height)
    title.draw()
    update_button_color()
    batch.draw()

# Fonction appelée lors d'un clic souris
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        if button_in_bounds(x, y):
            print("Lancement du jeu...")
            start_game()

# Fonction pour détecter le survol de la souris
@window.event
def on_mouse_motion(x, y, dx, dy):
    global is_hovered
    is_hovered = button_in_bounds(x, y)

# Fonction pour vérifier si la souris est dans les limites du bouton
def button_in_bounds(x, y):
    return (button.x <= x <= button.x + button.width and
            button.y <= y <= button.y + button.height)

# Fonction appelée lors de l'appui sur une touche
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        print("Lancement du jeu...")
        start_game()

# Fonction pour démarrer le jeu
def start_game():
    print("Le jeu commence ici !")
    # → Code pour changer d'écran ou lancer une nouvelle fenêtre

# Lance la boucle principale
pyglet.app.run()