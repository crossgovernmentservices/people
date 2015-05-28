from twilio.rest import TwilioRestClient
import os
from flask.ext.mail import Message
from application.extensions import mail


class Notification(object):

    TWILIO_ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT_ID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

    def notify_email(self, email, message):
         msg = Message(message,
            recipients=[email])
         mail.send(msg)

    def notify_sms(self, phone_number, message):

        # skip the default show&tell phone number
        if '123456789' not in phone_number:
            twilio_account_id = Notification.TWILIO_ACCOUNT_ID
            twilio_auth_token = Notification.TWILIO_AUTH_TOKEN
            twillio_phone_number = Notification.TWILIO_PHONE_NUMBER

            client = TwilioRestClient(twilio_account_id, twilio_auth_token)
            client.sms.messages.create(to=phone_number, from_=twillio_phone_number, body=message)
