import re

UP_REGEX = re.compile(r'[A-Z]')
LOW_REGEX = re.compile(r'[a-z]')
DIG_REGEX = re.compile(r'\d')

def isItStrong(pw):
    if len(pw) < 8:
        print('This is not a strong password. Please retry.')
    elif (UP_REGEX.search(pw) and LOW_REGEX.search(pw) and
                DIG_REGEX.search(pw)) != None:
        print('Good password!')
    else:
        print('This is not a strong password. Please retry.')
isItStrong('googlE3233')
        


