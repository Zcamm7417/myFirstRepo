import re
matches = []
#234-000-000-0000 or (234)-000-000-0000
phoneRegex = r'((\d{3}|\(\d{3}\))?(\.|-|\s)?\d{3}(\.|\s|-)?\d{3}(\.|\s|-)?\d{4})'
text = input('paste here: ')
phoneNum = re.findall(phoneRegex, text)
matches.append(phoneNum)
if phoneNum == []:
	print('No mobile number detected')
#else:
#	print('\n', phoneNum)

#alaroabdulroqeeb5@gmail.com	
emailRegex = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}'
email = re.findall(emailRegex, text)
matches.append(email)
if email == []:
	print('No email detected')
#else:
#	print('\n', email)
print('\n',matches)	

