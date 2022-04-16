from card import Card


class Suit:
    CARDS_IN_SUIT = 13

    def __init__(self, symbol):
        self._symbol = symbol
        self._cards = []
        self.fillSuit()

    def fillSuit(self):
        for i in range(Suit.CARDS_IN_SUIT):
            self._cards.append(Card(Card.valid_numberSymbols[i]))

    def removeCardFromSuit(self, symbol, card):
        self.cards

    def printSuit(self):
        print(self._symbol, *self._cards)


'''Test Suit Class
s = Suit(u"\u2666")
s.printSuit()'''
