# War Card Game in Python
This project implements a console-based version of the classic ["War" card game](https://en.wikipedia.org/wiki/War_(card_game)). The game is played between a player and the computer, where each player draws a card, and the player with the higher card value wins the round. In case of a tie, a "war" is initiated, where additional cards are drawn to determine the winner.

The main objective of this project is to simulate the War card game, allowing the player to compete against the computer. The game continues until one of the players runs out of cards.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/BenceToth/OOP-Games_Python.git
   ```
2. Navigate to the project directory:
   ```
   cd War-Card-Game
   ```

## How to Play

1. Run `main.py` to start the game.
```
python main.py
```
2. Enter your name when prompted.
3. The game will automatically deal cards and start the first round.
4. After each round, you'll see the outcome and be asked if you're ready for the next round.
5. The game ends when one player runs out of cards or you decide to quit.

## Requirements

- Python 3.x

## Modules and Classes
### 1. `main.py`
This is the entry point of the game. It initializes the player, computer, deck, and the game instance, then runs the game loop until the player decides to quit or one of the players runs out of cards.

### 2. `war_card_game.py`
This module contains the `WarCardGame` class, which manages the core game logic.

#### `WarCardGame` Class
- **Attributes:**
  - `_player`: An instance of the `Player` class representing the human player.
  - `_computer`: An instance of the `Player` class representing the computer.
  - `_deck`: An instance of the `Deck` class representing the main deck of cards.
  
- **Methods:**
  - `__init__(player, computer, deck)`: Initializes the game with player, computer, and deck.
  - `make_initial_decks()`: Shuffles the main deck and distributes cards to the player and computer.
  - `make_deck(character)`: Deals 26 cards to the specified character (player or computer).
  - `start_battle(cards_from_war=None)`: Handles a single round of battle between the player and the computer.
  - `get_round_winner(player_card, computer_card)`: Determines the winner of the round based on the card values.
  - `get_cards_won(player_card, computer_card, previous_cards)`: Collects the cards won in the round.
  - `add_cards_to_character(character, list_of_cards)`: Adds the won cards to the bottom of the winner's deck.
  - `start_war(cards_from_battle)`: Initiates a "war" in case of a tie.
  - `check_game_over()`: Checks if the game is over (i.e., if any player has run out of cards).
  - `print_stats()`: Prints the current stats of the game (number of cards each player has).
  - `print_welcome_message()`: Prints a welcome message at the start of the game.

### 3. `suit.py`
This module contains the `Suit` class, which represents the suit of a card.

#### `Suit` Class
- **Attributes:**
  - `_description`: A string representing the description of the suit (e.g., "hearts").
  - `_symbol`: A string representing the symbol of the suit (e.g., "♥").
  
- **Properties:**
  - `description`: Returns the description of the suit.
  - `symbol`: Returns the symbol of the suit.

### 4. `card.py`
This module contains the `Card` class, which represents a single playing card.

#### `Card` Class
- **Attributes:**
  - `_suit`: An instance of the `Suit` class representing the card's suit.
  - `_value`: An integer representing the card's value (2-14, where 11-14 represent Jack, Queen, King, and Ace).
  
- **Methods:**
  - `show()`: Prints the card's value and suit.
  
- **Properties:**
  - `value`: Returns the card's value.
  - `suit`: Returns the card's suit.

### 5. `deck.py`
This module contains the `Deck` class, which represents a deck of playing cards.

#### `Deck` Class
- **Attributes:**
  - `_cards`: A list of `Card` instances representing the deck.
  
- **Methods:**
  - `__init__(is_empty=False)`: Initializes the deck. If `is_empty` is `False`, it generates a full deck of 52 cards.
  - `shuffle()`: Shuffles the deck.
  - `draw()`: Draws a card from the top of the deck.
  - `add_card(card)`: Adds a card to the bottom of the deck.
  - `size()`: Returns the number of cards left in the deck.

### 6. `player.py`
This module contains the `Player` class, which represents a player in the game.

#### `Player` Class
- **Attributes:**
  - `name`: The name of the player.
  - `deck`: An instance of the `Deck` class representing the player's deck.
  - `is_computer`: A boolean indicating whether the player is the computer or a human.
  
- **Methods:**
  - `draw_card()`: Draws a card from the player's deck.
  - `add_card(card)`: Adds a card to the player's deck.
  - `has_empty_deck()`: Checks if the player's deck is empty.

