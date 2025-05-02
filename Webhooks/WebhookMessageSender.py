import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


class WebhookMessageSender:

    def _get_webhook_url():
        return os.environ.get("WEBHOOK_URL")

    def _get_headers():
        return {
                    'Content-Type': 'application/json'
                }

    @classmethod
    def send_message(cls, message):
        _webhook_url = cls._get_webhook_url()
        if _webhook_url is None:
            print("There has no value in webhook_url")
            return

        _headers = cls._get_headers()
        if _headers is None:
            print("There has no value in headers")
            return

        response = requests.post(
                                _webhook_url,
                                data=json.dumps(message),
                                headers=_headers
                                )

        if response.status_code != 204:
            print(f"an error has occurred: {response.status_code}")

    def get_everyone_mention():
        return "@everyone "
