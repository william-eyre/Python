car1Price = float(input('Car 1 Price:\n'))
car1milesPerGallon = float (input('Car 1 miles per Gallon:\n'))

car2Price = float(input('Car 2 Price\n'))
car2milesPerGallon = float(input('Car 2 miles per gallon:\n'))

gallonPrice = float(input('Price of a gallon of fuel:\n'))
milesPerYear = float(input('how many miles do you drive a year?\n'))

totalMiles = milesPerYear * 10
car1Gallons = (totalMiles / car1milesPerGallon)
car2Gallons = (totalMiles / car2milesPerGallon)

car1TotalPrice = car1Price + (car1milesPerGallon * gallonPrice)
car2TotalPrice = car2Price + (car2milesPerGallon * gallonPrice)

print(car1TotalPrice)
print(car2TotalPrice)