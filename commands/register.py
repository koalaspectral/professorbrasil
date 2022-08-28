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
    @commands.command(name="registrar", help="Se registra na Liga!")
    async def equipe(self, ctx):
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM equipe WHERE EXISTS(SELECT user_id FROM equipe WHERE user_id = '{ctx.author.id}')")
        date = cursor.fetchone()
        if date == None: 
            cursor.execute(f"INSERT INTO equipe (user_id) VALUES ({ctx.author.id})")
            db.commit()
            response = "Você acabou de se registrar na LIGA use b!liga para ver sua ficha de treinador \n ou b!equipe para ver sua equipe"
            await ctx.send(response)
        else:
            response = "Você Ja se registrou na liga de b!liga \n para ver suas informações ou b!equipe para ver sua equipe bagmons"
            await ctx.send(response)
            
def setup(bot):
    bot.add_cog(Start(bot))

    
