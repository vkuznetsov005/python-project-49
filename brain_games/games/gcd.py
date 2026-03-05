"""Logic for the greatest common divisor (GCD) game."""

import random
import math

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_random_number():
    """Generate random number between 1 and 100."""
    return random.randint(1, 100)


def find_gcd(num1, num2):
    """
    Find the greatest common divisor of two numbers.
    
    Args:
        num1: first integer
        num2: second integer
        
    Returns:
        int: greatest common divisor
    """
    return math.gcd(num1, num2)


def generate_round():
    """
    Generate a round of the GCD game.
    
    Returns:
        tuple: (question, correct_answer)
            question: string with two numbers (e.g., "25 50")
            correct_answer: string with their GCD
    """
    num1 = get_random_number()
    num2 = get_random_number()
    question = f"{num1} {num2}"
    gcd_result = find_gcd(num1, num2)
    correct_answer = str(gcd_result)
    return question, correct_answer
