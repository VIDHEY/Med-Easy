from twilio.rest import Client

def send_message(to_num,content):
	account_sid = "ACa47e383f3196dbdf357329fa5c4c52a9"
	auth_token  = "bca092c95743c6aed91f4a2d304e9657"

	client = Client(account_sid, auth_token)
	message = client.messages.create(
	    to=to_num, 
	    from_="+19122446970",
	    body=content)

# print(message.sid)