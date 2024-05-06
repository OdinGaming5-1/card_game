class CardLayoutManager:
    deckIndex=0

    def __init__(self,maxWidth,maxHeight):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.cards = []

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
        for card in self.cards:
            x=left_padding+card.width*(row-1)+10*row
            if(x + left_padding + right_padding + card.width > self.maxWidth):
                col=col+1
                row=1
                x=left_padding+10
            y=vertical_padding+(card.height+10)*(col-1)
            row=row+1
            card.blit_color(screen,(x,y))
    