import pygame
import json

class Card:
    width=0
    height=0
    image=[]
    __magic_color=(255,0,255,255)
    
    font=None
    cards_attack_magical=None
    cards_attack_physical=None
 
    def __init__(self):
        surface=pygame.image.load("img/card_base.png").convert()
        self.image=pygame.transform.scale_by(surface,2)
        self.width,self.height=self.image.get_size()

        self.font= pygame.font.SysFont('Arial', 20)

        with open('cards/attack_magical.json', 'r') as file:
            data = ' '.join(file.readlines())
            self.cards_attack_magical=json.loads(data)
        
        with open('cards/attack_physical.json', 'r') as file:
            data = ' '.join(file.readlines())
            self.cards_attack_physical=json.loads(data)

    # self.cards_attack_magical[0]["Name"]
    # self.cards_attack_physical[0]["Name"]

    def blit_color(self,screen,pos,color):
        data=pygame.PixelArray(self.image.copy())
        for x in range(0,self.width):
            for y in range(0,self.height):
                if data[x,y]==(screen.map_rgb(self.__magic_color) & 0xffffffff):
                    data[x,y]=color
        pygame.surfarray.blit_array(screen.subsurface(pygame.Rect(pos[0],pos[1],self.width,self.height)),data)

        text_surface = self.font.render('Name', True, (0, 0, 0))
        screen.blit(text_surface,(40,20))

        return self

