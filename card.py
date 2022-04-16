class Card:
    valid_numberSymbols = ["A", "2", "3", "4", "5",
                           "6", "7", "8", "9", "10", "J", "Q", "K"]
    valid_cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def __init__(self, numberSymbol):
        self._numberSymbol = numberSymbol
        self._cardValue = 0

    @property
    def numberSymbol(self):
        return self._numberSymbol

    @numberSymbol.setter
    def numberSymbol(self, numberSymbol):
        if numberSymbol not in Card.valid_numberSymbols:
            raise ValueError("numberSymbol must be a valid symbol!")
        self._numberSymbol = numberSymbol

    @property
    def cardValue(self):
        return self._cardValue

    @cardValue.setter
    def cardValue(self, cardValue):
        if cardValue not in Card.valid_cardValues:
            raise ValueError("cardValue must be a valid value!")
        self._cardValue = cardValue

    def __str__(self) -> str:
        return self._numberSymbol

'''Test Card Class
c = Card("K")
print(c)'''
