Play_Again = "Y" 
while Play_Again == "Y": #until and unless play_again is Y, loop will continue
    num1 = int(input("Enter the first number: ")) #input two integers
    if num1 <= 0:
        print("Enter a positive number: ")
        Play_Again ="Y"
    else:
        num2pos = False
        while num2pos == False:
            num2 = int(input("Enter the second number: "))
            if num2 <= 0: #check if the integers are positive
                print("please enter positive number")
                num2pos = False
            else:
                num2pos = True
                if num1 > num2: #Check if the integers are greater, smaller or equal
                    print(f"{num1} is greater than {num2}.") #Greater
                    ran = num2
                elif num1 < num2:
                    print(f"{num1} is smaller than {num2}.") #smaller
                    ran = num1
                else:
                    print(f"{num1} is equal to {num2}.") #equalto
                    ran = num1
                print("common factors of both these number are = ", end = "") 
                for i in range(1, ran + 1): #Finding out the common factors
                      if num1 % i == 0 and num2 % i == 0:
                           print(i, end = " ")
                x = True
                while x == True:
                    Play_Again = input("\nEnter if you want to play again Y/N: ").upper()
                    if Play_Again == "N":
                        print("Thank you for using the program")    # if you wanna stop
                        x = False
                    elif Play_Again != "Y": # if there is an error
                        print("error, please choose Y/N or y/n: ")
                    else:   # if you wanna continue
                        x = False