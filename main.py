from data import data
from random import choice


def game():
    active = 1
    points = 0
    while active:
        first = random_account()
        second = random_account()
        print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']} ")
        print("vs")
        print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']} ")
        decision = input("Who has more followers? Type 'A' or 'B': ").upper()

        more = 'A'
        if first['follower_count'] < second['follower_count']:
            more = 'B'
        if decision == more:
            print("You won!")
            points += 1
        else:
            print(f"You lost with {points} points")
            x = input("Wanna play again? y/n")
            if x == 'y':
                points = 0
            else:
                active = 0


def random_account():
    return choice(data)


game()
