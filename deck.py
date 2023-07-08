import random
from suit import Suit


class Deck:
    def __init__(self):
        self._suit_in_deck = []
        self.fill_deck()
        self._total_cards = 52

    def fill_deck(self):
        diamond_suit = Suit(u"\u2666")  # Diamond
        heart_suit = Suit(u"\u2665")  # Heart
        club_suit = Suit(u"\u2663")  # Club
        spade_suit = Suit(u"\u2660")  # Spade
        suits = [diamond_suit, heart_suit, club_suit, spade_suit]
        for suit in suits:
            self._suit_in_deck.append(suit)

    def get_card_from_deck(self):

        for suit in self._suit_in_deck:
            if suit.check_empty_suit():
                self._suit_in_deck.remove(suit)

        random_suit_index = self._suit_in_deck.index(
            random.choice(self._suit_in_deck))
        random_card_index = self._suit_in_deck[random_suit_index]._cards.index(
            random.choice(self._suit_in_deck[random_suit_index]._cards))
        self._total_cards -= 1
        return (self._suit_in_deck[random_suit_index]._symbol, self._suit_in_deck[random_suit_index].get_card_from_suit(random_card_index))

    def print_deck(self):
        print("\n")
        for suit in self._suit_in_deck:
            suit.print_suit()
        print("\n")


# Test Deck Class
# d = Deck()
# d.print_deck()
# for i in range(51):
#     d.get_card_from_deck()
# d.print_deck()
