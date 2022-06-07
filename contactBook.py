import sys
print('WELCOME TO YOUR CONTACT BOOK')
newData = []
def addData():
    name = input('Enter name to add: ')
    newData.append(name)
    try:
        number = int(input('Enter number: '))
        newData.append(number)
    except:
        print('wrong input, phone number only.')
    print('add another data?')
    another = input('Enter y or n or all data: ')
    if another == 'y':
        addData()
    elif another == 'n':
        sys.exit()
    elif another.upper() == 'ALL DATA':
        print(newData)
    else:
        print('wrong input.')
        print(another)

def findData():
    term = input('Enter search term: ')
    if term in newData:
        print(newData)
    else:
        print(term + ' not found, would you like to add data?: ')
        addData2 = input('Enter yes or no: ')
        if addData2 == 'yes':
            addData()
        elif addData2 == 'no':
            print('till next time USER')
        else:
            print(addData)
choice = input('Type TO FIND, TO ADD OR ALL DATA: ')
if choice.upper() == 'TO ADD':
    addData()
elif choice.upper() == 'TO FIND':
    findData()
elif choice.upper() == 'ALL DATA':
    print(newData)
else:
    print(choice)