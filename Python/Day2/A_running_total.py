MAX = 5
def main():
    # initialise an accumulator variable
    total=0.0
    # explain what we are doing
    print('This program calculates the sum of')
    print(MAX, 'Numbers you will enter')
    # Get the numbers and accumulate them
    for counter in range(MAX):
        number = int(input('Enter a number:\n'))
        total = total + number

        print('The total is', total)

main()
