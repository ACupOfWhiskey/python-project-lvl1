from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 2  # constant within the definition of a random number: start of range
END = 20  # constant within the definition of a random number: end of range


def is_prime_number(num):
    '''
    Program to check whether a number is prime or not.

    The loop will iterate over the possible divisors
    of a number from two to half of the number being checked,
    since there is no point in checking numbers further
    (any number is completely divisible by a maximum of half of itself).
    '''
    if num <= 1:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(START, END)
    if is_prime_number(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, str(correct_answer)
