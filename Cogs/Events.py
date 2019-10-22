import discord
from discord.ext import commands
from .StaticMethods import StaticMethods

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name=StaticMethods.getGame()))

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(Events(bot))
    print("Added Events")
