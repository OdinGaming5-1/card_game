import pygame
import math
from CardData import CardData

class Card:
    bg_image=None
    image=None
    width=0
    height=0

    glow=False

    cardData=None
    font=None
    def __init__(self,damage_type,index):
        self.font= pygame.font.SysFont('Arial', 20)
        self.cardData=CardData(damage_type,index)
        self.bg_image=pygame.Surface((160,200))
        
        self.width,self.height=self.bg_image.get_size()
        color1=0
        color2=255
        data=pygame.PixelArray(self.bg_image)
        for x in range(0,self.width):
            for y in range(0,self.height):
                res=math.floor((1-y/self.height)*color1+(y/self.height)*color2)
                if damage_type=="Magical":
                    data[x,y]=(0,0,res)
                else:
                    data[x,y]=(res,0,0)
        pygame.surfarray.blit_array(self.bg_image,data)

    def get_image(self):
        self.image=pygame.transform.scale(pygame.image.load(self.cardData.Icon).convert().copy(), (self.width-20,self.width-20))
        self.bg_image.blit(self.image,(10,10))

        self.font= pygame.font.SysFont('Arial', 18, bold=False)
        text_surface = self.font.render(self.cardData.Name, True, (255, 255, 255))
        self.bg_image.blit(text_surface,(10,self.width))

        self.font= pygame.font.SysFont('Arial', 18, bold=False)
        text_surface = self.font.render(str(self.cardData.Damage)+"d", True, (255, 255, 255))
        self.bg_image.blit(text_surface,(self.width-30,10))

        text_surface = self.font.render(str(self.cardData.DamageDuration)+"r", True, (255, 255, 255))
        self.bg_image.blit(text_surface,(self.width-30,30))

        color=(255, 0, 0)
        if self.cardData.AreaOfEffect:
            color=(0, 255, 0)
        text_surface = self.font.render("AOE", True, color)
        self.bg_image.blit(text_surface,(10,30))

        text_surface = self.font.render(str(self.cardData.Mana)+"m", True, (255, 255, 255))
        self.bg_image.blit(text_surface,(10,10))

        
        return self.bg_image

    def blit_color(self,screen,pos):
        screen.blit(self.get_image(),pos)
        if self.glow:
            rec=self.get_image().get_rect()
            pygame.draw.rect(screen, (255,255,255),pygame.Rect(pos[0],pos[1],rec[2],rec[3]) , width=2)
        return self
