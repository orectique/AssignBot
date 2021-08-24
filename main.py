import discord
import os
import random
import math

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

lock = True
members = []



@client.event
async def on_message(message):

    global lock, members, category
    person = message.author
    guild = message.guild

    if message.author == client.user:
        return

    if message.content.startswith('$AssignMe'):
        if lock != False:
            return await message.channel.send('The player list has been locked by the Admin.')

        if person not in members:
            members.append(person)
            await message.channel.send('Added')

        else:
            await message.channel.send('You are already in the list.')

    if message.content.startswith('$MakeTeam') and person.guild_permissions.manage_messages == True:
        lock = True
        random.shuffle(members)
        size = 4
        n = math.ceil(len(members)/size)
        category = await guild.create_category_channel('Quiz')
        for i in range(n):
            team_name = 'team-' + str(i + 1)
            team = members[:size]
            members = members[size:]
            overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        }
            for member in team:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True)
        
            await category.create_text_channel(team_name, overwrites=overwrites)

    if message.content.startswith('$Lock') and person.guild_permissions.manage_messages == True:
        lock = True
        await message.channel.send('Locked')

    if message.content.startswith('$Unlock') and person.guild_permissions.manage_messages == True:
        lock = False
        await message.channel.send('Unlocked')

    if message.content.startswith('$AssignReset') and person.guild_permissions.manage_messages == True:
        members = []
        channels = category.channels
        for channel in channels:
            await channel.delete()
        await category.delete()


TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

    
