import random

secret_number = random.randrange(1, 100)
user_number = None

while user_number != secret_number:
    user_number = input('Guess the number:')
    user_number = int(user_number)
    if user_number < secret_number:
        print('The number correct is bigger.')
    if user_number > secret_number:
        print('The number correct is smaller.')
    if user_number == secret_number:
        print('Congratulations, you guessed the number correct')

