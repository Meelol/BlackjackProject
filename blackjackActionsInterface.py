from inspect import _void


class blackjackActionsInterface:
    def stay(self):
        raise NotImplementedError("Please implement this functon.")

    def hit(self):
        raise NotImplementedError("Please implement this functon.")

    def resetHand(self):
        raise NotImplementedError("Please implement this functon.")
