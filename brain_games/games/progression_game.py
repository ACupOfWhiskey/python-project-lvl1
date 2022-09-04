from random import randint


task = 'What number is missing in the progression?'


def question_and_answer():
    start = randint(1, 10)  # с какого числа начать
    step = randint(2, 7)  # определение "шага" прогрессии
    length = randint(6, 10)  # переменная для определения длины прогрессии
    end = step * length + start  # на каком значении остановить прогрессию
    random_index = randint(0, length - 1)
    progression = list(range(start, end, step))
    correct_answer = progression[random_index]
    progression[random_index] = ".."
    question = " ".join(map(str, progression))
    return question, str(correct_answer)
