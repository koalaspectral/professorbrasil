import os
from discord.ext import commands
from decouple import config

bot = commands.Bot("b!")

def load_cogs(bot):
    bot.load_extension("manager")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("key")
bot.run(TOKEN)