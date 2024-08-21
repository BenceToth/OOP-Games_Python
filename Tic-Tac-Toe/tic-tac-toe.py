from board import Board
from player import Player


class TicTacToeGame:
    
    def start(self):
        print("**************************")
        print("  Welcome to Tic-Tac-Toe  ")
        print("**************************")
        
        board = Board()
        human = Player()
        computer = Player(is_human=False)
        
        while True:  # Game
            
            board.print_board()
            
            while True:  # Round
                human_move = human.get_move()
                board.submit_move(human, human_move)
                board.print_board()
                
                # if human won
                if board.check_is_game_over(human, human_move):
                    print("Awesome. You won the game! 🎉")
                    break
                
                # computer moves
                computer_move = computer.get_move()
                board.submit_move(computer, computer_move)
                board.print_board()
                
                # if computer won
                if board.check_is_game_over(computer, computer_move):
                    print("Oops...😨 The computer won. Try again.")
                    break
                elif board.check_is_tie():
                    print("It's a tie! 👍 Try again.")
                    break
            
            play_again = input("Would you like to play again? Enter X for YES or O for NO: ").upper()
            
            if play_again == "O":
                print("Bye! Come back soon 👋")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again 💡")
                self.start_new_round(board)
                
    def start_new_round(self, board):
        print("*************")
        print("  New Round  ")
        print("*************")
        board.reset_board()


# Start Game  
game = TicTacToeGame()
game.start()