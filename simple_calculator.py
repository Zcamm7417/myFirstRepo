#this is a simple calculator program 
#this function add two numbers
def add (x, y):
	return x + y
#this function substract two numbers
def subtract (x, y):
  return x - y
#this function multiply two numbers
def multiply (x, y):
  return x * y
#this function divide two numbers
def divide (x, y):
	return x / y

print ('select a fucking operation.')
print ('1. Add')
print ('2. Subtract')
print ('3. Multiply')
print ('4. Divide')
while True :
	choice = input('Enter choice (1 / 2 / 3 / 4) : ')
#check if choice is one of the options
if choice in ('1', '2', '3', '4'):
	num1 = float(input('enter first number: '))
	num2 = float(input('enter second number:'))
	if choice == '1':
		print(num1, '+', num2, '=', add (num1, num2))
	elif choice == '2':
		print( num1, '-', num2, '=', subtract (num1, num2))
	elif chioce == '3':
		print( num1, '*', num2, '=', multiply (num1, num2))
	elif choice == '4':
		print( num1, '/', num2, '=', divide (num1, num2))
#to check if user want to perform another calculation
next_calculation = input ('lets do next calculation? (yes / no): ')
if next_calculation == 'no' :
	'break'	

else :
		print('Get the fuck out')