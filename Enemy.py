from config import *
import pygame
import math

from Character import Sprite

class EnemySprite(Sprite):
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

    def getSurface(self,dt):
        
        if self.template_img is None:
            self.template_img=pygame.image.load(config.config("enemy_character_folder")+self.template_fname+".png").convert_alpha()
            full_width,self.height=self.template_img.get_size()
            self.frames=full_width/self.width

        surface=self.template_img.subsurface(pygame.Rect(math.floor(self.i)*self.width,0,self.width,self.height))
        self.i=(self.i+((1 * dt)/self.duration))%self.frames
        return surface

class Enemy:
    sprites={"_Idle":EnemySprite("_Idle",150),"_Spear":EnemySprite("_Spear",150),"_Run":EnemySprite("_Run",150),"_Death":EnemySprite("_Death",150)}
    state="_Run"
    
    def __init__(self):
        pass        

    def blit_color(self,dt,screen,pos):
        sprite=self.sprites[self.state]
        scaled=pygame.transform.scale_by(sprite.getSurface(dt),2.5)
        screen.blit(scaled,pos)
        return self

    def change_state(self,state):
        self.state=state
        return self
