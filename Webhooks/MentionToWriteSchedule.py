import os
from WebhookMessageSender import WebhookMessageSender
from dotenv import load_dotenv

load_dotenv()
schedule_table_url = os.environ.get("SCHEDULE_TABLE_URL")
rd_development_id = os.environ.get("RDDEVELOPMENT_ID")

if schedule_table_url is None:
    print("There has no value in schedule_table_url")
    schedule_table_url = "none_url"

message = {
    "content":  (f"{WebhookMessageSender.get_specific_mention(rd_development_id)}\n"
                 f"明日はミーティングです\n"
                 f"稼働表を確認してください\n"
                 f"{schedule_table_url}"
                 )
}

WebhookMessageSender.send_message(message)
