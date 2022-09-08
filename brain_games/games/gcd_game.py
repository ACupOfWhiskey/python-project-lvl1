from random import randint


TASK = 'Find the greatest common divisor of given numbers.'
START = 1  # constant within the definition of a random number: start of range
END = 10  # constant within the definition of a random number: end of range


def gcd_logic(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def question_and_answer():
    base_num = randint(START, END)  # to reduce to a common divisor
    num1 = randint(START, END) * base_num
    num2 = randint(START, END) * base_num
    question = f'{num1} {num2}'
    return question, str(gcd_logic(num1, num2))
