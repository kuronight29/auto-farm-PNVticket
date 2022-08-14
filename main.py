import discord 
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

prefix = "-"

keep_alive()
token = (os.environ['TOKEN'])


bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command(pass_context=True)
async def farm(ctx):
    await ctx.message.delete()
    await ctx.send('auto farm **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(60)
            await ctx.send('.nhatrac')
            await asyncio.sleep(60)
            await ctx.send('.thuhoach')
            await ctx.send('.chatgo')

keep_alive()
bot.run(token, bot=False)