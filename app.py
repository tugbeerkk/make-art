import discord 
from discord.ext import commands
from config import *
from logic3 import *
from logic4 import *
from main import get_image

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")


@bot.command()
async def resim(ctx, *args: str):
    prompt = " ".join(args)
    encoded_image = get_image(prompt)
    toImg(encoded_image,"image.png")
    await ctx.send(file=discord.File("image.png"))

bot.run(TOKEN)