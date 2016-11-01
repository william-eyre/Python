from Day5.Coin_flip import Coin_class


def main():

    coin1 = Coin_class.Coin()
    coin2 = Coin_class.Coin()
    coin3 = Coin_class.Coin()

    print('I have three coins with these sides up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    print('I am tossing all three coins...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    print('Now here are the sides that are up')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())


main()
