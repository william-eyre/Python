original_price = float(input('Please enter the price of the item:\n'))
discount = original_price * 0.2
sale_price = original_price - discount
sale_price = sale_price.__round__(2)
print('The sale price is', sale_price)



