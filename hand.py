from card import Card


class Hand:
    def __init__(self):
        self._cards = []
        self._handValue = 0

    def addCard(self, numberSymbol, value):
        self._cards.append(Card(numberSymbol, value))
