#!/usr/bin/env python3

"""Script for start the game 'Brain-GCD'."""

from brain_games.game_engine import welcome_user
from brain_games.games import gcd


def main():
    welcome_user(gcd)


if __name__ == '__main__':
    main()

