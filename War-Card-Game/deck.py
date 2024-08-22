import random
from card import Card
from suit import Suit


class Deck:
    # class attribute
    SUITS = ("clubs", "diamonds", "hearts", "spades")
    
    def __init__(self, is_empty=False):
        self._cards = []  # Bottom -> Top
        
        if not is_empty:
            self.build()
        
    # how many cards in the deck?
    @property
    def size(self):
        return len(self._cards)
        
    # creating all cards
    def  build(self):
        for suit in Deck.SUITS:
            for value in range(2, 15):
                self._cards.append(Card(Suit(suit), value))
        
    # show all cards in deck        
    def show(self):
        for card in self._cards:
            # use the .snow() method from the Card class
            card.show()
            
    def shuffle(self):
        random.shuffle(self._cards)
        
    # draw a card from the top of the deck
    def draw(self):
        # if deck not empty
        if self._cards:
            return self._cards.pop()
        else:
            return None
        
    # add card to the bottom of the deck
    def add(self, card):
       self._cards.insert(0, card)