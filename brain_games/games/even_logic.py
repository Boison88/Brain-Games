import random
import prompt


def is_even():

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = input('Your answer: ')

        if random_number % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            correct_answers += 1
        elif random_number % 2 == 0 and answer.lower() != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'\nLet\'s try again, {name}!")
            break
        elif random_number % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
            correct_answers += 1
        elif random_number % 2 != 0 and answer.lower() != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'\nLet\'s try again, {name}!")
            break
        if correct_answers == 3:
            print(f'Congratulations, {name}!')
