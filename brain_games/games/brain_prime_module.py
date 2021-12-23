import random


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            # print(" # Число не является простым")
            return True
        else:
            # print(" # Число не является простым")
            return False


def generate_round():
    num = random.randint(2, 30)
    if is_prime() is True:
        return str(num), 'yes'  # возврат числа (question) и ответа (answer), которые будут использованы в engine.py   # noqa: E501
    else:
        return str(num), 'no'
