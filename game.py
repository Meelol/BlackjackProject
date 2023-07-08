import re
import sys
import time
from user import User
from dealer import Dealer


class Game:
    choice = ""

    def __init__(self, user_balance):
        self._user = User(user_balance)
        self._dealer = Dealer()
        self.potential_earnings = 0
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
        self.reset_hands()
        self.check_for_new_deck()
        print(f"Current balance: {self._user.get_balance()}")
        self.set_bet_and_potential()
        print(f"\nCurrent balance: {self._user.get_balance()}")
        stay = False
        print(f"Bet: {self._user.get_bet()}$")
        self._user._hand.add_card(self._dealer.start_round())
        self._dealer.show_cards_in_hand()
        self._user.show_cards_in_hand()
        if(self._mode1):
            print(self._dealer._deck._total_cards)
        while stay == False:
            choice = self.hit_or_stay()
            if choice == "hit" or choice == 'h':
                card = self._dealer.give_card_to_user()
                self._user.hit(card)
                self._user.show_cards_in_hand()
                if(self._mode1):
                    print(f"Card Counter: {self._dealer.get_card_counter()}")
                self.check_for_new_deck()
                if self.busted_hand(self._user._hand):
                    print(self._user._hand.get_hand_value())
                    print("You Bust!")
                    self.rounds()
            else:
                stay = self._user.stay()

        # Dealer's turn
        print("Dealer's Turn:")
        sys.stdout.flush()
        self.check_for_new_deck()
        self._dealer.show_cards_in_hand()
        time.sleep(2)
        self._dealer.dealer_advanced_AI(self._user.get_hand())

        # Game's decision
        print("-----------------------------")
        print(
            f"\nPlayer's Hand: {self._user.get_hand()}\n Dealer's hand: {self._dealer.get_hand()}")
        if self._user.get_hand_value() > self._dealer.get_hand_value() or self._dealer.get_hand_value() > 21 :
            print("You win...\n")
            self._user.set_balance(self.potential_earnings)
            self.rounds()
        elif self._user.get_hand_value() == self._dealer.get_hand_value():
            print("Tie!")
            self._user.set_balance(self._user.get_bet())
            self.rounds()
        else:
            print("Better luck next time!\n")
            self.rounds()

    def reset_hands(self):
        self._user.reset_hand()
        self._dealer.reset_hand()

    def set_bet_and_potential(self):
        try:
            bet = int(input("Place bet (min 20$) or -1 to exit: "))
            if bet == -1:
                print("Thank you for your money! Please comeback!")
                sys.exit()
            if self._user.get_balance() < 20:
                print("You lost all your money. Come back when you get more!")
                sys.exit()
            elif bet < 20 or bet > self._user.get_balance():
                print("Please enter a valid amount.")
                self.set_bet_and_potential()
            else:
                self._user.set_bet(bet)
                self._user.set_balance(-bet)
                self.potential_earnings = 2 * bet
        except ValueError:
            print("Please insert a valid value.")
            self.set_bet_and_potential()
        

    def busted_hand(self, hand):
        if hand.get_hand_value() > 21:
            return True
        else:
            return False

    def check_for_new_deck(self):
        if self._dealer._deck._total_cards <= 15:
            print("Dealer: Getting new deck...")
            self._dealer.get_new_deck()

    def hit_or_stay(self):
        choice = input("Hit or stay? (Press 'h' for Hit and 's' for Stay)")
        if re.match("H|S|h|s|((h|H)(i|I)(t|T))|((s|S)(t|T)(a|A)(y|Y))", choice):
            return choice.lower()
        else:
            print("Please insert a valid choice.")
            self.hit_or_stay()

