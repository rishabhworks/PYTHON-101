
#num1= int(input("Give a 5 digit integer: "))
#d1= num1%10
#d2= num1//10%10
#d3= num1//100%10
#d4= num1//1000%10
#d5= num1//10000%10
#print(d5, " ",d4, " ",d3, " ",d2, " ",d1)

message = f'Hello World'
name = 'Rishabh Mishra'
age = '19'
score = 928.123
print(name, age, score)
print(name + str(age) + str(score))
print(f'My name is {name}, I am {age}, The score is {score}')
print(f'My name is {name: <30}')
print(f'My age is {age: ^60}')
print(f'The score is {score: >30}')