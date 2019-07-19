import asyncio as asyncio
import discord
from discord import Embed, Color, Colour
from discord.ext import commands
import os
import sys
from datetime import datetime
import traceback

bot = commands.Bot(command_prefix="!")

today = datetime.today()
extensions = ["Cogs.Events","Cogs.Database","Cogs.School", "Cogs.Memes"]
if today.day == 20 and today.month == 7:
    extensions.append("Cogs.Birthday")

if __name__=="__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Caught an exception {e}", file=sys.stderr)
            traceback.print_exc()
       
bot.run(os.environ["SEC_KEY"])
