import random
TASK = "What is the result of the expression?"


def answer_check(random_number1, random_operation, random_number2):
    if random_operation == '+':
        return random_number1 + random_number2
    if random_operation == '-':
        return random_number1 - random_number2
    if random_operation == '*':
        return random_number1 * random_number2


<<<<<<< HEAD
def round():
=======
<<<<<<< HEAD
def round():
=======
def begin_round():
>>>>>>> f3e866529e428e78730cd1c17c968b1660f590e3
>>>>>>> 372eb9344b6e6b688b4e45b73826be654d132c9d
    operations = ['+', '-', '*']
    random_number1 = random.randint(1, 20)
    random_number2 = random.randint(1, 20)
    random_operation = random.choice(operations)
    question = f"{random_number1} {random_operation} {random_number2}"
    answer = answer_check(random_number1, random_operation, random_number2)  # noqa: E501
    return question, str(answer)
