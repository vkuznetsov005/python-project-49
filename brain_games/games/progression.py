import random

GAME_RULE = 'What number is missing in the progression?'

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 50
MIN_STEP = 1
MAX_STEP = 10


def generate_progression():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    
    progression = []
    for i in range(length):
        current_element = start + i * step
        progression.append(str(current_element))
    
    hidden_index = random.randint(0, length - 1)
    hidden_number = progression[hidden_index]
    
    progression[hidden_index] = '..'
    
    return progression, hidden_index, hidden_number


def generate_round():
    progression, _, hidden_number = generate_progression()
    question = ' '.join(progression)
    correct_answer = hidden_number
    return question, correct_answer
