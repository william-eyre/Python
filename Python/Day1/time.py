totalSeconds = float(input('please enter seconds:\n'))  # inputs a number, putting the float at the beginning
# to determine to date type

seconds = totalSeconds % 60
minutes = (totalSeconds // 60) % 60
hours = totalSeconds // 3600

print('seconds', seconds)
print('minutes', minutes)
print('hours', hours)




