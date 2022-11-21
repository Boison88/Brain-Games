"""Function of the game 'Brain-GCD'."""

from random import randint
import math

GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_solution():
    x = randint(MIN_NUMBER, MAX_NUMBER)
    y = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = str(gcd(x, y))
    question = (str(x) + ' ' + str(y))
    return question, correct_answer


def gcd(a, b):
    return math.gcd(a, b)
