"""
|--------------------------------------------------------------------------
| Binary Search
|--------------------------------------------------------------------------
| Jason Monroe
| jason@jasonmonroe.com
|
| December 24, 2024
| 
| Guess a number between y and x. If the guess is incorrect try again until
| the correct number is found.
"""

import random

print('Binary Search')

# Initialize the guessing game.
def init_guessing():
    min_val, max_val = int(input('Enter the minimum value: ')), int(input('Enter the maximum value: '))
    number = random.randint(min_val, max_val)
    print(f'The minimum value is {min_val} and the maximum value is {max_val}')

    return {'min_val': min_val, 'max_val': max_val, 'number': number}

# Start guessing the number.
def start_guessing(number):
    guess_cnt = 0
    guess = None
    max_guesses = 10

    while guess != number and guess_cnt < max_guesses:

        print(f'\nGuess count: {guess_cnt}')
        guess = int(input('Enter your guess: '))

        # If not the answer tell it's lower or higher?
        if guess < number:
            print('Higher')

        elif guess > number:
            print('Lower')

        guess_cnt += 1

    if guess_cnt == 10:
        print(f'You have reached the maximum number of tries. The number was {number}')

    if guess == number:
        print(f'* You have guessed the number {number} in {guess_cnt + 1} tries.')


def auto_guessing(data):
    guess_cnt = 0
    guess = None
    max_guesses = 20

    number = data['number']
    min_val = data['min_val']
    max_val = data['max_val']

    print('Auto guessing the number...')

    while guess != number and guess_cnt < max_guesses:
        print('\nGuess count:', guess_cnt)

        if guess is None:
            guess = (min_val + max_val) // 2

        print('Auto-Guess:', guess)

        if number < guess:
            print('Lower')
            max_val = guess
            guess = (min_val + guess) // 2


        elif number > guess:
            print('Higher')
            min_val = guess
            guess = (max_val + guess) // 2

        guess_cnt += 1

    if guess_cnt == 20:
        print(f'Auto-reached the maximum number of tries. The number was {number}')
        return

    if guess == number:
        print(f'* Auto-guessed the number {number} in {guess_cnt + 1} tries.')


guess_data = init_guessing()

# Start the guessing game.
start_guessing(guess_data['number'])

# Do this automatically by using binary search algorithm.
print('\nBinary Search Algorithm')
auto_guessing(guess_data)

# End of file

