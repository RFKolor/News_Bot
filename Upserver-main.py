import discord
from discord.ext import commands
import settings
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents,
                   activity=discord.Game(name="!help"))


@bot.event
async def on_ready():
   print("бот работает")


#вообще-то оно работать должно
@client.event
async def on_message_join(member):
    channel = client.get_channel(1096361181574340649)
    embed=discord.Embed(title=f"Welcome {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
   for i in settings.ban_words:
      if i in message.content:
         await message.delete()
         await message.channel.send(f"{message.author.mention} Не выражаться!")
         return
   await bot.process_commands(message)


@bot.command(name="flip", description="Орел и решка")
async def flip(ctx):
    coins = ["орел", "решка"]
    embed = discord.Embed(
        title=random.choice(coins),
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)


@bot.command(name='hello', description="Бот приветсвует вас")
async def hello(ctx):
    await ctx.send(f"Привет {ctx.author.name}!")


@bot.command(name="link", description="Ссылка на наш сайт")
async def link(ctx):
    embed = discord.Embed(
        title=">---сслыка---<",
        url="https://ya.ru/",
        description="ссылка на наш сайт",
        color=discord.Color.random()
    )
    await ctx.send(embed=embed)


@bot.command(name="authors", description="ссылки на аккаунты разабочтиков бота и сайта")
async def authors(ctx):
    embed1 = discord.Embed(
        title="Бот",
        url="https://discordapp.com/users/855320640008617984/",
        description="разработчик бота",
        color=discord.Color.gold()
        )
    embed2 = discord.Embed(
        title="Сайт",
        url="https://discordapp.com/users/374813384060829697/",
        description="разработчик сайта",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)


bot.run(settings.TOKEN)