import pyglet

# Crée une fenêtre
window = pyglet.window.Window(width=480, height=270, caption="Écran titre")

# Image de fond
background = pyglet.resource.image('assets/images/splashScreen.png')

# Crée un batch
batch = pyglet.graphics.Batch()

# Crée les sprites des boutons
sprite_nouvellepartie = pyglet.sprite.Sprite(pyglet.resource.image('assets/images/nouvellePartie.png'), x=330, y=150, batch=batch)
sprite_options = pyglet.sprite.Sprite(pyglet.resource.image('assets/images/options.png'), x=5, y=50, batch=batch)
sprite_quitter = pyglet.sprite.Sprite(pyglet.resource.image('assets/images/quitter.png'), x=360, y=20, batch=batch)

# Liste des boutons pour itération
buttons = [sprite_nouvellepartie, sprite_options, sprite_quitter]

@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        if sprite_nouvellepartie.x <= x <= sprite_nouvellepartie.x + sprite_nouvellepartie.width and \
           sprite_nouvellepartie.y <= y <= sprite_nouvellepartie.y + sprite_nouvellepartie.height:
            print("Lancement du jeu…")
            start_game()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        print("Lancement du jeu…")
        start_game()

def start_game():
    print("Le jeu commence ici !")
    # Ajoute ici la logique pour démarrer le jeu ou changer d’écran

pyglet.app.run()