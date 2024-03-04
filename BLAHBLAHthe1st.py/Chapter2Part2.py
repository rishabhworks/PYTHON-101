name = input('What is your name:')
s_p_q= int(input("Enter the Amount of small pizza ($9.5 each):"))
l_p_q= int(input("Enter the amount of large pizza ($12.99 each):"))
e_t= int(input("Enter the amount of extra toppings ($1.49 each):"))
_d_=int(input("Enter the amount of drinks ($2.23 each):"))

#calculations
s_p_c= 9.5 * s_p_q
l_p_c= 12.99 * l_p_q
t_c= 1.49 * e_t
d_c= 2.23 * _d_

Total_Cost = s_p_c+l_p_c+t_c+d_c

tax_rate= 5/100
Total_payment= Total_Cost * (1+tax_rate)

print("Total Payable Amoount (Before Tax):", Total_Cost)
print("Total Payable Amount (After TAXES):", Total_payment)