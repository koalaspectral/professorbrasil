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

    @commands.command(name='equipe', help='Mostra sua equipe')
    async def view_equipe(self, ctx):
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM equipe WHERE user_id = "{ctx.author.id}"')
        result = cursor.fetchone()
            
        bagdex = discord.Embed(
            title = f"BAGDEX",
            description = f" ",
            color = 0x964b00,
        )
        bagdex.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        bagdex.set_thumbnail(url=ctx.author.avatar_url)
        cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = {result[2]}')
        slot1 = cursor.fetchone()
        bagdex.add_field(name=f"1- {slot1[0]}", value="------------------------", inline=False)
        cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = {result[4]}')
        slot2 = cursor.fetchone()
        bagdex.add_field(name=f"2- {slot2[0]}", value=f"------------------------", inline=False)
        cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = {result[6]}')
        slot3 = cursor.fetchone()
        bagdex.add_field(name=f"3- {slot3[0]}", value=f"------------------------", inline=False)
        cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = {result[8]}')
        slot4 = cursor.fetchone()
        bagdex.add_field(name=f"4- {slot4[0]}", value=f"------------------------", inline=False)
        cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = {result[10]}')
        slot5 = cursor.fetchone()
        bagdex.add_field(name=f"5- {slot5[0]}", value=f"------------------------", inline=False)
        cursor.execute(f'SELECT bagmon FROM bagmon WHERE id = {result[12]}')
        slot6 = cursor.fetchone()
        bagdex.add_field(name=f"6- {slot6[0]}", value=f"------------------------", inline=False)
        await ctx.send(embed=bagdex)

def setup(bot):
    bot.add_cog(Start(bot))

    
