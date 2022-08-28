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

    @commands.command(name="select", help="Seleciona um bagmon dos capturados para colocar no seu time")
    async def select(self, ctx, message):
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT id FROM bagmon WHERE bagmon = "{message}"')
        bagid = cursor.fetchone()
        cursor.execute(f"SELECT * FROM capturas WHERE user_id = {ctx.author.id} AND bagmon_id = '{bagid[0]}'")
        bag_id = cursor.fetchone()
        cursor.execute(f"UPDATE equipe SET save = '{bag_id[1]}' AND save_id = '{bag_id[0]}' WHERE user_id = {ctx.author.id}")
        db.commit()
        select = discord.Embed(
                title = f'**Você Selecionou {message}**',
                description =  f"Digite b!slot e o numero do slot onde deseja colocalo",
                color = 0xff000f,
            )
        await ctx.send(embed=select)

def setup(bot):
    bot.add_cog(Start(bot))

    
