"""Function of the game 'Brain-calc'."""

from random import randint
from random import choice
GAME_RULES = 'What is the result of the expression?'


def get_solution():
    x = randint(0, 10)
    y = randint(0, 10)
    op = ['-', '+', '*']
    make_choice = choice(op)
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    question = (str(x) + ' ' + make_choice + ' ' + str(y))
    correct_answer = str(operation[make_choice])
    return question, correct_answer

