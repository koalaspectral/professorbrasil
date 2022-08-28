from discord.ext import commands, tasks
import aiosqlite

class Manager(commands.Cog):
    """work with spawn"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Estou Online')
        async with aiosqlite.connect("main.db") as db:
            
                await cursor.execute('CREATE TABLE IF NOT EXISTS bagmons (id INTEGER, name text, type text, nv INTEGER, hp INTEGER, move1 text, move2 text, move3 text, move4 text, move5 text)')
            await db.commit()

def setup(bot):
    bot.add_cog(Manager(bot))
