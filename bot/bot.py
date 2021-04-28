import os
import random

from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# commands are case sensitive. overwhelming feedback to fix this.
bot = commands.Bot(command_prefix='rat ')


@bot.command(name='whaddup', help='Say hi to your friendly neighbourhood RAT')
async def rat_reply(ctx):
    rat_replies = [
        'eat shit@@@@@@@@@@@',
        'roll me 10m rn.',
        'die.',
        'ay yo ock',
        'u r bich',
        ('Hi I am an IRS representative and I would like to inform you'
         'that you are in the IRS blacklist.'
         'Please provide me your SSN and debit card # if you dont want to be terminated.'),
        'gimme back my lunch money',
        'sawp',
        'get good when?'
    ]
    message = random.choice(rat_replies)
    await ctx.send(message)

@bot.command(name='rollme', help='roll the lil rat for bragging rights')
async def rat_roll(ctx):
    user_dice = random.choice(range(1, 100 + 1))
    rat_dice = random.choice(range(1, 100 + 1))

    await ctx.send('You: Rolling a 100-sided die, and rolled a ' + str(user_dice) +
                   '\nRat: Rolling a 100-sided die, and rolled a ' + str(rat_dice))
    if rat_dice > user_dice:
        await ctx.send('gimme my lunch money')
    elif rat_dice < user_dice:
        await ctx.send('die.')
    elif rat_dice == user_dice:
        await ctx.send('o.o')

bot.run(TOKEN)