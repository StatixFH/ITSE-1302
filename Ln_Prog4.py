price = float(input('Enter the purchase price: '))

# declaring variables
month_number = 1
int_rate = 0.15  # annual interest rate
down_payment = price * .10
monthly_payment = (price - down_payment) * .05  # monthly payment calculation (2x check)
current_balance = price - down_payment  # starting balance owed

# displays heading, field width specified with left justification "<", numbers refer to string values
print('{:<15s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}'.format('Month', 'Starting Balance', 'Interest to Pay',
                                                               'Principal to Pay', 'Payment', 'Ending Balance'))

while current_balance > 0:  # loops till balance reaches 0
    if current_balance < monthly_payment:  # checks if balance is less than the payment
        int_amt = 0  # no interest
        principal = current_balance  # monthly payment without interest
        payment = current_balance
        ending_balance = 0  # ending loop
    else:
        int_amt = current_balance * (int_rate / 12)  # interest amount
        principal = monthly_payment  # principal amount
        payment = int_amt + principal  # payment total
        ending_balance = current_balance - principal  # ending balance

    print('{:<15d} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:20.2f}'.format(month_number, current_balance, int_amt,
                                                                            principal, payment, ending_balance))

    current_balance = ending_balance  # updating balance
    month_number += 1  # updating month number
