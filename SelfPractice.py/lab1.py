# Prompting the user to enter two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Determining the range of numbers
if num1 < num2:
    start_num = num1
    end_num = num2
else:
    start_num = num2
    end_num = num1

print("Numbers between", start_num, "and", end_num, "that are multiples of 7:")

# Printing the multiples of 7 within the specified range
for num in range(start_num, end_num + 1):
    if num % 7 == 0:
        print(num)
