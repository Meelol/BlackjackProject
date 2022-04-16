import random


class Suit:
    def __init__(self, suit):
        self.symbol = ""
        self.suit = suit
        self.cards = []

    def crearCartas(self):
        numeros = ["A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K"]
        for i in numeros:
            self.cards.append(i+" "+self.suit)

        return self.cards


class Deck:
    def __init__(self, *args):
        self.deck = []
        for i in args:
            self.deck = self.deck + i

    def entregarDeck(self):
        return self.deck


suit1 = Suit(u"\u2666")
suit2 = Suit(u"\u2665")
suit3 = Suit(u"\u2663")
suit4 = Suit(u"\u2660")

cartas1 = suit1.crearCartas()
cartas2 = suit2.crearCartas()
cartas3 = suit3.crearCartas()
cartas4 = suit4.crearCartas()

cartas = Deck(cartas1, cartas2, cartas3, cartas4)


def crearMazo():

    suit1 = Suit(u"\u2666")
    suit2 = Suit(u"\u2665")
    suit3 = Suit(u"\u2663")
    suit4 = Suit(u"\u2660")

    cartas1 = suit1.crearCartas()
    cartas2 = suit2.crearCartas()
    cartas3 = suit3.crearCartas()
    cartas4 = suit4.crearCartas()

    cartas = Deck(cartas1, cartas2, cartas3, cartas4)

    playing_deck = cartas.entregarDeck()

    return playing_deck


playing_deck = cartas.entregarDeck()

print(random.choice(playing_deck)[2])

print(cartas.entregarDeck())


# print(suit.cards)

# print(suit.cards[0][0])

#valueDict = {"A": 1, }

#carta = suit.cards[0][0]

# print(valueDict[carta])
