import pyglet
from pyglet import shapes
from pyglet.window import mouse

# Création de la fenêtre
fenetre = pyglet.window.Window(480, 270, "Eco Runner")

# Chargement du fond
fond = pyglet.image.load('assets/images/background.png')
sprite_fond = pyglet.sprite.Sprite(fond)

# Variables d'état
musique_active = True
son_actif = True
ecran_actuel = "menu_principal"

# Chargement du titre des options
titre_options = pyglet.sprite.Sprite(pyglet.image.load('assets/images/titre_options.png'), x=120, y=180)

# Chargement des images pour les boutons
image_musique_on = pyglet.image.load('assets/images/musique_on_btn.png')
image_musique_off = pyglet.image.load('assets/images/musique_off_btn.png')
image_son_on = pyglet.image.load('assets/images/son_on_btn.png')
image_son_off = pyglet.image.load('assets/images/son_off_btn.png')
image_retour = pyglet.image.load('assets/images/retour_btn.png')

# Sprites du menu principal
sprite_nouvelle_partie = pyglet.sprite.Sprite(pyglet.image.load('assets/images/nouvellePartie.png'), x=330, y=150)
sprite_bouton_options = pyglet.sprite.Sprite(pyglet.image.load('assets/images/options.png'), x=5, y=50)
sprite_quitter = pyglet.sprite.Sprite(pyglet.image.load('assets/images/quitter.png'), x=360, y=20)

# Classe de bouton image
class BoutonImage:
    def __init__(self, image_on, image_off, x, y):
        self.image_on = image_on
        self.image_off = image_off
        self.sprite = pyglet.sprite.Sprite(image_on, x=x, y=y)
        self.active = True  # true = activé, false = désactivé

    def dessiner(self):
        self.sprite.draw()

    def basculer(self):
        self.active = not self.active
        self.sprite.image = self.image_on if self.active else self.image_off

    def contient_point(self, x, y):
        return (self.sprite.x <= x <= self.sprite.x + self.sprite.width and
                self.sprite.y <= y <= self.sprite.y + self.sprite.height)

# Boutons de l'écran options
bouton_musique = BoutonImage(image_musique_on, image_musique_off, 150, 120)
bouton_son = BoutonImage(image_son_on, image_son_off, 150, 80)
bouton_retour = pyglet.sprite.Sprite(image_retour, x=150, y=30)

# Gérer les clics souris
@fenetre.event
def on_mouse_press(x, y, bouton, modificateurs):
    global ecran_actuel, musique_active, son_actif

    if ecran_actuel == "menu_principal":
        if sprite_nouvelle_partie.x <= x <= sprite_nouvelle_partie.x + sprite_nouvelle_partie.width and sprite_nouvelle_partie.y <= y <= sprite_nouvelle_partie.y + sprite_nouvelle_partie.height:
            print("Nouvelle Partie")
        elif sprite_bouton_options.x <= x <= sprite_bouton_options.x + sprite_bouton_options.width and sprite_bouton_options.y <= y <= sprite_bouton_options.y + sprite_bouton_options.height:
            ecran_actuel = "options"
        elif sprite_quitter.x <= x <= sprite_quitter.x + sprite_quitter.width and sprite_quitter.y <= y <= sprite_quitter.y + sprite_quitter.height:
            pyglet.app.exit()

    elif ecran_actuel == "options":
        if bouton_musique.contient_point(x, y):
            bouton_musique.basculer()
            musique_active = bouton_musique.active
            print("Musique activée" if musique_active else "Musique désactivée")
        elif bouton_son.contient_point(x, y):
            bouton_son.basculer()
            son_actif = bouton_son.active
            print("Son activé" if son_actif else "Son désactivé")
        elif bouton_retour.x <= x <= bouton_retour.x + bouton_retour.width and bouton_retour.y <= y <= bouton_retour.y + bouton_retour.height:
            ecran_actuel = "menu_principal"

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

# Lancer l'application
pyglet.app.run()