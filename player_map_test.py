from Util import *
from pytmx.util_pyglet import pyglet_image_loader
from Classes import *
import time


key = pyglet.window.key
keys = key.KeyStateHandler()
window = pyglet.window.Window()
window.push_handlers(keys)

WINDOW_EDGE = window.width*.05

map_img = pyglet.resource.image("assets/temp/map_img.png")
map_sprite = pyglet.sprite.Sprite(map_img, 0, 0)
print(map_img.width, map_img.height)

user = Humanoid(
    (pyglet.resource.texture('assets/temp/Pink_Monster_Idle_4.png'), 1, 4),
    window.width/2,
    0,
    True,
    run=(pyglet.resource.texture('assets/temp/Pink_Monster_Run_6.png'), 1, 6))

user.setSize(1.5)
user.y = 96 - user.getPixelSize()

camera_x = 0
def step(dt):
    global camera_x

    pressedMovementKey = False
    # user.updateVelocity(0,0) # remet le v a 0
    v_x, v_y = user.getVelocity()

    # movement gauche
    if (keys[key.A] or keys[key.LEFT]):
        pressedMovementKey = True
        v_x = -1*MOVEMENT_SPEED*dt

        # gere le offset creer par l'inversement de l'image, lors du changement de direction
        if user.getXRotation() != -1:
            print(-1*MOVEMENT_SPEED*dt)
            user.x += 32

        user.setXRotation(-1)
        
    # movement droite
    elif (keys[key.D] or keys[key.RIGHT]):
        pressedMovementKey = True
        v_x = 1*MOVEMENT_SPEED*dt

        # gere le offset creer par l'inversement de l'image, lors du changement de direction
        if user.getXRotation() != 1:
            user.x -= 32

        user.setXRotation(1)
    
    

    if user.getVelocity()[0] != 0 and not pressedMovementKey: 
        flag = None if user.decelerating else "-start"
        v_x = user.decelerate(time.time(),FLAG=flag)
    elif pressedMovementKey and user.decelerating: # arreter la deceleration
        user.decelerate(time.time(),FLAG="-stop")

    v_x = clamp(v_x, MAX_X_VELOCITY[0], MAX_X_VELOCITY[1]) # pour faire en sorte que v ne soit pas trops grand ou petit (pour bug de vitesse anormale)
    user.updateVelocity(v_x, v_y)

    user.move()

    # restraindre la position du joeur au fenetre du jeu
    user.x = clamp(user.x, user.getPixelSize(), window.width-user.getPixelSize())

    # camera movement
    camera_x = clamp(camera_x, -(map_img.width - window.width), 0)

    startOfMap = camera_x == 0
    endOfMap = camera_x == -(map_img.width - window.width)

    vel_x = user.getVelocity()[0]
    if abs(vel_x) > 0: # le joueur doit etre en movement
        if not startOfMap and user.x <= WINDOW_EDGE: # si le joeur est au 10% de l'ecran mais pas au debut du niveau (on bouge le niveau vers le gauche)
            camera_x -= vel_x*1.25
            user.x = WINDOW_EDGE
            print("MOVED BACK")
        elif not endOfMap and user.x >= window.width - WINDOW_EDGE:  # si le joeur est au 90% de l'ecran mais pas a la fin du niveau (on bouge le niveau vers le gauche)
            camera_x -= vel_x*1.25
            user.x = window.width - WINDOW_EDGE

    camera_x = clamp(camera_x, -(map_img.width - window.width), 0)
    map_sprite.x = camera_x


@window.event
def on_draw():
    window.clear()
    map_sprite.draw()
    user.draw()

pyglet.clock.schedule_interval(step, 1/MAX_FPS)

pyglet.app.run()

