import discord
import os
from discord.ext import commands

class CommandsCommand(commands.Cog):

    def __init__(self, client):
        ## initializes the client
        self.client = client

    @commands.command()
    ## will detail the commands available. In this case the commands are foudn by the names of the files in the directory
    async def commands(self, ctx):
        ## creating an empty string to return as valid commands
        return_filename = ""
        ## checks for every item in the directory /Commands
        for filename in os.listdir('./Commands'):
            ## if the filename endswith Commands.py, also prevents random files being printed
            if filename.endswith("Command.py"):
                ## adds the names without the Command.py hence only giving filename
                return_filename += (("/" + f'{filename[:-10]}') + " ")
        ##  returns the string with the commands in it
        await ctx.send("Commands: " + return_filename)
        ## tells the user some basic commands
        await ctx.send("for more information on the commands type /help [name of command] and example being /help clear")
            

def setup(client):
    ## basically connects this to the bot
    client.add_cog(CommandsCommand(client))