from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
start = 2  # constant в рамках определения случайного числа: начало диапазона
end = 20  # constant в рамках определения случайного числа: конец диапазона


def prime_logic(num):
    if num <= 1:
        return False
# цикл будет перебирать возможные делители числа
# от двойки до половины проверяемого числа,
# т.к. проверять числа дальше нет смысла
# (любое число нацело делится максимум на половину себя)
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


def question_and_answer():
    question = randint(start, end)
    if prime_logic(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, str(correct_answer)
