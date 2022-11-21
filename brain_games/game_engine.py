"""Game engine"""

import prompt


ROUNDS = 3


def welcome_and_start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)

    for _ in range(ROUNDS):
        question, correct_answer = game.get_solution()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
