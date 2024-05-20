import os
import discord
from discord.ext import commands

# Read the token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Set up the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a simple command
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot
bot.run(TOKEN)
