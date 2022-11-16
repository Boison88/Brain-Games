#!/usr/bin/env python3

"""Script for start the game 'Brain-prime'."""

from brain_games.game_engine import welcome_user
from brain_games.games import prime


def main():
    welcome_user(prime)


if __name__ == '__main__':
    main()
