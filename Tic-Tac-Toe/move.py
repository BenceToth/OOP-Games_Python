class Move:

	def __init__(self, value):
		self._value = value
	
	@property
	def value(self):
		return self._value
		
	# expecting 1-9
	def is_valid(self):
		if isinstance(self._value, int):
			return 1 <= self._value <= 9
		else:
			return False
		
	def get_row(self):
		if self.value in (1, 2, 3):
			return 0  # First row
		elif self.value in (4, 5, 6):
			return 1  # Second row
		else:
			return 2  # Third row
		
	def get_column(self):
		if self.value in (1, 4, 7):
			return 0  # First column
		elif self.value in (2, 5, 8):
			return 1  # Second column
		else:
			return 2  # Third column