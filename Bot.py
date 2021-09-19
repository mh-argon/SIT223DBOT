import discord
import os

import Game

from GuessNumber import GuessNumber

# Registered Games
registered_games = [
    GuessNumber
]

# Games that have been created but not started yet. user:game
starting_games = {}
# Games that have been started but haven't finished yet.
running_games = {}

ctx = discord.Client()

prefix = "/"

@ctx.event
async def on_ready():
    print('We have logged in as {0.user}'.format(ctx))

@ctx.event
async def on_message(message: discord.Message):
    if message.author == ctx.user:
        return

    msg: str = message.content
    msg_lower = msg.lower()

    global prefix
    if msg_lower.startswith(prefix):
        command = msg_lower[len(prefix):].split(" ")
        root = command[0]
        # TODO: test python 3.10 match case
        # TODO: command alias system
        # TODO: register commands somewhere else?
        # TODO: help command (default to this?)
        # TODO: errors if wrong output
        # TODO: better system to retrieve arguments
        if root == "game":
            if message.author in starting_games.keys():
                await message.channel.send("Game Already Started. Use the " + prefix + "cancel command to cancel that game.")
                return
            if await start_game(ctx, message.channel, msg[(len(prefix) + len("game ")):], message.author):
                await message.channel.send("Started Game!")
            else:
                await message.channel.send("No Game Found.")
        elif root == "say":
            await message.channel.send(msg[(len(prefix) + len("say ")):])
        elif root == "prefix":
            prefix = msg[(len(prefix) + len("prefix ")):]
            await message.channel.send("Set prefix to: '" + prefix + "'")
        elif root == "play":
            if not message.author in starting_games.keys():
                await message.channel.send("No Game Found. Create a game with the " + prefix + "game command first")
                return
            game: Game.Game = starting_games[message.author]
            if game.channel != message.channel:
                await message.channel.send("Invalid channel. You can only play a game in the server/channel you created it in.")
                return
            starting_games.pop(message.author)
            if not game.owner in running_games.keys():
                running_games[game.owner] = []
            running_games[game.owner].append(game)
            await game.play()
            running_games[game.owner].remove(game)

async def start_game(ctx, channel, name, user) -> bool:
    for game in registered_games:
        if is_match(name, game.alias):
            starting_games[user] = await game.create(ctx, channel, user)
            return True
    return False

def is_match(input: str, alias: list()):
    return input.lower() in (s.lower() for s in alias)

# TODO: make sure everyone has created this file (warning maybe?)
with open("API_KEY.txt", "r") as f:
    key = f.read()
ctx.run(key)
