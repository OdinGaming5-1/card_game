import pygame
import pygame.surfarray
from pygame.locals import *
import time
import threading
import pygame.surflock
import math

from Card import Card
from Background import Background
from Character import Character
from Enemy import Enemy
from CardLayoutManager import CardLayoutManager
from Button import Button

class App:
    FPS=60
    prev_time=time.time()
    TARGET_FPS=60
    dt=0
    card_layout_manager=None

    vision_thread=None
    vision_surface=None
    vision_screen=None
    vision_render=False

    def __init__(self):
        self.running = True
        
        self.inmenu = False
        self.inintro = True
        self.inplay= False
        
        self.screen = None
        self.size = self.width, self.height = 1200, 820
        
        self.font=None
        self.clock=pygame.time.Clock()
        self.card_layout_manager=CardLayoutManager(self.width, self.height)

        self.bg=None
        self.character=None
        self.enemy=None
        
        self.bgsurf=None
    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.running = True
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.card_layout_manager.addCards([
            Card("Physical",0),
            Card("Magical",1),
            Card("Physical",1),
            Card("Magical",0),
            Card("Physical",0),
            Card("Magical",1),
            Card("Physical",1),
            Card("Magical",0),
        ])
        self.bg=Background()     
        self.character=Character()
        self.enemy=Enemy()

        self.button1=Button((200,200),"Play")
        self.button2=Button((200,200+50+10),"Exit")
        # self.vision_thread = threading.Thread(target=self.vision_thread, args=())
        # self.vision_th read.start()
        
    # a little effect
    def vision_thread(self):
        self.vision_surface=pygame.Surface((self.width,self.height))
        self.vision_screen.lock()
        data=pygame.PixelArray(self.vision_screen)
        val=0
        for x in range(0,self.width):
            for y in range(0,self.height):
                pix=data[x,y] & 0xffffff
                r=pix>>16 & 0xff
                g=pix>>8 & 0xff
                b=pix & 0xff
                val=math.floor((r+g+b)/3)
                data[x,y]=(val,val,val)
        pygame.surfarray.blit_array(self.vision_surface,data)
        self.vision_screen.unlock()
        return self
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # toggle menu
                if not self.inmenu:
                    self.inintro=False
                    self.inplay=False
                    self.inmenu=True
                    self.vision_screen=self.screen.copy()
                    self.vision_thread()
                else:
                    self.inmenu=False
                    self.inintro=True
                    self.inplay=False

            elif event.key == pygame.K_LEFT:
                self.character.change_state("_Attack")
            elif event.key == pygame.K_RIGHT:
                self.character.change_state("_Run")
            else:
                self.character.change_state("_Idle")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.card_layout_manager.event_handler(event)
        
        self.button1.event_handler(event,self.btn_click_play)
        self.button2.event_handler(event,self.btn_click_exit)

    #button clicks
    def btn_click_play(self):
        self.inmenu=False
        self.inintro=False
        self.inplay=True                               

        return self
    def btn_click_exit(self):
        self.running = False
        return self
                    
    def on_loop(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
        #self.clock.tick(self.FPS)

    def on_render(self):
        deltaTime = self.dt * self.TARGET_FPS

        if self.inintro:
            self.bg.blit_color(deltaTime, self.screen)
            self.character.blit_color(deltaTime,self.screen,(0,330))
            self.enemy.blit_color(deltaTime,self.screen,(100,290))
            
        if self.inmenu:
            if not self.vision_screen.get_locked():
                self.screen.blit(self.vision_surface,(0,0))
                self.button1.blit(self.screen)
                self.button2.blit(self.screen)
        if self.inplay:
            self.bgsurf=pygame.Surface((self.width,self.height))
            self.bgsurf.fill((0,0,0))
            self.screen.blit(self.bgsurf,(0,0))
            self.card_layout_manager.deckLayout(self.screen)
            #self.card_layout_manager.inventoryLayout(self.screen)

        pygame.display.flip()
                                       
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()