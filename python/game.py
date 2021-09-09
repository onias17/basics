# get guess
# generate comp code
# generate clues
# run logic

import random

def get_guess():
    return list(input("Guess a 3 digit number: "))

def comp_num():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

comp = comp_num()

def clues(guess, comp):
    if guess == comp:
        return 'Perfect Match'

    clues = []

    for ind, num in enumerate(guess):
        if num == comp[ind]:
            clues.append('match') 
        elif num in comp:
            clues.append('close')
        
    if clues == []:
        return ['Nope']
    else:
        return clues

print('Welcome to Code Breaker')

code = comp_num()

clue_report = []

while clue_report != 'Perfect Match':
    guess = get_guess()
    
    clue_report = clues(guess, code)
    print('here is the result of your guess: ')
    for clue in clue_report:
        print(clue)

# def simplegame(guess):
#     guess = get_guess()
#     print(guess)
#     new = [int(x) for x in str(guess)]
#     print(new)
        

