import pygame

class Background:
    width=0
    height=0
    images=[]
    pos=(0,0)
    def __init__(self):
        for i in range(0,12):
            fname = f"img/Background layers/Layer_{i}.png"
            self.images.append(pygame.image.load(fname).convert_alpha())
        self.width,self.height=self.images[0].get_size()

    def blit_color(self,screen,pos):
        for i in range(len(self.images)-1,-1,-1):
            screen.blit(self.images[i].subsurface(pygame.Rect(0,200,self.width,self.height-200)),pos)
        return self

