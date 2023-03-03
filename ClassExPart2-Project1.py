#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 2 Project 1

#get ending limit
print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go? '))

#print the table headings
print()
print('Number\tSquare')
print('--------------')

#print the numbers and their squares
for number in range(1,end+1):
    square = number**2
    print(f'{number}\t{square}')
    