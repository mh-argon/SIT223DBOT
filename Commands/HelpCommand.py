import discord
import os
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class HelpCommand(commands.Cog):

    def __init__(self, client):
        ## initializes the client
        self.client = client

    @commands.command(name="help", aliases=[""])
    async def help(self, ctx, command_name = None):
        if command_name == None:
            await ctx.send("Please type the command you wish to learn more about i.e /help [command name]")

        if command_name.lower() == "clear":
            await ctx.send("Clear allows the removal of lines in discord.\nThe format is /clear [amount of lines] \nExample: /clear 3")

        if command_name.lower() == "command":
            await ctx.send("Command lists all available commands.\nFor commands type /commands")

        if command_name.lower() == "game":
            await ctx.send("Game is how you select the game you want to play.\nFor example to play conenct four type /game C4")
            
            available_games = ""
            for game_name in os.listdir('./Games'):
                if game_name.endswith(".py"):
                    available_games += ((f'{game_name[:-3]}') + " ")
            await ctx.send("Available Games: " + available_games)
        
        if command_name.lower() == "invite":
            await ctx.send("Invite allows you to invite another player to your game.\n It is done in this format /invite [username]")

        if command_name.lower() == "play":
            await ctx.send("Play is the command for starting the game. Once you select a game (i.e /game C4) you can use /play to star the game")

        if command_name.lower() == "prefix":
            await ctx.send("Prefix sets the prefix of the commands for example (/prefix x) would set the prefix to x meaning future commands would be written as xgame")

        if command_name.lower() == "say":
            await ctx.send("Say is the command that allows you to make the bot say something such as typeing (/say hi) the bot would say hi")



def setup(client):
    ## basically connects this to the bot
    client.add_cog(HelpCommand(client))