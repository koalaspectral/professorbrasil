from discord.ext import commands
import discord

class Start(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="start", help="Mostra os inciais disponiveis")
    async def start_jorney(self, ctx):

        image = "https://i.imgur.com/nYKVBkm.jpg"

        iniciar = discord.Embed(
            title = "Qual sera seu inicial?",
            description = "Voara \n Pequemico \n Capi \n  Tamanduí",
            color = 0xff00ff,
        )
        iniciar.set_image(url=image)
        iniciar.set_footer(text="Digite b!pick <bagmon> para escolher seu inicial")

        await ctx.send(embed=iniciar)

    
def setup(bot):
    bot.add_cog(Start(bot))
