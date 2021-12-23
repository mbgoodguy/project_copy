import prompt
import sys
ROUNDS = 3


def start_game(game):
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.TASK)
    start_from_round = 1
    while start_from_round <= ROUNDS:
<<<<<<< HEAD
        question, answer = game.round()
=======
        question, answer = game.begin_round()
>>>>>>> f3e866529e428e78730cd1c17c968b1660f590e3
        print("Question: " + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}")  # noqa: E501
            print(f"Let's try again, {name}!")
            sys.exit()
        start_from_round += 1
    print(f'Congratulations, {name}!')
