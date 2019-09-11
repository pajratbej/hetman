import discord
from discord.ext import commands
from discord import Embed,Colour
from .StaticMethods import StaticMethods

class Memes(commands.Cog, name="Meme i jojo"):
    def __init__(self, bot):
        self.bot = bot

        
    @commands.command(pass_context=True)
    async def img(self, ctx):

        if str(ctx.message.channel) == "img":
            embed = Embed(
                title="OwO",
                Color=Colour.blue()
            )
            embed.set_image(url=StaticMethods.get_random_record("links", 2)[2: -2])
            print(ctx.message.channel)
            await ctx.send(embed=embed)
        else:
            await ctx.send(ctx.message.author, "To polecenie jest dostępne tylko w kanale #img w celu uniknięcia spamu na innych kanałach. The bois need their own space")

    @commands.command(pass_context=True)
    async def game(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name=ctx.message.content[6:]))
            
    @commands.command(pass_context=True)
    async def h(self, ctx):
        embed = Embed(
        title = "Pizda leci",
        Color = Colour.red()
        )
        embed.set_image(url=StaticMethods.get_specific_record("memes", 4, 1)[2:-2])
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def policja(self, ctx):
        embed = Embed(
            title = "Weeoo Weeoo",
            Color = Colour.blue()
        )
        embed.set_image(url=StaticMethods.get_specific_record("memes",4,2)[2:-2])
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def hetman(self, ctx):
        embed = Embed(
            title="?",
            Color= Colour.red()
        )
        embed.set_image(url="https://i.postimg.cc/YCr7211t/hetman.png")
        await ctx.send(embed=embed)

    
    @commands.command(pass_context=True)
    async def kys(self, ctx):
        await ctx.send("https://www.wikihow.com/Tie-a-Hangman%27s-Noose")

    @commands.command(pass_context=True)
    async def kms(self, ctx):
        await ctx.send("https://www.wikihow.com/Tie-a-Hangman%27s-Noose")

    @commands.command(pass_context=True)
    async def jojolice(self, ctx):
        embed = Embed(
            Color = Colour.blue()
        )
        embed.set_image(url=StaticMethods.get_specific_record("memes",4,0)[2:-2])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Memes(bot))
    print("Added Memes")
