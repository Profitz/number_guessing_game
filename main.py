from art import logo

from random import randint

print(logo)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.\n")
print("(easy = 10 guesses  |  hard = 5 guesses)")

difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'easy':
    print('You have 10 attempts remaining to guess the number.')
    attempts = 10
elif difficulty == 'hard':
    print('You have 5 attempts remaining to guess the number.')
    attempts = 5

# computer generates a random number for the game
number_to_guess = randint(1, 101)

while attempts != 0:
    guess = int(input('Make a guess: '))
    if guess > number_to_guess:
        print('Too high.')
        attempts -= 1
        print(f'You have {attempts} attempts remaining to guess the number.')
    elif guess < number_to_guess:
        print('Too low.')
        attempts -= 1
        print(f'You have {attempts} attempts remaining to guess the number.')
    elif guess == number_to_guess:
        print(f'You got it!  The answer is {number_to_guess}')
        break
    if attempts == 0:
        print("You've run out of guesses, you lose!")
        print(f"The number to guess was {number_to_guess}")
        break

