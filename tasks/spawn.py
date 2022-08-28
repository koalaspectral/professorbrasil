import discord
import mysql.connector
from discord.ext import commands, tasks
import random
from decouple import config

host = config('1')
base = config('2')
senha = config('4')
usuario = config('3')

class Spawn(commands.Cog):
    '''work with spawn'''
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(minutes=15)
    async def current_time(self):
        bagmon_id = random.randint(1, 139)
        db = mysql.connector.connect(host=f'{host}', user=f'{usuario}', password=f'{senha}', database=f'{base}')
        cursor = db.cursor()
        cursor.execute(f'SELECT (url) FROM bagmon WHERE id = "{bagmon_id}"')
        url = cursor.fetchone()
        cursor.execute(f'UPDATE spawn SET level = {bagmon_id} WHERE id = 1')
        db.commit()
        spawnb = discord.Embed(
        title = '**Um bagmon apareceu**',
        color = 0xff000f,
        )
        spawnb.set_image(url=url[0])
        spawnb.set_footer(text='Digite b!capturar <bagmon> para capturalo')

        channel = self.bot.get_channel(1004886201083375716)
        await channel.send(embed=spawnb)
        print(url[0])
        cursor.close()
        db.close()
        
    @commands.command(name='ligar')
    @commands.has_permissions(administrator=True)
    async def turn_on(self, ctx):
        self.current_time.start()
    @commands.command(name='desligar')
    @commands.has_permissions(administrator=True)
    async def turn_off(self, ctx):
        self.current_time.start()
def setup(bot):
    bot.add_cog(Spawn(bot))

    
