import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
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
@bot.command(name="name")
async def name(ctx):
    await ctx.send(ctx.author)


# Function that count the number of members on the server typing the command !count #
@bot.command(name="count")
async def count(ctx):
    members = bot.guilds[0].members
    size = len(members) - 1
    # text = ' members are online' 
    await ctx.send(size)
    for member in members :
        if (not member.bot):
            await ctx.send(member.name)


token = "ODkyODIyMTY4MzE0OTk4ODA0.YVSfcA.ixPqpvPRJCQPx6k-lfoDiFkvnpo"
bot.run(token)  # Starts the bot