while True:
    num1_str = input("Enter the first positive integer: ")
    num2_str = input("Enter the second positive integer: ")

    if not num1_str.isdigit() or not num2_str.isdigit():
        print("Invalid input. Please enter positive integers.")
        continue

    num1, num2 = int(num1_str), int(num2_str)

    if num1 <= 0 or num2 <= 0:
        print("Invalid input. Please enter positive integers.")
        continue

    comparison = "greater than" if num1 > num2 else "less than" if num1 < num2 else "equal to"
    print(f"{num1} is {comparison} {num2}.")

    common_factors = [i for i in range(1, min(num1, num2) + 1) if num1 % i == 0 and num2 % i == 0]
    print(f"Common factors: {', '.join(map(str, common_factors))}")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != 'Y':
        print("Program terminated.")
        break
