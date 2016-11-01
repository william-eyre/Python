def main():
    show_interest(rate=0.01, periods=10, principal=10000.0)


def show_interest(rate, periods, principal):
    interest = rate * periods * principal
    print('The simple interest will be £', format(interest, ',.2f'), sep=' ')


main()