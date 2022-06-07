print('Welcome to Zcamm Advanced Calculator')
while True:
	print('Enter Password')
	password=input('')
	if password!='Goodboy':
		continue
	else:
		print('Choose Operation from below listed 👀')
		break
print('History')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exponential')
print('6. SquareRoot')
print('7. Sine')
print('8. Cosine')
print('9. Tangent')
print ('10. FindAreaOfCircle')
print('11. Factorial')
print('12. HighestCommonFactor')
print('13. DegreeToRadian')
print('14. RadianToDegree')
print('15. ToKnowIfANumberIsPrime')
print('16. Logarithms')

history=[]

while True:
	import math
	operation=input('')
	if operation=='history':
		history.append(work)
		print(history)
		break
	elif operation=='1':
		a=float(input('Enter first number:'))
		b=float(input('Enter second number:'))
		work=a+b
		print(work)
	elif operation=='2':
		a=float(input('Enter first number:'))
		b=float(input('Enter second number:'))
		work=a-b
		print(work)
	elif operation=='3':
		a=float(input('Enter first number:'))
		b=float(input('Enter second number:'))
		work=a*b
		print(work)
	elif operation=='4':
		a=float(input('Enter first number:'))
		b=float(input('Enter divisor:'))
		work=a/b
		print(work)
	elif operation=='5':
		a=float(input('Enter first number:'))
		b=float(input('Enter power:'))
		work=a**b
		print(work)
	elif operation=='6':
		a=float(input('Enter number:'))
		work=math.sqrt(a)
		print(work)
	elif operation=='7':
		print('q=multiplication then sine')
		print('r=sine only')
		choices=input('q or r:')
		if choices=='q':
			a=float(input('Enter first number:'))
			b=float(input('Enter number to sine:'))
			work=math.sin(b)
			print(work*a)
		if choices=='r':
			a=float(input('Enter number to sine:'))
			work=math.sin(a)
			print(work)
	elif operation=='8':
		print('q=multiplication then cosine')
		print('r=cosine only')
		choices=input('q or r:')
		if choices=='q':
			a=float(input('Enter first number:'))
			b=float(input('Enter number to cosine:'))
			work=math.cos(b)
			print(work*a)
		if choices=='r':
			a=float(input('Enter number to cosine:'))
			work=math.cos(a)
			print(work)
	elif operation=='9':
		print('q=multiplication then tagent')
		print('r=tagent only')
		choices=input('q or r:')
		if choices=='q':
			a=float(input('Enter first number:'))
			b=float(input('Enter number to tagent:'))
			work=math.sin(b)
			print(work*a)
		if choices=='r':
			a=float(input('Enter number to tagent:'))
			work=math.sin(a)
			print(work)
	elif operation=='10':
		work=math.pi
		r=float(input('Enter radius of the circle'))
		print(work * r * r)
	elif operation=='11':
		work=math.factorial
		a=int(input('Enter number to factorial: !'))
		print(work(a))
	elif operation=='12':
		a=int(input('Enter first number:'))
		b=int(input('Enter second number:'))
		work=(math.gcd(a,b))
		print(work)
	elif operation=='13':
		a=float(input('Enter number degrees to radians:'))
		work=(math.radians(a))
		print(work)
	elif operation=='14':
		a=float(input('Enter number radians to degrees'))
		work=(math.degrees(a))
		print(work)
	elif operation=='15':
		a=int(input('Enter number:'))
		flag=0
		for i in range(2, a):
			if a %i==1:
				print(f'{a} is a prime number')
				flag=1
			break
		else:
			print(f'{a} is not a prime number')
	elif operation=='16':
		a=float(input('Enter number:'))
		b=float(input('Enter base:'))
		work=math.log(a,b)
		print(work)
	else:
			print('Syntax Error')		