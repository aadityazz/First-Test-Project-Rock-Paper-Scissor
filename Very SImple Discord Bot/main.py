import discord
import os
from discord.ext import commands
from random import choice
from Alive import keep_alive

client = discord.Client()
bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")
l = ['rock', 'paper', 'scissor']
p = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global l
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('.hello'):
        await message.channel.send("Hello!, Lets play")

    elif msg.startswith('.r'):
        random = choice(l)
        if random == l[0]:
            await message.channel.send("I am rock, Its tie play again")
        elif random == l[1]:
            await message.channel.send("I am paper, I wom U loose Now Fcuk off")
        else:
            await message.channel.send("I am scissor, Shit! u won I loose")

    elif msg.startswith('.p'):
        random = choice(l)
        if random == l[0]:
            await message.channel.send("I am rock, Shit! u won I loose")
        elif random == l[1]:
            await message.channel.send("I am paper, Its tie play again")
        else:
            await message.channel.send("I am scissor, I wom U loose Now Fcuk off")

    elif msg.startswith('.s'):
        random = choice(l)
        if random == l[0]:
            await message.channel.send("I am rock, I wom U loose Now Fcuk off")
        elif random == l[1]:
            await message.channel.send("I am paper,Shit! u won I loose")
        else:
            await message.channel.send("I am scissor, Its tie play again")


keep_alive()
client.run(os.getenv('TOKEN'))