"""Function of the game 'Brain-progression'."""

from random import randint
from random import choice

GAME_RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 20
MIN_STEP = 1
MAX_STEP = 10
LIST_LENGTH = 10


def get_solution():
    numbers = progression()
    correct_answer = str(choice(numbers))
    target = numbers.index(int(correct_answer))
    numbers[target] = '..'
    question = (' '.join(map(str, numbers)))
    return question, correct_answer


def progression():
    first_num = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    numbers = [first_num]

    while len(numbers) < LIST_LENGTH:
        numbers.append(numbers[-1] + step)
    return numbers

