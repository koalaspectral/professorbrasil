from discord.ext import commands
import discord

class Start(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="liga", help="Mostra os inciais disponiveis")
    async def liga(self, ctx):

        image = "https://i.imgur.com/nYKVBkm.jpg"

        iniciar = discord.Embed(
            title = f"Perfil de {ctx.author.name}",
            description = "Ainda em desenvolvimento!",
            color = 0xff00ff,
        )
        iniciar.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=iniciar)

    
def setup(bot):
    bot.add_cog(Start(bot))
