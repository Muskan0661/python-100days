from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    # Uncomment the next line for testing:
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0

    while guess != answer and turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if guess != answer and turns > 0:
            print("Guess again.")

    if turns == 0 and guess != answer:
        print(f"You have run out of guesses. You lose. The answer was {answer}.")


# Main loop
while True:
    game()

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again not in ["yes", "y"]:
        print("Thanks for playing!")
        break