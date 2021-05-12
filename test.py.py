import pygame                                           # Stellt Objekte und Konstanten zur Spielprogrammierung zur Verfügung
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT,K_SPACE,K_KP_MINUS,K_KP_PLUS,K_F10,K_BACKSPACE)
import random
import os

class Settings(object):

        
    width = 700                            # Hier wird das Fenster defieniert 
    height = 400
    fps = 60       
    title = "Test" 
    file_path = os.path.dirname(os.path.abspath(__file__)) # Hier wird auf der ordner hingewiesen  
    images_path = os.path.join(file_path, "images")   # in dem sich die bilder befinden 


    def get_dim(self):
        return (self.width, self.height)            

class Cat(pygame.sprite.Sprite):                          
    
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.image = pygame.image.load(os.path.join(self.settings.images_path, "kreis3.png")).convert_alpha()  # katzen bild wird geladen 
        self.image = pygame.transform.scale(self.image, (24, 24))           # große der katze 
        self.rect = self.image.get_rect()
        self.rect.left = (settings.width - self.rect.width) // 2                # position der katze wird von links zu Mitte  
        self.rect.top = settings.height - self.rect.height - 1                 # "                           oben zu unten 
        self.direction = 0
        self.speed = 5


    def update(self):
        newleft = self.rect.left + (self.direction * self.speed)
        newright = newleft + self.rect.width
        if newleft > 0 and newright < settings.width:
            self.rect.left = newleft


class Game(object):
    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.get_dim())
        self.pygame.display.set_caption(self.settings.title)
        self.background = self.pygame.image.load(os.path.join(self.settings.images_path, "background2.png")).convert()
        self.background_rect = self.background.get_rect()
        self.katze = Cat(settings)
        self.clock = pygame.time.Clock()
        self.done = False
        
        self.cat_1 = pygame.sprite.Group()
        self.cat_1.add(self.katze)






    def run(self):
        while not self.done:                            # Hauptprogrammschleife mit Abbruchkriterium   
            self.clock.tick(self.settings.fps)          # Setzt die Taktrate auf max 60fps   
            for event in self.pygame.event.get():       # Durchwandere alle aufgetretenen  Ereignisse
                if event.type == QUIT:                  # Wenn das rechts obere X im Fenster geklickt
                    self.done = True                    # Flag wird auf Ende gesetzt
                elif event.type == KEYDOWN:             # Reagiere auf Taste drücken
                    if event.key == K_ESCAPE:
                        self.done = True

            self.update()
            self.draw()
 
    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.cat_1.draw(self.screen)
        self.pygame.display.flip()   # Aktualisiert das Fenster

    def update(self):
        self.cat_1.update()



if __name__ == '__main__':      
                                    
    settings = Settings()       

    pygame.init()              

    game = Game(pygame, settings)
    game.run()
  

    pygame.quit()               