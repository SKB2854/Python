#import random function
import random
#Computer generated number using random function and store in variable n
n = random.randint(0, 100)
print("You have total 9 guesses to guess the correct number")
i = 1
while (i<10):
    num = int(input("Guess the number between 0 and 100: "))
    if n > num:
        i = i+1
        print("Please enter a larger number")
        print(f"You left with {10-i} guesses")
    elif n < num:
        i = i+1
        print("Please enter a smaller number")
        print(f"You left with {10 - i} guesses")
    elif n == num:
        print(f"You won! your guess {num} is correct")
        print(f"You guess the correct number in {i} guesses")
        break
print("Game Over!")