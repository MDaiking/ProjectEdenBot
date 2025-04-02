from dotenv import load_dotenv
load_dotenv()

import os

async def get_upmarin_user(client):
    return await client.fetch_user(os.getenv('UPMARIN_ID'))


async def get_token():
    return await os.getenv('TOKEN')