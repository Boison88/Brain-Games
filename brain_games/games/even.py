"""Function of the game 'Brain-even'."""

from random import randint
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_solution():
    x = randint(1, 100)
    question = str(x)

    if x % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
