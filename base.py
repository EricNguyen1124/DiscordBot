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
        file = open('Events', 'a')
        file.write(msg.content + "\n")
        await message.channel.send('THANKS')
        file.close()
        return

    if message.content.startswith('$current'):
        file = open('Events', 'r')
        fileLines = file.readlines()
        await message.channel.send('~~Listing events~~')
        for i in file:
            list.append(i)
        print(fileLines[4])


client.run('Njc2OTE3MTUwOTE2NjczNTg2.Xkb9IQ.P5ECTi1g0ihEe4ouIzCHIgMM9vw')