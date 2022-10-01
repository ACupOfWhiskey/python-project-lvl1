from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
# constant within the definition of a random number: start of range
START = 0
# constant within the definition of a random number: end of range
END = 100


def get_question_and_answer():
    question = randint(START, END)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
