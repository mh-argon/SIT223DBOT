from Game import *

import random

class GuessNumber(Game):
	name = "Number Guessing"
	alias = [name, "GuessNumber", "GuessMyNumber", "gn"]
	async def create(ctx, channel, user):
		return GuessNumber(ctx, channel, user)

	def __init__(self, ctx, channel, user):
		super().__init__(ctx, channel, user)
		self.state = GuessNumberState(self, random.randint(1, 100))

class GuessNumberState(GameState):
	parent: GuessNumber
	def __init__(self, parent: GuessNumber, number):
		super().__init__(parent, 0)
		self.number = number
		self.fin = False

	async def finished(self):
		if self.fin:
			return [self.parent.owner], "Correct! You guessed my number in " + self.index + " guesses."
		return False

	def to_string(self):
		return "Guess a number between 1 and 100"

	async def next(self):
		self.index += 1
		guess: int = await self.parent.read_int()
		if guess < self.number:
			await self.parent.send("Higher")
		elif guess > self.number:
			await self.parent.send("Lower")
		elif guess == self.number:
			self.fin = True
		return self
