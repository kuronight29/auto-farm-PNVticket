import discord 
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

prefix = ('-')
token = os.getenv('Token')

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    print("Online!")

@bot.command()
async def farm(ctx, prefix):
    await ctx.message.delete()
    await ctx.send('.diemdanh')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(60)
            await ctx.send('.nhatrac')
            await asyncio.sleep(60)
            await ctx.send('.thuhoach')
            await ctx.send('.chatgo')

bot.run(token, bot=False)
