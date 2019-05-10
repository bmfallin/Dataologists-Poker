from card import Card
from colorama import Fore, Back, Style

class PokerHand():
    """
    This class is used to represent a poker hand
    """

    def __iter__(self):
        """
        The cards of the hand

        Yields:
            list: The cards of this hand
        """
        yield from self.cards
    
    def __str__(self):
        """
        The ASCII string representation of the hand

        Returns:
            str: The ASCII string representation of the hand
        """

        lines = []
        
        card_output = ["","","",""]
        for card in self.cards:
            card_lines = card.card_ascii
            for i in range(4):
                card_output[i] += card_lines[i]

        lines.append("Type: " + self.hand_name)

        return "\n".join(card_output + lines)

    @property
    def cards(self):
        """
        The cards of this hand

        Returns:
            list: A list of cards in this hand
        """
        return self.__cards

    @property
    def hand_name(self):
        """
        The name of the hand

        Returns:
            str: The name of the type of this hand as reported by the
                 Kaggle Dataset
        """
        names = [
            "High Card",
            "One Pair",
            "Two Pair",
            "Three of a kind",
            "Straight",
            "Flush",
            "Full house",
            "Four of a kind",
            "Straight flush",
            "Royal flush"
        ]

        return names[self.__hand_type]

    @staticmethod
    def from_cards(cards, hand_type):
        """
        static construction method for the PokerHand class

        This method will return a new instance of the PokerHand
        class from five cards and a hand type

        Args:
            cards     (List): A list of five instances of the Card class
            hand_type  (int): The hand type as reported by the Kaggle Dataset

        Returns:
            PokerHand: A new instance of the PokerHand class
        """
        assert (isinstance(cards, list)), "Cards parameter must be a list of cards!"
        assert (len(cards) == 5), "PokerHand must be instantiated with five cards!"
        for card in cards:
            assert (isinstance(card, Card)), "All items in cards list must be of type Card!"

        assert (isinstance(hand_type, int), "hand_type must be of type int!")

        hand = PokerHand()
        hand.__cards = cards
        hand.__hand_type = hand_type
        return hand

    @staticmethod
    def from_csv_row(row):
        """
        static construction method for the PokerHand class

        This method will create a new instance of the PokerHand
        class from a csv row as defined in the Kaggle Dataset
        in the README.md

        Args:
            row (List): A list of strings as defined in the Kaggle Dataset

        Returns:
            PokerHand: A new instance of the PokerHand class
        """
        assert (isinstance(row, list)), "rows parameter must be a list of cards!"
        assert (len(row) == 11), "PokerHand must be instantiated with five cards!"
        for item in row:
            assert (isinstance(item, str)), "All items in cards list must be of type String!"

        cards = []
        for index in range(0,10,2):
            card = Card(int(row[index]), int(row[index + 1]))
            cards.append(card)

        hand = PokerHand()
        hand.__cards = cards
        hand.__hand_type = int(row[10])
        return hand
