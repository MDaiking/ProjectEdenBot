from WebhookMessageSender import WebhookMessageSender

message = {
    "content":  f"{WebhookMessageSender.get_everyone_mention()}\n"
                f"17:00からミーティングを開始します"
}

WebhookMessageSender.send_message(message)
