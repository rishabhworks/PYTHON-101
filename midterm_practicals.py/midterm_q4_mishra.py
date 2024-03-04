def function1(lowerbound, upperbound ):
    num1= int(input(f"Enter an integer between {lowerbound} and {upperbound} inclusive: "))
    if num1 < lowerbound and num1 > upperbound:
        print("The number is out of the required range")
        if num1 >= lowerbound and num1 <= upperbound:
            print(f"The number is in the required range: {num1}")
            return num1
def main():
    function1(1,20)
main()



