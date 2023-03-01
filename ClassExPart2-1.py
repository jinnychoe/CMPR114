#Jinny Choe
#2/27/2023
#Class Exercise Week 3 Part 2 Question 1:

MAX = 5

total = 0.0
print ('This program calculates the sum of')
print (f'{MAX} numbers you will enter')

for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

avg = total / MAX

print(f'The total is {total}.')
print(f'The average is {avg}.')