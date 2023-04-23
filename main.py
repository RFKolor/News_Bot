import discord
from discord.ext import commands
import settings
import random
import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents)
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents,
                   activity=discord.Game(name="!help"))
bot.remove_command("help")


#найтройка команды !help
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description="Используйте !help <команда>, чтобы получить описание команды",
        color=discord.Color.random())
    embed.add_field(name="Модерация", value="ban, kick, unban")
    embed.add_field(name="Развлечния", value="flip, rps, hello")
    embed.add_field(name="Сайт, Бот", value="link, about, get_roles")
    embed.add_field(name="Авторы", value="authors, feedback")
    await ctx.send(embed=embed)


@help.command()
async def ban(ctx):
    embed = discord.Embed(
        title="ban",
        description="Позволяет людям с ролью 'Модератор' банить пользователей",
        color=discord.Color.purple()
    )
    embed.add_field(name="**Синтаксис**", value="!ban <имя пользователя> <причина>")
    await ctx.send(embed=embed)


@help.command()
async def unban(ctx):
    embed = discord.Embed(
        title="unban",
        description="Позволяет людям с ролью 'Модератор' разбанить пользователей",
        color=discord.Color.purple()
    )
    embed.add_field(name="**Синтаксис**", value="!unban <имя пользователя>")
    await ctx.send(embed=embed)


@help.command()
async def kick(ctx):
    embed = discord.Embed(
        title="kick",
        description="Позволяет людям с ролью 'Модератор' кикать пользователей.",
        color=discord.Color.purple()
    )
    embed.add_field(name="**Синтаксис**", value="!kick <имя пользователя> <причина>")
    await ctx.send(embed=embed)


@help.command()
async def hello(ctx):
    embed = discord.Embed(
        title="hello",
        description="Бот с вами здоровается",
        color=discord.Color.purple()
    )
    await ctx.send(embed=embed)


@help.command()
async def flip(ctx):
    embed = discord.Embed(
        title="flip",
        description="Орел и решка",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)


@help.command()
async def rps(ctx):
    embed = discord.Embed(
        title="rps",
        description="Камень ножницы бумага.За победу над ботом выдается особая роль",
        color=discord.Color.green()
    )
    embed.add_field(name="**Синтаксис**", value="!rps <значение (камень,бумага или камень)>")
    await ctx.send(embed=embed)


@help.command()
async def get_roles(ctx):
    embed = discord.Embed(
        title="get_roles",
        description="все роли на сервере",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)


@help.command()
async def about(ctx):
    embed = discord.Embed(
        title="about",
        description="краткая информация о боте",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)


@help.command()
async def link(ctx):
    embed = discord.Embed(
        title="link",
        description="Ссылка на наш сайт",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)


@help.command()
async def authors(ctx):
    embed = discord.Embed(
        title="authors",
        description="ссылки на аккаунты разабочтиков бота и сайта",
        color=discord.Color.dark_blue()
    )
    await ctx.send(embed=embed)


@help.command()
async def feedback(ctx):
    embed = discord.Embed(
        title="feedback",
        description="позволяет вам отправить пожелания разработчикам."
                    "Сообщение нужно будет взять в кавычки",
        color=discord.Color.dark_blue())
    embed.add_field(name="**Синтаксис**", value='!feedbаck "<пожелания>"')
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
   print("бот работает")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1096361181574340649)
    role = discord.utils.get(member.guild.roles, id=1099246641325813781)
    await member.add_roles(role)
    await channel.send(embed=discord.Embed(description=f"{member.mention}, "
                                                       f"добро пожаловать на сервер!",
                                           color=discord.Color.green()))


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1096361181574340649)
    await channel.send(embed=discord.Embed(description=f"До новых встреч, {member.mention}!",
                                           color=discord.Color.green()))


@bot.event
async def on_message(message):
   for i in settings.ban_words:
      if i in message.content:
         await message.delete()
         await message.channel.send(f"{message.author.mention} Не выражаться!")
         return
   await bot.process_commands(message)


@bot.command(name="flip")
async def flip(ctx):
    coins = ["орел", "решка"]
    embed = discord.Embed(
        title=random.choice(coins),
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f"Привет {ctx.author.name}!")


@bot.command(name="link")
async def link(ctx):
    embed = discord.Embed(
        title=">---сслыка---<",
        url="https://ya.ru/",
        description="ссылка на наш сайт",
        color=discord.Color.random()
    )
    await ctx.send(embed=embed)


@bot.command(name="authors")
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


@bot.command(name="about")
async def about(ctx):
    open_file = open("about.txt", encoding="utf-8")
    text = open_file.read()
    await ctx.send(text)


@bot.command(name="feedback")
async def feedback(ctx, *text):
    channel = bot.get_channel(1098579383775658126)
    dt = datetime.datetime.now()
    author = ctx.author.mention
    await channel.send(f"Дата и время: { dt.strftime('%H:%M - %m.%d.%Y года')},")
    await channel.send(f"Отправитель: {author},")
    await channel.send(f"Пожелания: {''.join(text)}.")


@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, reason=None):
    moderator_role = 1099039238227509348
    text = ""
    if member:
        if moderator_role in [role.id for role in ctx.author.roles]:
            if reason is None:
                text = "Напишите причну бана."
            else:
                await member.ban(reason=reason)
                text = f"Вы успешно забанили пользователя {member}.Прична: {reason}"
        else:
            text = "У вас недостаточно прав для использования этой команды."
    else:
        text = "Укажите имя пользователя"
    await ctx.send(text)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У вас недостаточно прав для использования этой команды")


@bot.command(name="unban")
@commands.has_permissions(administrator=True)
async def unban(ctx, member: discord.User = None):
    moderator_role = 1099039238227509348
    if member:
        if moderator_role in [role.id for role in ctx.author.roles]:
            await ctx.guild.unban(member)
            await ctx.send(f"Вы успешно разбанили пользователя {member}.")
            await member.send(f"Вас разбанили на сервере.Ссылка - {settings.link}")
        else:
            await ctx.send("У вас недостаточно прав для использования этой команды.")
    else:
        await ctx.send("Укажите имя пользователя")


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У вас недостаточно прав для использования этой команды")


@bot.command(name="kick")
async def kick(ctx, member: discord.Member = None, *, reason=None):
    moderator_role = 1099039238227509348
    text = ""
    if moderator_role in [role.id for role in ctx.author.roles]:
        if reason:
            await member.kick(reason=reason)
            text = f"Вы успешно кикнули пользователя {member}.Прична: {reason}"
        else:
            text = "Укажите причину кика"
    else:
        text = "У вас недостаточно прав для использования этой команды."
    await ctx.send(text)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У вас недостаточно прав для использования этой команды")


@bot.command(name="get_roles")
async def get_roles(ctx):
    all_roles = []
    for role in ctx.guild.roles:
        all_roles.append(role.name)
    embed = discord.Embed(
        title="Все роли",
        description="\n".join(all_roles),
        colour=discord.Color.purple()
    )
    await ctx.send(embed=embed)


@bot.command(name="rps")
async def rps(ctx, text):
    arr = ["камень", "ножницы", "бумага"]
    member = ctx.author
    answer = random.choice(arr)
    role = discord.utils.get(member.guild.roles, id=1099623230790176768)
    if text == "камень" or text == "ножницы" or text == "бумага":
        if answer == text:
            await ctx.send("Ничья")
        elif answer == "камень" and text == "ножницы":
            await ctx.send(f"Ты выбрал {text}, я выбрал {answer}")
            await ctx.send("Я победил")
        elif answer == "камень" and text == "бумага":
            await ctx.send(f"Ты выбрал {text}, я выбрад {answer}")
            await ctx.send("Ты победил, молодец!")
            await member.add_roles(role)
        elif answer == "ножницы" and text == "бумага":
            await ctx.send(f"Ты выбрал {text}, я выбрал {answer}")
            await ctx.send("Я победил")
        elif answer == "ножницы" and text == "камень":
            await ctx.send(f"Ты выбрал {text}, я выбрал {answer}")
            await ctx.send("Ты победил, молодец!")
            await member.add_roles(role)
        elif answer == "бумага" and text == "камень":
            await ctx.send(f"Ты выбрал {text}, я выбрал {answer}")
            await ctx.send("Я победил")
        elif answer == "бумага" and text == "ножницы":
            await ctx.send(f"Ты выбрал {text}, я выбрал {answer}")
            await ctx.send("Ты победил, молодец!")
            await member.add_roles(role)
    else:
        await ctx.send("Неправильный ввод")


bot.run(settings.TOKEN)