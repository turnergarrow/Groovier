# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

queue = []

bot = commands.Bot(command_prefix='-')

def is_channel(channel_name):
    def predicate(ctx):
        return ctx.message.channel.name == channel_name
    return commands.check(predicate)

@bot.command(name='p')
@is_channel('music-bot-commands')
async def play(ctx, arg):
    response = "I should add music to the queue now"
    queue.append(arg)
    await ctx.send(response)

@bot.command(name='s')
@is_channel('music-bot-commands')
async def play(ctx):
    response = "I should stop music now"
    await ctx.send(response)

@bot.command(name='n')
@is_channel('music-bot-commands')
async def play(ctx):
    response = "I should skip the current song and play the next in the queue"
    queue.pop(0)
    await ctx.send(response)

@bot.command(name='c')
@is_channel('music-bot-commands')
async def play(ctx):
    response = "I should clear the queue"
    await ctx.send(response)

@bot.command(name='q')
@is_channel('music-bot-commands')
async def play(ctx):
    response = "I should read out the queue"
    await ctx.send(queue)

@bot.command(name='m')
@is_channel('music-bot-commands')
async def play(ctx, arg):
    response = "I should move the queue around"
    await ctx.send(response)

bot.run(TOKEN)
