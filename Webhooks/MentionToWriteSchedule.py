import os
import sys
from WebhookMessageSender import WebhookMessageSender

schedule_table_url = os.environ.get("SCHEDULE_TABLE_URL")

if schedule_table_url is None:
    print("There has no value in schedule_table_url")
    sys.exit(1)

message = {
    "content":  (f"{WebhookMessageSender.get_everyone_mention()}\n"
                 f"明日はミーティングです\n"
                 f"稼働表を確認してください\n"
                 f"{schedule_table_url}"
                 )
}

WebhookMessageSender.send_message(message)
