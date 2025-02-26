from enum import Enum, auto

class Suit(Enum):
    CLUBS = auto()
    SPADES = auto()
    DIAMONDS = auto()
    HEARTS = auto()

class Card:
    SUITS = {
        'Clubs': Suit.CLUBS,
        'Hearts': Suit.HEARTS,
        'Spades': Suit.SPADES,
        'Diamonds': Suit.DIAMONDS
    }
    VALUES = {
        'A': 1,
        **{str(x): x for x in range(2, 11)},
        'J': 11,
        'Q': 12,
        'K': 13, 
    }
    suit_names = {n: e for e, n in SUITS.items()}
    value_names = {n: e for e, n in VALUES.items()}

    
    def __init__(self, suit, value):
        self.suit = self.SUITS[suit]
        self.value = self.VALUES[value]

    def __str__(self):
        return f'{self.suit} of {self.value}'

    def hi(self):
        return 'hi'
    
class Game:
    def __init__(self):
        self.cards = []
    
    def add_card(self, suit, value):
        self.cards.append(Card(suit, value))
    
    def card_info(self, card):
        return card.__str__()
    
    def beats_card(self, card1, card2):
        return card1.value > card2.value
        