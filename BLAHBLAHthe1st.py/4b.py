name = str(input('Enter name: '))
while name != 'stop':
    print(f'{name} You have 5 courses, Enter the numbers obtained')
    total =  0
    for n in range(1, 6):
        mark = float(input(f'\t Course{n}'))
        while mark < 0 or mark > 100:
            mark = float(input(f'\t Course{n}'))
        total = total + mark
        print(f'{name}, your average is {total / 5}')