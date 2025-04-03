import discord
import Config
import BasicFunc
from server import server_thread

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    print(f'{client.user} responced the messages: {message.content}')

    if message.content == '/TestText':
        await message.channel.send('これはテスト用テキストです')

    if message.content == '/Close':
        await BasicFunc.close(message)

server_thread()
client.run(Config.get_token())
