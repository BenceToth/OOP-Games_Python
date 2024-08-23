# Dice Game in Python
This folder contains an implementation of a simple dice game developed to practice object-oriented programming (OOP) in Python. The game involves a player competing against a computer by rolling dice, with the goal to reach a counter value of zero first.

## Installation
1. Clone the repository:

   ```git clone https://github.com/BenceToth/OOP-Games_Python.git```

4. Navigate to the project directory:

   ```cd The-Dice-Game```


## Usage
Run the tic-tac-toe.py script to start the game:

```python dice-game.py```

## Classes and Methods
### Die Class
The Die class represents a single six-sided die.

**Methods**:
* \__init__(): Initializes the die with no value.
* roll(): Rolls the die and updates its value with a random number between 1 and 6.
* value(): Property that returns the current value of the die.
  
### Player Class
The Player class represents a player in the game, which can be either a human or a computer.

**Attributes**:
* die: Returns the player's die.
* is_computer: Returns if the player is a computer.
* counter: Returns the player's counter.

**Methods**:
* \__init__(die, is_computer=False): Initializes the player with a die and a counter set to 10. The is_computer flag indicates if the player is a computer.
* increment_counter(): Increments the player's counter by 1.
* decrement_counter(): Decrements the player's counter by 1.
* roll_die(): Rolls the player's die.

### DiceGame Class
The DiceGame class manages the flow of the game.

**Methods**:
* \__init__(player, computer): Initializes the game with a human player and a computer player.
* play(): Starts and manages the game loop.
* play_round(): Plays a single round of the game.
* print_round_welcome(): Prints a welcome message for a new round.
* roll_dice(): Rolls dice for both the player and the computer.
* show_dice(player_value, computer_value): Displays the values of the rolled dice.
* update_counters(winner, loser): Updates the counters of the winner and the loser.
* show_counters(): Displays the current counters of the player and the computer.
* check_game_over(): Checks if the game is over.
* show_game_over(winner): Displays the game over message and the winner.
