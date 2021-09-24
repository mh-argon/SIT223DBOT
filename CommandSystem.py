import discord
import os
import Game

from discord.ext import commands

## TODO: Create CommandSystem helper function that wraps the incoming string
## TODO: Create overall layout of the commandsystem (Complete)
## TODO: Set a overall help feature in case the inputted value is not of the list
## TODO: command alias system  
## TODO: register commands somewhere else?
## TODO: help command 
## TODO: errors if wrong output
## TODO: better system to retrieve arguments

## mainly using this for test will replace so we can use commands from bot.py
client = commands.Bot(command_prefix = '/')

## Currently this acts as a method of loading in the commands from the folder
class CommandSystemHandler():
    
    ## for loading in commands
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'Commands.{extension}')

    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'Commands.{extension}')

    for filename in os.listdir('./Commands'):
        if filename.endswith('Command.py'):
            client.load_extension(f'Commands.{filename[:-3]}')
    
    ## testing will make it so it runs when bot.py is run
    #client.run('ODgzNTk3MzAxNjIzNDM1MjY2.YTMQHQ.a32AQJJMpJqncRWv4Ka5RQBnMio')


    





        