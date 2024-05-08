import pygame

class StaticBackground:
    pos=(0,0)
    image=None
    def __init__(self, width, height, setToHeight=True):
        fname = f"img/Arena/stone_snake_head_1.jpg"
        self.image=pygame.image.load(fname).convert_alpha()
        self.width,self.height=self.image.get_size()

        if setToHeight:
            self.height=height
            self.width=height*self.width/self.height
        else:
            self.width=width
            self.height=width*self.height/self.width
        self.pos=(width/2-self.width/2, height/2-self.height/2)
        self.image=pygame.transform.scale(self.image,(self.width,self.height))

    def blit_color(self, screen):
        screen.blit(self.image,self.pos)
        return self

