import random

word_list = ["muskan", "masooma", "rutba", "ali", "sara", "ahmed"]

chosen_word = random.choice(word_list)

lives = 6
display = ["_"] * len(chosen_word)

print("Welcome to Hangman!")
print(" ".join(display))

while lives > 0 and "_" in display:

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

    print(" ".join(display))

if "_" not in display:
    print("🎉 Congratulations! You guessed the name:", chosen_word)
else:
    print("💀 Game Over!")
    print("The name was:", chosen_word)