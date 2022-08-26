import discord
import os
from dotenv import load_dotenv
import logging

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(debug_guilds=[1012716684274049136])
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


bot.run(os.getenv('TOKEN'), log_handler=handler)  # run the bot with the token
