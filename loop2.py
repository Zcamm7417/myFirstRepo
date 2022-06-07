mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my=[]
for i in mylist:
	result=i+2
	#print(result)
	my.append(result)
print(my)
print('Done')
for i in range(5):
	print('cool')
	print(i)
total=0
for num in range(0,101):
	total=total + num
print(total)
#TO CHECK IF A NUMBER IS A PRIME NUMBER
while True:
	num=int(input('enter a number:'))
	flag=0
	for i in range(2, num):
		if num %i==0:
			flag=1
			print(i)
			break
	if flag == 0:
		print(f'{num} is a prime number')
	else:
		print(f'{num} is not a prime number')