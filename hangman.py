import random, time
print('\nWELCOME TO HANGMAN GAME BY ZCAMM')
name=input('Enter your name: ')
print('Hello '+ name.upper() +' Best of luck!')
time.sleep(2)
print('The game is about to start! \n Lets play Hangman!')
time.sleep(3)
 
def main():
    global count
    global display
    global word
    global alreadyGuessed
    global length
    global playGame
    wordsToGuess =['january', 'border', 'image', 'film', 'promise', 'kids', 'dunno', 'doll', 'rhyme', 'damage', 'plants']
    word = random.choice(wordsToGuess)
    length=len(word)
    count = 0
    display = '_' * length
    alreadyGuessed = []
    playGame = ''
def playLoop():
    global playGame
    playGame = input('Do you want to play again? y = yes, n = no \n')
    if playGame=='y':
        main()
    elif playGame=='n':
        print('Thanks for playing!')
        exit()
def hangman():
    global count
    global display
    global word
    global alreadyGuessed
    global playGame
    limit = 5
    guess = input('This is the hangman word:'+ display +'Enter your guess: \n')
    guess = guess.strip()
    if len(guess.strip())== 0 or len(guess.strip())== 2:
        print('Invalid Input, try a LETTER \n')
        hangman()
    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[index]+'_'+ word[index+1:]
        display = display[index]+ guess + display[index + 1:]
        print(display + '\n')
    elif guess in alreadyGuessed:
        print('Try another letter, already guessed this one/s. '+ str(alreadyGuessed) +'\n')
    else:
        count += 1
        if count ==1:
            time.sleep(1)
            print('______\n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|__   \n')
            print('Wrong guess. '+ str(limit - count)+ ' guesses remaining \n')
        elif count ==2:
            time.sleep(1)
            print('______\n'
                  '|    |\n'
                  '|    |\n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|__   \n')
            print('Wrong guess. '+ str(limit - count)+ ' guesses remaining \n')
        elif count ==3:
            time.sleep(1)
            print('______\n'
                  '|    |\n'
                  '|    |\n'
                  '|    |\n'
                  '|     \n'
                  '|     \n'
                  '|     \n'
                  '|__   \n')
            print('Wrong guess. '+ str(limit - count)+ ' guesses remaining \n')
        elif count ==4:
            time.sleep(1)
            print('______\n'
                  '|    |\n'
                  '|    |\n'
                  '|    |\n'
                  '|    0\n'
                  '|     \n'
                  '|     \n'
                  '|__   \n')
            print('Wrong guess. '+ str(limit - count)+ ' guesses remaining \n')
        elif count ==5:
            time.sleep(1)
            print('______\n'
                  '|    |\n'
                  '|    |\n'
                  '|    |\n'
                  '|    0\n'
                  '|   /|\ \n'
                  '|   / \ \n'
                  '|__   \n')
            print('Wrong guess. You are HANGED!!! \n')
            print('The word was:', alreadyGuessed,word)
            playLoop()
    
    if word == '_' * length:
        print('Congrats!!! You have guessed the word CORRECTLY!')
        playLoop()
    elif count != limit:
        hangman()
main()
hangman()