N_O_T= int(input('Enter the number of Tickets ($7.50 each, 10+ discoun: 2%): '))
V_I_P= input('Are of a VIP? (VIP DISCOUNT: 10%) (Y/N): ')
W_E_D= input('Is today Saturday or Sunday (WEEKEND DISCOUNT: 5%) (Y/N): ')
total= N_O_T * 7.50
#calculations
if N_O_T >= 10:
    discount1= total - total * 0.02
else:
    discount1 = 0
if V_I_P == 'Y':
    discount2= total - total * 0.1
else:
    discount2= 0
if W_E_D == 'Y':
    discount3 = total - total * 0.05
else:
    discount3 = 0

total_payment= total - (discount1 + discount2 + discount3)
print(" THE TOTAL PAYABLE AMOUNT IS: ", total_payment)
