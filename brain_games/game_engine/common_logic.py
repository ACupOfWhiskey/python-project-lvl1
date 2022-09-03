import prompt
from random import randint
from random import randrange
from random import choice
import math


# Игра приветствует пользователя
def greetings_user():
    print('Welcome to the Brain Games!')


# Игра спрашивает имя пользователя
def asking_user_name():
    global user_name
    user_name = ' '
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


# Условие для игры "Проверка на чётность"
def brain_even_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


# Основная логика игры "Проверка на чётность"
def brain_even_logic():
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            result = "yes"
        elif random_number % 2 != 0:
            result = "no"
        if str(user_answer) == str(result):
            right_answers += 1
            print("Correct!")
        else:
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{result}".
Let's try again, {user_name}!''')
            right_answers = 0
            return 0
    print(f'Congratulations, {user_name}!')


# Условие для игры "Калькулятор"
def brain_calc_task():
    print('What is the result of the expression?')


# Основная логика игры "Калькулятор"
def brain_calc_logic():
    right_answers = 0
    while right_answers != 3:
        random_operator = choice("+-*")
        num1 = randint(1, 20)
        num2 = randint(1, 30)
        print(f'Question: {num1} {random_operator} {num2}')
        answer = prompt.string('Your answer: ')
        if random_operator == '+':
            result = num1 + num2
        elif random_operator == '-':
            result = num1 - num2
        elif random_operator == '*':
            result = num1 * num2
        if str(answer) == str(result):
            right_answers += 1
            print('Correct!')
        else:
            print(f'''"{answer}" is wrong answer ;(. \
Correct answer was "{result}".
Let's try again, {user_name}!''')
            return 0
    print(f'Congratulations, {user_name}!')


# Условие для игры "НОД"
def brain_gcd_task():
    print('Find the greatest common divisor of given numbers.')


# Основная логика игры "НОД"
def brain_gcd_logic():
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        num1 = randrange(0, 100, 5)
        num2 = randrange(0, 100, 5)
        print(f'Question: {num1} {num2}')
        user_answer = prompt.string('Your answer: ')
        game_answer = math.gcd(num1, num2)
        if str(user_answer) == str(game_answer):
            right_answers += 1
            print('Correct!')
        elif str(user_answer) != str(game_answer) or str(user_answer) == "...":
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{game_answer}".
Let's try again, {user_name}!''')
            return 0
    print(f'Congratulations, {user_name}!')


# Условие для игры "Арифметическая прогрессия"
def brain_progression_task():
    print('What number is missing in the progression?')


# Основная логика игры "Арифметическая прогрессия"
def brain_progression_logic():
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        num1 = randint(1, 10)
        num2 = randint(50, 100)
        num3 = randint(2, 10)
        progression = []
        progression = list(range(num1, num2, num3))
        index = randint(1, len(progression) - 1)
        answer = progression[index]
        progression[index] = '..'
        new_progression = (" ".join(map(str, progression)))
        print(f'Question: {new_progression}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(answer):
            right_answers += 1
            print('Correct!')
        elif str(user_answer) != str(answer) or str(user_answer) == "...":
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{answer}".
Let's try again, {user_name}!''')
            return 0
    print(f'Congratulations, {user_name}!')


# Условие для игры "Простое ли число?"
def brain_prime_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


# Основная логика для игры "Простое ли число?"
def brain_prime_logic():
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        random_number = randint(1, 100)
        divisor = 2
        while random_number % divisor != 0:
            divisor += 1
        if divisor == random_number:
            right_answer = "yes"
        else:
            right_answer = "no"
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your unswer: ')
        if user_answer == right_answer:
            right_answers += 1
            print('Correct!')
        elif user_answer != right_answer or user_answer == "...":
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{right_answer}".
Let's try again, {user_name}!''')
            return 0
    print(f'Congratulations, {user_name}!')


# Сообщение в случае правильного ответа пользователя


# Сообщение в случае неправильного ответа пользователя


# Завершение игры
