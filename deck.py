from suit import Suit

class Deck:
    def __init__(self):
        self._suit = []
        self.fillDeck()
    
    def fillDeck(self):
        diamondSuit = Suit(u"\u2666")
        heartSuit = Suit(u"\u2665")
        clubSuit = Suit(u"\u2663")
        spadeSuit = Suit(u"\u2660")
        suits = [diamondSuit, heartSuit, clubSuit, spadeSuit]
        for suit in suits:
            self._suit.append(suit)

    def playCardFromDeck():
        pass    

    def printDeck(self):
        for suit in self._suit:
            suit.printSuit()


'''Test Deck Class
d = Deck()
d.printDeck()'''
