from card import Card


class Hand:
    suitSymbol = 0
    card = 1

    def __init__(self):
        self._cards = []  # Tuples holding (symbol, card)
        self._handValue = 0

    def addCard(self, symbolAndCard):
        self._cards.append(symbolAndCard)

    def getHandValue(self):
        self._handValue = 0
        aces = []
        for card in self._cards:
            if card[self.card].numberSymbol != 'A':
                self._handValue += card[self.card]._cardValue
            else:
                aces.append(card[self.card])
        if len(aces) == 1:
            if self._handValue > 10:
                self._handValue += aces[0]._cardValue
            else:
                aces[0]._cardValue = 11
                self._handValue += aces[0]._cardValue
        else:
            for i, ace in enumerate(aces):
                if i == len(aces) - 1 and self._handValue < 10:
                    ace._cardValue = 11
                    self._handValue += ace._cardValue
                else:
                    self._handValue += ace._cardValue
        return self._handValue

    def __str__(self) -> str:
        string = ""
        for card in self._cards:
            string = string + str(card[self.suitSymbol]) + str(card[self.card].numberSymbol) + " "
        return string


'''h = Hand()
print(h.getHandValue())
h.addCard((u"\u2666", Card("8")))
h.addCard((u"\u2666", Card("9")))
print(h.getHandValue())
h.addCard((u"\u2666", Card("A")))
print(h.getHandValue())
h.addCard((u"\u2666", Card("A")))
print(h.getHandValue())
print(h)'''
