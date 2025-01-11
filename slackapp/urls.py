from django.urls import path
from slackapp.views import SlackEventView

urlpatterns = [
    path('events', SlackEventView.as_view(), name='slack_events'),
]
