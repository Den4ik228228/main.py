import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Я готов!")


@bot.command()
async def hello(ctx):
    await ctx.send("Привет, человек!")


@bot.command()
async def bye(ctx):
    await ctx.send("Пока, человек!")


@bot.command()
async def repeat(ctx, times: int, content = "repeating..."):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run("MTE1NTU0OTQxNzI0MDI3NzAzMg.G2m02z.iUxyZw0Ng0G_dtaMBPqVLoFktyWg_oP94K5DPU")
import time
print('Здравствуй, здесь переводчик со сленгового языка, наслаждайся)')
while True:
    meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                "РОФЛ": "шутка",
                "ЩИЩ": "одобрение или восторг",
                "РИПОВЫЙ": "страшный, пугающий",
                "АГРИТЬСЯ": "злиться"
                }
    word = input("Введите непонятное слово (большими буквами!) или слово стоп: ")
    if word.upper() in meme_dict.keys():
        print(meme_dict[word.upper()])
    elif word == 'стоп':
        break
    else:
        print('Такого слова нет в словаре(')
    time.sleep(2)
