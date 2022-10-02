from random import randint


TASK = 'Answer "yes" if number even otherwise answer "no".'
# constant within the definition of a random number: start of range
START = 0
# constant within the definition of a random number: end of range
END = 100


def is_even_number(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
    else:
        return False


def get_question_and_answer():
    question = randint(START, END)
    correct_answer = 'yes' if is_even_number(question) else 'no'
    return question, correct_answer
