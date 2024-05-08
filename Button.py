import pygame
import pygame.font

class Button:
    _rect:pygame.Rect
    _surface:pygame.Surface
    text=""
    bg=(180,180,180)

    def __init__(self,pos,text):
        w=200
        h=50
        self._rect=pygame.Rect((pos[0],pos[1],w,h))
        self._surface=pygame.Surface((w,h))
        self._surface.fill(self.bg)
        self.text=text


    def blit(self,screen:pygame.Surface):
        self._surface.fill(self.bg)
        font=pygame.font.SysFont('Arial', 18, bold=False)
        text_surface = font.render(self.text, True, (0, 0, 0))
        
        self._surface.blit(text_surface,(10,15))
        screen.blit(self._surface,self._rect)

        return self

    def event_handler(self,event,callback):
        (x, y)=pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(x, y):
                callback()
            
        if event.type == pygame.MOUSEMOTION:
            if self._rect.collidepoint(x, y):
                self.bg=(130,130,180)
            else:
                self.bg=(180,180,180)
                

        return self