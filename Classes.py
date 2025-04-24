from Util import *

STATES = ["run","jump","attack"]

E = 2.718,


class Humanoid():
    def __init__(self, idleAnimationInfo, X=0, Y=0, SUBPIXEL=True, **kwargs):
        
        self.__state_sprites = {
            "idle": pyglet.sprite.Sprite(getAnimation(idleAnimationInfo), x=X, y=Y,subpixel=SUBPIXEL)
        }

        self.__state = "idle"

        # ajoute les etats suplementaire si il y en a.
        for state in STATES:
            if state in kwargs.keys():
                self.__state_sprites[state] = pyglet.sprite.Sprite(getAnimation(kwargs[state]), x=X, y=Y,subpixel=SUBPIXEL)

        self.x = X
        self.y = Y
        
        self.__vel_x = 0
        self.__vel_y = 0

        self.decelerating = False

        self.__current_size = 1
        self.__current_rot = 1

    def getPixelSize(self):
        return self.__state_sprites[self.__state].width

    # modifie la taille (indirectement)
    def setSize(self, NEW_SCALE):
        self.__current_size = NEW_SCALE

    def getSize(self):
        return self.__current_size

    # renvoie l'etat actuelle
    def getState(self):
        return self.__state

    # modifie l'etat
    def setState(self, NEW_STATE):
        self.__state = NEW_STATE

    # renvoie le velocity du humanoid
    def getVelocity(self):
        return (self.__vel_x, self.__vel_y)

    # modify comment le humanoid va bouger
    def updateVelocity(self, VEL_X, VEL_Y):
        self.__vel_x = VEL_X
        self.__vel_y = VEL_Y

    # function reponsable pour le movement du humanoid
    def move(self):
        self.x += self.__vel_x
        self.y += self.__vel_y

        if self.getVelocity() == (0,0):
            self.setState('idle')
        else:
            self.setState('run')

    # fonction qui modify l'orientation du humanoid (droite/gauche)
    def setXRotation(self,SCALE):
        self.__current_rot = SCALE

    # fonction qui renvoie l'orientation du humanoid
    def getXRotation(self):
        return self.__current_rot
    
    # fonction qui renvoie v (x et y) (decelerer)
    def decelerate(self,current_t,FLAG=None):
        v_x, v_y = self.getVelocity()

        if FLAG == "-start":
            self.__dece_start_vel_x = v_x
            self.__start = current_t
            self.__t = 0
            self.__decelerateTime = .35
            self.decelerating = True
        elif FLAG == "-stop":
            self.decelerating = False

        if self.decelerating:

            self.__t = current_t - self.__start
            
            elapsed = min(self.__t / self.__decelerateTime, 1)
            v_x = lerp(self.__dece_start_vel_x, 0, elapsed)

            return v_x

    # fonction responsable pour dessiner le humanoid en fonction de son etat
    def draw(self):
        draw_prite = self.__state_sprites[self.__state]
        
        draw_prite.scale_x = self.__current_rot
        draw_prite.scale = self.__current_size

        draw_prite.x = self.x
        draw_prite.y = self.y
        
        draw_prite.draw()
        