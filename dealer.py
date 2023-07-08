from blackjackActionsInterface import blackjackActionsInterface
from card import Card #For testing
from hand import Hand
from deck import Deck
from time import sleep

class Dealer(blackjackActionsInterface):
    def __init__(self):
        self._hand = Hand()
        self._deck = Deck()

    def get_hand(self):
        return self._hand

    def get_deck_total_cards(self):
        return self._deck._total_cards

    def get_new_deck(self):
        self._deck = Deck()

    def give_card_to_user(self):
        return self._deck.get_card_from_deck()

    def start_round(self):
        self._hand.add_card(self._deck.get_card_from_deck())
        return self._deck.get_card_from_deck()

    def dealer_advanced_AI(self, user_hand):
        while self._hand.get_hand_value() < 17 or self._hand.get_hand_value() <= user_hand.get_hand_value() :
            self.hit()
            sleep(2)
            self.show_cards_in_hand()
            if self._hand.get_hand_value() > 21:
                sleep(2)
                print("Lucky you!")
                break
        else:
            self.stay()

    def stay(self):
        sleep(2)
        print("Dealer: Stay.")

    def hit(self):
        print("Dealer: Hit.")
        self._hand.add_card(self._deck.get_card_from_deck())

    def get_hand_value(self):
        return self._hand.get_hand_value()

    def reset_hand(self):
        self._hand = Hand()

    def show_cards_in_hand(self):
        print(f"Dealer's hand: {self._hand} ")


# d = Dealer()
# user_hand = Hand()
# user_hand.add_card((u"\u2666", Card("A")))
# user_hand.add_card((u"\u2666", Card("A")))
# user_hand.add_card((u"\u2666", Card("9")))
# print(user_hand.get_hand_value())
# d.start_round()
# d.show_cards_in_hand()
# d.dealer_advanced_AI(user_hand)
