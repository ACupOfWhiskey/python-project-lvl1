from random import randint
from random import choice


TASK = 'What number is missing in the progression?'
# from which number to start the progression (start of range)
START_RANGE = 1
# from which number to start the progression (end of range)
END_RANGE = 10
# progression length (start of range)
START_LENGTH = 80
# progression length (end of range)
END_LENGTH = 100
# progression step (start of range)
START_STEP = 2
# progression step (end of range)
END_STEP = 10
# missed index (start of range)
INDEX_START = 0
# missed index (end of range)
INDEX_END = 5


def get_progression(start, length, step):
    numbers = []
    for i in range(start, length, step):
        numbers.append(i)
    random_index = randint(INDEX_START, INDEX_END)
    correct_answer = str(numbers[random_index])
    numbers[random_index] = '..'
    # determine the ammount of numbers in a progression
    string = ' '.join(map(str, numbers[INDEX_START:INDEX_END]))
    return string, correct_answer


def get_question_and_answer():
    start = randint(START_RANGE, END_RANGE)
    step = randint(START_STEP, END_STEP)
    length = randint(START_LENGTH, END_LENGTH)
    question, correct_answer = get_progression(start, length, step)
    return question, correct_answer
