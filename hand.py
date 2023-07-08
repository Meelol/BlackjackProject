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
        aces_counter = 0
        for card in self._cards:
            if card[self.card].number_symbol != 'A':
                self._hand_value += card[self.card]._card_value
            else:
                aces_counter += 1
        if aces_counter == 1:
            if self._hand_value > 11:
                self._hand_value += 1
            else:
                self._hand_value += 11
        else:
            for i in range(aces_counter):
                if i == (aces_counter - 1) and self._hand_value < 10:
                    self._hand_value += 11
                else:
                    self._hand_value += 1
        return self._hand_value

    def __str__(self) -> str:
        string = ""
        for card in self._cards:
            string = string + str(card[self.suit_symbol]) + str(card[self.card].number_symbol) + " "
        return string


h = Hand()
h.add_card((u"\u2666", Card("6")))
h.add_card((u"\u2666", Card("A")))
h.add_card((u"\u2666", Card("8")))
print(h)
print(h.get_hand_value())
