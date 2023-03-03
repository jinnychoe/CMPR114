#Jinny Choe
#3/2/2023
#Week 3 Class Exercise Part 2 Project 2

MAX = 5 #max number

#initialize var
total = 0.0

print ('This program calculates the sum of')
print (f'{MAX} numbers you will enter')

#get user input & accumulate them
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number
    

#prints results
print(f'The total is {total}.')
