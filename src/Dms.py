from discord import User

class Dms():
    async def sendDmTo(self,message):
        args = message.content.split(' ', 2)
        try:
            if(message.author.dm_channel == None):
                await User.create_dm(self=User)
            await message.guild.get_member_named(args[1]).send(args[2])
            await message.add_reaction("\U00002705")
        except AttributeError:
            print("No User named {0} on this Server".format(args[1]))        
            await message.add_reaction("\U0000274C")