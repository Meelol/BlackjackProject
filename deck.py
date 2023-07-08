import random
from suit import Suit


class Deck:
    def __init__(self):
        self._suitInDeck = []
        self.fillDeck()
        self.cardCounter = 52
        
    def fillDeck(self):
        diamondSuit = Suit(u"\u2666")
        heartSuit = Suit(u"\u2665")
        clubSuit = Suit(u"\u2663")
        spadeSuit = Suit(u"\u2660")
        suits = [diamondSuit, heartSuit, clubSuit, spadeSuit]
        for suit in suits:
            self._suitInDeck.append(suit)

    def getCardFromDeck(self):
        random_suitInDeck = random.randint(0, len(self._suitInDeck) -1 )
        random_cardFromSuit = random.randint(0, len(self._suitInDeck[random_suitInDeck]._cards) -1)
        try:
            if self._suitInDeck[random_suitInDeck]._cards[random_cardFromSuit] is None:
             self.getCardFromDeck()
            else:
                self.cardCounter -= 1
                return (self._suitInDeck[random_suitInDeck]._symbol, self._suitInDeck[random_suitInDeck].getCardFromSuit(random_cardFromSuit)) 
        except IndexError:
            self.getCardFromDeck()
            
    def printDeck(self):
        for suit in self._suitInDeck:
            suit.printSuit()


# Test Deck Class
d = Deck()
d.printDeck()
