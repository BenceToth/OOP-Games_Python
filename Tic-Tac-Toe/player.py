
import random

from move import Move


class Player:
	# class attributes
	PLAYER_MARKER = "X"
	COMPUTER_MARKER = "O"
	
	def __init__(self, is_human=True):
		self._is_human = is_human
		
		# assign markers
		if is_human:
			self._marker = Player.PLAYER_MARKER
		else:
			self._marker = Player.COMPUTER_MARKER
			
	# read-only attributes
	@property
	def is_human(self):
		return self._is_human
		
	@property
	def marker(self):
		return self._marker
		
	def get_move(self):
		if self._is_human:
			return self.get_human_move()  # need to return explicitly
		else:
			return self.get_computer_move()
		
	def get_human_move():
		# loop until user enters a valid input
		while True:
			user_input = int(input("Please enter your move (1-9): "))
			move = Move(user_input)
			if move.is_valid():
				break  # exit
			else:
				print("Please enter an integer between 1 and 9.")
				
	def get_computer_move():
		random_choice = random.choice(list(range(1, 10)))
		move = Move(random_choice)
		print("Computer move (1-9):", move.value)
		return move