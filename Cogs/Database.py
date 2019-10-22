import discord
from discord.ext import commands
from .StaticMethods import StaticMethods
import random as r

class Database(commands.Cog, name="Cytaty"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addcytat(self, ctx):
        """Developer command"""
        role_names = [role.name for role in ctx.message.author.roles ]
        if "Developer" in role_names:
            await ctx.send(StaticMethods.push_record("cytat", ctx.message.content, 1))
        else:
            await ctx.send("Odmowa dostępu")

    @commands.command()
    async def cytat(self, ctx, number=None):
        if(number!=None):
            try:
                print(StaticMethods.get_specific_record("cytat", 1, int(number))[2:-2])
                await ctx.send("Cytat #"+number+"\"" + StaticMethods.get_specific_record("cytat", 1, int(number))[2:-2] + "\"")
            except Exception:
                print("Nie ma takiego cytatu")
                await ctx.send("Nie ma takiego cytatu!")
        else:
            r2 = r.randint(1,StaticMethods.number_of_quotes("cytat", 1))
            print("\"" +StaticMethods.get_random_record("cytat", 1)[2:-2] + "\"")
            await ctx.send( "Cytat #"+str(r2)+" \"" +StaticMethods.get_specific_record("cytat", 1, r2)[2:-2] + "\"")

def setup(bot):
    bot.add_cog(Database(bot))
    print("Added Database")
