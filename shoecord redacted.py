from discord.ext import commands
import discord

from app import app_run

bot_token = ""
channel_ = 0

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

shoestate = app_run()

@bot.event
async def on_ready():
    #print("Test.")
    channel = bot.get_channel(channel_)
    await channel.send(shoestate)

bot.run(bot_token)