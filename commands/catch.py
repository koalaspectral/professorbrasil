from discord.ext import commands
import discord
import random
import mysql.connector
from decouple import config

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Start(commands.Cog):
    '''Talks with user'''
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='catch', help='Captura os bagmons que aparecem pelo chat')
    async def catch(self, ctx, message):
        xp = 0
        exp = random.randint(1, 50)
        hp = random.randint(100, 500)
        iv = random.randint(1, 100)
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f"SELECT level FROM spawn WHERE id = 1")
        spawn_id = cursor.fetchone()
        id = spawn_id[0]
        cursor.execute(f'SELECT * FROM capturas WHERE user_id = "{ctx.author.id}"')
        verify = cursor.fetchone()
        check = verify[12]
        a = 1
        c = int(check) + int(a)
        cursor.execute(f"UPDATE capturas SET new_id = '{c}' WHERE user_id {ctx.author.id}")
        db.commit()
        
        if verify[0] == None:
            res = "Escolha seu inicial digite b!start e veja as opções"
            ctx.send(res)
        else:
            print(check)
            cursor.execute(f"SELECT bagmon, url, id FROM bagmon WHERE id = '{id}'")
            bagmon = cursor.fetchone()
            if bagmon[0] == message:
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, xp, iv) VALUES ({c}, {ctx.author.id}, "{bagmon[2]}", {exp}, {hp}, {xp}, {iv})')
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
        cursor.close()
        db.close()


def setup(bot):
    bot.add_cog(Start(bot))

    
