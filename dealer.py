from blackjackActionsInterface import blackjackActionsInterface
from hand import Hand
from deck import Deck


class Dealer(blackjackActionsInterface):
    def __init__(self):
        self._hand = None
        self_deck = None

    def pullCardFromDeck(self):
        pass

    def getNewDeck(self):
        pass

    def stay(self):
        pass

    def hit(self):
        pass
