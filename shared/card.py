from colorama import Fore, Back

class Card:
    """
    This class is used to represent a playing card
    """

    def __init__(self, suit, value):
        """
        The constructor for the Card class

        Args:
            value (int): The face value of the card
            suit  (int): The suit of the card
        """
        self.__value = value
        self.__suit = suit

    def __str__(self):
        return "\n".join(self.card_ascii)

    @property
    def card_name(self):
        """
        The name of the card

        Returns:
            str: The name of the card

        Example:
            "Ace of Spades"
        """
        return "{} of {}".format(self.value_name, self.suit_name)

    @property
    def short_name(self):
        """
        The short name of the card

        Returns:
            str: The short name of the cards

        Example:
            "8H", "AD", "10S"
        """
        try:
            return "{}{}".format(str(int(self.value_name)), self.suit_symbol)
        except ValueError:
            return "{}{}".format(self.value_name[0], self.suit_symbol)

    @property
    def suit(self):
        """
        The suit of the card

        Returns:
            int: The suit of the card
        """
        return self.__suit

    @property
    def suit_name(self):
        """
        The suit name of the card

        Returns:
            str: The suit of the card

        Example:
            "Spades", "Diamonds"
        """
        names = ["Hearts", "Spades", "Diamonds", "Clubs"]
        return names[self.suit - 1]

    @property
    def suit_symbol(self):
        """
        The symbol of the card

        Returns:
            str: an ASCII version of the suit symbol

        Example:
            "♥", "♠", "♦", "♣"
        """

        symbols = ["♥", "♠", "♦", "♣"]
        return symbols[self.suit - 1]

    @property
    def value(self):
        """
        The value of the card

        Returns:
            int: The face value of this card
        """
        return self.__value

    @property
    def value_name(self):
        """
        The value name of the card

        Returns:
            str: The face value name of the card

        Example: 
            "King"
        """
        if self.value == 1:
            return "Ace"

        if self.value == 11:
            return "Jack"

        if self.value == 12:
            return "Queen"

        if self.value == 13:
            return "King"

        return str(self.value)                                                                                  

    @property
    def short_value_name(self):
        """
        The short version of the value name

        Returns:
            str: The short version of the value name

        Example:
            "8", "J", "A"
        """
        try:
            return str(int(self.value_name))
        except ValueError:
            return self.value_name[0]
        
    @property
    def card_ascii(self):
        """
        The ASCII representation of the card

        Returns:
            list: A list of strings representing the ASCII
                  version of the card
        """

        lines = []

        beg = Fore.BLACK + Back.WHITE
        end = Fore.RESET + Back.RESET

        lines.append(beg + "╔═══╗" + end)

        if self.suit_symbol == "♥" or self.suit_symbol == "♦":
            symbol = Fore.RED + self.suit_symbol + Fore.BLACK
        else:
            symbol = self.suit_symbol

        lines.append(beg + "║ {} ║".format(symbol) + end)

        if(len(self.short_value_name) == 2):
            lines.append(beg + "║{} ║".format(self.short_value_name) + end)
        else:
            lines.append(beg + "║ {} ║".format(self.short_value_name) + end)

        lines.append(beg + "╚═══╝" + end)

        return lines