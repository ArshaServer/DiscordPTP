import discord

def uwu_translator(text):
        text = text.replace("r","w")
        text = text.replace("l","w")
        return text

class UWU():
    async def translation(message):
        args = message.content.split(' ',1)
        await message.channel.send(uwu_translator(args[1]), tts=True)

    