from card import Card


class Suit:
    CARDS_IN_SUIT = 13

    def __init__(self, symbol):
        self._symbol = symbol
        self._cards = []
        self.fillSuit()

    def fillSuit(self):
        for key in Card.valid_numberSymbolsAndValues:
            self._cards.append(Card(key))

    def getCardFromSuit(self, number):
         return self._cards.pop(number)

    def printSuit(self):
        print(self._symbol, *self._cards)


#Test Suit Class
'''s = Suit(u"\u2666")
s.printSuit()'''
