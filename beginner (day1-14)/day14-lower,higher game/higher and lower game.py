import random
from logo import draw

print(draw)

data = [
    {
        'name': 'Cristiano Ronaldo',
        'followers': 650,
        'description': 'football player',
        'country': 'Portugal'
    },
    {
        'name': 'Selena Gomez',
        'followers': 420,
        'description': 'singer and actress',
        'country': 'United States'
    },
    {
        'name': 'Virat Kohli',
        'followers': 280,
        'description': 'cricketer',
        'country': 'India'
    },
    {
        'name': 'Kim Kardashian',
        'followers': 360,
        'description': 'media personality and entrepreneur',
        'country': 'United States'
    }
]

def format_data(account):
    acc_name = account["name"]
    acc_des = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_des}, from {acc_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game_should_continue = True

while game_should_continue:

    acc_a = random.choice(data)
    acc_b = random.choice(data)

    while acc_a == acc_b:
        acc_b = random.choice(data)

    print("Compare A:", format_data(acc_a))
    print("VS")
    print("Against B:", format_data(acc_b))

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = acc_a["followers"]
    b_followers = acc_b["followers"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong.")
        print(f"{acc_a['name']} has {a_followers} million followers.")
        print(f"{acc_b['name']} has {b_followers} million followers.")
        print(f"Final score: {score}")
        game_should_continue = False