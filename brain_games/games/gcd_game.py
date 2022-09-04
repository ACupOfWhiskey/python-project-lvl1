from random import randint


task = 'Find the greatest common divisor of given numbers.'
start = 1  # constant в рамках определения случайного числа: начало диапазона
end = 10  # constant в рамках определения случайного числа: конец диапазона


def gcd_logic(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def question_and_answer():
    base_num = randint(start, end)  # переменная для приведения к общему делителю
    num1 = randint(start, end) * base_num
    num2 = randint(start, end) * base_num
    question = f'{num1} {num2}'
    return question, str(gcd_logic(num1, num2))
