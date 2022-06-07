#TO KNOW THE LARGEST NUMBER IN LIST
mylist=[1,2,3,4,5,6,7]
jnum=0
for y in mylist:
	if y>jnum:
		jnum=y
print(f'largest number is {jnum}')
#TO KNOW THE SMALLEST NUMBER IN LIST
jnum=4627 #very large number
for y in mylist:
	if y<jnum:
		jnum=y
print(f'smallest number is {jnum}')
#TO KNOW THE NUMBER OF ELEMENT IN A LIST
gnum=0
for y in mylist:
	gnum +=1
print(gnum)
#TO KNOW THE NUMBER OF EVEN NUM IN LIST
odds=[]
evens=[]
onum=0
enum=0
for y in mylist:
	if y==0:
		continue
	elif y%2==0:
		odds.append(y)
		enum +=1
	#elif y%2==1:
#		enum +=1
	else:
		evens.append(y)
		onum +=1
print(enum)
print(onum)