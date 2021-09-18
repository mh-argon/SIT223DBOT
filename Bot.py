import discord
import os

import Game

from GuessNumber import GuessNumber

games = [
    GuessNumber
]

# TODO: track active games and stuff
active_games = []

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
        command = msg_lower.split(" ")
        root = command[0].removeprefix(prefix)
        # TODO: test python 3.10 match case
        # TODO: command alias system
        # TODO: register commands somewhere else?
        # TODO: help command (default to this?)
        # TODO: errors if wrong output
        # TODO: better system to retrieve arguments
        if root == "game":
            await start_game(ctx, message.channel, command[1], message.author)
            await message.channel.send("Started Game!")
        elif root == "say":
            await message.channel.send(msg[(len(prefix) + len("say ")):])
        elif root == "prefix":
            prefix = msg[(len(prefix) + len("prefix ")):]
            await message.channel.send("Set prefix to: '" + prefix + "'")
        elif root == "play":
            await active_games[0].play()

async def start_game(ctx, channel, name, user):
    for game in games:
        if is_match(name, game.alias):
            active_games.append(await game.create(ctx, channel, user))

def is_match(input: str, alias: list()):
    return input.lower() in (s.lower() for s in alias)

# TODO: make sure everyone has created this file (warning maybe?)
with open("API_KEY.txt", "r") as f:
    key = f.read()
ctx.run(key)
