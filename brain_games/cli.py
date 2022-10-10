import promt


def welcome_user():
    name = promt.string('May I have your name? ')
    print(f'Hello, {name}!')
