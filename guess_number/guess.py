import random

random_number = random.randint(0, 100)


def guess_number():

    while True:
        user_guess = int(input("Guess a number: "))
        if user_guess == random_number:
            print("Just right!")
            return random_number
        elif user_guess < random_number:
            print("Too low")
        elif user_guess > random_number:
            print("Too high")


# An alternative to the guessing game: have the computer guess the number
secret_number = 6
high = 10
low = 0
guess = (high + low) // 2


while True:
    print(f"Is your guess {guess}?")

    user_guess = input(
        "Type 'high' if the guess is too high. Type 'low' if the guess is too low."
    )

    if guess == secret_number:
        print("you got it!")
        break
    elif user_guess == "high":
        high = guess
        print("too high")
    elif user_guess == "low":
        low = guess
        print("too low")
    guess = (high + low) // 2


# # Modify this program, such that it gives the user only 3 chances to guess the correct number.
# # If they try three times without success, they’re told that they didn’t guess in time, and the program exits.
total_guesses = 0
random_number = random.randint(0, 100)

while total_guesses < 4:
    user_guess = int(input("Guess a number: "))
    total_guesses += 1

    if total_guesses == 3:
        print("You didn't guess in time")
        break

    elif user_guess == random_number:
        print("You got it!")

    elif user_guess > random_number:
        print("Too high")

    elif user_guess < random_number:
        print("Too low")
