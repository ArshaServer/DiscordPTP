from PIL import Image, ImageDraw, ImageFont
import inspect
from discord import User
from discord import Intents
from discord import File


async def getImage(message):
    args = message.content.split(' ', 2)
    try:
        if(message.author.dm_channel == None):
            await User.create_dm(self=User)
                
        # create an image
        out = Image.new("RGB", (700, 500), (255, 10, 70))
        # get a font
        fnt1 = ImageFont.truetype("src/data/Chalkboard.ttc", 20)
        fnt2 = ImageFont.truetype("src/data/Zapfino.ttf", 20)
        # get a drawing context
        d = ImageDraw.Draw(out)

        # draw multiline text
        d.multiline_text((10,10), "Ein {0} sagte eins:".format(message.author.name), font=fnt1, fill=(0, 0, 0))
        d.multiline_text((10,50), args[2], font=fnt2, fill=(0, 0, 0))
        
        out.save("src/data/img.png","png")
        with open('src/data/img.png', 'rb') as f:
            picture = File(f)
            await message.guild.get_member_named(args[1]).send(file=picture)
        await message.add_reaction("\U00002705")
    except AttributeError:
        print("No User named {0} on this Server".format(args[1]))  
        await message.add_reaction("\U0000274C")
        

def autism_text(str):
    b = True
    r = ""
    for char in str:
        if(b):
            r += char.lower()
        else:
            r += char.upper()
        b = not(b)
    return r
        

def add_autism(str):
    # create an image
    out = Image.open("src/data/blabla.jpg")
    # get a font
    fnt = ImageFont.truetype("src/data/Chalkboard.ttc", 100)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text
    d.multiline_text((50,450),autism_text(str) , font=fnt, fill=(255, 255, 255))

    out.save("src/data/autism.png","png")

async def getImage(message):
    args = message.content.split(' ', 2)
    try:
        if(message.author.dm_channel == None):
            await User.create_dm(self=User)
                
        # create an image
        out = Image.new("RGB", (700, 500), (255, 10, 70))
        # get a font
        fnt1 = ImageFont.truetype("src/data/Chalkboard.ttc", 20)
        fnt2 = ImageFont.truetype("src/data/Zapfino.ttf", 20)
        # get a drawing context
        d = ImageDraw.Draw(out)

        # draw multiline text
        d.multiline_text((10,10), "Ein {0} sagte eins:".format(message.author.name), font=fnt1, fill=(0, 0, 0))
        d.multiline_text((10,50), wrap_text(args[2],600,fnt2), font=fnt2, fill=(0, 0, 0))
        
        out.save("src/data/img.png","png")
        with open('src/data/img.png', 'rb') as f:
            picture = File(f)
            await message.guild.get_member_named(args[1]).send(file=picture)
        await message.add_reaction("\U00002705")
    except AttributeError:
        print("No User named {0} on this Server".format(args[1]))  
        await message.add_reaction("\U0000274C")
           
