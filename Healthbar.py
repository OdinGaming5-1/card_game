import pygame

class Healthbar:
    _rect:pygame.Rect
    _surface:pygame.Surface
    bg=(50,170,50)
    __percent=50
    __w=300
    __h=30
    __x=0
    __y=0
    
    def __init__(self,pos,bg=(50,170,50)):
        self.__x=pos[0]
        self.__y=pos[1]
        self.bg=bg

    def blit(self,screen:pygame.Surface):
        self._rect=pygame.Rect((self.__x,self.__y,self.__w*self.__percent/100,self.__h))
        self._surface=pygame.Surface((self.__w*self.__percent/100,self.__h))
        self._surface.fill(self.bg)
        screen.blit(self._surface,self._rect)

        rect=pygame.Rect((self.__x,self.__y,self.__w*self.__percent/100,self.__h//2))
        surface=pygame.Surface((self.__w*self.__percent/100,self.__h//2), pygame.SRCALPHA)
        surface.fill((255,255,255,100))
        screen.blit(surface,rect)

        return self

    def set_percent(self,percent):
        self.__percent=percent
        if self.__percent>100:
            self.__percent=100
        elif self.__percent<0:
            self.__percent=0
        return self
    
    def get_percent(self):
        return self.__percent
    
    def increment(self,val=1):
        self.__percent+=val
        if self.__percent>100:
            self.__percent=100
        elif self.__percent<0:
            self.__percent=0
        return self
    
    def decrement(self,val=1):
        self.increment(-val)
        return self