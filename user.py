from blackjackActionsInterface import blackjackActionsInterface
from hand import Hand


class User(blackjackActionsInterface):
    def __init__(self, balance):
        self._balance = balance
        self._hand = Hand()
        self._bet = 0

    def getHand(self):
        return self._hand

    def getBalance(self):
        return self._balance

    def setBalance(self, amount):
        self._balance += amount

    def setBet(self, amount):
        self._bet = amount

    def getBet(self):
        return self._bet

    def stay(self):
        print("Stay.")
        return True

    def hit(self, card):
        self._hand.addCard(card)

    def resetHand(self):
        self._hand = Hand()

    def printBetAndBalance(self):
        print(f"Balance: {self._balance}$\nCurrent bet: {self._bet}$")

    def showCardsInHand(self):
        print(f"Your hand: {self._hand} ")

    def getHandValue(self):
        return self._hand.getHandValue()
