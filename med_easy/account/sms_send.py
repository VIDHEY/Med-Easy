from twilio.rest import Client

def send_message(to_number,content, pin):
	account_sid = "ACa47e383f3196dbdf357329fa5c4c52a9"
	auth_token  = "bca092c95743c6aed91f4a2d304e9657"

	client = Client(account_sid, auth_token)
	pin='4545'
	message = client.messages.create(
	    to="+917017005842", 
	    from_="+19122446970",
	    body="Your One Time Password for med_easy.com is "+pin)

# print(message.sid)