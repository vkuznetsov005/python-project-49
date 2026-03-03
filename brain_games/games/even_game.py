import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number: integer to check
        
    Returns:
        bool: True if number is even, False otherwise
    """
    return number % 2 == 0


def generate_round():
    """
    Generate a round of the game.
    
    Returns:
        tuple: (question, correct_answer)
            question: string with the number to check
            correct_answer: 'yes' if number is even, 'no' otherwise
    """
    number = random.randint(1, 100)
    
    question = str(number)

    correct_answer = 'yes' if is_even(number) else 'no'
    
    return question, correct_answer

