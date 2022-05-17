import random

top_range = input('Please enter the max number: ')

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Please type a number greater than 0')
        quit()
else:
    print('Please enter a number')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Please make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number')
        continue

    if user_guess == random_number:
        print(f'You got it! It took {guesses} guesses!')
        break
    elif user_guess > random_number:
        print('You guessed above the number, please guess lower!')
    else:
        print('You guessed below the number, please guess higher! ')
