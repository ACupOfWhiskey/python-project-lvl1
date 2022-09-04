# game engine for all games
import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.task)
    max_game_score = 3
    for _ in range(max_game_score):
        question, correct_answer = game.question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'''"{user_answer}" is wrong answer ;(. '''
                f'''Correct answer was "{correct_answer}".\n'''
                f'''Let's try again, {user_name}!''')
            return 0
    else:
        print(f'Congratulations, {user_name}!')
