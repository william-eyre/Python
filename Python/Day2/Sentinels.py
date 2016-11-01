# this program prints the average of salary values that are terminated with a sentinel
# Initialise variables to maintain the running total and count.
total = 0.0
count = 0
# initialise salary to any non
salary = 0.0

while salary >= 0.0:
    salary = float(input("Please enter a salary or -1 to finish"))

    if salary >= 0.0:

        total = total + salary
        count = count + 1

if count > 0 :
    average = total / count
    print("Average Salary is", average)
else:
    print("No data was entered")