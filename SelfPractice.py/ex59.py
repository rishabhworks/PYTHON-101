#Write a program that reads three integers, sorts and
#displays the numbers in an increasing order

x = int(input('First Integer: '))
y = int(input('Second Integer: '))
z = int(input('Third Integer: '))

print('The numbers are: ', x , y , z )

if x > y:
    x , y = y , x
if y > z:
    y , z = z , y
if z > x:
    z , x = x , z 

print('The increasing order is', x , y , z)
