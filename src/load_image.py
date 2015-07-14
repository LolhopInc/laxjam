#load_image.py

#Shorthand to load image from assets directory

import os, sys, pygame

def load_image(name):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()

    return image
