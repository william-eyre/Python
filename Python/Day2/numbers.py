number = int(input('Please enter a speed in MPH:'))
if number <= 0 and number < 200:
    print("You are travelling", number, "MPH")
else:
    print("Slow down")