#!/usr/bin/env python3

"""Script for start the game 'Brain-progression'."""

from brain_games.game_engine import welcome_and_start
from brain_games.games import progression


def main():
    welcome_and_start(progression)


if __name__ == '__main__':
    main()
