from discord.ext import commands
import discord
import random
import mysql.connector
from decouple import config
import math

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Start(commands.Cog):
    '''Talks with user'''
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='capturar', help='Captura os bagmons que aparecem pelo chat')
    async def capturar(self, ctx, message):
        xp = 0
        exp = random.randint(1, 50)
        hp = random.randint(100, 500)
        iv = random.randint(1, 100)
        id = 1
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT user_id, capturados, id FROM user WHERE user_id = {ctx.author.id}')
        verify = cursor.fetchone()
        if verify == None:
            resposta = "Antes de capturar algum bagmon escolha eu inicial"
            ctx.send(resposta)
        else:
            go = verify[1]
            userid = verify[2]
            novo = int(go) + int(id)
            cursor.execute(f'UPDATE user SET capturados = "{novo}" WHERE id = {userid}')
            db.commit()
            cursor.execute(f"SELECT level FROM spawn WHERE id = 1")
            spawn_id = cursor.fetchone()
            bagmonid = spawn_id[0]
            cursor.execute(f"SELECT bagmon, url, id FROM bagmon WHERE id = '{bagmonid}'")
            bagmon = cursor.fetchone()
            if bagmon[0] == message:
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, xp, iv) VALUES ({novo}, {ctx.author.id}, "{bagmon[2]}", {exp}, {hp}, {xp}, {iv})')
                db.commit()
                user = ctx.author.name
                catch = discord.Embed(
                title = f'{user} capturou {bagmon[0]}',
                color = 0xff00ff,
                )
                catch.set_image(url=bagmon[1])
                await ctx.send(embed=catch)
                
            else:
                resp = f'Ops, bagmon errado'
                await ctx.send(resp)

def setup(bot):
    bot.add_cog(Start(bot))

    
