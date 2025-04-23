import pyglet
from pyglet import shapes
from pyglet.window import mouse

# Création de la fenêtre
fenetre = pyglet.window.Window(480, 270, "Eco Runner")

# Chargement des fonds et titres
fond = pyglet.image.load('assets/images/background.png')
sprite_fond = pyglet.sprite.Sprite(fond)

titre_options = pyglet.sprite.Sprite(pyglet.image.load('assets/images/titre_options.png'), x=157.5, y=200)
titre_pause = pyglet.sprite.Sprite(pyglet.image.load('assets/images/titre_pause.png'), x=184, y=200)

# Variables d'état
musique_active = True
son_actif = True
ecran_actuel = "menu_principal"

# Chargement des images des boutons
image_musique_on = pyglet.image.load('assets/images/musique_on_btn.png')
image_musique_off = pyglet.image.load('assets/images/musique_off_btn.png')
image_son_on = pyglet.image.load('assets/images/son_on_btn.png')
image_son_off = pyglet.image.load('assets/images/son_off_btn.png')
image_retour = pyglet.image.load('assets/images/retour_btn.png')
image_pause = pyglet.image.load('assets/images/pause_btn.png')

# Sprites du menu principal
sprite_nouvelle_partie = pyglet.sprite.Sprite(pyglet.image.load('assets/images/nouvellePartie.png'), x=330, y=150)
sprite_bouton_options = pyglet.sprite.Sprite(pyglet.image.load('assets/images/options.png'), x=5, y=50)
sprite_quitter = pyglet.sprite.Sprite(pyglet.image.load('assets/images/quitter.png'), x=360, y=20)

# Sprite bouton pause (affiché pendant le jeu)
bouton_pause = pyglet.sprite.Sprite(image_pause, x=420, y=220)

# Classe de bouton image
class BoutonImage:
    def __init__(self, image_on, image_off, x, y):
        self.image_on = image_on
        self.image_off = image_off
        self.sprite = pyglet.sprite.Sprite(image_on, x=x, y=y)
        self.active = True

    def dessiner(self):
        self.sprite.draw()

    def basculer(self):
        self.active = not self.active
        self.sprite.image = self.image_on if self.active else self.image_off

    def contient_point(self, x, y):
        return (self.sprite.x <= x <= self.sprite.x + self.sprite.width and
                self.sprite.y <= y <= self.sprite.y + self.sprite.height)

# Boutons audio partagés
bouton_musique = BoutonImage(image_musique_on, image_musique_off, 165, 130)
bouton_son = BoutonImage(image_son_on, image_son_off, 165, 80)
bouton_retour = pyglet.sprite.Sprite(image_retour, x=165, y=20)

# Gérer les clics souris
@fenetre.event
def on_mouse_press(x, y, bouton, modificateurs):
    global ecran_actuel, musique_active, son_actif

    if ecran_actuel == "menu_principal":
        if sprite_nouvelle_partie.x <= x <= sprite_nouvelle_partie.x + sprite_nouvelle_partie.width and sprite_nouvelle_partie.y <= y <= sprite_nouvelle_partie.y + sprite_nouvelle_partie.height:
            print("Nouvelle Partie")
            ecran_actuel = "jeu"
        elif sprite_bouton_options.x <= x <= sprite_bouton_options.x + sprite_bouton_options.width and sprite_bouton_options.y <= y <= sprite_bouton_options.y + sprite_bouton_options.height:
            ecran_actuel = "options"
        elif sprite_quitter.x <= x <= sprite_quitter.x + sprite_quitter.width and sprite_quitter.y <= y <= sprite_quitter.y + sprite_quitter.height:
            pyglet.app.exit()

    elif ecran_actuel == "jeu":
        if bouton_pause.x <= x <= bouton_pause.x + bouton_pause.width and bouton_pause.y <= y <= bouton_pause.y + bouton_pause.height:
            print("Pause activée")
            ecran_actuel = "pause"

    elif ecran_actuel in ["options", "pause"]:
        if bouton_musique.contient_point(x, y):
            bouton_musique.basculer()
            musique_active = bouton_musique.active
            print("Musique activée" if musique_active else "Musique désactivée")
        elif bouton_son.contient_point(x, y):
            bouton_son.basculer()
            son_actif = bouton_son.active
            print("Son activé" if son_actif else "Son désactivé")
        elif bouton_retour.x <= x <= bouton_retour.x + bouton_retour.width and bouton_retour.y <= y <= bouton_retour.y + bouton_retour.height:
            ecran_actuel = "menu_principal" if ecran_actuel == "options" else "jeu"

# Affichage
@fenetre.event
def on_draw():
    fenetre.clear()
    sprite_fond.draw()

    if ecran_actuel == "menu_principal":
        sprite_nouvelle_partie.draw()
        sprite_bouton_options.draw()
        sprite_quitter.draw()

    elif ecran_actuel == "options":
        rectangle = shapes.Rectangle(0, 0, 480, 270, color=(0, 0, 0))
        rectangle.opacity = 120
        rectangle.draw()
        titre_options.draw()
        bouton_musique.dessiner()
        bouton_son.dessiner()
        bouton_retour.draw()

    elif ecran_actuel == "jeu":
        bouton_pause.draw()  # Affiche le bouton pause

    elif ecran_actuel == "pause":
        rectangle = shapes.Rectangle(0, 0, 480, 270, color=(0, 0, 0))
        rectangle.opacity = 120
        rectangle.draw()
        titre_pause.draw()
        bouton_musique.dessiner()
        bouton_son.dessiner()
        bouton_retour.draw()

# Lancer l'application
pyglet.app.run()