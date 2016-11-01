def main():
    # create a variable to control the loop
    keep_going = 'y'
    # calculate a series of commission
    while keep_going == 'y':
        sales = float(input("Enter the amount of sales:\n"))
        comm_rate = float(input("Enter the commission rate:\n"))
        commission = sales * comm_rate
        print("The commission is £", format(commission, ',.2f'), sep='')
        # asks the user if they want another go
        keep_going = input('Do you want to calculate another ' +\
                           'commission (Enter y for yes):')


main()
