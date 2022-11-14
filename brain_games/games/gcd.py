"""Function of the game 'Brain-GCD'."""

from random import randint

GAME_RULES = 'Find the greatest common divisior of given numbers.'

def get_solution():
    x = randint(0, 100)
    y = randint(0, 100)
    correct_answer = str(gcd(x, y))
    question = (str(x) + ' ' + str(y))
    return question, correct_answer

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
