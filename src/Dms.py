import inspect
from discord import User
from discord import Intents

class Dms():
    async def sendDmTo(message):
        args = message.content.split(' ', 2)
        if(message.guild.get_member_named("Madafii") == None):
            print("tried to send Message to {0}, but no matching username in the guild".format(args[1])) 
            message.guild.get_members()
            async for member in message.guild.fetch_members(limit=150):
                print(member.name)
        else:
            if(message.author.dm_channel == None):
                await User.create_dm(self=User)
            await message.guild.get_member_named(args[1]).send(args[2])