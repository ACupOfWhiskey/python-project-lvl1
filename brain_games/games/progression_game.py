from random import randint
from random import choice


TASK = 'What number is missing in the progression?'
# from which number to start the progression (start of range)
START_RANGE = 1
# from which number to start the progression (end of range)
END_RANGE = 10
# progression length (start of range)
START_LENGTH = 5
# progression length (end of range)
END_LENGTH = 10
# progression step (start of range)
START_STEP = 1
# missed index (start of range)
END_STEP = 10


def get_progression(start, length, step):
    progression = []
    for i in range(length):
        progression.append(str(start + step * i))
    return progression


def get_question_and_answer():
    start = randint(START_RANGE, END_RANGE)
    length = randint(START_LENGTH, END_LENGTH)
    step = randint(START_STEP, END_STEP)
    progression = get_progression(start, length, step)
    random_index = choice(range(len(progression)))
    missing_member = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    correct_answer = str(missing_member)
    return question, correct_answer
