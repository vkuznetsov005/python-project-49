"""Logic for the prime number game."""

import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
        number: integer to check
        
    Returns:
        bool: True if number is prime, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_random_number():
    """Generate random number between MIN_NUMBER and MAX_NUMBER."""
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def generate_round():
    """
    Generate a round of the prime game.
    
    Returns:
        tuple: (question, correct_answer)
            question: string with the number to check
            correct_answer: 'yes' if number is prime, 'no' otherwise
    """
    number = get_random_number()
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
