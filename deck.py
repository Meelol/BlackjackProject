import random
from suit import Suit


class Deck:
    def __init__(self):
        self._suit = []
        self.fillDeck()
        self.cardCounter = 52
        
    def fillDeck(self):
        diamondSuit = Suit(u"\u2666")
        heartSuit = Suit(u"\u2665")
        clubSuit = Suit(u"\u2663")
        spadeSuit = Suit(u"\u2660")
        suits = [diamondSuit, heartSuit, clubSuit, spadeSuit]
        for suit in suits:
            self._suit.append(suit)

    def getCardFromDeck(self):
        random_suit = random.randint(0, 3)
        random_cardFromSuit = random.randint(0, 12)
        try:
            if self._suit[random_suit]._cards[random_cardFromSuit] is None:
             self.getCardFromDeck()
            else:
                self.cardCounter -= 1
                return (self._suit[random_suit]._symbol, self._suit[random_suit].getCardFromSuit(random_cardFromSuit)) 
        except IndexError:
            self.getCardFromDeck()
            
    def printDeck(self):
        for suit in self._suit:
            suit.printSuit()


# Test Deck Class
'''d = Deck()
d.printDeck()
d.getCardFromDeck()
d.printDeck()
'''