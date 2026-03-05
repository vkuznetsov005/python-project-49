#!/usr/bin/env python3
"""Script to run the greatest common divisor (GCD) game."""

from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """Run the GCD game."""
    run_game(gcd)


if __name__ == '__main__':
    main()