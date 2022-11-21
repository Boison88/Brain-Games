"""Function of the game 'Brain-calc'."""

from random import randint, choice
import operator

GAME_RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def get_solution():
    operation_sign, operation = choice(OPERATIONS)
    x = randint(MIN_NUMBER, MAX_NUMBER)
    y = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = operation(x, y)
    question = '{0} {1} {2}'.format(x, operation_sign, y)
    return question, str(correct_answer)
