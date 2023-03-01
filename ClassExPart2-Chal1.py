#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Challenge 1: Sum of all numbers

MAX = 5 #max number

#initialize var
total = 0.0

print ('This program calculates the sum of')
print (f'{MAX} numbers you will enter')

#get user input & accumulate them
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number
    
#calculate average
avg = total / MAX

#prints results
print(f'The total is {total}.')
print(f'The average is {avg}.')
