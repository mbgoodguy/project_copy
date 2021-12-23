#!/usr/bin/env python3


from brain_games.engine import start_game
from brain_games.games import brain_prime_module


def main():
    start_game(brain_prime_module)  # аргумент - импортированный модуль игры


if __name__ == '__main__':
    main()
