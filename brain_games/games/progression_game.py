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


def get_progression():
    start = randint(START_RANGE, END_RANGE)
    length = randint(START_LENGTH, END_LENGTH)
    step = randint(START_STEP, END_STEP)
    return list(range(start, length, step))


def get_question_and_answer():
    progression = get_progression()
    correct_answer = str(choice(progression))
    progression = ' '.join(str(i) for i in progression)
    question = progression.replace(correct_answer, "..")
    return question, correct_answer
