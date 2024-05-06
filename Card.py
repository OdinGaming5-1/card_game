from config import *
import pygame
import json
import math

class Card:
    bg_image=None
    image=None
    width=0
    height=0
    Name=""
    Icon=""
    Description=""
    DamageType=""
    DamageDuration=0
    Damage=0
    Mana=0
    AreaOfEffect=False

    cards=[]
    font=None
    def __init__(self,damage_type,index):
        self.font= pygame.font.SysFont('Arial', 20)
 
        if damage_type=="Magical":
            with open(config.config("magicalcards"), 'r') as file:
                data = ' '.join(file.readlines())
                self.cards=json.loads(data)
        elif damage_type=="Physical":   
            with open(config.config("physicalcards"), 'r') as file:
                data = ' '.join(file.readlines())
                self.cards=json.loads(data)

        self.bg_image=pygame.Surface((240,280))
        width,height=self.bg_image.get_size()
        color1=0
        color2=255
        data=pygame.PixelArray(self.bg_image)
        for x in range(0,width):
            for y in range(0,height):
                res=math.floor((1-y/height)*color1+(y/height)*color2)
                if damage_type=="Magical":
                    data[x,y]=(0,0,res)
                else:
                    data[x,y]=(res,0,0)
        pygame.surfarray.blit_array(self.bg_image,data)
       
        card=self.cards[index]
        self.Name=card["Name"]
        self.Icon=card["Icon"]
        self.Description=card["Description"]
        self.DamageType=card["DamageType"]
        self.DamageDuration=card["DamageDuration"]
        self.Damage=card["Damage"]
        self.Mana=card["Mana"]
        self.AreaOfEffect=card["AreaOfEffect"]

    def get_image(self):
        self.image=pygame.transform.scale(pygame.image.load(self.Icon).convert().copy(), (220,220))
        width,height=self.image.get_size()
        self.width=width
        self.height=height


        self.bg_image.blit(self.image,(10,10))

        self.font= pygame.font.SysFont('Arial', 25, bold=False)
        text_surface = self.font.render(self.Name, True, (255, 255, 255))
        self.bg_image.blit(text_surface,(10,240))

        self.font= pygame.font.SysFont('Arial', 18, bold=False)
        text_surface = self.font.render(str(self.Damage)+"d", True, (255, 255, 255))
        self.bg_image.blit(text_surface,(195,10))

        text_surface = self.font.render(str(self.DamageDuration)+"r", True, (255, 255, 255))
        self.bg_image.blit(text_surface,(210,32))

        color=(255, 0, 0)
        if self.AreaOfEffect:
            color=(0, 255, 0)
        text_surface = self.font.render("AOE", True, color)
        self.bg_image.blit(text_surface,(200,50))

        text_surface = self.font.render(str(self.Mana)+"m", True, (255, 255, 255))
        self.bg_image.blit(text_surface,(10,10))

        
        return self.bg_image

    def blit_color(self,screen,pos):
        screen.blit(self.get_image(),pos)
        return self
