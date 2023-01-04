#this implementation uses python 3.10 and above
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Your Account SID and Auth Token from twilio.com/console


account_sid = 'AC950d6468759c4f5d16cf5b9b052baaad'
auth_token = 'e219c55a5bfb128aea3c8593a19e65f2'

# The phone number you want to send the SMS from, and the phone number you want to send it to
from_number = '+12058394287'
to_number = '+2347033377186'

# The body of the SMS message
message_body = 'Hello, world!'
client = Client(account_sid, auth_token)
message = client.messages.create(
  to='+2347033377186',
  from_='+12058394287',
  body='Hello, world!'
)
