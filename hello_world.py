#This program check the lenght of your name and estimate how old you will be in four years with your present age.
print('Hello world!')

print('what is your name?')
#This will take input from user
my_name=input('Enter your name:')
#This will get the lenght of the inputed name
my_prefix = input('Enter Mr or Mrs(Mr/Mrs):')
if my_prefix=="Mr":
	print('Mr ' +my_name + ' It is good to meet you.')
elif my_prefix=="Mrs":
	print('Mrs '+my_name + ' It is good to meet you.')
print('The lenght of your name is:')
print(len(my_name))
#This will plus one your age
print('what is your age?')
my_age=input('Enter your age:')
print('you will be ' + str(int(my_age)+4) + ' in four years.')
print('Wish you good health from Zcamm')

