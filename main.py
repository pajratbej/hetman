import asyncio as asyncio
import random as r
import discord
from discord import Embed, Color, Colour
from discord.ext import commands
import SELECT
import json
import os
import sys
import datetime
import traceback

bot = commands.Bot(command_prefix="!")

extensions = ["Cogs.Events","Cogs.Database","Cogs.School", "Cogs.Memes"]


if __name__=="__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Caught an exception {e}", file=sys.stderr)
            traceback.print_exc()
    
bot.run(os.environ["SEC_KEY"])
