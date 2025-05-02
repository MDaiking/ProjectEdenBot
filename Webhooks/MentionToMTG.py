import os
import sys
import requests
import json

webhook_url = os.environ.get("WEBHOOK_URL")

if webhook_url is None:
    print("There has no value in webhook_url")
    sys.exit(1)


def get_everyone_mention():
    return "@everyone "


message = {
    "content":  get_everyone_mention() + '\n' +
                "17:00からミーティングを開始します"
}


headers = {
    'Content-Type': 'application/json'
}


response = requests.post(webhook_url,
                         data=json.dumps(message),
                         headers=headers)

if response.status_code != 204:
    print(f"an error has occurred: {response.status_code}")
