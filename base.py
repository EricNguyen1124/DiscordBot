import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello') and message.author.id == 217067578533740544:
        await message.channel.send('Please type in a new event!')

        msg = await client.wait_for('message')
        file = open('Events', 'w')
        file.write(msg.content)

        await message.channel.send('THANKS')
        return

client.run('Njc2OTE3MTUwOTE2NjczNTg2.XkMsRA.X1B-vZLWEr3sqK2vaBTEzp3BVX0')