from random import randint
import math


TASK = 'Find the greatest common divisor of given numbers.'
# constant within the definition of a random number: start of range
START = 1
# constant within the definition of a random number: end of range
END = 20


def get_question_and_answer():
    num1 = randint(START, END)
    num2 = randint(START, END)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
