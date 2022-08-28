from discord.ext import commands
import discord
import asyncio
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


def setup(bot):
    bot.add_cog(Start(bot))

    
