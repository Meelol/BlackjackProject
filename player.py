class Player:
    def __init__(self):
        self._balance = 0
        self._hand = []

    def setBalance(self, balance):
        self._balance = balance

    def getBalance(self):
        return self._balance

    def addCardToHand(self, card):
        self._hand.append(card)

    def resetHand(self):
        self._hand = []
