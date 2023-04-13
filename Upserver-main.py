import discord
from discord.ext import commands
import random
TOKEN = "MTAwNTU1NjAyNDcwODcxNDQ5Ng.G_rGMJ.Grl93vvL41--svtgGBhgBJSeJAeGkzr7bVleIA"

bot = commands.Bot(command_prefix=('!'))
@bot.event
async def on_ready():
    print("Я запущен!")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("wait your comand :D"), afk=True)

@bot.command()
async def lx(ctx, *text):
    channel = bot.get_channel(id=int((1005755492200632381)))
    await channel.send(*text)


@bot.command()
async def report(ctx):
    user = await bot.fetch_user(user_id=575345431240769548)
    await user.send('bug report')

@bot.command()
async def hi(ctx):
    await ctx.send("Привет")

@bot.command()
async def flip(ctx):
    coins = ["орел", "решка"]
    embed = discord.Embed(
        title=random.choice(coins),
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)
