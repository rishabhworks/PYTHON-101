# while True:
#     name=str(input("Last Name: "))
#     name1= int(input("Student ID: "))
#     print(f"Welcome, {name}")
#     print(f"Your Login Name is: {name}{name1}")

# while True:    
#     num1= float(input("Cost of Meal: "))
#     num2= float(input("Tip Percent: "))
#     Tip_amount= num1 * (num2 / 100)
#     print(f"Tip Amount: {Tip_amount:.2f}")
#     total_amount = num1 + Tip_amount
#     print(f"Total Bill: ${total_amount:.2f}")

# students= int(input("Number of Students: "))

# count1 = 0
# count2= 0 
# count3= 0
# count4= 0 
# count5= 0 
# total_marks= 0 

# for i in range(1, students + 1):
#     marks = float(input(f'Marks {i}: '))
#     total_marks += marks
#     if 90<= marks <=100:
#         count1 += 1
#     elif 80<= marks <= 89:
#         count2 += 1
#     elif 70<= marks <=79:
#         count3 += 1
#     elif 60 <= marks <= 69:
#         count3 += 1
#     elif 50<= marks <= 50:
#         count4 += 1
#     else:
#         count5 += 1

# print(f"A: {count1}, B: {count2}, C: {count3}, D: {count4}, F: {count5}")

# average =  total_marks / i
# print(f"Average Marks= {average}")

# bonus = 0
# goods_sold= 0

# num= int(input("Total goods sold: "))
# goods_sold += num
# if goods_sold > 500000:
#     bonus += 10000
# print(bonus)

# shelf_life= 0
# outside_temperutre= 0

# num1= int(input("Enter the shelf life: "))
# shelf_life += num1

# num= int(input("Enter the outside temperature: "))
# outside_temperutre += num
# if outside_temperutre > 90:
#     shelf_life -= 4
#     print(f"The shelf life for this temperature will be: {shelf_life}")

# `while True:
#     gpa = 0
#     deans_list= 0
#     student_name= 0 

#     num= float(input("Enter GPA: "))
#     gpa += num

#     num1= str(input("Enter Student's Name: "))
#     student_name = num1

#     if gpa >= 3.5:
#         deans_list += 1
#         print(f"{student_name} has this {gpa} gpa")
#     else:
#         break

# num1= int(input("Enter 1st: "))
# num2= int(input("Enter 2nd: "))
# num3= int(input("Enter 3rd: "))

# sum= num1 + num2 + num3
# average= sum / 3
# product= num1 * num2 * num3
# if num1 > num2 and num1> num3:
#     print(f"{num1} is the greatest")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is greatest")
# else: print(f"{num3} is the greatest")

# if num1 < num2 and num1 < num3:
#     print(f"{num1} is the smallest")
# elif num2 < num1 and num2 < num3:
#     print(f"{num2} is smallest")
# else: print(f"{num3} is the smallest")

# print(f"The average of all is: {average:.2f}")

# if num1 > average:
#     print(f"{num1} is greater than average")

# if num2 > average:
#         print(f"{num2} is greater than average")
    
# if num3 > average:
#         print(f"{num3} is greater than average")
# else:
#     print(f"{num1}, {num2}, {num3} are smaller than the average")


# pay= 0
# score= 0

# num= int(input("Enter your pay: "))
# pay += num

# num1= int(input("Enter the score: "))
# score += num1

# if score > 90:
#     pay = pay + (pay * 3/100)
#     print(f"Your score is 90+ so pay is: {pay}")
# else:
#     pay = pay + pay * 1 / 100
#     print(f"Your score is < 90 so pay is: {pay}")

# ticket = int(input("Enter the number of tickets ($7.50 each, 10+ discount: 2%): "))
# vip= str(input("Are you a VIP (VIP discount: 10%) (Y/N): "))
# weekend=  str(input("is it a weekend? (Weekend Discount: 5%)(Y/N): "))
# total_payment= ticket * 7.50

# if ticket >=10:
#     total_payment -= (total_payment * 2/100)

# if vip == "Y":
#     total_payment -= (total_payment * 10/100)

# if weekend == "Y":
#     total_payment -= (total_payment * 5/100)

# print(f"Total Payment: {total_payment}")

# import math

# def print_operations():
#     num = float(input("Enter a number: "))
#     if num >= 0:
#         square_root = math.sqrt(num)
#         print(f"Square: {num ** 2}")
#         print(f"Cube: {num ** 3}")
#         print(f"Square root: {square_root}")
#         print(f"Cube root: {num ** (1/3)}")
#     else:
#         print("Cannot calculate square root, cube root, and other operations for negative numbers.")

# # Call the function to start the program
# print_operations()


# def is_triangle(side1, side2, side3):
#     if (side1+ side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
#         print("The given sides form a triangle")
#     else:
#         print("The given sides dont make a triangle")
# side1 = float(input("Enter Side 1: "))
# side2= float(input("Enter side 2:"))
# side3= float(input("Enter side 3: "))
# is_triangle(side1, side2, side3)

# def sum(num1,num2):
#     return num1+ num2
# num1= int(input("Enter 1st: "))
# num2= int(input("Enter 2nd: "))
# result = sum(num1,num2)
# print(result)

# def get_names():
#     firstname = input('Enter firstname: ')
#     lastname = input('Enter lastname: ')
#     return firstname, lastname   
# get_names()

# def area_perimeter(width, length):
#     area = width * length
#     perimeter= 2 * (width + length)
#     print("Area of the room:", area, "Square units")
#     print("Perimeter of the room is", perimeter)

# width = float(input("Enter Width: "))
# length= float(input("Enter Length: "))
# area_perimeter(width, length)

# def display_message(message, times):
#     for i in range(times):
#         print(message, i)

# message = input("Enter your message: ")
# times = int(input( "number of times: "))
# display_message(message, times)

# def a_func(integer, integer2):
#     if integer % integer2 == 0:
#         print("First is the multiple of second: ", integer)
    
# integer = int(input("1st: "))
# integer2= int(input("2nd: "))
# a_func(integer, integer2)

# def peri(w,b):
#     per=2*(w+b)
#     return per

# def area(w,b):
#     area=w*b
#     return area

# def main():
#     width=int(input("Enter Width:"))
#     breadth=int(input("Enter breadth:"))
#     print(peri(width,breadth))
#     print(area(width,breadth))
# main()

# def show_tax(price=100, tax_rate=0.07):
#     tax = price * tax_rate
#     print(f'The tax is {tax}.')

# show_tax()

# import random 

# def random_tester():
#     # randint()
#     print('Random integers:', end=' ')
#     for n in range(10): 
#         x = random.randint(20, 50)
#         print(x, end=' ')
#     print() 

#     # randrange()
#     print('Random integers:', end=' ')
#     for n in range(10): 
#         x = random.randrange(10, 100, 5)
#         print(x, end=' ')
#     print() 

#     # random()
#     print('Random float [0, 1):', end=' ')
#     for n in range(10): 
#         x = random.random()
#         print(x, end=' ')
#     print() 

#     # uniform()
#     print('Random float:', end=' ')
#     for n in range(10): 
#         x = random.uniform(20.0, 50.0)
#         print(x, end=' ')
#     print() 

# # random_tester()
# import random
# times = int(input("Enter the number of times, dice has to roll: "))
# def throw_coin(times):
#     heads, tails = 0, 0 
#     for i in range(times):
#         # get a random int, if 0 - head, 1 - tail 
#         coin = random.randint(0, 1)
#         if coin == 0: heads += 1 
#         else: tails += 1 
#     print(f'Heads: {heads}, Tails: {tails}')

# throw_coin(times)

# lower= 0
# upper= 10
# def get_mark(lower, upper, prompt='Test'):
#     if lower > upper: return None
#     mark = float(input(f'Enter mark ({lower} - {upper}) for {prompt}: '))
#     while mark < lower or mark > upper:
#         mark = float(input(f'Enter mark ({lower} - {upper}) for {prompt}: '))
#     return mark        

# get_mark(lower, upper)

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def main():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Exit")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", addition(num1, num2))
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()



































































































































































































































































