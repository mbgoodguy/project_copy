#!/usr/bin/env python


from brain_games.engine import start_game
from brain_games.games import brain_calc_module


def main():
    start_game(brain_calc_module)


if __name__ == '__main__':
    main()
