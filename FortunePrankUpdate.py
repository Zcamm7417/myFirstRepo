#fortune teller update 
import random
input('Enter full name:')
while True:
	try:
		age=int(input('Enter age:'))
		break
	except ValueError:
		print('Age in number olodoo')
number= random.randint(1, 30)
print('I am thinking of a number between 1 to 30')
print(number)
for i in range(1, 6):
	print('Guess the number')
	guess=int(input('==>'))
	if guess< number:
		print('That was close buh too low')
	elif guess >30:
		print('Number between 1 to 30, Olodoo')
	elif guess> number and guess< 30:
		print('That was close buh too high')
	else:
		break
if guess==number:
	print('Good job folk, you guessed the number in '+ str(i) +' guess.')
	print('YOUR FORTUNE !!!!!')
	fortune = ['It is certain you will make it😊😊',
 'It is decidedly you will make it so🤔🤔',
 'Yes definitely make it👌👌',
 'Reply hazy try again😞😞',
 'Ask again later😼😼',
 'Concentrate and ask again🙃🙃',
 'My reply is no, no fortune😼😼',
 'Outlook not so good, work harder😑😑',
 'Very doubtful, be sure🥺🥺']
print(fortune[random.randint(0, len(fortune) - 1)])