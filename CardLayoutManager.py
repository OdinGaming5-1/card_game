import pygame
from Card import Card

class CardLayoutManager:
    deckIndex=0

    def __init__(self,maxWidth,maxHeight):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.cards = []

        self.rects =[]
        self.selected_card_index=0

    def addCards(self, cards):
        for card in cards:
            self.cards.append(card)
    
    def deckLayout(self,screen):
        
        for i in range(0,len(self.cards)):
            card=self.cards[i]
            card.blit_color(screen,(card.width*i+10*(i+1),self.maxHeight-card.height-10))
    
    def inventoryLayout(self,screen):
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
    
    def event_handler(self,event):
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
