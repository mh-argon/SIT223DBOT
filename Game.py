from typing import Tuple
import discord

class Game():
    name = "Game"
    async def create(ctx, channel, user):
        """Called when a user starts a new game"""
        return Game(ctx, channel, user)

    players = []
    def __init__(self, ctx: discord.Client, channel: discord.TextChannel, user):
        self.ctx = ctx
        self.owner = user
        self.players.append(user)
        self.channel = channel
    
    async def play(self):
        """Plays the game in a sequence of display state -> next state -> is_finished loops
        Override for a custom loop"""
        fin = False
        while fin == False:
            await self.state.display()
            self.state: GameState = await self.state.next()
            fin = await self.state.finished()
        winners, msg = fin
        if msg == None:
            # Set default message
            winners_count = len(winners)
            if winners == None or winners_count == 0:
                msg = "You lose :("
            elif winners_count == 1:
                msg = "Congratulations " + winners[0] + "! You Win!"
            else:
                msg = "Congratulations "
                for i, winner in enumerate(winners):
                    msg += winner
                    if i == winners_count - 2:
                        msg += " and " # Comma Here?
                    elif i < winners_count - 2:
                        msg += ", "
                msg += " for winning!"
        await self.send(msg)

    async def send(self, message):
        """Send a message to the current channel.
        Error checked"""
        if message:
            await self.channel.send(message)

    async def read_float(self, prompt:str="", check=None) -> Tuple[discord.Message, float]:
        """Reads the next message that is also an float from a player
        Prompts the player if the message is not an float."""
        message = await self.read_string(prompt, check)
        while not is_float(message.content):
            message = await self.read_string("Please enter a valid number \n" + prompt, check)
        return message, float(message.content)

    async def read_int(self, prompt:str="", check=None) -> Tuple[discord.Message, int]:
        """Reads the next message that is also an integer from a player
        Prompts the player if the message is not an integer."""
        message = await self.read_string(prompt, check)
        while not message.content.isdigit():
            message = await self.read_string("Please enter a valid integer \n" + prompt, check)
        return message, int(message.content)

    # TODO: read only from the correct channel, self.channel
    async def read_string(self, prompt:str="", check=None) -> discord.Message:
        """Read the next message from a player (in the game)
        check function allows you to check for a specific user."""
        await self.send(prompt)

        def _check(m: discord.Message):
            return m.author in self.players and check != None and check(m)

        message: discord.Message = await self.ctx.wait_for("message", check=_check)
        return message
        

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

    async def display(self) -> None:
        """Display the current game state to the user."""
        await self.parent.send(self.to_string())

    def to_string(self) -> str:
        """Return the string representation of the current game state."""
        return self.parent.name + " | Turn Count: " + str(self.index)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
