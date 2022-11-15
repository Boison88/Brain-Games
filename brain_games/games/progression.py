"""Function of the game 'Brain-progression'."""

from random import randint
from random import choice

GAME_RULES = 'What number is missing in the progression?.'


def get_solution():
    numbers = progression()
    correct_answer = str(choice(numbers))
    target = numbers.index(int(correct_answer))
    numbers[target] = '..'
    question = (' '.join(map(str, numbers)))
    return question, correct_answer


def progression():
    first_num = randint(0, 10)
    step = randint(0, 10)
    numbers = [first_num]

    while len(numbers) < 10:
        numbers.append(numbers[-1] + step)
    return numbers
