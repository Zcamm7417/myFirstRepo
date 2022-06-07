import re 

test = "name is roqerbb and phone number is 234-567-890-3627. please call me, 234-676-891-3728, "

test2= "my name is me"
phoneRegex = r'\d{3}|\(\d{3}\)?(\.|-|\s)?\d{3}(\.|\s|-)?\d{3}(\.|\s|-)?\d{4}'

phone = re.findall(r"\d{3}-\d{3}-\d+", test)
print(re.findall(phoneRegex, test))

if phone == []:
	print("No number detected")
print('\n',phone)
#for i in phone:
#	'\n'.sep(phone2.append(str(i)))
	
#print('\n'.sep(phone2))


email = "I am a good boy and my email address is abdulroqeebalaro5@gmail.com"

emailRegex = r'[a-zA-Z0-9+]+@[a-zA-Z0-9]+\.[a-z]{2,4}'

emailResult = re.findall(emailRegex, email)
print(emailResult)
