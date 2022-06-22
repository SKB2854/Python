"""
Pattern Printing
Input = Integer n
Print below star pattern
Input Boolean variable = True or False

True
*
**
***
****
False
****
***
**
*

"""
print("Star(*) Pattern Printing")
n = int(input("Enter the numbers of rows you want to print: "))
bool1 = int(input("Please enter 0 or 1: "))
try:
    if bool1 == 1:
        b = bool(True)
        for i in range(1, n + 1):
            print(i * "*")
    elif bool1 == 0:
        b = bool(False)
        for i in range(n, 0, -1):
            print(i * "*")
    else:
        print("Do not enter value other than 0  or 1")
except Exception as e:
    print(e)

