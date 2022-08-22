#!/usr/bin/env/python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f'Hello {user_name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    i = 0
    win_score = 3
    while i < win_score:
        random_number = randint(1, 100)
        print(f"Question: {random_number}")
        user_answer = prompt.string("Your answer: ")
        if (user_answer == 'yes' and random_number % 2 == 0) or (user_answer == 'no' and random_number % 2 != 0):
            print("Correct!")
            i += 1
        elif user_answer == "yes" and random_number % 2 != 0:
            return (print(f'''"yes" is wrong answer ;(. Correct answer was "no".\nLet's try again, {user_name}!'''))
        elif user_answer == "no" and random_number % 2 == 0:
            return (print(f'''"no" is wrong answer ;(. Correct answer was "yes".\nLet's try again, {user_name}!'''))
    print(f"Congratulations, {user_name}!")
