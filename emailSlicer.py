import time
print('WELCOME TO EMAIL SLICER')
time.sleep(3)
email = input('Enter your Email: ').strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]

print('Your username is ' + username + ' and your domain is '+ domain )