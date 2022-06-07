import random
print('Guess the number I am thinking of ')
num = random.randint(1, 10)
#print(num)
for i in range(-5, 0):
    try:
        guess = int(input('Enter guess: '))
    except:
        print('Integers only')
    
    if guess == num:
        print('Congratulations you won ')
        break
    else:
       print('try again ' + str(i+1)+  ' tries left')
    