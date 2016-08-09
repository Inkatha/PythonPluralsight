# This is a random number guessing game
import random
secretNumber = random.randint(1, 20)
print('Welcome to the random number guessing game!')
print('What is your name?');
name = input()
print("Well " + name + " I'm thinking of a number between 1 and 20... ");
print('Can you figure out what it is?');
print('You have 6 chances');
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = input()

    if int(guess) == secretNumber:
        print("You've guessed the correct number!")
        break;
    elif guessTaken == 6:
        print("Game Over - You've ran out of guesses!")
        break;
    elif int(guess) < secretNumber:
        print('Your guess is too low')
    elif int(guess) > secretNumber:
        print('Your guess is too high')
        
