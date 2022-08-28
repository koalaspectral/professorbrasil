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
    
    @commands.command(name="definir")
    async def defined(self, ctx, message):
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT save, save_id FROM equipe WHERE user_id = {ctx.author.id}')
        bag = cursor.fetchone()
        cloud = message
        if message == "slot1":
            cursor.execute(f"UPDATE equipe SET slot1 = '{bag[0]}' AND slot1_id = {bag[1]} WHERE user_id = {ctx.author.id}")
            db.commit()
            select = discord.Embed(
                    title = f'**SUCESSO**',
                    description =  f"Slot 1 definido com sucesso!",
                    color = 0xff000f,
                )
            await ctx.send(embed=select)
        elif message == "slot2":
            cursor.execute(f"UPDATE equipe SET slot2 = '{bag}' WHERE user_id = {ctx.author.id}")
            db.commit()
            select = discord.Embed(
                    title = f'**SUCESSO**',
                    description =  f"Slot 2 definido com sucesso!",
                    color = 0xff000f,
                )
            await ctx.send(embed=select)
        elif message == "slot3":
            cursor.execute(f"UPDATE equipe SET slot3 = '{bag}' WHERE user_id = {ctx.author.id}")
            db.commit()
            select = discord.Embed(
                    title = f'**SUCESSO**',
                    description =  f"Slot 3 definido com sucesso!",
                    color = 0xff000f,
                )
            await ctx.send(embed=select)
        elif message == "slot4":
            cursor.execute(f"UPDATE equipe SET slot4 = '{bag}' WHERE user_id = {ctx.author.id}")
            db.commit()
            select = discord.Embed(
                    title = f'**SUCESSO**',
                    description =  f"Slot 4 definido com sucesso!",
                    color = 0xff000f,
                )
            await ctx.send(embed=select)
        elif message == "slot5":
            cursor.execute(f"UPDATE equipe SET slot5 = '{bag}' WHERE user_id = {ctx.author.id}")
            db.commit()
            select = discord.Embed(
                    title = f'**SUCESSO**',
                    description =  f"Slot 5 definido com sucesso!",
                    color = 0xff000f,
                )
            await ctx.send(embed=select)
        elif message == "slot6":
            cursor.execute(f"UPDATE equipe SET slot6 = '{bag}' WHERE user_id = {ctx.author.id}")
            db.commit()
            select = discord.Embed(
                    title = f'**SUCESSO**',
                    description =  f"Slot 6 definido com sucesso!",
                    color = 0xff000f,
                )
            await ctx.send(embed=select)
        

def setup(bot):
    bot.add_cog(Start(bot))

    
