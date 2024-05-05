import pygame
import json
import math

class CardObj:
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
        # surface=pygame.image.load("img/cards/card_bg.png").convert()
        # self.bg_image=pygame.transform.scale(surface, (240,280))
        # pygame.draw.rect(self.bg_image, (0,0,0), pygame.Rect(0, 0, 240, 280))
        self.bg_image=pygame.Surface((240,280))
        width,height=self.bg_image.get_size()
        # self.bg_image.fill((0,0,0))
        color1=0
        color2=255
        data=pygame.PixelArray(self.bg_image)
        for x in range(0,width):
            for y in range(0,height):
                res=math.floor((1-y/height)*color1+(y/height)*color2)
                data[x,y]=(res,0,0)
        pygame.surfarray.blit_array(self.bg_image,data)
        
        if damage_type=="Magical":
            with open('cards/attack_magical.json', 'r') as file:
                data = ' '.join(file.readlines())
                self.cards=json.loads(data)
        elif damage_type=="Physical":   
            with open('cards/attack_physical.json', 'r') as file:
                data = ' '.join(file.readlines())
                self.cards=json.loads(data)
        
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

        self.font= pygame.font.SysFont('Arial', 24, bold=True)
        text_surface = self.font.render(self.Name, True, (255, 255, 255))
        self.bg_image.blit(text_surface,(10,240))

        self.font= pygame.font.SysFont('Arial', 18, bold=True)
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


class Card:
    __magic_color=(255,0,255,255)
    
    obj=None

    def __init__(self,type,index):
        self.obj=CardObj(type,index)
    
    def blit_color(self,screen,pos,i):
        # data=pygame.PixelArray(self.image.copy())
        # for x in range(0,self.width):
        #     for y in range(0,self.height):
        #         if data[x,y]==(screen.map_rgb(self.__magic_color) & 0xffffffff):
        #             data[x,y]=color
        # pygame.surfarray.blit_array(screen.subsurface(pygame.Rect(pos[0],pos[1],self.width,self.height)),data)
        screen.blit(self.obj.get_image(),pos)
        
        return self

