import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Its certain'
    elif answerNumber == 2:
        return 'its so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'try again'
    elif answerNumber == 5:
        return 'later dude'
    elif answerNumber == 6:
        return 'this is 6'
    elif answerNumber == 7:
        return 'no'
    elif answerNumber == 8:
        return 'not looking good'
    elif answerNumber == 9:
        return 'very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)