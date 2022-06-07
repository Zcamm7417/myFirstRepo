import re
import sys
password = r'[a-zA-Z]\d+'
text = input()
if len(text) < 8:
	print("password length is less than required")
	sys.exit()
strongPassword = re.search(password, text)
#print (strongPassword)
if strongPassword == None:
	print('weak password')
else:
	print('strong password')