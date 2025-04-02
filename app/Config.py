import os

async def get_upmarin_user(client):
    return await client.fetch_user(os.environ.get("UPMARIN_ID"))


async def get_token():
    return await os.environ.get("TOKEN")