import discord
import os
from dotenv import load_dotenv
import logging
import components

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(debug_guilds=[1012716684274049136])

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logger.addHandler(handler)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="start", description="Begin your conversation...")
async def start(ctx):
    await ctx.respond(embed=discord.Embed(
        title="Why, hello there!",
        description="Are you ready to have your nation's fortune told?"
    ), view=components.StartView())


bot.run(os.getenv('TOKEN'))  # run the bot with the token
