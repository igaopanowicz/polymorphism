# Card Class

import pygwidgets

class Card():

    def __init__(self, window, rank, suit, value):
        
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        
        self.nameOfCard = str(value) + ' of ' + suit

        if value == 1:
            self.nameOfCard = 'Ace of ' + suit
        if value == 11:
            self.nameOfCard = 'Jack of ' + suit
        if value == 12:
            self.nameOfCard = 'Queen of ' + suit
        if value == 13:
            self.nameOfCard = 'King of ' + suit
        
 
        #print('ImageName is .....' + self.nameOfCard)
        self.imageName = 'images/' +  self.nameOfCard + '.png'

        self.cardImage = pygwidgets.Image(window, (85, 300), self.imageName)
        self.backOfCardImage = pygwidgets.Image(window, (85, 300), 'images/BackOfCard.png')
        
        self.concealorRevealState = 0

    def conceal(self):
        self.concealorRevealState=0
        #print('Must conceal the card here')

    def setLoc(self, locTuple):
        #print('Called setLoc method, passed in', locTuple)
        self.cardImage = pygwidgets.Image(self.window, locTuple, self.imageName)
        self.backOfCardImage = pygwidgets.Image(self.window, locTuple, 'images/BackOfCard.png')
        
    def reveal(self):
        self.concealorRevealState=1
        #print('Must reveal card here')

    def getName(self):
        return self.nameOfCard
        #print('Get the name of the card here')

    def getValue(self):
        return self.value
        print('Get the value of the card here')

    def draw(self):
        #print('Draw the card here......' + str(self.concealorRevealState))
        if self.concealorRevealState == 1:
            self.cardImage.draw()
        if self.concealorRevealState == 0:
            self.backOfCardImage.draw()
            

    def getCardNameAndValue(self):
        #print("Get the card name and value here")
        return self.nameOfCard, self.value
