import pygame
import pygame.surfarray
from pygame.locals import *

from Card import Card

class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.weight, self.height = 800, 600
        
        self.card=[]
 
    def on_init(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.card=Card()
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    def on_loop(self):
        pass
    def on_render(self):
        # self.screen.blit(self.image_card,(0,0))
        self.card.blit_color(self.screen,(10,0),(255,0,0))
        self.card.blit_color(self.screen,(10+self.card.width+20,0),(255,255,0))
        self.card.blit_color(self.screen,(10+(self.card.width+20)*2,0),(0,255,0))
        
        pygame.display.flip()
                                       
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()