def isPhoneNumber(text):
	if len(text) !=12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal:
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal:
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i]. isdecimal:
			return False
	return True
message=input('paste text: ')
#message='Call me at 234-426-3618 tomorrow, office at 425-472-2848.'
for i in range(len(message)):
	chunk= message[i:i+12]
	if isPhoneNumber(chunk):
		print('phone number found: ' + chunk)
#print('Done')
