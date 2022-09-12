from random import randint
from random import choice


TASK = 'What is the result of the expression?'
START = 1  # constant within the definition of a random number: start of range
END = 50  # constant within the definition of a random number: end of range


def get_question_and_answer():
    num1 = randint(START, END)
    num2 = randint(START, END)
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    if random_operator == '+':
        correct_answer = num1 + num2
    elif random_operator == '-':
        correct_answer = num1 - num2
    elif random_operator == '*':
        correct_answer = num1 * num2
    question = f'{num1} {random_operator} {num2}'
    return question, str(correct_answer)
