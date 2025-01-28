from enum import Enum, auto

class Suit(Enum):
    CLUBS = auto()
    SPADES = auto()
    DIAMONDS = auto()
    HEARTS = auto()


class Card:
    SUITS = {
        'Clubs': Suit.CLUBS,
        'Spades': Suit.SPADES,
        'Diamonds': Suit.DIAMONDS,
        'Hearts': Suit.HEARTS
    }

    VALUE = {
        'A': 1,
        **{str(n) : n for n in range(2, 11)},
        'J': 11,
        'Q': 12,
        'K': 13,
    }
    SUIT_NAMES = {e: n for n, e in SUITS.items()}
    VALUE_NAMES = {e: n for n, e in VALUE.items()}

    def __init__(self, suit, value):
        self.suit = self.SUITS[suit]
        self.value = self.VALUE[value]
        
    def __str__(self) -> str:
        return f"{self.VALUE_NAMES[self.value]} of {self.SUIT_NAMES[self.suit]}"


class Joker(Card):
    COLOURS = {
        'Red': 'Red',
        'Black': 'Black'
    }
    COLOUR_NAMES = {e: n for n, e in COLOURS.items()}
    
    def __init__(self, color):
        self.color = self.COLOURS[color]
        self.value = 14
        
    def __str__(self) -> str:
        return f"{self.COLOUR_NAMES[self.color]} Joker"
        


class Game:
    def __init__(self):
        self.cards: list[Card] = []
    
    def add_card(self, suit, value):
        self.cards.append(Card(suit, value))
        
    def add_joker(self, color):
        self.cards.append(Joker(color))
        
    def card_string(self, card):
        return str(self.cards[card])
    
    def card_beats(self, card1, card2):
        return self.cards[card1].value > self.cards[card2].value
    
    
        
if __name__ == "__main__":
    game = Game()
    suit, value = "Joker Red".split()
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = "Spades K".split()
    game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")