#Fortune teller with guess the letter 
input('Enter full name:')
while True:
	try:
		age = int(input('Enter age:'))
		break
	except ValueError:
		print('Age in number folk')

import random
number=random.randint(1, 30)
print('I am thinking of a number between 1 to 30')
#print(number)
for guesses in range(1, 6):
	print('Guess the number')
	guess=int(input('==>'))
	if guess> 30:
		print('Number btw 1 to 30, Olodoo')
	elif guess < number:
		print('That was close buh low.')
	elif guess > number and number <30:
		print ('That was close buh high.')

	else:
		break
if guess==number:
	print ('Good job folk, you guess my number in ' + str(guesses) + ' guesses.' 'You can now proceed to your fortune.')
	print('Your fortune is.......')
	def getNumber(answerNumber):
		if answerNumber==1:
			return 'It is certain you will make it😁😁.'
		elif answerNumber==2:
			return 'It is decidedly you will make it🤔🤔.'
		elif answerNumber==3:
			return 'Yes, right track. Keep at it🙃🙃.'
		elif answerNumber==4:
			return 'Fortune hazy, try again😐😐.'
		elif answerNumber==5:
			return 'Try again later, there is hope🙂🙂.'
		elif answerNumber==6:
			return 'Concentrate your mind and try again🥲🥲.'
		elif answerNumber==7:
			return 'I feel bad for you, Struggle harder😞😞.'
		elif answerNumber==8:
			return 'Outlook not so good folk, no advice👌👌.'
		elif answerNumber==9:
			return 'Very doubtful, for this....make offering to 2284828033....Zenith🙏🙏.'
	Rh=random.randint(1, 9)
	fortune=getNumber(Rh)
	print(fortune)
			
else:
	print('Oops, the number I was thinking of was ' + str(number) + '.')