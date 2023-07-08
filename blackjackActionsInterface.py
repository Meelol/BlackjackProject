from inspect import _void


class blackjackActionsInterface:
    def stay(self):
        raise NotImplementedError("Please implement this function.")

    def hit(self):
        raise NotImplementedError("Please implement this function.")

    def reset_hand(self):
        raise NotImplementedError("Please implement this function.")
