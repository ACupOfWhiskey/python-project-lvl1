#!/usr/bin/env python3
import prompt
import random


def brain_calc():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("What is the result of the expression?")
    congratulation = f"Cogratulations {user_name}!"
    operator = ["+", "-", "*"]
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        random_operator = random.choice(operator)
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 10)
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
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{game_question}". 
            Let's try again, {user_name}!''')
            return 0
        print(congratulation)
