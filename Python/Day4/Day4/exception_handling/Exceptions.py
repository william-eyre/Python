def main():

    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter another number'))

    if num2 != 0:
        result =num1 / num2
        print(num1, 'divided by', num2, 'is', result)
    else:
        print('Cannot divide by zero.')


def main2():

    try:
        hours = int(input('How many hours did you work?'))

        pay_rate = float(input('Enter your hourly pay rate:'))

        gross_pay = hours * pay_rate

        print('Grosspay: £', format(gross_pay, ',.2f'), sep='')
    except ValueError as errr:
        print('ERROR: Hours worked and hourly pay rate must')
        print('be valid integers.')
        print(errr)

main2()

def main3():   # this is supposed to have errors

    total = 0.0
    try:
        infile = open('Sale_time', 'r')

        for line in infile:
            amount = float(line)     # this reads from a file and prints the values on the file
            total += amount
            infile.close()
            print(format(total, ',.2f'))
    except IOError:
        print('An error has occurred trying to read the file.')
    except ValueError:
        print('Non numeric data found in file.')



