from django.http import JsonResponse
from rest_framework.views import APIView
import os
import requests

class SlackEventView(APIView):
    def post(self, request, *args, **kwargs):
        event_data = request.data

        if "challenge" in event_data:
            return JsonResponse({"challenge": event_data["challenge"]})

        event = event_data.get("event", {})
        if event.get("type") == "message" and "hello" in event.get("text", "").lower():
            self.send_message(event["channel"], "hello_slack!")

        return JsonResponse({"status": "ok"})

    def send_message(self, channel, text):
        url = "https://slack.com/api/chat.postMessage"
        headers = {
            "Authorization": f"Bearer {os.environ.get('SLACK_BOT_TOKEN')}",
            "Content-Type": "application/json",
        }
        payload = {"channel": channel, "text": text}
        requests.post(url, json=payload, headers=headers)
