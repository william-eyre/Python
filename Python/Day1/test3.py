import random


def main():

    number1 = random.randrange(10)  # gives a random number between 0 - 9

    number2 = random.randrange(5, 10)  # gives a random number between 5-10

    number3 = random.randrange(0, 101, 10)  # gives a random number between 0-100 and in increments of 10

    number4 = random.random() # just a random number

    print('the number is', number1, number2, number3, number4)

    print(random.randint(1,10))


main()
