#!/usr/bin/env python3

"""Script for start the game 'Brain-even'."""

from brain_games.game_engine import welcome_and_start
from brain_games.games import even


def main():
    welcome_and_start(even)


if __name__ == '__main__':
    main()
