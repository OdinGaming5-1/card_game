import pygame
from Card import Card

class CardLayoutManager:
    # deckIndex=0

    def __init__(self,maxWidth,maxHeight):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.cards:list[Card] = []

        self.rects:list[pygame.Rect] =[]
        self.selected_card_index=0

    def addCards(self, cards):
        for card in cards:
            self.cards.append(card)
        return self
    
    def dragCard(self,screen:pygame.Surface):
        (x, y)=pygame.mouse.get_pos()
        card=self.cards[self.selected_card_index]
        card.drag=True
        card.blit_color(screen,(x-card.width/2,y-card.height/2))
        
    def dropCard(self,screen:pygame.Surface):
        (x, y)=pygame.mouse.get_pos()
        card=self.cards[self.selected_card_index]
        card.drag=False
        card.blit_color(screen,(x-card.width/2,y-card.height/2))
        

    def deckLayout(self,screen:pygame.Surface):
        # deck_height=self.cards[0].height+50+10
        # surface=pygame.Surface((self.maxWidth,deck_height))
        # surface.fill((0,0,0))
        # screen.blit(surface,(0,self.maxHeight-deck_height))

        self.rects =[]
        glow_i=None
        length=len(self.cards)
        index=0
        for i in range(0,length):
            card=self.cards[i]
            if i == self.selected_card_index and card.drag:
                continue
            (x,y)=(card.width*0.5*index+10*(index+1),self.maxHeight-card.height-10)
            collision=1
            if i != length-1:
                collision=0.5
            if card.glow:
                glow_i=i
                self.rects.append(pygame.Rect(x,y-50,card.width*collision,card.height))
            else:
                card.blit_color(screen,(x,y))
                self.rects.append(pygame.Rect(x,y,card.width*collision,card.height))
            index = index + 1

        # draw on top
        if glow_i is not None:
            card=self.cards[glow_i]
            (x,y)=(card.width/2*glow_i+10*(glow_i+1),self.maxHeight-card.height-10)
            self.cards[glow_i].blit_color(screen,(x,y-50))
            
        return self
    
    def inventoryLayout(self,screen:pygame.Surface):
        left_padding=50
        right_padding=350
        vertical_padding=50
        row=1
        col=1
        self.rects =[]
        for card in self.cards:
            x=left_padding+card.width*(row-1)+10*row
            if(x + left_padding + right_padding + card.width > self.maxWidth):
                col=col+1
                row=1
                x=left_padding+10
            y=vertical_padding+(card.height+10)*(col-1)
            row=row+1
            card.blit_color(screen,(x,y))
            self.rects.append(pygame.Rect(x,y,card.width,card.height))
        
        # render a chosen card
        selected_card=pygame.transform.scale2x(self.cards[self.selected_card_index].get_image())
        self.cards[self.selected_card_index].glow=True
        w,h=selected_card.get_size()
        screen.blit(selected_card,(self.maxWidth-w-30,vertical_padding))
        return self
    
    def event_handler(self):
        index=None
        for card in self.cards:
            card.glow=False

        (x, y)=pygame.mouse.get_pos()
        for i in range(0,len(self.rects)):
            rect=self.rects[i]
            if rect.collidepoint(x, y):
                index=i
                break
        
        if index is not None:
            self.selected_card_index=index
            self.cards[index].glow=True

        return self
