class Customer:
    RESIDENTIAL = 'r'
    COMMERCIAL = 'c'
    INDUSTRIAL = 'i'
    customer_code = None
    start_meter = None
    ending_meter = None
    gallons_used = None
    water_bill= None
    def __init__(self, customer_code, start_meter, ending_meter):
        self.__customer_code = customer_code
        self.__start_meter = start_meter
        self.__ending_meter = ending_meter

class Residential:

    def calculate_bill(self):

        water_bill = 5 + (gallons_used*0.0005)



class Commercial:

    def calculate_bill(self):

    extra_gallons_used = gallons_used - 4000000

    if gallons_used < 4000000:
        water_bill = 1000
    elif gallons_used > 4000000:
        water_bill = 1000 + (extra_gallons_used*0.00025)


class Industrial:

    def calculate_bill(self):

        extra_gallons_used = gallons_used - 10000000

    if gallons_used < 4000000:
        water_bill = 1000
    if gallons_used > 4000000 and gallons_used < 10000000:
        water_bill = 2000
    if gallons_used > 10000000:
        water_bill = 2000 + (extra_gallons_used*0.00025)






def console():
    customer_code = str(input('Enter customer code:  '))
    start_meter = int(input('Enter Beginning meter reading:  '))
    ending_meter = int(input('Enter ending meter reading:   '))
    gallons_used = ending_meter - start_meter / 10


def output():


print("Customer code:", customer_code)
print("Beginning meter reading:", start_meter)
print("Ending meter reading:", ending_meter)
print("Gallons of water used:", gallons_used)
print("Amount billed: £")

