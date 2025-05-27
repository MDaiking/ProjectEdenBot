import os
from WebhookMessageSender import WebhookMessageSender
from dotenv import load_dotenv

load_dotenv()
rd_development_id = os.environ.get("RDDEVELOPMENT_ID")

message = {
    "content":  f"{WebhookMessageSender.get_specific_mention(rd_development_id)}\n"
                f"17:00からミーティングを開始します"
}

WebhookMessageSender.send_message(message)
