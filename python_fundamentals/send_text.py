from twilio.rest import Client

def sendMeassage(client, body, to, from_):
	message = client.messages.create(
				body= body,
				to= to,
				from_= from_)
	# print(message.sid)

def verify(verificationInput, verificationCode):
	if verificationInput == verificationCode:
		print('Verification successful')
	else:
		print('Verification failed')



if __name__ == '__main__':
	account_sid = 'ACc75093f964bf9c24643b864c2700f9b9'
	auth_token = 'd353927aca5530dc070ba54fe37eff3f'		# Renew before use

	verificationCode = '123456'
	receiverNumber = '919090480487'
	senderNumber = '12038729948'

	client = Client(account_sid, auth_token)
	sendMeassage(client, verificationCode, receiverNumber, senderNumber)
	
	verificationInput = input('Enter verification code: ')
	verify(verificationInput, verificationCode)