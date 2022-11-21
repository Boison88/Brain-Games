"""Function of the game 'Brain-even'."""

from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_solution():
    x = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(x)

    if x % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
