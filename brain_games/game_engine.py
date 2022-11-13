"""Game engine"""

import prompt


def welcome_user(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)

    count = 0
    while 0 <= count < 3:
        question, correct_answer = game.get_solution()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.\n"
                f"Let\'s try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')

