# Jinny Choe
# 2/27/2023
# Class Exercise Week 3.7 Lists Question 2:


def main1():
    prodNums = ['V475', 'F987', 'Q143', 'R688']  # List of values

    search = input('Enter a product ')

    if search in prodNums:  # determines if the product number is on the List

        print(search, ' was found on the list.')

    else:

        print(search, ' was not found on the list.')


main1()


def main2():
    nameList = []
    again = 'y'

    while again == 'y':
        name = input('Enter a name ')
        nameList.append(name)  # appends name to list
        print()

        print(' do you want to add another name? ')
        again = input('y = Yes, hit any other key for No')
        print()
        print(' here are the names you entered')

        for name in nameList:  # loop through each name
            print(name)

        outfile = open('names.txt', 'w')
        outfile.write(str(nameList))
        outfile.close()
        print('recorded the names in the list ')

main2()
