import discord
from discord.ext import commands
import random
TOKEN = "MTAwNTU1NjAyNDcwODcxNDQ5Ng.G_rGMJ.Grl93vvL41--svtgGBhgBJSeJAeGkzr7bVleIA"

bot = commands.Bot(command_prefix=('!'))
check = 0
@bot.event
async def on_ready():
    print("Я запущен!")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("DOKA 2"), afk=True)

@bot.command()
async def lx(ctx, *text):
    channel = bot.get_channel(id=int((1005755492200632381)))
    await channel.send(*text)


@bot.command()
async def tl(ctx):
    embed = discord.Embed(
        title=">---жми---<",
        description="ссылка на Tlauncher",
        url='https://tlauncher.org/',
    )
    await ctx.send(embed=embed)

@bot.command()
async def start(ctx):
    user = await bot.fetch_user(user_id=575345431240769548)
    await user.send('запусти сервер пж')

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

@bot.command()
async def spam(ctx, text):
    number = random.randint(0, 9)
    while True:
        await ctx.send("fuck")

# код для спама рандомным людям
@bot.command()
# не используется на данный момент из-за ненадобности
# async def id(ctx):
    id = ""
    count = 0
    while True:
        global check
        #собирается id из 18 рандомных чисел
        for i in range(18):
            id += str(random.randint(0, 9))
            count += 1
        if count == 18:
            # id будет использовтся для user id, сейчас находится мое id
            await ctx.send(int(id))
            count = 0
            id = ""
            check += 1
            #будет использоваться переменная id для отправки сообщения user
            user = await bot.fetch_user(user_id=855320640008617984)
            # используеют глобальную переменную для счета созданных id, но отправляет их юзеру id которого было только что создано
            #для удобства стоит испльзовать 2 вывода
            await user.send(check)


bot.run(TOKEN)
