import pygame
import json

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
        surface=pygame.image.load("img/cards/card_bg.png").convert()
        self.bg_image=pygame.transform.scale_by(surface,0.08)

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
        self.image=pygame.transform.scale_by(pygame.image.load(self.Icon).convert().copy(),0.2)
        width,height=self.image.get_size()
        self.width=width
        self.height=height


        self.bg_image.blit(self.image,(15,45))

        self.font= pygame.font.SysFont('Arial', 20)
        text_surface = self.font.render(self.Name, True, (0, 0, 0))
        self.bg_image.blit(text_surface,(30,20))

        self.font= pygame.font.SysFont('Arial', 15)
        text_surface = self.font.render("Dam:"+str(self.Damage), True, (0, 0, 0))
        self.bg_image.blit(text_surface,(120,50))

        text_surface = self.font.render("Dur:"+str(self.DamageDuration), True, (0, 0, 0))
        self.bg_image.blit(text_surface,(120,80))

        text_surface = self.font.render("Man:"+str(self.Mana), True, (0, 0, 0))
        self.bg_image.blit(text_surface,(120,110))

        
        return self.bg_image


class Card:
    __magic_color=(255,0,255,255)
    
    obj=None

    def __init__(self):
        self.obj=CardObj("Magical",0)
    
    def blit_color(self,screen,pos,i):
        # data=pygame.PixelArray(self.image.copy())
        # for x in range(0,self.width):
        #     for y in range(0,self.height):
        #         if data[x,y]==(screen.map_rgb(self.__magic_color) & 0xffffffff):
        #             data[x,y]=color
        # pygame.surfarray.blit_array(screen.subsurface(pygame.Rect(pos[0],pos[1],self.width,self.height)),data)
        screen.blit(self.obj.get_image(),pos)
        
        return self

