from random import randint
import math


TASK = 'Find the greatest common divisor of given numbers.'
START = 1  # constant within the definition of a random number: start of range
END = 10  # constant within the definition of a random number: end of range


def get_question_and_answer():
    base_num = randint(START, END)  # to reduce to a common divisor
    num1 = randint(START, END) * base_num
    num2 = randint(START, END) * base_num
    question = f'{num1} {num2}'
    return question, str(math.gcd(num1, num2))
