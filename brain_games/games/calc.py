import random
import operator

GAME_RULE = 'What is the result of the expression?'

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_random_number():
    return random.randint(1, 100)  # NOSONAR


def generate_round():
    num1 = get_random_number()  # NOSONAR
    num2 = get_random_number()  # NOSONAR
    operation = random.choice(list(OPERATIONS.keys()))  # NOSONAR
    question = f"{num1} {operation} {num2}"
    result = OPERATIONS[operation](num1, num2)
    correct_answer = str(result)
    return question, correct_answer
