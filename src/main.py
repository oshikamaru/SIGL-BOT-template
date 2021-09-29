import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client()

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


# Function that count the number of members on the server #
@bot.command(name="count")
async def count(ctx):
    members = ctx.guild.members
    size = len(members) - 1
    # text = ' members are online' 
    await ctx.send(size)
    for member in members :
        if (not member.bot):
            await ctx.send(member.name)

# Function that create an admin role and attribute to the name given in arg #
@bot.command(name="admin")
async def give_admin(ctx, arg):
    guild = ctx.guild
    admin_role = await guild.create_role(name='new role', permissions=discord.Permissions.all(), colour=discord.Colour.default(), hoist=False, mentionable=False)
    client.add_roles(admin_role, arg)

# Function that ban from the server the name given in arg #
@bot.command(name="ban")
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

# Function that post a random comic from https://xkcd.com #
@bot.command(name="xkcd")
async def random_comic(ctx):
    random_int = random.randint(1, 2100)
    url = 'https://xkcd.com/' + str(random_int)
    await ctx.send(url)




token = "ODkyODIyMTY4MzE0OTk4ODA0.YVSfcA.ixPqpvPRJCQPx6k-lfoDiFkvnpo"
bot.run(token)  # Starts the bot