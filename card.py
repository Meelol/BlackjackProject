class Card:
    valid_cards = {
                    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 
                    "J": 10, "Q": 10, "K": 10   }

    def __init__(self, number_symbol):
        if number_symbol not in Card.valid_cards.keys():
            raise KeyError("Invalid Card!")
        else:
            self._number_symbol = number_symbol
            self._card_value = Card.valid_cards[number_symbol]

    @property
    def number_symbol(self):
        return self._number_symbol

    @number_symbol.setter
    def number_symbol(self, number_symbol):
        if number_symbol not in Card.valid_cards.keys():
            raise ValueError("number_symbol must be a valid symbol!")
        self._number_symbol = number_symbol

    @property
    def card_value(self):
        return self._card_value

    @card_value.setter
    def card_value(self, card_value):
        if card_value not in Card.valid_cards.values():
            raise ValueError("card_value must be a valid value!")
        self._card_value = card_value

    def __str__(self) -> str:
        return self._number_symbol

#Card Test
#c = Card("K")
#print(c)