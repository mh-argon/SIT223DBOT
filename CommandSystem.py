import discord
import os
from Commands.HelpCommand import HelpCommand
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
## TODO: make the system print the commands in one line

## mainly using this for test will replace so we can use commands from bot.py
client = commands.Bot(command_prefix = '/', help_command=None)

## Currently this acts as a method of loading in the commands from the folder
class CommandSystemHandler():

    ## for loading in commands
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'Commands.{extension}')

    ## unloads the command
    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'Commands.{extension}')

    ## for every filename in the directory
    for filename in os.listdir('./Commands'):
        ## if the filename ends with Command.py
        if filename.endswith('Command.py'):
            ## load the file removing the .py at the end.
            client.load_extension(f'Commands.{filename[:-3]}')

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Please type the command you wish to learn more about i.e /help [command name]")
        

    ## the test API_Key
    with open("API_KEY.txt", "r") as f:
        key = f.read()
    client.run(key)


    





        