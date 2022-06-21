# Health Management System
# 3 clients - Harry, Rohan and Hammad

# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# Total 6 files
# Write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client

# with open("1_harry_food.txt", "w") as f:
#     f.write("Harry Food Schedule")
# with open("1_rohan_food.txt", "w") as f:
#     f.write("Rohan Food Schedule")
# with open("1_hammad_food.txt", "w") as f:
#     f.write("Hammad Food Schedule")
# with open("1_harry_exercise.txt", "w") as f:
#     f.write("Harry Exercise Schedule")
# with open("1_rohan_exercise.txt", "w") as f:
#     f.write("Rohan Exercise Schedule")
# with open("1_hammad_exercise.txt", "w") as f:
#     f.write("Hammad Exercise Schedule")

import datetime
def gettime():
    return datetime.datetime.now()
def log1(do1):
    if (do1 == 1):
        do2 = int(input("Enter 1 for exercise and 2 for food"))
        if (do2 == 1):
            value = input("Type here\n")
            with open("1_harry_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif (do2 == 2):
            value = input("Type here\n")
            with open("1_harry_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")

    if (do1 == 2):
        do2 = int(input("Enter 1 for exercise and 2 for food"))
        if (do2 == 1):
            value = input("Type here\n")
            with open("1_rohan_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif (do2 == 2):
            value = input("Type here\n")
            with open("1_rohan_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")

    if (do1 == 3):
        do2 = int(input("Enter 1 for exercise and 2 for food"))
        if (do2 == 1):
            value = input("Type here\n")
            with open("1_hammad_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif (do2 == 2):
            value = input("Type here\n")
            with open("1_hammad_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    # else:
    #     print("plz enter valid input (1(harry),2(rohan),3(hammad)")

def ret1(do1):
    if (do1 == 1):
        do2 = int(input("Enter 1 for exercise and 2 for food"))
        if (do2 == 1):
            with open("1_harry_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (do2 == 2):
            with open("1_harry_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (do1 ==2):
        do2 = int(input("Enter 1 for exercise and 2 for food"))
        if (do2 == 1):
            with open("1_rohan_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (do2 == 2):
            with open("1_rohan_food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (do1 == 3):
        do2 = int(input("Enter 1 for exercise and 2 for food"))
        if (do2 == 1):
            with open("1_hammad_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (do2 == 2):
            with open("1_hammad_food.txt") as op:
                for i in op:
                    print(i, end="")
    # else:
    #     print("plz enter valid input (1(harry),2(rohan),3(hammad)")

print("HEALTH MANAGEMENT SYSTEM")
a = int(input("Press 1 for log the value or press 2 for retrieve"))
if (a == 1):
    do1 = int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad"))
    log1(do1)
elif (a == 2):
    do1 = int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad"))
    ret1(do1)
else:
    print("plz enter valid input (1(harry),2(rohan),3(hammad)")

