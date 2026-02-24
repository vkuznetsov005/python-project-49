#!/usr/bin/env python3
"""Script to run the even check game."""

from brain_games.engine import run_game
from brain_games.games import even


def main():
    """Run the even check game."""
    run_game(even)


if __name__ == '__main__':
    main()