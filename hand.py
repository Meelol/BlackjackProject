from card import Card


class Hand:
    suitSymbol = 0
    card = 1

    def __init__(self):
        self._cards = []  # Tuples holding (symbol, card)
        self._handValue = 0

    def addCard(self, card):
        self._cards.append(card)

    def getHandValue(self):
        self._handValue = 0
        aces = []
        for card in self._cards:
            if card[self.card].numberSymbol != 'A':
                self._handValue += card[self.card]._cardValue()
            else:
                aces.append[card[self.card]]
        for ace in aces:
            if self._handValue > 10:
                self._handValue += ace.cardValue()
            else:
                self._handValue += ace.cardValue(11)
        return self._handValue

    def __str__(self) -> str:
        for card in self._cards:
            string = str(card[self.suitSymbol]) + \
                str(card[self.card].numberSymbol)
            return string
