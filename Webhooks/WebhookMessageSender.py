import os
import requests
import json


class WebhookMessageSender:

    _webhook_url = os.environ.get("WEBHOOK_URL")

    _headers = {
        'Content-Type': 'application/json'
    }

    def send_message(self, message):
        if self._webhook_url is None:
            print("There has no value in webhook_url")
            return

        response = requests.post(
                                self._webhook_url,
                                data=json.dumps(message),
                                headers=self._headers
                                )

        if response.status_code != 204:
            print(f"an error has occurred: {response.status_code}")

    def get_everyone_mention():
        return "@everyone "
