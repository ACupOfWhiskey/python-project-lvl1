#!/usr/bin/env python3
import prompt
import random
import math


def brain_gcd():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Find the greatest common divisor of given numbers.")
    congratulation = f"Cogratulations {user_name}!"
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        num1 = random.randrange(0, 100, 5)
        num2 = random.randrange(0, 100, 5)
        print(f"Question: {num1} {num2}")
        user_answer = prompt.string("Your answer: ")
        game_answer = math.gcd(num1, num2)
        if str(user_answer) == str(game_answer):
            right_answers += 1
            print("Correct!")
        elif str(user_answer) != str(game_answer) or str(user_answer) == "...":
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{game_answer}".''')
            print(f"Let's try again, {user_name}!")
            return 0
    print(congratulation)
