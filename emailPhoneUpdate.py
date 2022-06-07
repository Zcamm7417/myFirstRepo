import pyperclip, re
#234-814-3615
phoneRegex = r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)?\d{4}(\s*(ext|x|ext.)\s*\d{2, 5})?)'
#abdulroqeebalaro5@gmail.com		
emailRegex = r'[a-bA-B0-9._%+]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2, 4})'
text = str(input('Paste here: '))

print("regex found", re.findall(phoneRegex, text))
matches=[]
for groups in re.findall(phoneRegex, text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	print ("phoneNum", phoneNum)
	if groups[0] != '':
		phoneNum += 'x' + groups[0]
		matches.append(phoneNum)
for groups in emailRegex.findall(emailRegex, text):
	print('Email found', re.findall(emailRegex, text))
	matches.append(groups[0])
	
if len(matches) > 0:
	print(matches)
else:
	print('No phone number or Email address found')