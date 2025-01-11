import os
import json
from django.core.wsgi import get_wsgi_application
from mangum import Mangum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()

def lambda_handler(event, context):
    print("Received event:", event)

    if event.get("body"):
        body = json.loads(event["body"])
        if body.get("type") == "url_verification":
            return {
                "statusCode": 200,
                "body": body["challenge"]
            }

    handler = Mangum(application)
    return handler(event, context)
