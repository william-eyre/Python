customer_code = str(input("Enter customer code: "))
beginning_meter_reading = int(input("Enter beginning meter reading:  "))
ending_meter_reading = int(input("Enter ending meter reading:  "))
gallons_used = (ending_meter_reading - beginning_meter_reading) / 10
four_million = 4000000



def calculate_bill():

    if customer_code == 'r':
        extra_gallons_used = float(gallons_used * 0.0005)
        bill = 5.00 + extra_gallons_used
        print(beginning_meter_reading)
        print(ending_meter_reading)
        print(gallons_used)
        print("Water bill £", format(bill, ',.2f'), sep='')

    if customer_code == commercial and gallons_used < four_million:
        bill = 1000
        print("your water bill is £", bill)

    if customer_code == commercial and gallons_used > four_million:
        bill = 1000
        extra_gallons_used = float(gallons_used * 0.00025)
        bill += extra_gallons_used
        print(beginning_meter_reading)
        print(ending_meter_reading)
        print("Water bill £", format(extra_gallons_used, ',.2f'), sep='')

main()
