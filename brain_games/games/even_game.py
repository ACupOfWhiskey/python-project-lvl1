from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0  # constant within the definition of a random number: start of range
END = 100  # constant within the definition of a random number: end of range


def get_question_and_answer():
    question = randint(START, END)
    correct_answer = 'no'
    if question % 2 == 0:
        correct_answer = 'yes'
    return question, str(correct_answer)
