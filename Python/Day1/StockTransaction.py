sharesPurchased = 1000
pricePerShare = 32.87
totalCost = sharesPurchased * pricePerShare
commission = totalCost * 0.02

sharesSold = 1000
sellPrice = 33.92
totalSale = sharesSold * sellPrice
sellCommission = totalSale * 0.02

profit = totalSale - (totalCost + commission + sellCommission)


print('The total cost of the buy £', totalCost)
print('Commission payed £', commission)
print('Revenue of sale £', totalSale)
print('Commission for sale £', sellCommission)

print("total profit: " + format(profit, '.2f'))