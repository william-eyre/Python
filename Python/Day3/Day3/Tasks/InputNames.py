def main1():
    name_list = []  # put names in a list and asks you if you want to repeat the function
    again = 'y'
    while again == 'y':
        name = input('A man must have a name:')
        name_list.append(name)
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no:')
        print()
        print('Here are the names you entered')
    for name in name_list:
        print(name)
main1()