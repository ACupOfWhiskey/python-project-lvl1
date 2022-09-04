from random import randint
from random import choice


task = 'What is the result of the expression?'
start = 1  # constant в рамках определения случайного числа: начало диапазона
end = 50  # constant в рамках определения случайного числа: конец диапазона


def question_and_answer():
    num1 = randint(start, end)
    num2 = randint(start, end)
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
