import time
print("""WELCOME TO THE ADVENTURE GAME!
    Let's start the action! ☆-🎬-☆
     
    Lily wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house.
    Now she has two choices she can either stay in the room or check what the sound might be about.
     
    Type your choice: Stay or Evaluate?
""")
def scene1():
    action = input('==>')
    if action.upper() == 'STAY':
        print('\nLily decides to stay in the room and ends up staying inside forever as none seems to come to help her.')
    elif action.upper() == 'EVALUATE':
        print('Lily exits the room silently and reaches the main hall.')
        scene2()
    else:
        print('ENTER THE CORRECT CHOICE')
       
def scene2():
    print("""
            In the main hall, she finds a strange but cute teddy bear on the floor. 
            She wanted to pick the teddy up. 
            But should she? It doesn't belong to her. (•˳̂•̆)
 
            Type your choice: Pick or Ignore?
 
            """)
    time.sleep(2)
    action = input('==>')
    if action.upper()=='PICK':
        print("""\nThe moment Lily picked up the the teddy bear. The Teddy bear starts TALKING!The bear tells Lily that she is in grave danger as there is a monster in the house.And the monster has captured her PARENTS as well!But he hugged her and told her not to get scared as he knows how to beat the moster!""")
        time.sleep(4)
        print("""\nThe bear handed lily a magical potion which can weaken the moster and make him run away!He handed her the potion and then DISAPPEARED!Lily moved forward.""")
    elif action.upper()=='IGNORE':
        print("""\nLily decided not to pick up the bear and walked forward.""")
    else:
        print('Wrong Input! Enter pick or ignore?')
        time.sleep(4)
    scene3()
def scene3():
    print("""\n\nAfter walking for a while, Lily saw the MONSTOR in front of her!
    It had red eyes and evil looks. She got very scared! """)
    print('Throw the magical portion or Ignore')
    action= input('==>')
    time.sleep(4)
    if (action.upper()=='THROW'):
        time.sleep(4)
        print("""But then she remembered! She had the magic portion and she threw it on the moster!
              Well she had nothing to lose!""")
        time.sleep(2)
        print('\n The monster SCREAMED in pain but he managed to make a portal and pushed Lily to a new world!')
    elif(action.upper()=='IGNORE'):
        print('The monster attacked Lily and hurt her! She was then thrown to the new world by the monster!')
scene1()
print('\n\n')
print('========End of chapter one=======')