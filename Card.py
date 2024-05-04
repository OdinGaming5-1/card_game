import pygame

class Card:
    width=0
    height=0
    image=[]
    data=[]
    pos=(0,0)
    def __init__(self):
        self.image=pygame.image.load("img/card_base.png").convert()
        self.width,self.height=self.image.get_size()

    def blit_color(self,screen,pos,color):
        self.data=pygame.PixelArray(self.image)
        for x in range(0,self.width):
            for y in range(0,self.height):
                if self.data[x,y]==(screen.map_rgb((255,0,255,255)) & 0xffffffff):
                    self.data[x,y]=color
        pygame.surfarray.blit_array(screen.subsurface(pygame.Rect(pos[0],pos[1],self.width,self.height)),self.data)
        return self

