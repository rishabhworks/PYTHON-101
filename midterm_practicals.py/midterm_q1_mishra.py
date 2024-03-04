#Q1:

ticket = float(input("Price for one ticket ($11.99): "))
n_f= int(input("Enter the number of tickets: "))
Total_Cost = ticket * n_f

if n_f >= 10:
    print("Ten or More tickets, 5% disount")
    Total_Cost *= 0.95
elif n_f < 10:
    print("Less than 10 tickets, no discount")

print(f"Total Cost: {Total_Cost:.2f}")
