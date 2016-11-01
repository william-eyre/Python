def main():
    firstage = int (input ('Please enter your age:\n') )
    secondage = int (input('Please enter your best friends age:\n'))
    total = sum ( firstage, secondage )
    print ('Together you are', total, 'years old')


def sum (num1,num2):
        result = num1 + num2

        return result


main()