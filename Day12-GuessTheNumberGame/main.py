from random import randint

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def difficulty_level():
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def guess_the_number():
    attempts = difficulty_level()
    number = randint(1, 100)
    for _ in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number")
        attempts -= 1
        guess = int(input("Make a guess:"))
        if guess == number:
            print("Great guess, you win!")
            return
        elif guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        if attempts == 0:
            print("No more guesses left, you lose")


guess_the_number()
