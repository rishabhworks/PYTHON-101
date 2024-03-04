# radius = int(input("Enter Radius: "))
# while radius != -1:
#     print(f'Radius of the circle is {3.14 * radius**2}')
#     radius = int(input("Enter Radius: "))

# r= int(input("Enter the radius of the circles: "))
# while True:
#     print(f'The area and perimeter of the circles are {3.14 * r ** 2}, {2 * 3.14 * r}')
#     r= int(input("Enter the radius of the circles: "))

# Play_Again = 'y'
# while Play_Again == "y":
#     num = int(input("Enter an integer: "))
#     if num % 2 == 0:
#         print(f'{num} is Even')
#     else:
#         print(f'{num} is odd')

#     if num < 0:
#         print(f'{num} is negative')
#     elif num > 0:
#         print(f'{num} is positive')
#     else: 
#         print(f"{num} is equal to 0")   
    
#     Play_Again = str(input("Enter y to continue: "))

# while True:
#     print("Hello")
#     choose = input("Print again? (y/n): ")
#     if choose != "y":
#         break

# count = 0
# while count < 10:
#     name= input("Enter a name: ")
#     print(f'Hello {name}')
#     count = count + 1

# while True:
#     marks = int(input("Enter marks: "))
#     if marks < 0:
#         break
#     if marks > 100:
#         print("Please enter a positive percentage")
#     if  90 <= marks <= 100:
#         print("A")
#     elif 70 <= marks <= 90:
#         print("B")
#     elif 50 <= marks <= 70:
#         print("C")
#     else:
#         print("F")

# print("Numbers 1 to 10 with their squares: ")
# num = 0
# while num<=100:
#     print(f"{num} squared is {num*num}")
#     num += 1

# print ("Backwards is: ")
# num = 100
# while num >=0:
#     print(f"{num} squared is {num*num}")
#     num -=1
        
# weight= float(input("Enter mass is pounds: "))
# while weight <=10:
#     print(f"{weight} of pound is {weight *0.45359237}kg(S)")
#     weight= float(input("Enter mass is pounds: "))

# tution = 10000
# years = 0
 
# while tution < 20000:
#   tution *= 1.07
#   years += 1
# print(f"It will take {years} for tution to double")

# stop_number = int(input("Enter the stop number: "))

# print("Numbers from 1 to", stop_number)
# for i in range(0, stop_number +1, 2):
#  print (i)
        
# for num in range(0, 200):
#     if num % 2 == 0: 
#         if num % 3 == 0:
#             print(num, end=" ")

# prin = int(input("Enter Principle Amount: "))
# rate= float(input("Enter the rate: "))
# time= int(input("Enter the time: "))

# print(f"The compund interest gained on {prin} at {rate}% for {time}years is: {prin * 1+rate**time}")


# for i in range(1, 6):
#     count = 1
#     for j in range(1, i+1):
#         count *= j
#     print(f"{i}!= {count}")

# sum_even= 0
# for i in range(2, 101, 2):
#     sum_even += i
# print(f"The sum of all even numbers is: {sum_even}")


# sum_even= 0
# product_even= 1
# for i in range(10):
#     num = float(input("Enter a number: "))
#     sum_even += num
#     product_even *= num

# print(f"The sum is {sum_even} and product is {product_even}")

# def pass_it(x,y):
#     z= x, " , " , y
# num1= 4
# num2= 8
# answer = pass_it(num1, num2)
# print (answer)

# decimal_num = int(input("Enter an integer: "))

# # Convert to binary
# binary_num = ""
# while decimal_num > 0:
#     binary_num = str(decimal_num % 2) + binary_num 
#     decimal_num //= 2

# # Convert to octal
# decimal_num = int(input("Enter an integer: "))
# octal_num = ""
# while decimal_num > 0:
#     octal_num = str(decimal_num % 8) + octal_num
#     decimal_num //= 8

# # Convert to hexadecimal
# decimal_num = int(input("Enter an integer: "))
# hex_chars = "0123456789ABCDEF"
# hexadecimal_num = ""
# while decimal_num > 0:
#     hexadecimal_num = hex_chars[decimal_num % 16] + hexadecimal_num
#     decimal_num //= 16

# print("Binary: ", binary_num)
# print("Octal: ", octal_num)
# print("Hexadecimal: ", hexadecimal_num)


# while True:
#     def calculate_Sales_commission():
#         sales_amount = float(input("Enter the sales amount: "))
#         commission_rate= float(input("Enter the rate: "))

#         commission = sales_amount * (commission_rate / 100)
#         print(f"The sales commission is: ${commission:.2f}")

#     calculate_Sales_commission()

# def read_integer():
#     while True:
#             ask= int(input("Enter an Integer: "))
#             if ask == 0:
#                 break
#             elif ask % 2 == 0:
#                 print(f"{ask} is even")
#             else:
#                 print(f"{ask} is odd")
# read_integer()



# def main():
#     value = 5
#     show_double(value)

# def show_double(number):
#     result = number * 2
#     print(result)

# main()

# def main():
#     print('The sum of 12 and 45 is')
#     show_sum(12, 45)

#     def show_sum(num1, num2):
#         result= num1 + num2
#         print(result)

# main()

# def sum_and_average(num1, num2):
#     total = num1 + num2
#     average =  total / 2

#     print("Sum:", total)
#     print("Average: ", average)

# num1= int(input("Enter number 1: "))
# num2= int(input("Enter the 2nd number: "))
# sum_and_average(num1, num2)
        
# def sq_cu_cubr_sqr(square, cube, cube_r, num1):
#     square= num1 ** 2
#     cube = num1 ** 3
#     cube_r= num1 ** 1/3
#     if num1 > 0:
#         print(f"The square root is: {num1 ** 1/2}")
# num1 = float(input("Enter a number: "))
# sq_cu_cubr_sqr()

# def hypo(num1, num2):
#     hypotenuse = (num1**2 + num2 **2) ** 0.5
#     return hypotenuse

# num1= int(input("Enter 1st side: "))
# num2= int(input("Enter 2nd side: "))
# result = hypo(num1, num2)
# print(f"The length of hypotenuse will be: {result:.2f}")








































































































































