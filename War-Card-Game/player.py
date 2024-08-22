class Player:
    
    def __init__(self, name, deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer
        
    @property
    def is_computer(self):
        return self._is_computer
    
    # check if player's own deck is empty
    def has_empty_deck(self):
        # use size property from the Deck class
        return self._deck.size == 0
    
    # draw card from the top of the player's own deck
    def draw_card(self):
        if not self.has_empty_deck():
            # use draw method from the Deck class
            return self._deck.draw()
        else:
            None
         
    # add card to the bottom of the deck   
    def add_card(self, card):
        self._deck.add(card)