#!/usr/bin/env python3
import prompt
from random import randint


def brain_progression():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("What number is missing in the progression?")
    congratulation = f"Cogratulations {user_name}!"
    right_answers = 0
    win_score = 3
    while right_answers < win_score:
        num1 = randint(1, 10)
        num2 = randint(50, 100)
        num3 = randint(2, 10)
        progression = []
        progression = list(range(num1, num2, num3))
        index = randint(1, len(progression) - 1)
        correct_answer = progression[index]
        progression[index] = ".."
        new_progression = (" ".join(map(str, progression)))
        print(f"Question: {new_progression}")
        user_answer = prompt.string("Your answer: ")
        if str(user_answer) == str(correct_answer):
            right_answers += 1
            print("Correct!")
        elif str(user_answer) != str(correct_answer) or str(user_answer) == "...":
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}". Let's try again, {user_name}!''')
            return 0
    print(congratulation)
