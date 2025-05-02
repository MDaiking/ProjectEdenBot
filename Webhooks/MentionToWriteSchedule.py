import os
import sys
import requests
import json

webhook_url = os.environ.get("WEBHOOK_URL")
schedule_table_url = os.environ.get("SCHEDULE_TABLE_URL")

if webhook_url is None:
    print("There has no value in webhook_url")
    sys.exit(1)

if schedule_table_url is None:
    print("There has no value in schedule_table_url")
    sys.exit(1)


def get_everyone_mention():
    return "@everyone "


message = {
    "content":  get_everyone_mention() + '\n' +
                "明日はミーティングです" + '\n' +
                "稼働表を確認してください" + '\n' +
                schedule_table_url
}


headers = {
    'Content-Type': 'application/json'
}


response = requests.post(webhook_url,
                         data=json.dumps(message),
                         headers=headers)

if response.status_code != 204:
    print(f"an error has occurred: {response.status_code}")
