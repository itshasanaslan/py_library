import discord

TOKEN = 'NjY2NzcwNTA0OTI4OTg1MDg4.Xh5Axw.TKAOJOGQ_ecDiBB3k2vJGMlVZDE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} You can type !info'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("!info"):
        msg = 'I am coded by Aslan. I am still on the beta process.\nI will be Jarvis in a year.'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)