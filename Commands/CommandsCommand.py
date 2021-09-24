import discord
import os
from discord.ext import commands

## TODO: Somthing is causing the last few files 'PrefixCommand' and 'SayCommand' to bre printed out quite slowly, try to fix this

class CommandsCommand(commands.Cog):

    def __init__(self, client):
        ## initializes the client
        self.client = client

    @commands.command()
    async def commands(self, ctx):
        for filename in os.listdir('./Commands'):
            if filename.endswith("Command.py"):
                await ctx.send(f'{filename[:-10]}')

def setup(client):
    ## basically connects this to the bot
    client.add_cog(CommandsCommand(client))