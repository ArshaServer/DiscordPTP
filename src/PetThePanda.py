import discord
import asyncio

from src.Dms import Dms
from src.Games.TicTacToe import TicTacToe
from src.youtubeAPI import YouTubeHandler
from src.inspireMe import Inspirator
from src.Channel import Channel

class PetThePanda(discord.Client):
    commands = {
        "PetThePeepo" : "!Pet the peepo",
        "CommandsList" : '!INeedSomeHelp',
        "TicTacToe" : "!start TicTacToe",
        "TicTacToeNextTurn" : "!next ",
        "sendDmTo" : "!send ",
        "inspireMe" : "!inspire ",
        "kickRandom" : "!ksr"
    }
    reactToMessageAuthors = [
        "Madafii",
        "Droxt"
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ticTacToe = TicTacToe()

    async def on_ready(self):
        print(self.user.name + " is ready")

    async def status_task(self):
        await self.change_presence(activity=discord.Game("Mit dir"), status=discord.Status.online)
        await asyncio.sleep(5)
        await asyncio.sleep(5)
        await self.change_presence(activity=discord.Game("Pandas"), status=discord.Status.online)

    #TODO Custom Reactions
    async def authorReactions(self, author, message):
        if self.reactToMessageAuthors[0] == author:
            await message.add_reaction('<:UGAY:642807039780716604>')
        if self.reactToMessageAuthors[1] == author:
            await message.add_reaction('<:UGAY:642807039780716604>')
            await message.add_reaction('<:thalthy:642806635575640104>')

    async def on_message(self, message):
        if message.author.bot:
            return
        if self.commands["PetThePeepo"] in message.content:
            await message.channel.send(YouTubeHandler.petThePeepo(self))
        if self.commands["CommandsList"] in message.content:
            helpEmbed = discord.Embed(title='You need some help?',
                                    description='Here I give help:',
                                    color=0x22a7f0)
            helpEmbed.add_field(name='Commands:', value=list(self.commands.values()), inline=True)
            await message.channel.send(embed=helpEmbed)
        if message.author.display_name in self.reactToMessageAuthors:
            await self.authorReactions(message.author.display_name, message)
        if self.commands["TicTacToe"] in message.content:
            await self.ticTacToe.restart(message)
        if self.commands["TicTacToeNextTurn"] in message.content:
            await self.ticTacToe.next_turn(message)
        if self.commands["sendDmTo"] in message.content:
            await Dms.sendDmTo(message)
        if self.commands["inspireMe"] in message.content:
            await inspireMe.getImage(message)    
        if self.commands["kickRandom"] in message.content:
            await Channel.kickRandom(message)
