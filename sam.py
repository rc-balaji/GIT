from twilio.rest import Client

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+916383579334",  # Make sure to include the '+' and the country code
    from_="+16508806956",  # Replace with your Twilio phone number
    body="Hello! This is a test message.",  # Add the message content
)

print(message.sid)
