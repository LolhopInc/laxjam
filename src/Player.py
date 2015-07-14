import pygame, GameObject, load_image

class Player(GameObject):

    image = load_image("PlayerSprite.png")

    def __init__(self, location, radius):

        super().__init__(self, location, radius)

        self.surface = pygame.transform.scale(self.image, (self.size, self.size))

    def update():
        #called once per frame
        #animation code

    def runTo(target):
        #set velocities to RUN to given point

    def strafeTo(target):
        #set velocities to STRAFE to given point
