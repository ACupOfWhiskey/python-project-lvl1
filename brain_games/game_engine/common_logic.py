#!/usr/bin/env python3
import prompt
from random import randint
from random import choice


# Игра приветствует пользователя
def greetings_user():
    print("Welcome to the Brain Games!")

# Игра спрашивает имя пользователя
def asking_user_name():
    global user_name
    user_name = " "
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

# Условие для игры "Проверка на чётность"
def brain_even_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')

# Условие для игры "Калькулятор"
def brain_calc_task():
    print("What is the result of the expression?")

# Основная логика игры "Калькулятор"
def brain_calc_logic():
    operator = ["+", "-", "*"]
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        random_operator = choice(operator)
        num1 = randint(1, 20)
        num2 = randint(1, 10)
        game_question = f"{num1} {random_operator} {num2}"
        print("Question:", game_question)
        user_answer = prompt.string("Your answer: ")
        if random_operator == operator[0]:
            game_question = num1 + num2
        elif random_operator == operator[1]:
            game_question = num1 - num2
        elif random_operator == operator[2]:
            game_question = num1 * num2
        if str(user_answer) == str(game_question):
            right_answers += 1
            print("Correct!")
        elif str(user_answer) != str(game_question) or str(user_answer) == "...":
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{game_question}". Let's try again, {user_name}!''')
            return 0
    print(f"Congratulations, {user_name}!")

# Сообщение в случае правильного ответа пользователя
def right_user_answer():
    if str(user_answer) == str(game_question):
        right_answers += 1
        print("Correct!")

# Сообщение в случае неправильного ответа пользователя
def wrong_user_answer():
    if str(user_answer) != str(game_question) or str(user_answer) == "...":
        print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{game_question}". 
        Let's try again, {user_name}!''')
        return 0    

# Условие для игры "НОД"
def brain_gcd_task():
    print("Find the greatest common divisor of given numbers.")

# Условие для игры "Арифметическая прогрессия"
def brain_progression_task():
    print("What number is missing in the progression?")

# Условие для игры "Простое ли число?"
def brain_prime_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

# Завершение игры
def congratulation():
    print(f"Congratulations, {user_name}!")