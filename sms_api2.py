import requests

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC950d6468759c4f5d16cf5b9b052baaad'
auth_token = 'e219c55a5bfb128aea3c8593a19e65f2'
phones=['+23436363667','+2347033377186']
for phone in phones[:]:
# The phone number you want to send the SMS from, and the phone number you want to send it to
    from_number = '+12058394287'
    to_number = phone

    # The body of the SMS message
    message_body = 'Kindly see your token here'

    # Make the request to the Twilio API
    response = requests.post(
        f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json',
        auth=(account_sid, auth_token),
        data={
            'From': from_number,
            'To': to_number,
            'Body': message_body
        }
    )

    # Print the response from the API
    print(response.status_code)
    print(response.text)