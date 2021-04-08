import discord
import asyncio

from Games.TicTacToe import TicTacToe
from src.youtubeAPI import YouTubeHandler

class PetThePanda(discord.Client):
    commands = {
        "PetThePeepo" : "!Pet the peepo",
        "CommandsList" : '!INeedSomeHelp',
        "TicTacToe" : "!start TicTacToe",
        "TicTacToeNextTurn" : "!next "
    }
    reactToMessageAuthors = [
        "Madafii",
        "Ƭhalthყ"
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ticTacToe = TicTacToe()

    async def on_ready(self):
        print(self.user.name+ " is ready")

    async def status_task(self):
        await self.change_presence(activity=discord.Game("Mit dir"), status=discord.Status.online)
        await asyncio.sleep(5)
        await asyncio.sleep(5)
        await self.change_presence(activity=discord.Game("Pandas"), status=discord.Status.online)

    #TODO Custom Reactions
    async def authorReactions(self, author, message):
        if self.reactToMessageAuthors[0] == author:
            await message.add_reaction('<:UGAY:642807039780716604>')
        if  self.author[1] == author:
            await message.add_reaction('<:UGAY:642807039780716604>')
            await message.add_reaction('<:thalthy:642806635575640104>')

    async def on_message(self, message):
        if message.author.bot:
            return
        if self.commands["PetThePeepo"] in message.content:
            await message.channel.send(YouTubeHandler.petThePeepo())
        if self.commands["CommandsList"] in message.content:
            helpEmbed = discord.Embed(title='You need some help?',
                                    description='Here I give help:',
                                    color=0x22a7f0)
            helpEmbed.add_field(name='Commands:', value=self.commands.values, inline=True)
            await message.channel.send(embed=helpEmbed)
        if message.author in self.reactToMessageAuthors:
            await self.authorReactions(message.author, message)
        if self.commands["TicTacToe"] in message.content:
            await self.ticTacToe.restart(message)
        if self.commands["TicTacToeNextTurn"] in message.content:
            await self.ticTacToe.next_turn(message)


    

        


           
        
    
