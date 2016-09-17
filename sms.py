import time
from sinchsms import SinchSMS
number = '+15879268106'
message = 'Do you need an uber?'
client = SinchSMS('06dd6c6a-97fc-479c-8559-f0140b1332e8', '+hPVMAIA5kalu6QJdiG/nA==')
print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']
response = client.check_status(message_id)
#while response['status'] != 'Successful':
#	print(response['status'])
time.sleep(1)
response = client.check_status(message_id)
print(response['status'])