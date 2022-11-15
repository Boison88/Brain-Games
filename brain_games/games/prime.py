"""Function of the game 'Brain-prime'."""

from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def get_solution():
    x = randint(0, 100)
    question = str(x)
    correct_answer = is_prime(x)
    return question, correct_answer


def is_prime(x):
    if x <= 1:
        return 'no'
    for i in range(2, x):
        if x % i == 0:
            return 'no'
    return 'yes'

