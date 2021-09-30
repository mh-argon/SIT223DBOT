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

    # Example of errors
    #@commands.Cog.listener()
    #async def on_command_error(self, ctx, error):
    #    if isinstance(error, commands.MissingRequiredArgument):
    #        await ctx.send("Testing")

    @commands.command()
    async def clear(self, ctx, amount : int):
        if amount > 0:
            amount += 1
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("The amount inputted was invalid")


    ## basically will run only if a missing requried argument error occurs for clear method
    @clear.error
    ## takes in self, context, and error and returns a string as of now
    async def clear_error(self, ctx, error):
        ## if the instance has a error and the commands MissingRequiredArgument is true
        if isinstance(error, commands.MissingRequiredArgument):
            ## prints out a statement relating to a plausaible fix
            await ctx.send("Please input a value into the command i.e /clear 5")

def setup(client):
    ## basically connects this to the bot
    client.add_cog(ClearCommand(client))