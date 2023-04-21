import discord
from discord.ext import commands
import settings
import random
import datetime

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


@bot.command(name="about", description="краткая информация о боте")
async def about(ctx):
    open_file = open("about.txt", encoding="utf-8")
    text = open_file.read()
    await ctx.send(text)


@bot.command(name="feedback", description="позволяет вам отправить пожелания разработчику")
async def feedback(ctx, *text):
    channel = bot.get_channel(1098579383775658126)
    dt = datetime.datetime.now()
    author = ctx.author.mention
    await channel.send(f"Дата и время: { dt.strftime('%H:%M - %m.%d.%Y года')},")
    await channel.send(f"Отправитель: {author},")
    await channel.send(f"Пожеалния: {''.join(text)}.")


@bot.command(name="ban", description="Позволяет людям с ролью 'Модератор' банить пользователей")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, reason=None):
    moderator_role = 1099039238227509348
    if member:
        if moderator_role in [role.id for role in ctx.author.roles]:
            if reason is None:
                await ctx.send("Напишите причну бана.")
            else:
                await member.ban(reason=reason)
                await ctx.send(f"Вы успешно забанили пользователя {member}.Прична: {reason}")
                await member.send(f"Вас забанили на сервере."
                                  f"Забанивший модератор {ctx.author.mention}.")
        else:
            await ctx.send("У вас недостаточно прав для использования этой команды.")
    else:
        await ctx.send("Укажиет имя пользователя")


@bot.command(name="unban",
             description="Позволяет людям с ролью 'Модератор' разбанить пользователей")
async def unban(ctx, member: discord.User = None):
    moderator_role = 1099039238227509348
    invite = ctx.channel.create_invite()
    if member:
        if moderator_role in [role.id for role in ctx.author.roles]:
            await ctx.guild.unban(member)
            await ctx.send(f"Вы успешно разбанили пользователя {member}.")
            await member.send(f"Вас разабанили на сервере."
                              f"Разбанивший модератор {ctx.author.mention}.")
            await member.send(invite)
        else:
            await ctx.send("У вас недостаточно прав для использования этой команды.")
    else:
        await ctx.send("Укажиет имя пользователя")


@bot.command(name="kick", description="Позволяет людям с ролью 'Модератор' кикать пользователей.")
async def kick(ctx, member: discord.Member = None, reason=None):
    moderator_role = 1099039238227509348
    if moderator_role in [role.id for role in ctx.author.roles]:
        if reason:
            await member.kick(member, reason=reason)
            await ctx.send(f"Вы успешно кикнули пользователя {member}.Прична: {reason}")
            await member.send(f"Вас кикнули с сервера.Кикнувший модератор{ctx.author.mention}")

    else:
        await ctx.send("У вас недостаточно прав для использования этой команды.")


@bot.command(name="get_roles", description="все роли на сервере")
async def get_roles(ctx):
    all_roles = []
    for role in ctx.guild.roles:
        all_roles.append(role.name)
    embed = discord.Embed(
        title="\n".join(all_roles),
        description="все роли",
        colour=discord.Color.purple()
    )
    await ctx.send(embed=embed)


bot.run(settings.TOKEN)