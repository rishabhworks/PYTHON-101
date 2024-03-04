def check_number_properties(number):
    if number > 0:
        print("Positive")
        if number < 50:
            print("Less than 50")
        elif number == 50:
            print("Equal to 50")
        elif 51 <= number <= 84:
            print("Between 51 and 84")
        elif number == 85:
            print("Equal to 85")
        else:
            print("Greater than 85")
    elif number < 0:
        print("Negative")
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Zero")

    # Check divisibility conditions
    if number % 2 == 0 and number % 3 == 0:
        print("Divisible by 2 and 3")
    elif number % 2 == 0 or number % 3 == 0:
        print("Divisible by 2 or 3 but not both")
    else:
        print("Not divisible by either 2 or 3")


# Get user input
user_input = input("Enter an integer: ")

try:
    number = int(user_input)
    check_number_properties(number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
