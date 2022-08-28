from discord.ext import commands
import discord
import mysql.connector
from decouple import config
import random

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Pick(commands.Cog):
    '''Select your starter bagmon'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pick')
    async def pick(self, ctx, message):
        lv = 5
        hp = 100
        iv = random.randint(1, 100)
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT user_id FROM user WHERE user_id = {ctx.author.id}')
        verify = cursor.fetchone()
        if verify == None:
            cursor.execute(f"INSERT INTO user (user_id, capturados) VALUES ({ctx.author.id}, 1)")
            db.commit()
            iv = random.randint(1, 100)
            if message == 'Voara':  
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, iv) VALUES (1, {ctx.author.id}, 1, 5, 100, {iv})')
                db.commit()
                cursor.execute(f'SELECT id FROM capturas WHERE user_id = "{ctx.author.id}"')
                bagmon = cursor.fetchone()
                cursor.execute(f'INSERT INTO equipe (user_id, slot1, slot1_id) VALUES ("{ctx.author.id}", 1, "{bagmon[0]}")')
                db.commit()
                image = 'https://i.imgur.com/f7vKcBO.jpg'

                voara = discord.Embed(
                    title = 'Parabens',
                    description = 'Seu inicial é a Voara',
                    color = 0x00ff00,
                )
                voara.set_image(url=image)

                await ctx.send(embed=voara)

            elif message == 'Pequemico':
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, iv) VALUES (1, {ctx.author.id}, 4, 5, 100, {iv})')
                db.commit()
                cursor.execute(f'SELECT id FROM capturas WHERE user_id = "{ctx.author.id}"')
                bagmon = cursor.fetchone()
                cursor.execute(f'INSERT INTO equipe (user_id, slot1, slot1_id) VALUES ("{ctx.author.id}", 4, "{bagmon[0]}")')
                db.commit()
                image = 'https://i.imgur.com/REcOY5t.jpg'

                Pequemico = discord.Embed(
                    title = 'Parabens',
                    description = 'Seu inicial é o Pequemico',
                    color = 0xff0000,
                )
                Pequemico.set_image(url=image)

                await ctx.send(embed=Pequemico)
        
            elif message == 'Capi':
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, iv) VALUES (1, {ctx.author.id}, 7, 5, 100, {iv})')
                db.commit()
                cursor.execute(f'SELECT id FROM capturas WHERE user_id = "{ctx.author.id}"')
                bagmon = cursor.fetchone()
                cursor.execute(f'INSERT INTO equipe (user_id, slot1, slot1_id) VALUES ("{ctx.author.id}", 7, "{bagmon[0]}")')
                db.commit()
                image = 'https://i.imgur.com/f0mJXzH.jpg'

                capi = discord.Embed(
                    title = 'Parabens',
                    description = 'Seu inicial é o Capi',
                    color = 0x0000ff,
                )
                capi.set_image(url=image)

                await ctx.send(embed=capi)

            elif message == 'Tamanduí':
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, iv) VALUES (1, {ctx.author.id}, 10, 5, 100, {iv})')
                db.commit()
                cursor.execute(f'SELECT id FROM capturas WHERE user_id = "{ctx.author.id}"')
                bagmon = cursor.fetchone()
                cursor.execute(f'INSERT INTO equipe (user_id, slot1, slot1_id) VALUES ("{ctx.author.id}", 10, "{bagmon[0]}")')
                db.commit()
                image = 'https://i.imgur.com/BYnVwQF.jpg'

                tamandui = discord.Embed(
                    title = 'Parabens',
                    description = 'Seu inicial é o Tamanduí',
                    color = 0x964b00,
                )
                tamandui.set_image(url=image)

                await ctx.send(embed=tamandui)
            elif message == 'Caralata':
                cursor.execute(f'INSERT INTO capturas (captura_id, user_id, bagmon_id, level, hp, iv) VALUES (1, {ctx.author.id}, 13, 5, 100, {iv})')
                db.commit()
                cursor.execute(f'SELECT id FROM capturas WHERE user_id = "{ctx.author.id}"')
                bagmon = cursor.fetchone()
                cursor.execute(f'INSERT INTO equipe (user_id, slot1, slot1_id) VALUES ("{ctx.author.id}", 13, "{bagmon[0]}")')
                db.commit()
                img = "https://dc722.4shared.com/img/B-kq3Zbaiq/s24/18266927ae0/Caralata?async&rand=0.2535460832935694"
                tamandui = discord.Embed(
                    title = 'Parabens',
                    description = 'Seu inicial é o Caralata',
                    color = 0x964b00,
                )
                tamandui.set_image(url=img)

                await ctx.send(embed=tamandui)
            else:
                res = "Você já escolheu seu inicial"
                ctx.send(res)
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(Pick(bot))

    
