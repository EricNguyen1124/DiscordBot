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

        if msg.author != client.user:
            file = open('Events', 'a')
            file.write(msg.content + "\n")
            await message.channel.send('THANKS')
            file.close()

        return

    if message.content.startswith('$current'):
        count = 0
        file = open('Events', 'r')
        embed = discord.Embed(title="Listing Events", description="", color=0x00ff00)

        for i in file:
            count += 1
            embed.add_field(name=str(count), value=i, inline=False)

        await message.channel.send(embed=embed)
        file.close()
        return

    if message.content.startswith('$edit'):
        count = 0
        file = open('Events', 'r')
        embed = discord.Embed(title="Listing Events", description="", color=0x00ff00)

        for i in file:
            count += 1
            embed.add_field(name=str(count), value=i, inline=False)

        embed.add_field(name='Instructions:', value='Please reply with what event you would like to edit', inline=False)
        await message.channel.send(embed=embed)
        file.close()

client.run('Njc2OTE3MTUwOTE2NjczNTg2.Xkb9IQ.P5ECTi1g0ihEe4ouIzCHIgMM9vw')