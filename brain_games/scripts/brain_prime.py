#!/usr/bin/env python3

"""Script for start the game 'Brain-prime'."""

from brain_games.game_engine import welcome_and_start
from brain_games.games import prime


def main():
    welcome_and_start(prime)


if __name__ == '__main__':
    main()
