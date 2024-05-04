import pygame
import math

class Sprite:
    width=0
    height=0
    frames=None
    template_img=None
    template_fname=""
    duration=0 # of frame
    i=0
    def __init__(self,fname,slice_width,duration=5):
        self.template_fname=fname
        self.width=slice_width
        self.duration=duration

    def getSurface(self):
        if self.template_img is None:
            self.template_img=pygame.image.load("img/Free Knight 120x80/"+self.template_fname+".png").convert()
            full_width,self.height=self.template_img.get_size()
            self.frames=full_width/self.width

        surface=self.template_img.subsurface(pygame.Rect(math.floor(self.i)*self.width,0,self.width,self.height))
        self.i=(self.i+1/self.duration)%self.frames
        return surface

class Character:
    sprites={"_Idle":Sprite("_Idle",120),"_Attack":Sprite("_Attack",120),"_Run":Sprite("_Run",120),"_Roll":Sprite("_Roll",120)}
    state="_Idle"
    
    def __init__(self):
        pass        

    def blit_color(self,screen,pos):
        sprite=self.sprites[self.state]
        scaled=pygame.transform.scale_by(sprite.getSurface(),2.5)
        screen.blit(scaled,pos)
        return self

    def change_state(self,state):
        self.state=state
        return self
