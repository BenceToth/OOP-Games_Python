# Tic-Tac-Toe Game in Python
This repository contains an implementation of the classic Tic-Tac-Toe game using Python. This project is designed to practice object-oriented programming (OOP) concepts.

## Files
* `board.py`: Contains the `Board` class, which manages the game board, prints the board, submits moves, and checks for game over conditions.
* `move.py`: Contains the `Move` class, which handles the coordinates of each move while validating the input.
* `player.py`: Contains the `Player` class, which can be either a human or computer player. It serves and an interface to input moves from the human player and generates a random move for the computer player. 
* tic-tac-toe.py: Contains the TicTacToeGame class, which orchestrates the game flow and start the game.

## Installation
1. Clone the repository:

   ```git clone https://github.com/BenceToth/OOP-Games_Python.git```

4. Navigate to the project directory:

   ```cd Tic-Tac-Toe```

## Usage
Run the tic-tac-toe.py script to start the game:

```python tic-tac-toe.py```


## Classes and Methods
### Board Class (board.py)
**Attributes**:
* EMPTY_CELL: Constant representing an empty cell on the board.
* game_board: 3x3 matrix representing the Tic-Tac-Toe board.
**Methods**:
* \__init__(): Initializes the game board with empty cells.
* print_board(): Prints the current state of the board.
* print_board_with_positions(): Prints the board positions for reference.
* submit_move(player, move): Submits a move for a player.
* check_is_game_over(player, last_move): Checks if the game is over.
* check_row(player, last_move): Checks if a row is complete.
* check_column(player, last_move): Checks if a column is complete.
* check_diagonal(player): Checks if the main diagonal is complete.
* check_antidiagonal(player): Checks if the anti-diagonal is complete.
* check_is_tie(): Checks if the game is a tie.
* reset_board(): Resets the game board.
  
### Move Class (move.py)
**Attributes**:
* position: Position of the move (1-9).

**Methods**:
* \__init__(position): Initializes the move with a position.
* get_row(): Returns the row index of the move.
* get_column(): Returns the column index of the move.

### Player Class (player.py)
**Attributes**:
* is_human: Boolean indicating if the player is human.
* marker: Player's marker ('X' or 'O' by default).
**Methods**:
* \__init__(is_human=True): Initializes the player.
* get_move(): Gets the player's move (either from user input or computer logic).

### TicTacToeGame Class (tic-tac-toe.py)
**Methods**:
* start(): Starts the game and manages the game loop.
* start_new_round(board): Starts a new round by resetting the board.

## Game Flow
1. The game starts and welcomes the player.
2. The board is printed with the current state.
3. The human player makes a move by entering a position (1-9).
4. The move is submitted and the board is updated.
5. The game checks for a win, loss, or tie.
6. If the game is not over, the computer makes a move.
7. The game checks for a tie.
8. Steps 3-6 repeat until the game ends.
9. The player is asked if they want to play again.
