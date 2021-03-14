from twilio.rest import Client
import os
accountSid = os.environ.get("TWILIO_API_ID")
authToken = os.environ.get("TWILIO_API_TOKEN")
SENDER_NUMBER = "ENTER SENDER NUMBER HERE"
RECEIVER_NUMBER = "ENTER RECEIVING NUMBER HERE"


class NotificationManager:
    def __init__(self):
        self.client = Client(accountSid, authToken)
    def sendAlert(self,message):
        message = self.client.messages \
            .create(
            body=f"{message}",
            from_=SENDER_NUMBER,
            to=RECEIVER_NUMBER
        )