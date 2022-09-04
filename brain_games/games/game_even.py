from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'
start = 0  # constant в рамках определения случайного числа: начало диапазона
end = 100  # constant в рамках определения случайного числа: конец диапазона


def question_and_answer():
    question = randint(start, end)
    correct_answer = "no"
    if question % 2 == 0:
        correct_answer = "yes"
    return question, str(correct_answer)
