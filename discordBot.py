import discord 

TOKEN = "QTQwOTgzNjExNjgxODA4Mzg0.YgPVRw.4kU1yQbBKv1Rxhnfxaz9xavdpfw"

client = discord.client()

@client.event
async def on_ready():
    print("{0.user is online!".format(client))

@client.event
async def on_message(message):
    if message.autor == client.user:
        return
    
    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("hello from the side")

client.run(TOKEN)