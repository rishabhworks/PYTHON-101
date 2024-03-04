#Q2
num1 = int(input("First Integer: "))
num2= int(input("Second Integer: "))

if num1 % 2 != 0 and num2 % 2 == 0:
    print(f"{num1} is odd, {num2} is even.")
elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f"{num1} is even, {num2} is odd.")
elif num1 % 2 == 0 and num2 % 2 == 0:
    print("Both are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both are odd.")
