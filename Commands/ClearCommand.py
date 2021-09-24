import discord
from discord.ext import commands

class ClearCommand(commands.Cog):

    def __init__(self, client):
        ## initializes the client
        self.client = client

    # Events 
    #@commands.Cog.listener()
    #async def on_ready(self):
    #    print('Bot is online')

    # Commands
    #@commands.command()
    #async def ping(self, ctx):
    #    await ctx.send("Pong!")

    @commands.command()
    async def clear(self, ctx, amount = 0):
        if amount > 0:
            amount += 1
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("The amount inputted was invalid")

def setup(client):
    ## basically connects this to the bot
    client.add_cog(ClearCommand(client))