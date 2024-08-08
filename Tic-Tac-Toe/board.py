from move import Move
from player import Player


class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL], 
                           [Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL], 
                           [Board.EMPTY_CELL, Board.EMPTY_CELL, Board.EMPTY_CELL]]
											 
    def print_board(self):
        print("\nPositions")
        self.print_board_with_positions()
		
        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()
		
    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
  
    def submit_move(self, player, move):
        row = move.get_row()
        column = move.get_column()
        # current content of the board at position
        value = self.game_board[row][column]
        if value == Board.EMPTY_CELL:
            self.game_board[row][column] = player.marker
        else:
            print("This position is already taken. Please enter another one")