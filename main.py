import pygame
import pygame.surfarray
from pygame.locals import *
import numpy

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._image_surf =pygame.image.load("img/okeypieces.jpeg").convert()
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))

        # surf = pygame.display.set_mode((8,2),depth=3)
        # width, height = surf.get_size()
        # print(str(width)+"x"+str(height)+"x")
        # pixels = numpy.array([
        # [(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)],
        # [(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)]
        # ])
        # print(pixels)
        # pygame.surfarray.blit_array( surf, pixels )
        # self._display_surf.blit(surf,(0,0))

        background=pygame.Surface((40,40))
        background.fill(Color(1,2,3,4)) #gbar
        pxarray=pygame.surfarray.array2d(background)
        for x in range(0,40):
            for y in range(0,40):
                pix=pxarray[x,y]
                r=pix >> 24 & 0xFF
                g=pix>> 16 & 0xFF
                b=pix>> 8 & 0xFF
                a=pix & 0xFF
                print("r:"+str(r)+" g:"+str(g)+" b:"+str(b)+" a:"+str(a))
        pygame.surfarray.blit_array(self._display_surf.subsurface(Rect(0,0,40,40)),pxarray)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()