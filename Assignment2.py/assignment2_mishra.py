# Name: Rishabh Atul Mishra 
# Class: PROG1004 PROGRAMMING PRINCIPLES.
# Assignment: Assignment #2
# Date: FEBRUARY 19TH, 2O24
# Program: Bachelor's of Computer Science 
# File: assignment_2_mishra.py
# Description: Create 3 functions, use 2 modules, 
#              helper module and main module    
#              use helper module for all the calculations and prompts
#              use the main module to call all the functions and run the program
#              Make a dice roll, make the program take random numbers
#              Output the program as shown.
import assignment2_mishra_helper as help  # Importing the helper module

import math  # Importing the math module for mathematical operations

def main():
    # Calling func1 from the helper module to get user input for the number of rolls
    help.func1(1, 10000, "Rolling Times (1-10000), 0 to stop: ", "Invalid input")
    print(help.rolls)  # Printing the number of rolls obtained from func1
    help.func2()  # Calling func2 from the helper module to simulate dice rolls

    # Calculating the maximum count among all faces
    Max = max(help.face1, help.face2, help.face3, help.face4, help.face5, help.face6)
    
    # Calculating the lengths of bars for each face proportionate to the maximum count
    first = math.floor(70 * (help.face1 / Max))
    second = math.floor(70 * (help.face2 / Max))
    third = math.floor(70 * (help.face3 / Max))
    fourth = math.floor(70 * (help.face4 / Max))
    fifth = math.floor(70 * (help.face5 / Max))
    sixth = math.floor(70 * (help.face6 / Max))
    
    # Calling func3 from the helper module to print bar charts for each face count
    help.func3("One   ", "=", first, help.face1)
    help.func3("two   ", "=", second, help.face2)
    help.func3("three ", "=", third, help.face3)
    help.func3("four  ", "=", fourth, help.face4)
    help.func3("five  ", "=", fifth, help.face5)
    help.func3("six   ", "=", sixth, help.face6)
    return

# Setting the initial value of rolls to 1 to enter the loop
help.rolls = 1

# Looping until rolls become 0
while help.rolls != 0:
    main()  # Calling the main function
