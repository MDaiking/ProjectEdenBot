import os
from dotenv import load_dotenv


load_dotenv()


async def get_upmarin_user(client):
    return await client.fetch_user(os.getenv('UPMARIN_ID'))


def get_token():
    return os.getenv('TOKEN')
