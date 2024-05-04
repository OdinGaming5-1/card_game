import pygame
import pygame.surfarray
from pygame.locals import *

from Card import Card
from Background import Background
from Character import Character

class App:
    FPS=60
    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.weight, self.height = 928, 793
        
        self.font=None

        self.clock=pygame.time.Clock()
        self.card=None
        self.bg=None
        self.character=None
        
    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.running = True
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.card=Card()
        self.bg=Background()     
        self.character=Character()
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running=False
            elif event.key == pygame.K_LEFT:
                self.character.change_state("_Attack")
            elif event.key == pygame.K_RIGHT:
                self.character.change_state("_Run")
            elif event.key == pygame.K_SPACE:
                self.character.change_state("_Roll")
            else:
                self.character.change_state("_Idle")

    def on_loop(self):
        self.clock.tick(self.FPS)
        pass
    def on_render(self):
        self.bg.blit_color(self.screen)

        self.character.blit_color(self.screen,(0,330))

        self.card.blit_color(self.screen,(0,0),(255,0,0))

        # self.card.blit_color(self.screen,(10+self.card.width+20,0),(255,255,0))
        # self.card.blit_color(self.screen,(10+(self.card.width+20)*2,0),(255,255,0))
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