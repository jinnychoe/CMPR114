#Jinny Choe
#2/13/2023
#Homework Week 2 Question 1: Quarter of the year 

month = int(input('Enter the month as a numerical character between 1 and 12: '))

if (month < 1 or month > 12): #determine if input is invalid
    print ('Error. Invalid input.') #prints error message
elif (month >=1 and month <=3 ): #determines if month is in 1st quarter & prints statement
    print ('The month is in the first quarter.')
elif (month >= 4 and month <= 6):#determines if month is in 2nd quarter & prints statement
    print('The month is in the second quarter')
elif (month >= 7 and month <= 9):#determines if month is in 3rd quarter & prints statement
    print('The month is in the third quarter')
elif (month >= 10 and month <= 12):#determines if month is in 4th quarter & prints statement
    print('The month is in the fourth quarter')
