class Card:
    valid_numberSymbolsAndValues = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                                    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

    def __init__(self, numberSymbol):
        self._numberSymbol = numberSymbol
        self._cardValue = Card.valid_numberSymbolsAndValues[numberSymbol]

    @property
    def numberSymbol(self):
        return self._numberSymbol

    @numberSymbol.setter
    def numberSymbol(self, numberSymbol):
        if numberSymbol not in Card.valid_numberSymbolsAndValues.keys:
            raise ValueError("numberSymbol must be a valid symbol!")
        self._numberSymbol = numberSymbol

    @property
    def cardValue(self):
        return self._cardValue

    @cardValue.setter
    def cardValue(self, cardValue):
        if cardValue not in Card.valid_numberSymbolsAndValues.values:
            raise ValueError("cardValue must be a valid value!")
        self._cardValue = cardValue

    def __str__(self) -> str:
        return self._numberSymbol


'''Test Card Class
c = Card("K")
print(c)'''
