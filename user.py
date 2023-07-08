from blackjackActionsInterface import blackjackActionsInterface
from hand import Hand


class User(blackjackActionsInterface):
    def __init__(self, balance):
        self._balance = balance
        self._hand = Hand()
        self._bet = 0

    def get_hand(self):
        return self._hand

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance += amount

    def set_bet(self, amount):
        self._bet = amount

    def get_bet(self):
        return self._bet

    def stay(self):
        print("Stay.")
        return True

    def hit(self, card):
        self._hand.add_card(card)

    def reset_hand(self):
        self._hand = Hand()

    def print_bet_and_balance(self):
        print(f"Balance: {self._balance}$\nCurrent bet: {self._bet}$")

    def show_cards_in_hand(self):
        print(f"Your hand: {self._hand} ")

    def get_hand_value(self):
        return self._hand.get_hand_value()
