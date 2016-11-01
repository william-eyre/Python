from Day5.Bank import bank_account_class


def main():

    start_bal = float(input('Enter your starting balance:'))

    savings = bank_account_class.BankAccount(start_bal)

    pay = float(input('How much were paid this week?'))
    print('I will deposit that into your account')
    savings.deposit(pay)

    print(savings)

    cash = float(input('How much would you like to withdraw?'))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    print(savings)

main()
