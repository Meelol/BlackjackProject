from blackjackActionsInterface import blackjackActionsInterface
from hand import Hand
from deck import Deck
from time import sleep

class Dealer(blackjackActionsInterface):
    def __init__(self):
        self._hand = Hand()
        self._deck = Deck()

    def getHand(self):
        return self._hand

    def getCardCounter(self):
        return self._deck.cardCounter

    def getNewDeck(self):
        self._deck = Deck()

    def giveCardToUser(self):
        return self._deck.getCardFromDeck()

    def startRound(self):
        self._hand.addCard(self._deck.getCardFromDeck())
        return self._deck.getCardFromDeck()

    def dealerAdvancedAI(self, userHand):
        while self._hand.getHandValue() < 17:
            self.hit()
            sleep(2)
            self.showCardsInHand()
            if self._hand.getHandValue() > 21:
                sleep(2)
                print("You won...")
                break
        else:
            self.stay()

    def stay(self):
        print("Dealer: Stay.")

    def hit(self):
        print("Dealer: Hit.")
        self._hand.addCard(self._deck.getCardFromDeck())

    def getHandValue(self):
        return self._hand.getHandValue()

    def resetHand(self):
        self._hand = Hand()

    def showCardsInHand(self):
        print(f"Dealer's hand: {self._hand} ")


'''d = Dealer()
d.startRound()
d.showCardsInHand()'''
