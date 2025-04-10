import pyglet

# Police personnalisée
pyglet.font.add_file('assets/fonts/BebasNeue-Regular.ttf')
FONT_NAME = "Bebas Neue"

# Fenêtre
window = pyglet.window.Window(width=480, height=270, caption="Écran titre")

# États
current_screen = "menu"
music_on = True
sound_on = True

# Images
background = pyglet.resource.image('assets/images/splashScreen.png')
img_options_btn = pyglet.resource.image('assets/images/options.png')

# Batch principal
batch = pyglet.graphics.Batch()

# Sprites du menu principal
sprite_nouvellepartie = pyglet.sprite.Sprite(pyglet.resource.image('assets/images/nouvellePartie.png'), x=330, y=150, batch=batch)
sprite_options = pyglet.sprite.Sprite(img_options_btn, x=5, y=50, batch=batch)
sprite_quitter = pyglet.sprite.Sprite(pyglet.resource.image('assets/images/quitter.png'), x=360, y=20, batch=batch)

# Labels stylisés pour le menu options
label_music = pyglet.text.Label("Musique : ON", font_name=FONT_NAME, font_size=22,
                                x=240, y=160, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
label_sound = pyglet.text.Label("Son : ON", font_name=FONT_NAME, font_size=22,
                                x=240, y=120, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
label_back = pyglet.text.Label("Retour", font_name=FONT_NAME, font_size=22,
                               x=240, y=70, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

# Fonction de dessin
@window.event
def on_draw():
    window.clear()
    background.blit(0, 0)

    if current_screen == "menu":
        batch.draw()
    elif current_screen == "options":
        draw_overlay()
        label_music.draw()
        label_sound.draw()
        label_back.draw()

# Overlay sombre
def draw_overlay():
    overlay = pyglet.shapes.Rectangle(0, 0, window.width, window.height, color=(0, 0, 0))
    overlay.opacity = 200
    overlay.draw()

# Clics souris
@window.event
def on_mouse_press(x, y, button, modifiers):
    global current_screen, music_on, sound_on

    if button == pyglet.window.mouse.LEFT:
        if current_screen == "menu":
            if sprite_in_bounds(sprite_nouvellepartie, x, y):
                start_game()
            elif sprite_in_bounds(sprite_options, x, y):
                current_screen = "options"
            elif sprite_in_bounds(sprite_quitter, x, y):
                pyglet.app.exit()

        elif current_screen == "options":
            if label_in_bounds(label_music, x, y):
                music_on = not music_on
                label_music.text = f"Musique : {'ON' if music_on else 'OFF'}"
            elif label_in_bounds(label_sound, x, y):
                sound_on = not sound_on
                label_sound.text = f"Son : {'ON' if sound_on else 'OFF'}"
            elif label_in_bounds(label_back, x, y):
                current_screen = "menu"

# Touche clavier
@window.event
def on_key_press(symbol, modifiers):
    global current_screen
    if symbol == pyglet.window.key.ENTER and current_screen == "menu":
        start_game()
    elif symbol == pyglet.window.key.ESCAPE and current_screen == "options":
        current_screen = "menu"

# Collision avec sprite
def sprite_in_bounds(sprite, x, y):
    return sprite.x <= x <= sprite.x + sprite.width and sprite.y <= y <= sprite.y + sprite.height

# Collision avec label
def label_in_bounds(label, x, y):
    width = label.content_width
    height = label.content_height
    return (label.x - width // 2 <= x <= label.x + width // 2 and
            label.y - height // 2 <= y <= label.y + height // 2)

# Démarrer le jeu
def start_game():
    print("Le jeu commence ici !")
    # Tu peux ici charger un nouvel écran ou scène de jeu

# Lancer l’app
pyglet.app.run()