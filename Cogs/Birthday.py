import discord
from discord.ext import commands
from .StaticMethods import StaticMethods

class Birthday(commands.Cog, name="Polecenia urodzinowe (tylko 20 lipca)"):
    def __init__(self, bot):
        self.bot = bot
    
    cake = []
    pieces_eaten = {}
    @commands.command()
    async def bake(self, ctx):
        if not self.cake:
            self.cake = [1, 2, 3, 4, 5, 6, 7, 8]
            await ctx.send(str(ctx.message.author.nick) + " upiekł mi tort :3. Użyj !piece aby się poczęstować")
        else:
            await ctx.send("Ktoś już upiekł tort. Użyj !piece aby się poczęstować")

    @commands.command()
    async def piece(self, ctx):
        if not self.cake:
            await ctx.send("Nie ma upieczonego tortu 😔. Użyj !bake aby upiec mi tort :3")
        else:
            
            if self.pieces_eaten.get(str(ctx.message.author.id)) is None:
                self.pieces_eaten[str(ctx.message.author.id)] = 0
            

            if self.pieces_eaten[str(ctx.message.author.id)] == 3:
                await ctx.send("Zjadłeś już 2 kawałki tortu. Zostaw coś dla reszty bambaryło 👿")
            else:
                temp = self.cake[0:len(self.cake)-1]
                self.cake = temp
                self.pieces_eaten[str(ctx.message.author.id)] += 1

                if not self.cake:
                    self.pieces_eaten = {}
                    await ctx.send("Prosze " + str(ctx.message.author.nick) +". Oto twój kawałek tortu. \n 🍰 " +
                        "Zjadłeś ostatni kawałek tortu! 😱 Należy teraz upiec kolejny. Użyj !bake aby upiec tort")
                else:
                    await ctx.send("Prosze " + str(ctx.message.author.nick) +". Oto twój kawałek tortu. \n 🍰 ")    
                
    @commands.command()
    async def left(self, ctx):
        if not self.cake:
            await ctx.send("Nie ma upieczonego tortu 😔. Użyj !bake aby upiec mi tort :3")
        else:
            await ctx.send("Pozostało " + str(len(self.cake)) + " kawałków tortu.")

    @commands.command()
    async def bin(self, ctx):
        """Developer command"""
        role_names = [role.name for role in ctx.message.author.roles ]
        if "Developer" in role_names:
            if self.cake:
                self.cake = []
                self.pieces_eaten = {}
                await ctx.send(str(ctx.message.author.nick) + " wyrzucił tort bo nikt nie chciał jeść 😭")
            else:
                await ctx.send("Nie ma upieczonego tortu 😔. Użyj !bake aby upiec mi tort :3")
        else:
            await ctx.send("Odmowa dostępu")

def setup(bot):
    bot.add_cog(Birthday(bot))
    print("Added Birthday")