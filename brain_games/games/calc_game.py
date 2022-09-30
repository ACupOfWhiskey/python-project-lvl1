from random import randint
from random import choice


TASK = 'What is the result of the expression?'
# constant within the definition of a random number: start of range
START = 1
# constant within the definition of a random number: end of range
END = 50


def get_question_and_answer():
    num1 = randint(START, END)
    num2 = randint(START, END)
    random_operator = choice(['+', '-', '*'])
    question = f'{num1} {random_operator} {num2}'
    return question, str(is_this_correct_operator(num1, num2, random_operator))


def is_this_correct_operator(num1, num2, random_operator):
    if random_operator == '+':
        correct_answer = num1 + num2
    elif random_operator == '-':
        correct_answer = num1 - num2
    elif random_operator == '*':
        correct_answer = num1 * num2
    return correct_answer
