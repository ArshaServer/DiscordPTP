import random

from discord import channel

class Channel():
    def __init__(self):
        pass

    #TODO not done
    async def kickRandom(message):
        if(message.author.voice.channel == None):
            await message.channel.send("you must be in a channel to use this command")
            return
        try:
            rand = random.randint(0, len(message.author.voice.channel.members)-1)
            for channel in message.guild.voice_channels:
                if(channel.name == "AFK"):
                    await message.author.voice.channel.members[rand].move_to(None)
                    await message.channel.send("bye {0}".message.author.voice.channel.members[rand])
        except RuntimeError:
            print("Konnte niemanden kicken")