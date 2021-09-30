import discord
import os
from discord.ext import commands

class GameCommand(commands.Cog):

    def __init__(self, client):
        ## initializes the client
        self.client = client


    

def setup(client):
    ## basically connects this to the bot
    client.add_cog(GameCommand(client))