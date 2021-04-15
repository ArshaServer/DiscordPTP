from PIL import Image, ImageDraw, ImageFont
import inspect
from discord import User
from discord import Intents
from discord import File

class Inspirator():
    def wrap_text(text, width, font):
        text_lines = []
        text_line = []
        text = text.replace('\n', ' [br] ')
        words = text.split()

        for word in words:
            if word == '[br]':
                text_lines.append(' '.join(text_line))
                text_line = []
                continue
            text_line.append(word)
            w = font.getsize(' '.join(text_line))
            if w > width:
                text_line.pop()
                text_lines.append(' '.join(text_line))
                text_line = [word]

        if len(text_line) > 0:
            text_lines.append(' '.join(text_line))

        return "\n".join( text_lines)

    async def getImage(message):
        args = message.content.split(' ', 2)
        try:
            if(message.author.dm_channel == None):
                await User.create_dm(self=User)
                 
            # create an image
            out = Image.new("RGB", (700, 500), (255, 10, 70))
            # get a font
            fnt1 = ImageFont.truetype("data/Chalkboard.ttc", 20)
            fnt2 = ImageFont.truetype("data/Zapfino.ttf", 20)
            # get a drawing context
            d = ImageDraw.Draw(out)

            # draw multiline text
            d.multiline_text((10,10), "Ein {0} sagte eins:".format(message.author.name), font=fnt1, fill=(0, 0, 0))
            d.multiline_text((10,50), self.wrap_text(args[2],600,fnt2), font=fnt2, fill=(0, 0, 0))
            
            out.save("data/img.png","png")
            with open('data/img.png', 'rb') as f:
                picture = File(f)
                await message.guild.get_member_named(args[1]).send(file=picture)
            await message.add_reaction("\U00002705")
        except AttributeError:
            print("No User named {0} on this Server".format(args[1]))  
            await message.add_reaction("\U0000274C")
           