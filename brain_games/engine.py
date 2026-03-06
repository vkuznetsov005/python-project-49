import prompt


def run_game(game_module):
    """
    Run a brain game.
    
    Args:
        game_module: module with game logic
            Must have:
            - GAME_RULE: string with game description
            - generate_round(): function returning (question, correct_answer)
    """

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!') 
    print(game_module.GAME_RULE)
    rounds_to_win = 3
    
    for round_num in range(rounds_to_win):
        question, correct_answer = game_module.generate_round()
        
        print(f'Question: {question}')
        
        user_answer = prompt.string('Your answer: ').lower()
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print('Correct!')
    
    print(f'Congratulations, {name}!')