import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

team_name = 1

overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    guild.me: discord.PermissionOverwrite(read_messages=True)
}

def make_channel(team_name):
  text_channel = await guild.create_text_channel(str(team_name), overwrites = overwrites)
  voice_channel = await guild.create_voice_channel(str(team_name), overwrites = overwrites)
  global team_name += 1

user_list = []

@client.event
async def on_member_join(member):
  global user_list
  if len(user_list) < 5:
    user_list.append(member)
    
