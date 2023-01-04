#this implementation uses python 3.10 and above
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Your Account SID and Auth Token from twilio.com/console


account_sid = 'sid'
auth_token = 'token'

# The phone number you want to send the SMS from, and the phone number you want to send it to


# The body of the SMS message
message_body = 'Hello, world!'
client = Client(account_sid, auth_token)
message = client.messages.create(
  to='+234567778888888',
  from_='+12345678909',
  body='your token'
)
