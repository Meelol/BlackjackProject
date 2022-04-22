import re
import sys
from user import User
from dealer import Dealer


class Game:
    choice = ""

    def __init__(self, userBalance):
        self._user = User(userBalance)
        self._dealer = Dealer()
        self.potentialEarnings = 0
        self._mode1 = False
        self._mode2 = False
        self._mode3 = False

    def start(self):
        print("Welcome to XBlackjackX by Omar Rodriguez.")
        self.rounds()
        # mode = int(input(
        #    "Select mode: \n (1)Casino Hacker - Card Counter and 1 Deck\n (2)Expert Card Counter - 1 Card Deck \n (3)Test Your Luck - Random Cards\n\nSelect -1 to exit"))

    def rounds(self):
        # User's turn
        self.resetHands()
        self.checkForNewDeck()
        print(f"Current balance: {self._user.getBalance()}")
        self.setBetAndPotential()
        print(f"\nCurrent balance: {self._user.getBalance()}")
        stay = False
        print(f"Bet: {self._user.getBet()}$")
        self._user._hand.addCard(self._dealer.startRound())
        self._dealer.showCardsInHand()
        self._user.showCardsInHand()
        if(self._mode1):
            print(self._dealer._deck.cardCounter)
        while stay == False:
            choice = self.hitOrStay()
            if choice == "hit" or choice == 'h':
                card = self._dealer.giveCardToUser()
                self._user.hit(card)
                self._user.showCardsInHand()
                if(self._mode1):
                    print(f"Card Counter: {self._dealer.getCardCounter()}")
                self.checkForNewDeck()
                if self.bustedHand(self._user._hand):
                    print("You Bust!")
                    break
            else:
                stay = self._user.stay()

        # Dealer's turn
        print("Dealer's Turn:")
        self.checkForNewDeck()
        self._dealer.showCardsInHand()
        self._dealer.dealerAdvancedAI(self._user.getHand())

        # Game's decision
        print("-----------------------------")
        print(
            f"\nPlayer's Hand: {self._user.getHand()}\n Dealer's hand: {self._dealer.getHand()}")
        if(self._user.getHandValue() > self._dealer.getHandValue()):
            print("You win...\n")
            self._user.setBalance(self.potentialEarnings)
            self.rounds()
        elif(self._user.getHandValue() == self._dealer.getHandValue()):
            print("Tie!")
            self._user.setBalance(self._user.getBet())
            self.rounds()
        else:
            print("Better luck next time!\n")
            self.rounds()

    def resetHands(self):
        self._user.resetHand()
        self._dealer.resetHand()

    def setBetAndPotential(self):
        bet = int(input("Place bet (min 20$) or -1 to exit: "))
        if bet == -1:
            print("Thank you for your money! Please comeback!")
            sys.exit()
        if self._user.getBalance() < 20:
            print("Lmao you lost all your money. Come back when you get more!")
            return
        elif bet < 20 or bet > self._user.getBalance():
            print("Please enter a valid amount.")
            self.setBetAndPotential()
        else:
            self._user.setBet(bet)
            self._user.setBalance(-bet)
            self.potentialEarnings = 2 * bet

    def bustedHand(self, hand):
        if hand.getHandValue() > 21:
            return True
        else:
            return False

    def checkForNewDeck(self):
        if self._dealer._deck.cardCounter <= 15:
            print("Dealer: Getting new deck...")
            self._dealer.getNewDeck()

    def hitOrStay(self):
        choice = input("Hit or stay? (Press 'h' for Hit and 's' for Stay)")
        if re.match("H|S|h|s|((h|H)(i|I)(t|T))|((s|S)(t|T)(a|A)(y|Y))", choice):
            return choice.lower()
        else:
            print("Please insert a valid choice.")
            self.hitOrStay()
