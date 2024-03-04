sex = int(input("Enter the integer: "))
play = 'y'
while play == 'y':
    if sex > 0:
        print(f'{sex} is positive')
    elif sex < 0:
        print(f'{sex} is negative')
    elif sex == 0:
        print(f'{sex} is equals to zero')
    if sex  % 2 == 0: 
       print(f'{sex} is even')
    else: 
       print(f'{sex} is odd')
    play = input("Enter if you wanna continue with Y/y: ").lower()
    sex = int(input("Enter the integer: "))


 