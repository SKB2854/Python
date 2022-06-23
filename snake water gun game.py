# Sanke Water Gun Game
import random
print("Snake, Water, Gun Game! Are you ready to play?")
print("Snake and Water: Snake will win!")
print("Snake and Gun: Gun will win!")
print("Gun and Water: Water will win!")


def game1():
    i = 0
    lost = 0
    won = 0
    tie = 0
    while (i < 10):
        print(f"You left with {10-i} Chances")
        i = i + 1
        user1 = input("Enter s for snake or w for water or g for gun: ")
        l = ["s","w","g"]
        comp1 = random.choice(l)

        if (user1 == comp1):
            tie = tie + 1
            print(f"Match Tie! Match ties {tie} times")

        elif (user1 == "s" and comp1 == "w"):
            won = won + 1
            print(f"you won! you won {won} times ")

        elif (user1 == "g" and comp1 == "s"):
            won = won + 1
            print(f"you won! you won {won} times ")

        elif (user1 == "w" and comp1 == "g"):
            won = won + 1
            print(f"you won! you won {won} times ")

        elif (user1 == "w" and comp1 == "s"):
            lost = lost + 1
            print(f"you lost! you lost {lost} times ")

        elif (user1 == "s" and comp1 == "g"):
            lost = lost + 1
            print(f"you lost! you lost {lost} times ")

        elif (user1 == "g" and comp1 == "w"):
            lost = lost + 1
            print(f"you lost! you lost {lost} times ")
        else:
            print("Please enter valid input")

    print("\nComplete Result")
    if won>lost and won>tie:
        print(f"Out of 10 chances you won {won} times and you are the WINNER!")
    elif won<lost and lost>tie:
        print(f"Out of 10 chances computer won {lost} times and Computer is the WINNER!")
    elif won == lost and won>tie:
        print(f"Out of 10 chances you and computer both won {lost} times, Match tied !")
    else:
        print(f"Out of 10 chances match tied {tie} times, so no one is WINNER!")
    print(f"Match ties {tie} times")
    print(f"you won {won} times")
    print(f"you lost {lost} times ")
game1()






