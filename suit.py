from card import Card


class Suit:
    CARDS_IN_SUIT = 13

    def __init__(self, symbol):
        self._symbol = symbol
        self._cards = []
        self.fill_suit()

    def fill_suit(self):
        for key in Card.valid_cards:
            self._cards.append(Card(key))

    def get_card_from_suit(self, index):
        return self._cards.pop(index)
    
    def check_empty_suit(self):
        if len(self._cards) == 0:
            return True
        else:
            return False
    
    def print_suit(self):
        print(self._symbol, *self._cards)


# Test Suit Class
# s = Suit(u"\u2666")
# s.print_suit()
# s.get_card_from_suit(2)
# print(s.check_empty_suit())
