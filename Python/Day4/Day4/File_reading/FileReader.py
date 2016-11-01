# file = open("/Users/william.eyre/Desktop/Bootcamp/Python/Day4/Day4/test")
# contents = file.read()
# print(contents)
# file.close()
# #  looks in a file and see the contents of the file
#
# file = open(r"test2.txt", "a")   # w write to the file, r reads the file, a amends the file.
# file.write("\n hi will")
# file.close()

#  create a file, called "text2", you must define the file type as well

#
# file = open("/Users/william.eyre/Desktop/Bootcamp/Python/Day4/Day4/test")
# name = "William"
# file.write(name)
# file.close()


def main1():

    outfile = open("names.txt", "w")

    outfile.write('Will Eyre\n')
    outfile.write('Robin Bradford\n')
    outfile.write('Pascale Smith\n')

    outfile.close()

    #  creates a file and puts whatever contents you put in

def main2():

    infile = open('names.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    infile.close()     # reads lines within a file, as long as the lines are specified

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')   # strip removes the white spaces at the beginning and the end
    line3 = line3.rstrip('\n')

    print(line1, end='')
    print(line3, end='')
    print(line2, end='')

def main3():

    print('Enter the name of three friends')
    name1 = input('Friend 1:')
    name2 = input('Friend 2:')
    name3 = input('Friend 3:')

    myfile = open('names.txt', 'w')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    myfile.close()
    print('The names were written to friends.txt.')

def main4():

    outfile = open('numbers.txt', 'w')

    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    num3 = int(input("Enter another number:"))

    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    outfile.close()
    print('Data written to numbers.txt')

def main5():

    num_days = int(input('For how many days do' + ' you have Sale_time?'))

    sales_file = open('Sale_time', 'w')

    for count in range(1, num_days + 1):
        sales = float(input('Enter the Sale_time for days' + str(count) + ': '))

        sales_file.write(str(sales) + '\n')

    sales_file.close()
    print('Data written to Sale_time.txt.')



def main6():
    # open the Sale_time.txt file for reading
    sales = open('Sale_time.txt', 'r')
    # read the first line from the file,
    # don't convert to a number yet.
    # need to test for an empty string
    line = sales.readline()

    while line != '':

        amount = float(line)
        print(format(amount, ',.2'))
        line = sales.readline()

    sales.close()




def main7():

    sales_file = open('Sale_time', 'r')

    for line in sales_file:
        amount = float(line)
        print(format(amount, '.2f'))     # opens a file and reads what is inside

    sales_file.close()

  #  must make sure that the file is closed before running it



import os

def main8():
    # create a bool variable to use as a flag
    found = False
    # get the file to delete
    search = input('Which employee do you want to delete?')
    # open the original file
    emp_file = open('employees', 'r')
    # open the temporary file
    temp_file = open('temp.txt', 'w')
    # read the first records description
    name = emp_file.readline()

    while name != '':

        qty = float(emp_file.readline())
        name = name.rstrip('\n')
        if name != search:

            temp_file.write(name + '\n')
            temp_file.write(str(qty) + '\n')

        else:
            found = True
            # set the found flag to true
        name = emp_file.readline()
    # Close the file and the temporary file
    emp_file.close()
    temp_file.close()
    # Delete the original emp file
    os.remove('employees')
    # Rename the temporary file
    os.rename('temp.txt', 'employees')
    # If the search calue was not found in the file
    # display a message
    if found:
        print('The file has been updated')

    else:
        print('That item was not found in the file')

