import random
TASK = "Answer 'yes' if the number is even, otherwise answer 'no'."


<<<<<<< HEAD
def round():
=======
<<<<<<< HEAD
def round():
=======
def begin_round():
>>>>>>> f3e866529e428e78730cd1c17c968b1660f590e3
>>>>>>> 372eb9344b6e6b688b4e45b73826be654d132c9d
    num = random.randint(0, 30)
    answer = 'yes' if is_even(num) is True else 'no'
    return str(num), answer


def is_even(num):
    return True if num % 2 == 0 else False
