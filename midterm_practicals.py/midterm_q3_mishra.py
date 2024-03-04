#Q3
def calculate_squares(start, stop):
    total_Squares=0
    count= 0
    print("Numbers  Squared")
    for num in range(start, stop +1):
        square= num**2
        total_Squares += square
        count += 1
        print(f"{num}    {num**2}")

    average = total_Squares / count
    print(f"Average of Squares: {average}")
        
start_num = int(input("Start Number: "))
stop_num= int(input("Stop Number: "))

calculate_squares(start_num, stop_num)

    

