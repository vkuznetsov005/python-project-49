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
    return random.randint(1, 100)


def generate_round():
    num1 = get_random_number()
    num2 = get_random_number()
    operation = random.choice(list(OPERATIONS.keys()))
    
    question = f"{num1} {operation} {num2}"
    result = OPERATIONS[operation](num1, num2)
    correct_answer = str(result)
    
    return question, correct_answer

