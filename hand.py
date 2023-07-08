from card import Card


class Hand:
    suit_symbol = 0
    card = 1

    def __init__(self):
        self._cards = []  # Tuples holding (symbol, card)
        self._hand_value = 0

    def add_card(self, symbol_and_card):
        self._cards.append(symbol_and_card)

    def get_hand_value(self):
        self._hand_value = 0
        aces = []
        for card in self._cards:
            if card[self.card].number_symbol != 'A':
                self._hand_value += card[self.card]._card_value
            else:
                aces.append(card[self.card])
        if len(aces) == 1:
            if self._hand_value > 11:
                self._hand_value += aces[0]._card_value
            else:
                aces[0]._card_value = 11
                self._hand_value += aces[0]._card_value
        else:
            for i, ace in enumerate(aces):
                if i == len(aces) - 1 and self._hand_value <= 10:
                    ace._card_value = 11
                    self._hand_value += ace._card_value
                else:
                    self._hand_value += ace._card_value
        return self._hand_value

    def __str__(self) -> str:
        string = ""
        for card in self._cards:
            string = string + str(card[self.suit_symbol]) + str(card[self.card].number_symbol) + " "
        return string


# h = Hand()
# h.add_card((u"\u2666", Card("A")))
# h.add_card((u"\u2666", Card("A")))
# h.add_card((u"\u2666", Card("A")))
# h.add_card((u"\u2666", Card("A")))
# h.add_card((u"\u2666", Card("2")))
# h.add_card((u"\u2666", Card("K")))
# print(h)
# print(h.get_hand_value())
