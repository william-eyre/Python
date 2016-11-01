def main():
    customer_code = str(input("Enter customer code: "))
    beginning_meter_reading = int(input("Enter beginning meter reading:  "))
    ending_meter_reading = int(input("Enter ending meter reading:  "))

    if beginning_meter_reading > ending_meter_reading:
        ending_meter_reading += 1000000000.0

    program_quit = False
    gallons_used = (ending_meter_reading - beginning_meter_reading) / 10

    if customer_code != "r" or "c" or "i":
        program_quit == True

    if program_quit == True:
        print("Program will now close")

    def calculate_bill():

        if customer_code == "r":
            extra_gallons_used = float(gallons_used * 0.0005)
            bill = 5.00 + extra_gallons_used
            print("Water bill £", bill)

        if customer_code == "c":
            bill = 1000
            if gallons_used > 4000000:



                extra_gallons_used = float(gallons_used - 4000000.00)
                bill = bill + (extra_gallons_used * 0.00025)

        #print("Water bill £", format(bill, ',.2f'), sep='')

        if customer_code == "i":
            if gallons_used < 4000000:
                bill = 1000
                print("Water bill £", format(bill, ',.2f'), sep='')
            elif 4000000 < gallons_used < 10000000:
                bill = 2000
                print("Water bill £", format(bill, ',.2f'), sep='')
            elif gallons_used > 10000000:
                extra_gallons_used = float(gallons_used - 10000000)
                bill = 2000 + (extra_gallons_used * 0.00025)
                print("Water bill £", format(bill, ',.2f'), sep='')

    while not program_quit:
        print("Customer code", customer_code)
        print("Beginning meter reading", beginning_meter_reading)
        print("End reading", ending_meter_reading)
        print("Gallons used", gallons_used)
        calculate_bill()
        program_quit = True


main()
