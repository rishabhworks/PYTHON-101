# Name: Rishabh Atul Mishra 
# Class: PROG1004 PROGRAMMING PRINCIPLES.
# Assignment: Assignment #2
# Date: FEBRUARY 19TH, 2O24
# Program: Bachelor's of Computer Science 
# File: assignment_2_mishra_helpers.py
# Description: Create 3 functions, use 2 modules, 
#              helper module and main module    
#              use helper module for all the calculations and prompts
#              use the main module to call all the functions and run the program
#              Make a dice roll, make the program take random numbers
#              Output the program as shown.
def func1(lowerbound, upperbound, prompt, error):
    global rolls  # Define 'rolls' as a global variable
    while True:
        rolls = int(input(prompt))  # Get user input for the number of rolls
        if rolls == lowerbound - 1:  # Check if user input is one less than the lower bound
            print("Thank You")  # Print a message
            break  # Exit the loop
        elif lowerbound <= rolls <= upperbound:  # Check if user input is within the specified bounds
            print()  # Print a blank line
            break  # Exit the loop
        else:
            print(error)  # Print an error message if the input is out of bounds
    return rolls  # Return the number of rolls


import random


def func2():
    global face1, face2, face3, face4, face5, face6  # Define faces variables as global
    face1, face2, face3, face4, face5, face6 = 0, 0, 0, 0, 0, 0  # Initialize face variables to 0
    for i in range(0, rolls):  # Iterate over the number of rolls
        dice = random.randint(1, 6)  # Generate a random number between 1 and 6
        if dice == 1:
            face1 += 1  # Increment face1 if dice is 1
        elif dice == 2:
            face2 += 1  # Increment face2 if dice is 2
        elif dice == 3:
            face3 += 1  # Increment face3 if dice is 3
        elif dice == 4:
            face4 += 1  # Increment face4 if dice is 4
        elif dice == 5:
            face5 += 1  # Increment face5 if dice is 5
        elif dice == 6:
            face6 += 1  # Increment face6 if dice is 6
    return face1, face2, face3, face4, face5, face6  # Return the counts for each face


def func3(title, char, length, note):
    if length <= 70:  # Check if length is less than or equal to 70
        print(f"{title}: ", end="")  # Print the title followed by a colon
        for i in range(0, length):  # Iterate over the specified length
            print(char, end="")  # Print the specified character
        print(f" {note}")  # Print the note after the character sequence


if __name__ == "_main_":  # Check if the script is run as the main program
    func1()  # Call func1
    func2()  # Call func2
    func3()  # Call func3
