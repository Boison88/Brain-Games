#!/usr/bin/env python3

"""Script for start the game 'Brain-calc'."""

from brain_games.game_engine import welcome_and_start
from brain_games.games import calc


def main():
    welcome_and_start(calc)


if __name__ == '__main__':
    main()
