import sys
import Config
from flask import Flask
from threading import Thread


async def close(client, message):
    if message.author.guild_permissions.administrator:
        upmarin_mention = Config.get_upmarin_user(client).mention
        await message.channel.send('Botを停止します。'
                                   f'再度起動したい場合は {upmarin_mention} を呼んでください')
        await client.close()
        sys.exit()
    else:
        await message.channel.send("このコマンドを実行する権限がありません")

app = Flask('')


@app.route('/')
def main():
    return "Bot is alive"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
