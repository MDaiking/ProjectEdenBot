import os

async def get_upmarin_user(client):
    await upmarin_id = os.environ.get("UPMARIN_ID")
    return await client.fetch_user(upmarin_id)


async def get_token():
    return await os.environ.get("TOKEN")