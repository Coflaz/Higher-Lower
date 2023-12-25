import random
from game_data import data
import os
import time

dt = data

def build_comparison(dt, versus):
    if len(versus) == 0:
        for _ in range(2):
            versus.append(dt.pop(random.randint(0, len(dt) - 1)))
    else:
        if versus[0]['follower_count'] > versus[1]['follower_count']:
            versus.pop(1)
            versus.append(dt.pop(random.randint(0, len(dt) - 1)))
        elif versus[0]['follower_count'] < versus[1]['follower_count']:
            versus.pop(0)
            versus.append(dt.pop(random.randint(0, len(dt) - 1)))
    
    random.shuffle(versus)

    return versus

def compare(versus):
    print("\nWhich one has more followers?\n")
    print("A => {}, {} from {}".format(versus[0]['name'], versus[0]['description'], versus[0]['country']))
    print("\nOR\n")
    print("B => {}, {} from {}\n".format(versus[1]['name'], versus[1]['description'], versus[1]['country']))

    player_choice = input("Type 'A' or 'B': ").upper()

    return player_choice

def check_answer(player_choice, versus):
    if player_choice == 'A':
        return versus[0]["follower_count"] > versus[1]["follower_count"]
    elif player_choice == 'B':
        return versus[0]["follower_count"] < versus[1]["follower_count"]
    else:
        return False

def game():
    score = 0
    versus = []
    while len(dt) > 1:
        os.system("cls" if os.name == "nt" else "clear")
        if score != 0:
            print("\nYour score is {}\n".format(score))
        versus = build_comparison(dt, versus)
        player_choice = compare(versus)
        if check_answer(player_choice, versus):
            score += 1
            print("\nCorrect! Your score is {}.\n".format(score))
            time.sleep(1)
            print("{} has {} million followers and {} has {} million followers.".format(versus[0]['name'], versus[0]['follower_count'], versus[1]['name'], versus[1]['follower_count']))
            time.sleep(5)
            print("\nNext round!\n")
            time.sleep(1)
        else:
            print("\nWrong! Your final score is {}.\n".format(score))
            print("{} has {} million followers and {} has {} million followers.".format(versus[0]['name'], versus[0]['follower_count'], versus[1]['name'], versus[1]['follower_count']))
            break

if __name__ == "__main__":
    game()
