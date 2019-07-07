import discord
from discord.ext import commands
from .StaticMethods import StaticMethods
from discord import Embed, Colour
import random as r

class School(commands.Cog, name="Szkoła itd."):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def updateplan(self, ctx):
        role_names = [role.name for role in ctx.message.author.roles]
        if "Developer" in role_names:
            StaticMethods.replace(ctx.message.content[12:])
            await ctx.send("Zaktualizowano plan")
        else:
            await ctx.send("Odmowa dostępu")

    @commands.command()
    async def ocena(self, ctx):
        r_ocena = r.randint(1,6)
        await ctx.send(str(ctx.message.author.name) + " dostał: "+str(r_ocena))

    @commands.command()
    async def gac(self, ctx):
        await ctx.send("http://www.pangac.c0.pl")

    @commands.command()
    async def plan(self, ctx):
        embed = Embed(
            Color = Colour.red()
        )
        embed.set_image(url=StaticMethods.getPlan())
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(School(bot))
    print("Added School")