import pygame
import pygame.surfarray
from pygame.locals import *

from Card import Card

class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.size = self.weight, self.height = 640, 400
        
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
        # background=pygame.Surface((40,40))
        # background.fill(pygame.Color(1,2,3,255)) #gbar
        # pxarray=pygame.surfarray.array2d(background)

        # w,h=120,160
        # pxarray=pygame.PixelArray(self.screen.subsurface(Rect(0,0,w,h)))
        # for x in range(0,w):
        #     for y in range(0,h):
        #         if pxarray[x,y]==(self.screen.map_rgb((255,0,255,255)) & 0xffffffff):
        #             pxarray[x,y]=(255,0,0)
        
        # pygame.surfarray.blit_array(self.screen.subsurface(Rect(0,0,w,h)),pxarray)
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