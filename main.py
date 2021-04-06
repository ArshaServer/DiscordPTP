import os
import discord

from dotenv import load_dotenv
from src.PetThePanda import PetThePanda

def main():
    client = PetThePanda()
    
    load_dotenv()
    client.run(os.getenv('DISCORD_TOKEN')) 

if __name__ == "__main__":
    main()
