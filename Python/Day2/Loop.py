def main():
    sales= float(input('Enter the amount of sales'))
    if sales > 50000:
        bonus = 500
    commission_rate = 0.12
    commission = sales * commission_rate
    print('Well done, you met your quota you get a £', bonus, 'bonus well done')
    print('The commission is £', format(commission, ',.2'), sep='')


main()

