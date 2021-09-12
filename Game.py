import discord

class Game():
	name = "Game"
	async def create(ctx, channel, user):
		return Game(ctx, channel, user)

	players = []
	def __init__(self, ctx: discord.Client, channel: discord.TextChannel, user):
		self.ctx = ctx
		self.owner = user
		self.players.append(user)
		self.channel = channel
	
	async def play(self):
		self.state: GameState
		fin = False
		while fin == False:
			await self.state.display()
			self.state = await self.state.next()
			fin = await self.state.finished()

	async def send(self, message):
		await self.channel.send(message)

	async def read_int(self, prompt:str="") -> int:
		out = await self.read_string(prompt)
		while not out.isdigit():
			await self.send("Please enter a valid integer")
			out = await self.read_string(prompt)
		return int(out)

	async def read_string(self, prompt:str="") -> str:
		if prompt:
			await self.send(prompt)

		def check(m: discord.Message):
			return m.author in self.players

		return str(await self.ctx.wait_for("message", check=check))
		

class GameState():
	def __init__(self, parent: Game, index):
		self.parent = parent
		self.index = index

	async def next(self):
		"""Return the next game state. 
		Read user move here"""
		return None

	async def finished(self):
		"""Check if the game has been won/finished and return the winner and the result message.
		Return False if the game has not finished yet.
		Return ([] or [winners], None or custom message) otherwise."""
		return False

	async def display(self):
		"""Display the current game state to the user."""
		await self.parent.send(self.to_string())

	def to_string(self) -> str:
		"""Return the string representation of the current game state."""
		return self.parent.name + " | Turn Count: " + str(self.index)
