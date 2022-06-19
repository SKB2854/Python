l = ["*", "+", "/", "-"]
print(l)
c = input("Enter the operation name from above list: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if l[0] == c:
    if a==45 and b==3:
        print("Multiplication of a and b is:", 555)
    else:
        print("Multiplication of a and b is:", a*b)
elif l[1] == c:
    if a==56 and b==9:
        print("Sum of a and b is:", 77)
    else:
        print("Sum of a and b is:", a + b)
elif l[2] == c:
    if a==56 and b==6:
        print("Divison of a and b is:", 4)
    else:
        print("Divison of a and b is:", a/b)
elif l[3] == c:
    print("Subtraction of a and b is:", a-b)
else:
    print("Please choose correct operation")