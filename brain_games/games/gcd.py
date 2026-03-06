import random
import math

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_random_number():
    return random.randint(1, 100)


def find_gcd(num1, num2):
    return math.gcd(num1, num2)


def generate_round():
    num1 = get_random_number()
    num2 = get_random_number()
    question = f"{num1} {num2}"
    gcd_result = find_gcd(num1, num2)
    correct_answer = str(gcd_result)
    return question, correct_answer
