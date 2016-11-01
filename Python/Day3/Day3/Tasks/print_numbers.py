even_numbers = [2, 4, 6, 8, 10]
print(even_numbers)

names = ['Will', 'Robin', 'Pascale', 'Nic']
print(names)

numbers = [2, 4, 8] * 5  # prints the numbers in the list 5 times
print(numbers)

numbers = list(range(6))
print(numbers)  # prints the numbers between 1 and 6

numbers = [1, 2, 3] * 3
print(numbers)

numbers = [99, 100, 101, 102]
for n in numbers:
    print(numbers)


my_list = [10, 20, 30, 40]
print(my_list[0], my_list[1], my_list[2], my_list[3])
print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])

my_list = [10, 20, 30, 40, 50, 60]
print(my_list[0], my_list[1], my_list[2], my_list[3])
print(my_list[-1], my_list[2], my_list[-3], my_list[5])

my_list = [10, 20, 30, 40]
index = 0  # sets where to start looking in the list
while index < len(my_list):
    print(my_list[index])
    index += 1  # chooses how many indexes to jump


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list1)
print(list2)
print(list3)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
mid_days = days[0:6:2]  #
print(mid_days)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[-5:])


# def main():
#     prod_nums = ['V475', 'F987', 'Q143', 'R688']
#     search = input('Enter a product number:')
#     if search in prod_nums:
#         print(search, 'was found in the list')
#     else:
#         print(search, 'item not found')
#
# main()




# def main1():
#     name_list = []  # put names in a list and asks you if you want to repeat the function
#     again = 'y'
#     while again =='y':
#         name = input('A man must have a name:')
#         name_list.append(name)
#         print('Do you want to add another name?')
#         again = input ('y = yes, anything else = no:')
#         print()
#         print('Here are the names you entered')
#     for name in name_list:
#         print(name)
# main1()