from Day5.CellPhone import cellphone

def main():

    manufact = input('Enter phone manufacturer:')
    model = input('Enter phone model:')
    price = float(input('Enter the phone price:'))

    phone = cellphone.CellPhone(manufact, model, price)

    print(manufact)
    print(model)
    print(price)


main()
