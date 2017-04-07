

class cardDeck(object):
    def __init__(self):
        self.deck = {}
        self.colors = ['purple', 'white', 'blue', 'yellow', 'red', 'orange', 'green']
        for i in self.colors:
            self.deck[1] = 12
        self.deck['wild'] = 14
    
    def __str__(self):
        return self.deck
            

    def drawCard(self):
        print 'cards remaining {}'.format(self.deck)
