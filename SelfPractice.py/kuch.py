num1= int(input('Enter a number: '))
if num1 > 0:
    print(f'{num1} is positive')
    if num1 < 50:
        print(f'{num1} is less than 50')
    elif num1 == '50':
        print(f'{num1} is equal to 50')
    elif 51 >= num1 <= 84:
        print(f'{num1} is between 51 and 84')
    elif  num1 >= 85:
        print(f'{num1} is greater than or equal to 85')
else:
    print(f'{num1} is a negative number')

if num1 % 2 == 0:
    print(f'{num1} is even')
else:
    print(f'{num1} is odd')

if num1 % 3 == 0 and num1 % 2 == 0: print(f'{num1} is divisble by both 2 and 3')

if num1 % 2 == 0 or num1 % 3 ==0:
   print(f'{num1} is divible by 2 or 3 but not both')

if num1 % 2 != 00 and num1 % 3 != 0:
    print(f'{num1} is not divible by both 2 and 3')
    
    