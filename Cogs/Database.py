import discord
from discord import Embed, Colour
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
                cytat = StaticMethods.get_specific_record("cytat",1, int(number))[2:-2]
                await ctx.send(f"Cytat #{number}: \"{cytat}\"")
            except Exception:
                print("Nie ma takiego cytatu")
                await ctx.send("Nie ma takiego cytatu!")
        else:
            r2 = r.randint(1,StaticMethods.number_of_quotes("cytat", 1))
            cytat = StaticMethods.get_specific_record("cytat",1,r2)[2:-2]
            await ctx.send(f"Cytat #{str(r2)}:  \"{cytat}\" ")



    @commands.command()
    async def meme(self, ctx, number=None):
        embed = Embed(
                title="funni",
                Color=Colour.blue()
                )
        r2 = r.randint(1,StaticMethods.number_of_quotes("pompa", 5))
        obraz = StaticMethods.get_specific_record("pompa",5,r2)[2:-2]
        print(obraz)
        embed.set_image(url=obraz)

        if(number!=None):
            try:
                obraz = StaticMethods.get_specific_record("pompa",5, int(number))[2:-2]
                print(obraz)
                embed.set_image(url=obraz)
                await ctx.send(embed=embed)
            except Exception:
                print("Ten meme nie istanieje w tej rzeczywistości")
                await ctx.send("Ten meme nie istnieje w tej rzeczywistości")
        else:
             await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Database(bot))
    print("Added Database")
