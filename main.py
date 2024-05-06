import pygame
import pygame.surfarray
from pygame.locals import *
import time

from Card import Card
from Background import Background
from Character import Character
from Enemy import Enemy
from CardLayoutManager import CardLayoutManager

class App:
    FPS=60
    prev_time=time.time()
    TARGET_FPS=60
    dt=0
    card_layout_manager=None
    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.weight, self.height = 1200, 820
        
        self.font=None
        self.clock=pygame.time.Clock()
        self.card_layout_manager=CardLayoutManager(self.weight, self.height)

        self.bg=None
        self.character=None
        self.enemy=None
        
    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.running = True
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.card_layout_manager.addCards([
            Card("Physical",0),
            Card("Magical",1),
            Card("Physical",1),
            Card("Magical",0),
            Card("Physical",0),
            Card("Magical",1),
            Card("Physical",1),
            Card("Magical",0),
        ])
        self.bg=Background()     
        self.character=Character()
        self.enemy=Enemy()
        
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
            else:
                self.character.change_state("_Idle")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.card_layout_manager.event_handler(event)
    def on_loop(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
        #self.clock.tick(self.FPS)

    def on_render(self):
        deltaTime = self.dt * self.TARGET_FPS

        self.bg.blit_color(deltaTime, self.screen)
        self.character.blit_color(deltaTime,self.screen,(0,330))

        self.enemy.blit_color(deltaTime,self.screen,(100,290))
        #self.card_layout_manager.deckLayout(self.screen)
        self.card_layout_manager.inventoryLayout(self.screen)

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