import random

def guess_the_number():
    number = random.randint(1, 20) 
    print("I'm thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        guess = input("Take a guess: ")

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempts} guesses!")
            break

guess_the_number()
