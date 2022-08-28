from discord.ext import commands
import discord
import random
import asyncio
import mysql.connector
from decouple import config
import math
host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Manager(commands.Cog):
    """work with spawn"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Estou Online')


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f"SELECT slot1_id, slot1 FROM equipe WHERE user_id = {message.author.id}")
        bagid = cursor.fetchone()
        equipe = bagid[0]
        eqbagmon = bagid[1]

        cursor.execute(f"SELECT xp FROM capturas where id = {equipe}")
        xpnew = cursor.fetchone()
        send = xpnew[0]
        if int(send) >= int(99):
            new = xpnew[0]
            lv = 100
            resp = int(new) - int(lv)
            cursor.execute(f'UPDATE capturas SET xp = {resp} WHERE user_id = {message.author.id}')
            cursor.execute(f"SELECT level FROM capturas where id = {equipe}")
            lvnew = cursor.fetchone()
            levelnew = lvnew[0]
            t = 1
            newlv = int(levelnew) + 1
            cursor.execute(f'UPDATE capturas SET level = {newlv} WHERE user_id = {message.author.id}')
            db.commit
            cursor.execute(f"SELECT bagmon_id FROM capturas where id = {equipe}")
            float = cursor.fetchone()
            cursor.execute(f"SELECT bagmon FROM bagmon where id = {float[0]}")
            name = cursor.fetchone()
            await message.channel.send(f"@{message.author} seu {name[0]} subiu de nv!")
        cursor.execute(f"SELECT xp FROM capturas where id = {equipe}")
        xp = cursor.fetchone()
        a = random.randint(1, 10)
        b = xp[0]
        c = int(a) + int(b)
        cursor.execute(f'UPDATE capturas SET xp = {c} WHERE user_id = {message.author.id} AND id = {equipe}')
        db.commit()
        cursor.execute(f"SELECT evlevel, evolution, bagmon, url FROM bagmon where id = {eqbagmon}")
        evolv = cursor.fetchone()
        transform = evolv[0]
        evolution = evolv[1]
        bagname = evolv[2]
        cursor.execute(f"SELECT level FROM capturas where id = {equipe}")
        lvnew = cursor.fetchone()
        levelnew = lvnew[0]
        if int(levelnew) >= int(transform):
            cursor.execute(f"SELECT bagmon, url FROM bagmon where id = {evolution}")
            newbag = cursor.fetchone()
            evoluir = discord.Embed(
            title = f'Evolução',
            description = f'{message.author.name} Seu {bagname} evoluiu para {newbag[0]}',
            color = 0xff00ff,
            )
            url = newbag[1]
            evoluir.set_image(url=url)
            await message.channel.send(embed=evoluir)
            cursor.execute(f'UPDATE capturas SET bagmon_id = {evolution} WHERE id = {equipe}')
            cursor.execute(f'UPDATE equipe SET slot1 = {evolution} WHERE slot1_id = {equipe}')
            db.commit()


def setup(bot):
    bot.add_cog(Manager(bot))

    
