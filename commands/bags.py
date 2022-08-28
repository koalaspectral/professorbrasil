from discord.ext import commands
import discord
import mysql.connector
from decouple import config

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Start(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bagdex', help='Mostra os seus 6 primeiros bagmons')
    async def bagdex(self, ctx, message):
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM capturas WHERE user_id = "{ctx.author.id}"')
        result = cursor.fetchmany(6)
        if message == "ver":
            bagdex = discord.Embed(
                title = f"BAGDEX",
                description = f" ",
                color = 0x964b00,
            )
            bagdex.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            bagdex.set_thumbnail(url=ctx.author.avatar_url)
            bagdex.set_footer(text="Digite b!bagdex proximo para ver mais")
            for res in result:
                level = res[4]
                hp = res[5]
                iv = res[10]
                id = res[1]
                indece = res[0]
                cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = "{id}"')
                response = cursor.fetchone()
                bagdex.add_field(name=f"{response[0]}", value=f"Level:{level}, HP: {hp}, IV: {iv}", inline=False)
            await ctx.send(embed=bagdex)
        elif message == "proximo":
            await ctx.message.channel.purge(limit=2)
            result = cursor.fetchmany(6)
            bagdex = discord.Embed(
                title = f"BAGDEX",
                description = f" ",
                color = 0x964b00,
            )
            bagdex.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            bagdex.set_thumbnail(url=ctx.author.avatar_url)
            bagdex.set_footer(text="Digite b!bagdex proximo para ver mais")
            for res in result:
                response = res[3]
                bagdex.add_field(name=f"{response}", value=f"Level:{res[5]}, HP: {res[6]}", inline=False)
            await ctx.send(embed=bagdex)
        elif message == "voltar":
            result = cursor.fetchone()
            await ctx.message.channel.purge(limit=2)
            result = cursor.fetchmany(6)
            bagdex = discord.Embed(
                title = f"BAGDEX",
                description = f" ",
                color = 0x964b00,
            )
            bagdex.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            bagdex.set_thumbnail(url=ctx.author.avatar_url)
            bagdex.set_footer(text="Digite b!bagdex page4 para ver mais")
            for res in result:
                response = res[3]
                bagdex.add_field(name=f"{response}", value=f"Level:{res[5]}, HP: {res[6]}", inline=False)
            await ctx.send(embed=bagdex)
        elif message == "page4":
            await ctx.message.channel.purge(limit=2)
            result = cursor.fetchmany(6)
            bagdex = discord.Embed(
                title = f"BAGDEX",
                description = f" ",
                color = 0x964b00,
            )
            bagdex.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            bagdex.set_thumbnail(url=ctx.author.avatar_url)
            bagdex.set_footer(text="Digite b!bagdex page3 para voltar ou b!bagdex page5 para ver mais")
            for res in result:
                response = res[3]
                bagdex.add_field(name=f"{response}", value=f"Level:{res[5]}, HP: {res[6]}", inline=False)
            await ctx.send(embed=bagdex)
        else:
            return

def setup(bot):
    bot.add_cog(Start(bot))

    
