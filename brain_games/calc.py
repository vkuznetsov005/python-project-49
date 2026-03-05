"""Logic for the calculator game."""

import random
import operator

GAME_RULE = 'What is the result of the expression?'

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_random_number():
    """Generate random number between 1 and 100."""
    return random.randint(1, 100)


def generate_round():
    """
    Generate a round of the calculator game.
    
    Returns:
        tuple: (question, correct_answer)
            question: string with math expression (e.g., "35 + 16")
            correct_answer: string with result of the expression
    """
    num1 = get_random_number()
    num2 = get_random_number()
    
    operation = random.choice(list(OPERATIONS.keys()))
    
    question = f"{num1} {operation} {num2}"
    
    result = OPERATIONS[operation](num1, num2)
    correct_answer = str(result)
    
    return question, correct_answer
