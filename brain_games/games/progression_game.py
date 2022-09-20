from random import randint


TASK = 'What number is missing in the progression?'
# from which number to start the progression (start of range)
START_RANGE = 1
# from which number to start the progression (end of range)
END_RANGE = 10
# progression step (start of range)
START_STEP = 2
# progression step (end of range)
END_STEP = 7
# progression length (start of range)
START_LENGTH = 6
# progression length (end of range)
END_LENGTH = 10


def get_question_and_answer():
    start = randint(START_RANGE, END_RANGE)
    step = randint(START_STEP, END_STEP)
    length = randint(START_LENGTH, END_LENGTH)
    end = step * length + start
    random_index = randint(0, length - 1)
    progression = list(range(start, end, step))
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
