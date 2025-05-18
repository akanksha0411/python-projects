from art import logo, vs
from game_data import data
import random

def generate_random_choice(data_list):
    random_choice = random.choice(data)
    return random_choice

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take the user's guess and the follower counts and returns if the user got it right or not"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def play_game():
    game_continue = True
    print(logo)
    score = 0
    random_item_b = generate_random_choice(data)
    while game_continue:
        random_item_a = random_item_b
        random_item_b = generate_random_choice(data)

        if random_item_a == random_item_b:
            random_item_b = generate_random_choice(data_list=data)

        print(f"Compare A: {format_data(random_item_a)}")
        print(vs)
        print(f"Against B: {format_data(random_item_b)}")

        a_or_b = input("Who has more followers? A or B").lower()
        print("\n" * 20)
        print(logo)
        
        is_correct = check_answer(a_or_b, random_item_a['follower_count'], random_item_b['follower_count'])
        if is_correct:
            score += 1
            print(f"You're right. Current score is {score}")
        else:
            print(f"You're wrong. Final score is {score}")
            game_continue = False

play_game()







