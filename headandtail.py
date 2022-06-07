import random
#p= numpy.random.randint(1,20)
#print(p)
heads=[]
tails=[]
#coin = {0:head, 1:tail}
for n in range(10):
	f=(random.randint(0, 1))
	if f == 0:
		heads.append("head")
	else:
		tails.append("tail")
	#print(f)
	#print(len(heads))
print(f"there are {len(tails)} tails and {len(heads)} heads")