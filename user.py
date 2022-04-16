from blackjackActionsInterface import blackjackActionsInterface
from hand import Hand


class User(blackjackActionsInterface):
    def __init__(self, balance):
        self._balance = balance
        self._hand = None
        self._bet = 0

    def setBalance(self, amount):
        self._balance += amount

    def getBalance(self):
        return self._balance

    def setBet(self, amount):
        self._bet = amount

    def stay(self):
        pass

    def hit(self):
        pass

    def resetHand(self):
        pass
