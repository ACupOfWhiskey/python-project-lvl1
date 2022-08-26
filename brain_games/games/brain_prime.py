#!/usr/bin/env python3
import prompt
from random import randint


def brain_prime():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    congratulation = f"Cogratulations {user_name}!"
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
        print(f"Question: {random_number}")
        user_answer = prompt.string("Your unswer: ")
        if user_answer == right_answer:
            right_answers += 1
            print("Correct!")
        elif user_answer != right_answer or user_answer == "...":
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{right_answer}". Let's try again, {user_name}!''')
            return 0
    print(congratulation)