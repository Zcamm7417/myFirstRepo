import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAns = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s ='% (questionNumber, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes = ['^%s$' % (num1 * num2)],
        blockRegexes = [('.*', 'Incorrect')],
        timeout = 5, limit = 3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!!')
        correctAns += 1
        time.sleep(3)
        print('Score: %s / %s' % (correctAns, numberOfQuestions))