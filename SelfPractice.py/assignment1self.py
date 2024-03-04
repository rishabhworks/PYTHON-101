num1 = int(input('Enter the first positive integer: '))
num2 = int(input('Enter the second positive integer: '))
if num1 < 0 or num2 < 0: 
    print('Error! Enter a positive number')
else: 
    print(f'{num1} and {num2} are your choosen integers.')
    if num1 > num2: print(f'{num1} is greater than {num2}')
    elif num2 > num1: print(f'{num1} is smaller than {num2}')
    elif num1 == num2: print(f'{num1} is equal to {num2}')
    
