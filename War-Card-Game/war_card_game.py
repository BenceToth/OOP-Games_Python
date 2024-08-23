class WarCardGame:
    
    PLAYER = 0
    COMPUTER = 1
    TIE = 2
    
    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck
        
        self.make_initial_decks()
        
    # create game deck
    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)
        
    # deal out personal decks
    def make_deck(self, character):
        for i in range (26):
            card = self._deck.draw()
            character.add_card(card)
      
    # if one player has a higher card
    def start_battle(self, cards_from_war=None):
        print("\n== Let's Start the Battle ==\n")
        # draw 1 card each
        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()
        
        # show  cards
        print(f"Your card: ")
        player_card.show()
        
        print(f"\nComputer Card: ")
        computer_card.show()
        
        # determine winner
        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)
        
        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_character(self._player,  cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)
            
        return winner
    
    def get_round_winner(self, player_card, computer_card):
        if  player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE
        
    def  get_cards_won(self, player_card, computer_card, previous_cards):
        # joining two card objects to accumulated list of card objects
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:  # returning the two cards used in the battle
            return [player_card, computer_card]
        
    # add cards won to the bottom of the character's deck
    def add_cards_to_character(self,  character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)
            
    def start_war(self, cards_from_battle):
        # draw 3 cards for both characters
        player_cards = []
        computer_cards = []
        
        for i in range(3):
            player_card = self._player.draw_card()
            computer_card = self._computer.draw_card()
            
            player_cards.append(player_card)
            computer_cards.append(computer_card)
            
        print("Six hidden cards: XXX XXX")
        
        # start a new battle, carrying the accumulated cards
        self.start_battle(player_cards + computer_cards + cards_from_battle)