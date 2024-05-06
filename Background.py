import pygame

class Background:
    width=0
    height=0
    images=[]
    pos=(0,0)
    x=0
    def __init__(self):
        for i in range(0,12):
            fname = f"img/Background layers/Layer_{i}.png"
            self.images.append(pygame.image.load(fname).convert_alpha())
        self.width,self.height=self.images[0].get_size()

    def blit_color(self, dt, screen):
        imagesLength=len(self.images)
        for i in range(imagesLength-1,-1,-1):
            distance=self.x*(imagesLength-i)*0.2
            rect = pygame.Rect(0,200,self.width,self.height-200)
            surface=self.images[i].copy().subsurface(rect)
            for j in range(0,3):
                position=(distance%self.width-((j-1)*self.width),0)
                screen.blit(surface,position)
        self.x=self.x - (1 * dt)
        return self

