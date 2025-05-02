from WebhookMessageSender import WebhookMessageSender

message = {
    "content": "テストメッセージを送信"
}

WebhookMessageSender.send_message(message)
