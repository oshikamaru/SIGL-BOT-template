import os
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 336443857103486976  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

# Function that write back the name of the user typing the command !name #
@bot.event
async def on_message(message):
    if (message.content == "!name"):
        await message.channel.send(message.author)

token = "ODkyODIyMTY4MzE0OTk4ODA0.YVSfcA.ixPqpvPRJCQPx6k-lfoDiFkvnpo"
bot.run(token)  # Starts the bot